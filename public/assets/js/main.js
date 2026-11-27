/* Vivalr — vanilla JS: navigation, catalog filters, quote builder, copy actions */
(function () {
  'use strict';

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  /* ---------- mobile navigation ---------- */
  var navToggle = $('#nav-toggle');
  var mobileNav = $('#mobile-nav');
  if (navToggle && mobileNav) {
    var setNav = function (open) {
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      mobileNav.classList.toggle('open', open);
      mobileNav.setAttribute('aria-hidden', open ? 'false' : 'true');
      document.body.classList.toggle('nav-open', open);
    };
    navToggle.addEventListener('click', function () {
      setNav(navToggle.getAttribute('aria-expanded') !== 'true');
    });
    $$('a', mobileNav).forEach(function (a) { a.addEventListener('click', function () { setNav(false); }); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mobileNav.classList.contains('open')) { setNav(false); navToggle.focus(); }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 900 && mobileNav.classList.contains('open')) setNav(false);
    });
  }

  /* ---------- header shadow ---------- */
  var header = $('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- current year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- copy helper ---------- */
  function copyText(text, statusEl) {
    var done = function () {
      if (statusEl) {
        statusEl.textContent = 'Copied to clipboard ✓';
        window.setTimeout(function () { statusEl.textContent = ''; }, 2600);
      }
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done).catch(function () { fallbackCopy(text, done); });
    } else {
      fallbackCopy(text, done);
    }
  }
  function fallbackCopy(text, done) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); done(); } catch (e) { /* noop */ }
    document.body.removeChild(ta);
  }

  /* ---------- product quote builder ---------- */
  var quoteRoot = $('[data-quote-root]');
  if (quoteRoot) {
    var productName = quoteRoot.getAttribute('data-product-name') || 'Research peptide';
    var productShort = quoteRoot.getAttribute('data-product-short') || productName;
    var unit = quoteRoot.getAttribute('data-unit') || 'kit';
    var unitPlural = unit === 'pack' ? 'packs' : 'kits';
    var variantSelect = $('#variant-select', quoteRoot);
    var qtyInput = $('#qty', quoteRoot);
    var preview = $('#quote-preview', quoteRoot);
    var waBtn = $('#wa-quote', quoteRoot);
    var mailBtn = $('#email-quote', quoteRoot);
    var copyBtn = $('#copy-quote', quoteRoot);
    var status = $('#copy-status', quoteRoot);
    var vialSpec = $('#vial-spec');
    var vialSku = $('#vial-sku');
    var selectedSkuEl = $('#selected-sku');
    var waFloat = $('#wa-float');
    var baseWa = 'https://wa.me/8615866781826?text=';
    var baseMail = 'info@vivalr.com';

    function qty() {
      var n = parseInt(qtyInput && qtyInput.value, 10);
      if (isNaN(n) || n < 1) n = 1;
      if (n > 999) n = 999;
      if (qtyInput && String(n) !== qtyInput.value) qtyInput.value = n;
      return n;
    }
    function selectedOption() {
      if (!variantSelect) return null;
      return variantSelect.options[variantSelect.selectedIndex];
    }
    function specLabel() {
      var o = selectedOption();
      return o ? (o.getAttribute('data-label') || o.textContent.trim()) : '';
    }
    function sku() {
      var o = selectedOption();
      return o ? (o.getAttribute('data-sku') || '') : '';
    }
    function unitText(q) { return q + ' ' + (q === 1 ? unit : unitPlural); }
    function buildMessage() {
      var q = qty();
      var lines = [
        'Hello Vivalr, I would like a quotation for:',
        'Product: ' + productName,
        'Specification: ' + specLabel(),
        'Quantity: ' + unitText(q),
        sku() ? 'SKU: ' + sku() : '',
        '',
        'Please include bulk pricing, COA, lead time and shipping options to my country.'
      ];
      return lines.filter(function (l, i) { return l !== '' || i === 5; }).join('\n');
    }
    function refresh() {
      var q = qty();
      var label = specLabel();
      var msg = buildMessage();
      if (preview) {
        preview.innerHTML = '<strong>' + escapeHtml(productShort) + '</strong> · ' + escapeHtml(label) +
          '<br>' + unitText(q) + ' · batch COA & MS included';
      }
      if (waBtn) waBtn.href = baseWa + encodeURIComponent(msg);
      if (mailBtn) {
        mailBtn.href = 'mailto:' + baseMail +
          '?subject=' + encodeURIComponent('Quote request — ' + productShort + ' — ' + label + ' × ' + unitText(q)) +
          '&body=' + encodeURIComponent(msg);
      }
      if (waFloat) {
        waFloat.href = baseWa + encodeURIComponent('Hello Vivalr, I am interested in ' + productShort + ' (' + label + '). Please send bulk pricing and COA.');
      }
      var opt = selectedOption();
      var shortLabel = opt ? (opt.getAttribute('data-short') || label) : label;
      if (vialSpec) vialSpec.textContent = shortLabel;
      if (vialSku) vialSku.textContent = sku() || 'VVR-RP';
      if (selectedSkuEl) selectedSkuEl.textContent = sku() || '—';
    }
    function escapeHtml(s) {
      return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    if (variantSelect) variantSelect.addEventListener('change', refresh);
    if (qtyInput) {
      qtyInput.addEventListener('input', refresh);
      qtyInput.addEventListener('blur', refresh);
    }
    $$('.qty button', quoteRoot).forEach(function (b) {
      b.addEventListener('click', function () {
        var step = b.getAttribute('data-step') === '-1' ? -1 : 1;
        qtyInput.value = Math.min(999, Math.max(1, qty() + step));
        refresh();
      });
    });
    if (copyBtn) {
      copyBtn.addEventListener('click', function () { copyText(buildMessage(), status); });
    }
    refresh();
  }

  /* ---------- contact / RFQ form -> email or WhatsApp ---------- */
  var rfqForm = $('#rfq-form');
  if (rfqForm) {
    var formStatus = $('#form-status');
    var get = function (name) { var el = rfqForm.elements[name]; return el ? String(el.value || '').trim() : ''; };
    function formMessage() {
      return [
        'New quotation request — vivalr.com',
        '',
        'Name: ' + get('name'),
        'Company / institution: ' + (get('company') || '—'),
        'Email: ' + get('email'),
        'Country: ' + (get('country') || '—'),
        'Product / CAS: ' + (get('interest') || '—'),
        'Estimated quantity: ' + (get('quantity') || '—'),
        '',
        'Requirements:',
        (get('message') || '—')
      ].join('\n');
    }
    function validate() {
      if (!rfqForm.reportValidity()) return false;
      return true;
    }
    var waFormBtn = $('#wa-form');
    if (waFormBtn) {
      waFormBtn.addEventListener('click', function () {
        if (!validate()) return;
        window.open('https://wa.me/8615866781826?text=' + encodeURIComponent(formMessage()), '_blank', 'noopener');
        if (formStatus) formStatus.textContent = 'WhatsApp opened in a new tab.';
      });
    }
    var copyFormBtn = $('#copy-form');
    if (copyFormBtn) {
      copyFormBtn.addEventListener('click', function () {
        if (!validate()) return;
        copyText(formMessage(), formStatus);
      });
    }
    rfqForm.addEventListener('submit', function (e) {
      if (!validate()) { e.preventDefault(); return; }
      e.preventDefault();
      var subject = 'Quotation request — ' + (get('interest') || 'Vivalr products');
      window.location.href = 'mailto:info@vivalr.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(formMessage());
      if (formStatus) formStatus.textContent = 'Your email draft is opening. If nothing happens, email info@vivalr.com directly.';
    });
  }

  /* ---------- catalog filter + search ---------- */
  var catalog = $('#catalog-grid');
  if (catalog) {
    var cards = $$('.pcard', catalog);
    var buttons = $$('.filter-btn');
    var search = $('#catalog-search');
    var countEl = $('#catalog-count');
    var empty = $('#catalog-empty');
    var activeFilter = 'all';

    function apply() {
      var term = (search && search.value || '').toLowerCase().trim();
      var visible = 0;
      cards.forEach(function (card) {
        var cat = card.getAttribute('data-cat') || '';
        var text = (card.getAttribute('data-search') || '').toLowerCase();
        var okCat = activeFilter === 'all' || cat === activeFilter;
        var okTerm = !term || text.indexOf(term) !== -1;
        var show = okCat && okTerm;
        card.classList.toggle('hidden', !show);
        if (show) visible++;
      });
      if (countEl) countEl.innerHTML = '<b>' + visible + '</b> of ' + cards.length + ' products';
      if (empty) empty.classList.toggle('visible', visible === 0);
    }
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        activeFilter = btn.getAttribute('data-filter') || 'all';
        buttons.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        apply();
      });
    });
    if (search) {
      search.addEventListener('input', apply);
      search.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { search.value = ''; apply(); }
      });
    }
    var initial = new URLSearchParams(window.location.search).get('category');
    if (initial) {
      var target = buttons.filter(function (b) { return b.getAttribute('data-filter') === initial; })[0];
      if (target) { target.click(); }
    }
    apply();
  }

  /* ---------- FAQ: close siblings for a tidy read ---------- */
  $$('.faq').forEach(function (group) {
    var items = $$('details', group);
    items.forEach(function (d) {
      d.addEventListener('toggle', function () {
        if (d.open) items.forEach(function (other) { if (other !== d) other.open = false; });
      });
    });
  });
})();

/* Vivalr — navigation, catalogue, inquiry cart and RFQ form */
(function () {
  'use strict';

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var CART_KEY = 'vivalr_cart_v1';
  var TRASH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 6h18M8 6V4h8v2M19 6l-1 14H6L5 6M10 11v5M14 11v5"/></svg>';

  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  function formatMoney(value) {
    var n = Number(value) || 0;
    var s = n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    if (s.slice(-3) === '.00') s = s.slice(0, -3);
    return '$' + s;
  }

  function unitLabel(unit, qty) {
    if (unit === 'pack') return qty === 1 ? 'pack' : 'packs';
    return qty === 1 ? 'kit' : 'kits';
  }

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

  /* ---------- copy helper (contact form) ---------- */
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

  /* =======================================================================
     Inquiry cart
     ======================================================================= */
  var cartToggle = $('#cart-toggle');
  var cartDrawer = $('#cart-drawer');
  var cartOverlay = $('#cart-overlay');
  var cartClose = $('#cart-close');
  var cartItemsEl = $('#cart-items');
  var cartEmpty = $('#cart-empty');
  var cartTotalEl = $('#cart-total');
  var cartSummaryEl = $('#cart-summary');
  var cartWa = $('#cart-wa');
  var cartEmail = $('#cart-email');
  var cartClear = $('#cart-clear');
  var lastFocus = null;
  var cart = loadCart();

  function loadCart() {
    try {
      var raw = window.localStorage.getItem(CART_KEY);
      var parsed = raw ? JSON.parse(raw) : [];
      if (!Array.isArray(parsed)) return [];
      return parsed.filter(function (x) {
        return x && x.sku && x.name && Number(x.price) > 0 && Number(x.qty) > 0;
      }).map(function (x) {
        return {
          sku: String(x.sku),
          name: String(x.name),
          short: String(x.short || x.name),
          spec: String(x.spec || ''),
          price: Number(x.price),
          qty: Math.max(1, Math.min(999, parseInt(x.qty, 10) || 1)),
          unit: x.unit === 'pack' ? 'pack' : 'kit',
          slug: String(x.slug || '')
        };
      });
    } catch (e) { return []; }
  }

  function saveCart() {
    try { window.localStorage.setItem(CART_KEY, JSON.stringify(cart)); } catch (e) { /* noop */ }
    updateCounts();
  }

  function cartCount() {
    return cart.reduce(function (sum, item) { return sum + Number(item.qty || 0); }, 0);
  }

  function cartTotal() {
    return Math.round(cart.reduce(function (sum, item) { return sum + item.price * item.qty; }, 0) * 100) / 100;
  }

  function updateCounts() {
    var count = cartCount();
    $$('#cart-count, #buy-cart-count').forEach(function (el) {
      el.textContent = count > 99 ? '99+' : String(count);
      el.classList.toggle('zero', count === 0);
    });
    if (cartToggle) {
      cartToggle.setAttribute('aria-label', count === 0 ? 'Open inquiry cart' : 'Open inquiry cart, ' + count + ' items');
    }
  }

  function messageForCart() {
    var lines = [
      'Hello Vivalr,',
      '',
      'I would like a quotation for the following items:',
      ''
    ];
    cart.forEach(function (item, i) {
      lines.push((i + 1) + '. ' + item.name + ' — ' + item.spec);
      lines.push('   Qty: ' + item.qty + ' ' + unitLabel(item.unit, item.qty) +
        ' × ' + formatMoney(item.price) + ' = ' + formatMoney(item.price * item.qty));
    });
    lines.push('');
    lines.push('Estimated total: ' + formatMoney(cartTotal()));
    lines.push('Prices are in USD. Please confirm availability, COA, lead time and shipping to my country.');
    return lines.join('\n');
  }

  function renderCart() {
    updateCounts();
    if (!cartItemsEl) return;
    var count = cartCount();

    if (!cart.length) {
      if (cartEmpty) cartEmpty.style.display = 'block';
      cartItemsEl.innerHTML = '';
      if (cartTotalEl) cartTotalEl.textContent = '$0';
      if (cartSummaryEl) cartSummaryEl.textContent = '0 items';
      if (cartWa) { cartWa.href = '#'; cartWa.classList.add('is-disabled'); cartWa.setAttribute('aria-disabled', 'true'); }
      if (cartEmail) { cartEmail.href = 'mailto:info@vivalr.com'; cartEmail.classList.add('is-disabled'); cartEmail.setAttribute('aria-disabled', 'true'); }
      if (cartClear) { cartClear.classList.add('is-disabled'); cartClear.setAttribute('aria-disabled', 'true'); }
      return;
    }

    if (cartEmpty) cartEmpty.style.display = 'none';
    cartItemsEl.innerHTML = cart.map(function (item) {
      return '<div class="cart-item" data-sku="' + escapeHtml(item.sku) + '">' +
        '<div class="cart-item-top"><strong>' + escapeHtml(item.short) + '</strong>' +
        '<button class="cart-item-remove" type="button" data-act="remove" aria-label="Remove ' + escapeHtml(item.short) + '">' + TRASH + '</button></div>' +
        '<div class="cart-item-spec">' + escapeHtml(item.spec) + ' · ' + formatMoney(item.price) + ' / ' + escapeHtml(unitLabel(item.unit, 1)) + '</div>' +
        '<div class="cart-item-bottom"><div class="cart-qty">' +
        '<button type="button" data-act="minus" aria-label="Decrease quantity">−</button>' +
        '<span>' + item.qty + '</span>' +
        '<button type="button" data-act="plus" aria-label="Increase quantity">+</button>' +
        '</div><div class="cart-line-price">' + formatMoney(item.price * item.qty) + '</div></div></div>';
    }).join('');

    if (cartTotalEl) cartTotalEl.textContent = formatMoney(cartTotal());
    if (cartSummaryEl) cartSummaryEl.textContent = count + (count === 1 ? ' item' : ' items');

    var msg = messageForCart();
    if (cartWa) {
      cartWa.href = 'https://wa.me/8615866781826?text=' + encodeURIComponent(msg);
      cartWa.classList.remove('is-disabled');
      cartWa.removeAttribute('aria-disabled');
    }
    if (cartEmail) {
      cartEmail.href = 'mailto:info@vivalr.com?subject=' + encodeURIComponent('Quotation request — Vivalr cart') +
        '&body=' + encodeURIComponent(msg);
      cartEmail.classList.remove('is-disabled');
      cartEmail.removeAttribute('aria-disabled');
    }
    if (cartClear) { cartClear.classList.remove('is-disabled'); cartClear.removeAttribute('aria-disabled'); }
  }

  function openCart() {
    if (!cartDrawer) return;
    lastFocus = document.activeElement;
    cartDrawer.classList.add('open');
    cartDrawer.setAttribute('aria-hidden', 'false');
    if (cartOverlay) { cartOverlay.classList.add('open'); cartOverlay.setAttribute('aria-hidden', 'false'); }
    document.body.classList.add('cart-open');
    if (cartClose) cartClose.focus();
  }

  function closeCart() {
    if (!cartDrawer) return;
    cartDrawer.classList.remove('open');
    cartDrawer.setAttribute('aria-hidden', 'true');
    if (cartOverlay) { cartOverlay.classList.remove('open'); cartOverlay.setAttribute('aria-hidden', 'true'); }
    document.body.classList.remove('cart-open');
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function addToCart(item) {
    var existing = cart.filter(function (x) { return x.sku === item.sku; })[0];
    if (existing) existing.qty = Math.min(999, existing.qty + item.qty);
    else cart.push(item);
    saveCart();
    renderCart();
    openCart();
  }

  function changeQty(sku, delta) {
    var item = cart.filter(function (x) { return x.sku === sku; })[0];
    if (!item) return;
    item.qty = Math.min(999, item.qty + delta);
    if (item.qty < 1) cart = cart.filter(function (x) { return x.sku !== sku; });
    saveCart();
    renderCart();
  }

  if (cartToggle) cartToggle.addEventListener('click', openCart);
  if (cartClose) cartClose.addEventListener('click', closeCart);
  if (cartOverlay) cartOverlay.addEventListener('click', closeCart);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && cartDrawer && cartDrawer.classList.contains('open')) closeCart();
  });
  if (cartItemsEl) {
    cartItemsEl.addEventListener('click', function (e) {
      var btn = e.target.closest('button[data-act]');
      if (!btn) return;
      var row = btn.closest('.cart-item');
      if (!row) return;
      var sku = row.getAttribute('data-sku');
      var act = btn.getAttribute('data-act');
      if (act === 'plus') changeQty(sku, 1);
      if (act === 'minus') changeQty(sku, -1);
      if (act === 'remove') { cart = cart.filter(function (x) { return x.sku !== sku; }); saveCart(); renderCart(); }
    });
  }
  if (cartClear) {
    cartClear.addEventListener('click', function () {
      if (!cart.length) return;
      if (window.confirm('Clear all items from the inquiry cart?')) {
        cart = [];
        saveCart();
        renderCart();
      }
    });
  }
  if (cartWa) cartWa.addEventListener('click', function (e) { if (!cart.length) e.preventDefault(); });
  if (cartEmail) cartEmail.addEventListener('click', function (e) { if (!cart.length) e.preventDefault(); });

  renderCart();

  /* =======================================================================
     Product buy bar
     ======================================================================= */
  var buyRoot = $('[data-buy-root]');
  if (buyRoot) {
    var productName = buyRoot.getAttribute('data-product-name') || 'Research peptide';
    var productShort = buyRoot.getAttribute('data-product-short') || productName;
    var productSlug = buyRoot.getAttribute('data-product-slug') || '';
    var buyUnit = buyRoot.getAttribute('data-unit') || 'kit';
    var variantSelect = $('#variant-select', buyRoot);
    var qtyInput = $('#buy-qty', buyRoot);
    var unitPriceEl = $('#unit-price', buyRoot);
    var lineTotalEl = $('#line-total', buyRoot);
    var buySkuEl = $('#buy-sku', buyRoot);
    var addBtn = $('#add-to-cart', buyRoot);
    var openBtn = $('#open-cart', buyRoot);
    var buyStatus = $('#buy-status', buyRoot);
    var vialSpec = $('#vial-spec');
    var vialSku = $('#vial-sku');

    function selectedOption() {
      if (!variantSelect) return null;
      return variantSelect.options[variantSelect.selectedIndex];
    }
    function selectedQty() {
      var n = parseInt(qtyInput && qtyInput.value, 10);
      if (isNaN(n) || n < 1) n = 1;
      if (n > 999) n = 999;
      if (qtyInput && String(n) !== qtyInput.value) qtyInput.value = n;
      return n;
    }
    function refreshBuy() {
      var opt = selectedOption();
      if (!opt) return;
      var price = parseFloat(opt.getAttribute('data-price')) || 0;
      var q = selectedQty();
      var label = opt.getAttribute('data-label') || opt.textContent.trim();
      var short = opt.getAttribute('data-short') || label;
      var sku = opt.getAttribute('data-sku') || '';
      if (unitPriceEl) unitPriceEl.textContent = formatMoney(price);
      if (lineTotalEl) lineTotalEl.textContent = formatMoney(price * q);
      if (buySkuEl) buySkuEl.textContent = sku;
      if (vialSpec) vialSpec.textContent = short;
      if (vialSku) vialSku.textContent = sku || 'VVR-RP';
    }

    if (variantSelect) variantSelect.addEventListener('change', refreshBuy);
    if (qtyInput) {
      qtyInput.addEventListener('input', refreshBuy);
      qtyInput.addEventListener('blur', refreshBuy);
    }
    $$('.qty button', buyRoot).forEach(function (b) {
      b.addEventListener('click', function () {
        var step = b.id === 'buy-qty-minus' ? -1 : 1;
        qtyInput.value = Math.min(999, Math.max(1, selectedQty() + step));
        refreshBuy();
      });
    });
    if (addBtn) {
      addBtn.addEventListener('click', function () {
        var opt = selectedOption();
        if (!opt) return;
        var q = selectedQty();
        var price = parseFloat(opt.getAttribute('data-price')) || 0;
        addToCart({
          sku: opt.getAttribute('data-sku') || '',
          name: productName,
          short: productShort,
          spec: opt.getAttribute('data-label') || opt.textContent.trim(),
          price: price,
          qty: q,
          unit: buyUnit,
          slug: productSlug
        });
        if (buyStatus) {
          buyStatus.textContent = q + ' ' + unitLabel(buyUnit, q) + ' added to your inquiry cart.';
          window.setTimeout(function () { buyStatus.textContent = ''; }, 5000);
        }
      });
    }
    if (openBtn) openBtn.addEventListener('click', openCart);
    refreshBuy();
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
    function validate() { return rfqForm.reportValidity(); }
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
      if (target) target.click();
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

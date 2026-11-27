# -*- coding: utf-8 -*-
"""Vivalr product dataset.

All product facts are written for a research-only B2B catalogue. Prices from the
source workbook are intentionally NOT included: the public site is quote-based.
"""

SITE = "https://vivalr.com"
BRAND = "Vivalr"
COMPANY = "Shandong Green International Trade Co., Ltd."
ADDRESS = ("Environmental Protection Science and Technology Park, High-Tech Zone, "
           "Jinan City, Shandong Province, China")
ADDRESS_SHORT = "Jinan High-Tech Zone, Shandong, China"
PHONE = "+86 15866781826"
PHONE_TEL = "+8615866781826"
WHATSAPP = "https://wa.me/8615866781826"
EMAIL = "info@vivalr.com"
UPDATED = "2026-11-27"
UPDATED_HUMAN = "27 November 2026"

CATEGORIES = {
    "cosmetic": {
        "label": "Cosmetic & Anti-Aging Peptides",
        "short": "Cosmetic & Anti-Aging",
        "desc": "Copper peptides, expression-line peptides and matrix peptides for skin, scalp and formulation research.",
        "icon": "spark",
    },
    "repair": {
        "label": "Repair & Bioregulator Peptides",
        "short": "Repair & Bioregulator",
        "desc": "Tissue-repair, immune-signalling and short bioregulator peptides for preclinical and cellular research.",
        "icon": "repair",
    },
    "blend": {
        "label": "Blend Kits (GLOW & KLOW)",
        "short": "Blend Kits",
        "desc": "Pre-formulated research blends supplied as single-vial kits with component-level COA documentation.",
        "icon": "blend",
    },
    "nad": {
        "label": "NAD+ & NMN",
        "short": "NAD+ & NMN",
        "desc": "NAD+ precursors, coenzymes and longevity small molecules for metabolic and cellular-aging research.",
        "icon": "nad",
    },
}

DEFAULT_PURITY = "≥99% (HPLC)"
DEFAULT_FORM = "Lyophilized powder"
DEFAULT_APPEARANCE = "White to off-white powder"
DEFAULT_STORAGE = "-20 °C, desiccated, protected from light"
DEFAULT_SHELF = "24 months at -20 °C"
DEFAULT_MOQ = "1 kit (10 vials)"


def V(label, sku):
    return {"label": label, "sku": sku}


def P(**kw):
    d = {
        "purity": DEFAULT_PURITY,
        "form": DEFAULT_FORM,
        "appearance": DEFAULT_APPEARANCE,
        "storage": DEFAULT_STORAGE,
        "shelf": DEFAULT_SHELF,
        "moq": DEFAULT_MOQ,
        "featured": False,
        "note": "",
        "tags": [],
        "research": [],
        "risks": [],
        "faqs": [],
        "related": [],
        "meta_title": "",
        "meta_desc": "",
    }
    d.update(kw)
    return d


PRODUCTS = [
    # ------------------------------------------------------------------ cosmetic
    P(
        slug="ghk-cu",
        name="GHK-Cu",
        full_name="GHK-Cu (Copper Tripeptide-1)",
        title_name="GHK-Cu",
        cat="cosmetic",
        cas="89030-95-5",
        seq="Gly-His-Lys·Cu(II)",
        mol="C14H22N6O4·Cu",
        mw="403.94 Da (copper complex)",
        appearance="Blue to blue-green powder",
        tagline="The benchmark copper tripeptide for collagen, ECM and skin-repair research.",
        intro=("GHK-Cu is a glycyl-histidyl-lysine tripeptide complexed with copper(II). It is one of the "
               "most extensively studied cosmetic peptides for collagen synthesis, extracellular-matrix "
               "remodelling and skin-barrier research, supplied here as a high-purity lyophilized powder "
               "for formulation evaluation."),
        overview=[
            ("GHK-Cu combines a small, highly conserved tripeptide with a copper ion. The peptide sequence "
             "gives the complex its affinity for skin proteins and its signalling profile, while copper acts "
             "as a cofactor for lysyl oxidase and copper-dependent antioxidant enzymes. This dual character "
             "is why the molecule appears in both dermal-repair and antioxidant research."),
            ("As a cosmetic raw material, GHK-Cu is valued for its solubility, low use level and compatibility "
             "with emulsion systems. Vivalr supplies the copper complex — not the free tripeptide — and "
             "verifies identity, peptide purity and copper content so formulators can calculate active copper "
             "dose reliably."),
        ],
        research=[
            ("Collagen & ECM signalling", "Studied for supporting fibroblast collagen and glycosaminoglycan production in in-vitro skin models."),
            ("Copper delivery", "Acts as a controlled Cu(II) source for lysyl oxidase and copper-dependent antioxidant systems."),
            ("Antioxidant & cytokine research", "Investigated for modulating oxidative stress and inflammatory signalling in skin cells."),
            ("Scalp & follicle models", "Evaluated in dermal papilla and follicle research for hair-cycle and extracellular-matrix signalling."),
        ],
        synthesis=("GHK-Cu is produced by Fmoc solid-phase peptide synthesis, purified by preparative C18 HPLC "
                    "to ≥99%, and then complexed with copper(II) acetate under controlled pH. The blue complex is "
                    "isolated, desalted and lyophilized. Identity is confirmed by ESI-MS; copper content is "
                    "verified by ICP-OES and reported on the batch COA."),
        risks=[
            ("pH-dependent complex stability", "high",
             "The Cu(II) complex dissociates at low pH and can precipitate or exchange copper above neutral pH. Formulate at pH 4.5–6.5."),
            ("Chelator incompatibility", "high",
             "EDTA, citric acid, phytate and other strong chelators strip the copper from the peptide. Keep them out of the same phase."),
            ("Redox cycling & light", "medium",
             "Copper can participate in redox reactions with reducing agents such as ascorbic acid. Add at cool-down and protect from light."),
        ],
        handling=("Store the sealed vial at -20 °C, desiccated and protected from light. Equilibrate to room "
                  "temperature before opening to avoid condensation. For formulation, dissolve in water or a "
                  "pH 5–6 buffer and add at cool-down below 40 °C."),
        formulation=("Typical cosmetic use levels are 0.05–0.5% as supplied, depending on the target copper dose. "
                     "Avoid ascorbic acid, EDTA, strong chelators and anionic surfactants in the same phase. Run a "
                     "four-week accelerated compatibility test in your base before scale-up."),
        applications=["Anti-aging serums and creams", "Firming and repair emulsions", "Scalp and hair-care formulas", "Post-procedure skin-care research"],
        faqs=[
            ("Is GHK-Cu the same as copper tripeptide-1?",
             "Yes. GHK-Cu, copper tripeptide-1 and the INCI name Copper Tripeptide-1 refer to the same Gly-His-Lys–copper(II) complex. Vivalr supplies the blue complex, not the uncomplexed tripeptide, and reports copper content on the COA."),
            ("Can GHK-Cu be combined with vitamin C?",
             "Not in the same phase. Ascorbic acid is a reducing agent and can destabilise the copper complex and discolour the formula. If a vitamin C step is required, separate the phases, use a non-reducing derivative, and validate colour and pH over four weeks."),
        ],
        related=["ahk-cu", "matrixyl", "snap-8"],
        tags=["copper peptide", "collagen", "skin repair", "anti-aging", "cosmetic"],
        featured=True,
        meta_desc="Bulk GHK-Cu (copper tripeptide-1), CAS 89030-95-5, ≥99% HPLC, MS verified. 50/100 mg kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="ahk-cu",
        name="AHK-Cu",
        full_name="AHK-Cu (Copper Tripeptide-3)",
        title_name="AHK-Cu",
        cat="cosmetic",
        cas="682809-81-0",
        seq="Ala-His-Lys·Cu(II)",
        mol="C15H24N6O4·Cu",
        mw="415.94 Da (copper complex)",
        appearance="Blue powder",
        tagline="A copper tripeptide studied for follicle, scalp and skin-repair signalling.",
        intro=("AHK-Cu is the alanyl-histidyl-lysine copper tripeptide, a close analogue of GHK-Cu with a "
               "research profile centred on hair-follicle biology and scalp care. It is supplied as a "
               "≥99% HPLC-purified, lyophilized copper complex for cosmetic and cellular research."),
        overview=[
            ("The extra alanine residue changes the peptide's shape and receptor interaction compared with "
             "GHK-Cu, which is why AHK-Cu is often selected for follicle and scalp formulations rather than "
             "mainstream anti-aging creams. Both peptides deliver copper, but they are not interchangeable in "
             "a formula without re-testing."),
            ("Vivalr supplies AHK-Cu as a batch-tested blue powder with identity confirmed by mass "
             "spectrometry. It is intended for laboratory formulation evaluation and is not a finished "
             "cosmetic product."),
        ],
        research=[
            ("Hair-follicle research", "Studied in dermal papilla and follicle cultures for effects on follicle maintenance and hair-cycle signalling."),
            ("Scalp extracellular matrix", "Investigated for collagen and matrix remodelling in scalp tissue models."),
            ("Copper-dependent enzymes", "Provides Cu(II) for lysyl oxidase and antioxidant enzyme systems in vitro."),
            ("Skin-repair signalling", "Evaluated alongside GHK-Cu in dermal repair and wound-model research."),
        ],
        synthesis=("AHK-Cu is assembled by Fmoc SPPS, cleaved and purified by preparative HPLC, then complexed "
                    "with copper(II) acetate and lyophilized. Each batch is tested for peptide purity, copper "
                    "content and mass identity before release."),
        risks=[
            ("Complex dissociation at pH extremes", "high",
             "Keep formulations between pH 4.5 and 6.5. Acidic or alkaline conditions reduce the available copper complex."),
            ("Oxidative discolouration", "medium",
             "Copper can catalyse oxidation in the presence of reducing sugars or ascorbic acid. Use a cool-down addition and test colour stability."),
            ("Chelating agents", "high",
             "EDTA and other chelators compete for copper and should be avoided in the same phase."),
        ],
        handling=("Store at -20 °C in the dark. Allow the vial to reach room temperature before opening. "
                  "Dissolve in water or pH 5–6 buffer; protect the stock solution from light and use it the "
                  "same day for best results."),
        formulation=("AHK-Cu is used at low percentages in scalp serums, tonics and leave-on formulas. Because "
                     "the target is often the follicle, choose a vehicle that wets the scalp rather than a heavy "
                     "cream, and confirm preservative compatibility with the copper complex."),
        applications=["Scalp serums and tonics", "Hair-follicle research formulations", "Anti-aging emulsions", "Copper-peptide combinations"],
        faqs=[
            ("What is the difference between AHK-Cu and GHK-Cu?",
             "AHK-Cu is Ala-His-Lys–Cu and GHK-Cu is Gly-His-Lys–Cu. The additional alanine changes molecular geometry and is associated with a stronger follicle-focused research profile; GHK-Cu has the larger dermal-collagen literature base."),
            ("Is AHK-Cu water-soluble?",
             "Yes. The lyophilized copper complex dissolves readily in water at the concentrations used in cosmetic formulation. For stock solutions, use pH 5–6 water and avoid chelating buffers."),
        ],
        related=["ghk-cu", "matrixyl", "bpc-157"],
        tags=["copper peptide", "hair follicle", "scalp", "cosmetic", "AHK"],
        meta_desc="AHK-Cu (copper tripeptide-3), CAS 682809-81-0, ≥99% HPLC. Bulk 50/100 mg kits with COA and MS verification. Cosmetic research supplier — request a quote.",
    ),
    P(
        slug="snap-8",
        name="Snap-8",
        full_name="Snap-8 (Acetyl Octapeptide-3)",
        title_name="Snap-8",
        cat="cosmetic",
        cas="868844-74-0",
        seq="Ac-Glu-Glu-Met-Gln-Arg-Arg-Ala-Asp-NH2",
        mol="C41H70N16O16S",
        mw="1075.16 Da",
        tagline="An eight-amino-acid expression-line peptide for cosmetic wrinkle research.",
        intro=("Snap-8, also known as acetyl octapeptide-3, is an extended analogue of the hexapeptide "
               "Argireline. It is designed to interact with the SNAP-25 component of the SNARE complex and is "
               "widely used in topical expression-line and anti-wrinkle research."),
        overview=[
            ("Snap-8 is a C-terminally amidated octapeptide supplied as the acetate salt. Its sequence "
             "combines a charged N-terminal region with a methionine and a C-terminal amide, features that "
             "influence both its solubility and its sensitivity to oxidation."),
            ("The peptide is normally incorporated into aqueous serums, gels and emulsions at cool-down. "
             "Vivalr verifies sequence, counter-ion and purity by HPLC and MS so formulators can compare lots "
             "reproducibly."),
        ],
        research=[
            ("SNARE-complex research", "Studied for interaction with SNAP-25 and modulation of neurotransmitter-release machinery in vitro."),
            ("Expression-line models", "Used in cosmetic research on dynamic lines and topical anti-wrinkle performance."),
            ("Formulation stability", "Evaluated for compatibility with aqueous gels, emulsions and low-pH serums."),
            ("Argireline comparison", "Frequently benchmarked against acetyl hexapeptide-8 in cosmetic studies."),
        ],
        synthesis=("Snap-8 is synthesized by Fmoc SPPS on Rink amide resin to give the C-terminal amide, "
                    "cleaved with TFA, precipitated and purified by preparative C18 HPLC. The acetate salt is "
                    "prepared by ion exchange and the product is lyophilized."),
        risks=[
            ("Methionine oxidation", "high", "Met can oxidise to the sulfoxide, shifting retention time and reducing activity. Use antioxidant-compatible packaging and avoid oxidizing preservatives."),
            ("C-terminal amide hydrolysis", "medium", "Prolonged exposure to pH >8 or high temperature can hydrolyse the amide. Target pH 5.0–6.5."),
            ("Thermal degradation", "medium", "Add at cool-down below 40 °C and avoid prolonged hold times at elevated temperature."),
        ],
        handling=("Store sealed at -20 °C under nitrogen if possible. Protect from light and moisture. "
                  "Reconstitute with water or pH 5–6 buffer; filter sterilise if required and avoid repeated "
                  "freeze–thaw cycles."),
        formulation=("Use Snap-8 in the water phase at cool-down. It is compatible with most non-ionic "
                     "emulsifiers and humectants, but should not be co-formulated with strong oxidizers or "
                     "high levels of transition metals. Test pH drift over four weeks."),
        applications=["Expression-line serums", "Eye and forehead gels", "Anti-wrinkle emulsions", "Cosmetic peptide blends"],
        faqs=[
            ("What is the difference between Snap-8 and Argireline?",
             "Snap-8 is an octapeptide (acetyl octapeptide-3); Argireline is the shorter hexapeptide acetyl hexapeptide-8. Snap-8 extends the sequence and is positioned in cosmetic research as a next-generation expression-line peptide."),
            ("Why does Snap-8 require oxidation control?",
             "Its methionine residue is susceptible to oxidation, which can convert the peptide to the sulfoxide. Use low-oxygen processes, avoid oxidizing preservatives and protect the finished formula from light."),
        ],
        related=["matrixyl", "ghk-cu", "ahk-cu"],
        tags=["expression lines", "wrinkle", "argireline", "cosmetic", "anti-aging"],
        featured=True,
        meta_desc="Bulk Snap-8 (acetyl octapeptide-3), CAS 868844-74-0, ≥99% HPLC. 10/100 mg kits, COA and MS verification, worldwide shipping. Request a quote.",
    ),
    P(
        slug="matrixyl",
        name="Matrixyl",
        full_name="Matrixyl (Palmitoyl Pentapeptide-4)",
        title_name="Matrixyl",
        cat="cosmetic",
        cas="214047-00-4",
        seq="Pal-Lys-Thr-Thr-Lys-Ser",
        mol="C39H75N7O10",
        mw="802.05 Da",
        tagline="Palmitoyl pentapeptide-4 for collagen and matrix-repair research.",
        intro=("Matrixyl is the trade name most often used for palmitoyl pentapeptide-4, a lipophilic "
               "matrikine peptide studied for collagen I/III and fibronectin synthesis. Vivalr supplies the "
               "equivalent palmitoylated pentapeptide raw material for cosmetic formulation research."),
        overview=[
            ("The palmitoyl chain makes the peptide lipophilic enough to associate with skin lipids and "
             "emulsion interfaces, while the Lys-Thr-Thr-Lys-Ser sequence carries the matrix-signalling "
             "motif. This combination is the basis of the Matrixyl family's use in anti-aging emulsions."),
            ("Matrixyl is a trademark of Sederma. Vivalr supplies palmitoyl pentapeptide-4 as a research raw "
             "material; it is not the branded finished ingredient. Formulators should confirm trade-name and "
             "regulatory status for their market before making label claims."),
        ],
        research=[
            ("Collagen synthesis", "Studied for upregulating collagen I and III in fibroblast and skin models."),
            ("Fibronectin & ECM", "Investigated for matrix-protein synthesis and dermal remodelling."),
            ("Lipophilic delivery", "The palmitoyl chain improves association with skin lipids and emulsion interfaces."),
            ("Anti-wrinkle research", "Used in cosmetic studies of fine lines, firmness and skin texture."),
        ],
        synthesis=("The pentapeptide is assembled by Fmoc SPPS, then N-palmitoylated on resin or in solution. "
                    "Crude product is purified by preparative HPLC, counter-ion adjusted and lyophilized. "
                    "Purity is assessed at 214 nm and identity confirmed by ESI-MS."),
        risks=[
            ("Hydrolysis at neutral/alkaline pH", "medium", "Ester-free but still susceptible to peptide-bond hydrolysis; formulate at pH 5–7 and avoid long high-temperature holds."),
            ("Aggregation in aqueous stock", "medium", "Palmitoylated peptides can self-assemble. Prepare stock solutions at the lowest practical concentration and use fresh."),
            ("Microbial risk", "medium", "The lipophilic peptide is prone to microbial growth in aqueous stocks; use appropriate preservation and cold storage."),
        ],
        handling=("Store at -20 °C, protected from light. Warm the vial gently to room temperature and mix "
                  "the powder thoroughly before weighing. For stocks, dissolve in a compatible alcohol/glycol "
                  "or surfactant system rather than pure water."),
        formulation=("Add Matrixyl to the oil or cool-down phase depending on the grade and carrier. Typical "
                     "use levels are 1–5% of the supplied raw material; confirm the active peptide content with "
                     "your supplier specification. Avoid strong oxidizers and extreme pH."),
        applications=["Anti-aging creams", "Firming serums", "Neck and eye formulas", "Matrix-peptide combinations"],
        faqs=[
            ("Is this the same as Matrixyl 3000?",
             "No. Matrixyl 3000 is a blend of palmitoyl tripeptide-1 and palmitoyl tetrapeptide-7. This product is palmitoyl pentapeptide-4, the original Matrixyl motif. We can quote the Matrixyl 3000 components separately on request."),
            ("Is Matrixyl a trademark?",
             "Matrixyl is a trademark of Sederma. Vivalr supplies the equivalent palmitoyl pentapeptide-4 raw material for research and formulation evaluation; it is not presented as the branded ingredient."),
        ],
        related=["ghk-cu", "snap-8", "ahk-cu"],
        tags=["matrixyl", "palmitoyl pentapeptide-4", "collagen", "cosmetic", "anti-aging"],
        featured=True,
        meta_desc="Bulk Matrixyl (palmitoyl pentapeptide-4), CAS 214047-00-4, ≥99% HPLC. 10 mg kits with COA and MS verification. Request a cosmetic research quote.",
    ),
    P(
        slug="glutathione",
        name="Glutathione",
        full_name="L-Glutathione (Reduced)",
        title_name="Glutathione",
        cat="cosmetic",
        cas="70-18-8",
        seq="γ-L-Glu-L-Cys-Gly",
        mol="C10H17N3O6S",
        mw="307.32 Da",
        appearance="White crystalline powder",
        form="Crystalline powder",
        purity="≥99% (HPLC)",
        tagline="Reduced glutathione for antioxidant, redox and skin-brightening research.",
        intro=("L-Glutathione (reduced) is a thiol-containing tripeptide and the principal non-enzymatic "
               "antioxidant in mammalian cells. It is supplied as a high-purity crystalline powder for "
               "cosmetic, redox-biology and formulation research."),
        overview=[
            ("Glutathione exists in reduced (GSH) and oxidised (GSSG) forms. The reduced form is the active "
             "thiol donor; its sulfur atom is also the site of oxidation, metal binding and conjugation. "
             "Those properties drive both its antioxidant value and its handling challenges."),
            ("In cosmetic research, glutathione is studied for its role in redox balance and melanin "
             "synthesis. Vivalr supplies the reduced form with low GSSG content and batch-specific HPLC "
             "data so formulators can distinguish it from oxidised or mixed material."),
        ],
        research=[
            ("Redox buffering", "Acts as a thiol antioxidant and cofactor for glutathione peroxidase and glutathione reductase."),
            ("Melanin-pathway research", "Studied for its influence on tyrosinase activity and melanin synthesis in skin models."),
            ("Detoxification", "Participates in phase II conjugation and glutathione-S-transferase reactions."),
            ("Formulation stability", "Evaluated for oxidation, pH-dependent degradation and compatibility with preservatives."),
        ],
        synthesis=("Glutathione is produced by enzymatic or fermentation routes and purified by ion-exchange "
                    "and preparative HPLC. The reduced form is concentrated under inert gas and dried to a "
                    "low-GSSG powder. Each lot is assayed for GSH content and oxidised fraction."),
        risks=[
            ("Oxidation to GSSG", "high", "Air, light, trace metals and alkaline pH accelerate oxidation. Use inert gas, chelating-free packaging and pH 3–5."),
            ("Metal-catalysed degradation", "high", "Trace iron and copper catalyse thiol oxidation. Use low-metal excipients and avoid metal contact during processing."),
            ("Hygroscopicity", "medium", "The powder picks up moisture readily; keep sealed with desiccant and equilibrate before weighing."),
        ],
        handling=("Store at -20 °C under dry, dark conditions. Open under nitrogen if available. Prepare "
                  "solutions with deoxygenated water at pH 3–5 and use them promptly; do not autoclave."),
        formulation=("Glutathione is used in aqueous serums and powders. Because it oxidises readily, consider "
                     "anhydrous or low-water formats, nitrogen-purged processing and opaque packaging. Confirm "
                     "compatibility with preservatives such as phenoxyethanol."),
        applications=["Brightening serums", "Antioxidant formulations", "Redox-biology research", "Cosmetic powder formats"],
        faqs=[
            ("Is this reduced or oxidised glutathione?",
             "This is L-glutathione in the reduced (GSH) form, with the oxidised GSSG fraction controlled and reported on the COA. If you need GSSG specifically, request a separate quotation."),
            ("Why is glutathione supplied as a powder?",
             "The reduced form is more stable as a dry powder than in aqueous solution. Aqueous stocks oxidise quickly and should be prepared fresh, deoxygenated and protected from light."),
        ],
        related=["nad-plus", "ghk-cu", "nmn"],
        tags=["antioxidant", "brightening", "redox", "glutathione", "cosmetic"],
        meta_desc="Bulk L-glutathione (reduced), CAS 70-18-8, ≥99% HPLC. 400/600/1500 mg kits, low GSSG, COA per batch, worldwide shipping. Request a quote.",
    ),

    # ------------------------------------------------------------------ repair
    P(
        slug="bpc-157",
        name="BPC-157",
        full_name="BPC-157 (Body Protection Compound-157)",
        title_name="BPC-157",
        cat="repair",
        cas="137525-51-0",
        seq="Gly-Glu-Pro-Pro-Pro-Gly-Lys-Pro-Ala-Asp-Asp-Ala-Gly-Leu-Val",
        mol="C62H98N16O22",
        mw="1419.53 Da",
        tagline="A pentadecapeptide widely used in preclinical tissue-repair research.",
        intro=("BPC-157 is a synthetic 15-amino-acid peptide derived from a gastric-juice protein. It is one "
               "of the most studied repair peptides in preclinical models of gastrointestinal, tendon, "
               "muscle and skin injury, and is supplied here as a research-grade lyophilized powder."),
        overview=[
            ("BPC-157's sequence is rich in proline and acidic residues, giving it unusual stability in "
             "aqueous and acidic environments compared with many short peptides. Preclinical literature has "
             "examined its effects on angiogenesis, fibroblast migration and inflammatory signalling."),
            ("Vivalr supplies BPC-157 as the acetate salt, with HPLC purity and MS identity confirmed per "
             "batch. It is intended strictly for laboratory research and is not for human or veterinary use."),
        ],
        research=[
            ("Gastrointestinal repair", "Studied in preclinical models of gastric, intestinal and anastomotic healing."),
            ("Angiogenesis", "Investigated for VEGFR2-linked angiogenic signalling and vessel formation."),
            ("Tendon & muscle models", "Evaluated for fibroblast migration, collagen deposition and soft-tissue repair."),
            ("Inflammatory signalling", "Studied for modulation of cytokine response in injury models."),
        ],
        synthesis=("BPC-157 is synthesized by Fmoc SPPS, cleaved with TFA/TIS/water, precipitated in cold "
                    "ether and purified by preparative C18 HPLC. The acetate salt is lyophilized and tested "
                    "for purity, water content and mass identity."),
        risks=[
            ("Acid hydrolysis at Asp-Pro", "medium", "The Asp-Pro motif is acid-labile over prolonged exposure. Keep lyophilized material dry and avoid strongly acidic stock solutions."),
            ("Aggregation at high concentration", "medium", "Prepare working solutions at modest concentration and avoid repeated freeze–thaw cycles."),
            ("Moisture uptake", "medium", "Lyophilized powder is hygroscopic; equilibrate sealed vials to room temperature before opening."),
        ],
        handling=("Store sealed at -20 °C, desiccated and protected from light. For laboratory use, "
                  "reconstitute with sterile water or a compatible buffer under aseptic conditions; aliquot "
                  "and avoid repeated freeze–thaw."),
        formulation=("BPC-157 is used in aqueous research formulations. Its stability is pH- and "
                     "temperature-dependent; prepare fresh working solutions and validate analytical recovery "
                     "in your buffer system."),
        applications=["Gastrointestinal research", "Soft-tissue repair models", "Angiogenesis studies", "Peptide-stability research"],
        faqs=[
            ("Is BPC-157 supplied as acetate or arginate?",
             "The standard catalogue grade is the acetate salt. Arginine and other counter-ion forms can be quoted on request, subject to minimum batch size."),
            ("How should BPC-157 be stored for long-term research use?",
             "Keep the lyophilized powder sealed at -20 °C with desiccant and protect it from light. Reconstituted working aliquots should be stored at -20 °C and used without repeated freeze–thaw."),
        ],
        related=["tb-500", "bpc-157-tb-500-blend", "kpv"],
        tags=["repair", "gastrointestinal", "angiogenesis", "tendon", "BPC"],
        featured=True,
        meta_desc="Bulk BPC-157, CAS 137525-51-0, ≥99% HPLC, MS verified. 2/5/10/20 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="tb-500",
        name="TB-500",
        full_name="TB-500 (Thymosin Beta-4)",
        title_name="TB-500",
        cat="repair",
        cas="77591-33-4",
        seq="Ac-SDKPDMAEIEKFDKSKLKKTETQEKNPLPSKETIEQEKQAGES (43 aa)",
        mol="C212H350N56O78S",
        mw="4963.44 Da",
        tagline="Thymosin beta-4 for actin dynamics, cell migration and repair research.",
        intro=("TB-500 is the synthetic, N-acetylated form of thymosin beta-4, a 43-amino-acid actin-binding "
               "peptide. It is used in preclinical research on cell migration, angiogenesis and "
               "extracellular-matrix remodelling."),
        overview=[
            ("Thymosin beta-4 sequesters actin monomers and influences cytoskeletal dynamics, which in turn "
             "affects cell migration and tissue remodelling. TB-500 reproduces the full acetylated sequence "
             "and is supplied as a high-purity lyophilized powder."),
            ("Because it is a relatively large peptide, TB-500 requires careful handling to avoid aggregation "
             "and oxidation. Vivalr tests identity by MS and purity by HPLC for every lot."),
        ],
        research=[
            ("Actin sequestration", "Binds G-actin and influences cytoskeletal dynamics in migrating cells."),
            ("Cell migration", "Studied for keratinocyte and endothelial cell migration in repair models."),
            ("Angiogenesis", "Investigated for vessel formation and endothelial signalling."),
            ("ECM remodelling", "Evaluated for matrix deposition and scar-related pathways in preclinical models."),
        ],
        synthesis=("TB-500 is produced by Fmoc SPPS, with the N-terminal acetyl group added on resin or in "
                    "solution. The peptide is cleaved, precipitated and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Methionine oxidation", "high", "The sequence contains methionine; oxidation shifts mass and retention time. Use low-oxygen handling and antioxidant-free packaging."),
            ("Aggregation", "medium", "Large peptides can self-associate at high concentration. Keep stocks dilute and avoid repeated freeze–thaw."),
            ("Proteolytic degradation", "medium", "Use aseptic technique and store working solutions cold; do not add protease-containing excipients."),
        ],
        handling=("Store at -20 °C, desiccated. Equilibrate to room temperature before opening. Reconstitute "
                  "under aseptic conditions, aliquot into single-use volumes and store at -20 °C."),
        formulation=("TB-500 is used in aqueous buffers for laboratory research. Avoid high shear and "
                     "foaming, which can promote aggregation of large peptides."),
        applications=["Cell-migration research", "Angiogenesis models", "Tissue-remodelling studies", "Actin-biology research"],
        faqs=[
            ("Is TB-500 the same as thymosin beta-4?",
             "The material supplied here is the N-acetylated 43-amino-acid thymosin beta-4 sequence (CAS 77591-33-4). Some suppliers use the short 17–23 fragment under similar names, so confirm the exact sequence and mass on the batch COA before comparing prices."),
            ("What is the molecular weight of TB-500?",
             "The acetylated 43-amino-acid peptide has a calculated molecular weight of 4963.44 Da and the formula C212H350N56O78S. Batch identity is confirmed by ESI-MS."),
        ],
        related=["bpc-157", "bpc-157-tb-500-blend", "glow"],
        tags=["repair", "thymosin", "actin", "cell migration", "TB4"],
        featured=True,
        meta_desc="Bulk TB-500 (thymosin beta-4), CAS 77591-33-4, ≥99% HPLC, MS verified. 2/5/10 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="bpc-157-tb-500-blend",
        name="BPC-157 / TB-500 Blend",
        full_name="BPC-157 + TB-500 Repair Blend",
        title_name="BPC-157 / TB-500 Blend",
        cat="blend",
        cas="— (multi-component blend)",
        seq="BPC-157 + TB-500, 1:1 ratio",
        mol="Components: C62H98N16O22; C212H350N56O78S",
        mw="1419.53 Da + 4963.44 Da",
        tagline="A 1:1 repair-peptide blend supplied as a single lyophilized kit.",
        intro=("The BPC-157 / TB-500 blend combines two of the most widely studied repair peptides in a "
               "single lyophilized vial. It is supplied in 5+5, 10+10 and 15+15 mg kits for laboratory "
               "research, with component-level identity and purity data."),
        overview=[
            ("BPC-157 and TB-500 act on different parts of the repair cascade: BPC-157 is associated with "
             "angiogenic and gastrointestinal signalling, while TB-500 is linked to actin dynamics and cell "
             "migration. Researchers combine them to study complementary repair pathways."),
            ("Each component is synthesized and purified separately before being combined. This matters for "
             "documentation: the COA reports each peptide's purity and identity, not just a single blend "
             "value."),
        ],
        research=[
            ("Complementary repair pathways", "Combines angiogenic and cytoskeletal repair signalling in one research format."),
            ("Tendon & muscle models", "Used in preclinical soft-tissue repair studies."),
            ("Blend stability", "Evaluated for co-lyophilization compatibility and moisture control."),
            ("Custom ratios", "Available on request for researchers who need a non-1:1 ratio."),
        ],
        synthesis=("BPC-157 and TB-500 are synthesized and HPLC-purified independently. The purified "
                    "peptides are quantified, combined in a 1:1 mass ratio, sterile-filtered and "
                    "co-lyophilized. Each component is identity-tested before blending."),
        risks=[
            ("Component-specific oxidation", "medium", "TB-500 contains methionine and is the more oxidation-sensitive component; protect the blend from light and oxygen."),
            ("Aggregation", "medium", "The large TB-500 peptide can aggregate; keep working solutions dilute and avoid foaming."),
            ("Content uniformity", "medium", "Co-lyophilized blends require validated mixing; request the blend uniformity data for your batch."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute under aseptic "
                  "conditions and aliquot immediately; avoid repeated freeze–thaw."),
        formulation=("Use a neutral to slightly acidic buffer for laboratory work. Do not add strong "
                     "oxidizers or protease-containing excipients."),
        applications=["Soft-tissue repair research", "Tendon and muscle models", "Combination-peptide studies", "Blend-stability research"],
        faqs=[
            ("What ratios are available?",
             "The standard catalogue ratios are 5+5, 10+10 and 15+15 mg per vial. Custom ratios and total fill weights can be quoted from 10 kits upward."),
            ("Does the COA cover both peptides?",
             "Yes. The blend COA reports the identity and purity of BPC-157 and TB-500 separately, plus the fill weight and moisture content of the finished vial."),
        ],
        related=["bpc-157", "tb-500", "glow"],
        tags=["blend", "repair", "BPC", "TB500", "soft tissue"],
        featured=True,
        meta_desc="BPC-157 / TB-500 1:1 repair blend, 5+5 to 15+15 mg kits. ≥99% HPLC per component, dual COA, worldwide shipping. Request a bulk quote.",
    ),
    P(
        slug="glow",
        name="GLOW",
        full_name="GLOW Peptide Blend (GHK-Cu + BPC-157 + TB-500)",
        title_name="GLOW Peptide Blend",
        cat="blend",
        cas="— (multi-component blend)",
        seq="GHK-Cu 50 mg + BPC-157 10 mg + TB-500 10 mg",
        mol="Components: C14H22N6O4·Cu; C62H98N16O22; C212H350N56O78S",
        mw="403.94 + 1419.53 + 4963.44 Da",
        appearance="Blue to off-white lyophilized cake",
        tagline="The 70 mg skin-and-repair research blend: GHK-Cu, BPC-157 and TB-500.",
        intro=("GLOW is a three-component research blend containing GHK-Cu (50 mg), BPC-157 (10 mg) and "
               "TB-500 (10 mg) per vial — 70 mg total. It combines a copper peptide with two repair "
               "peptides in a single lyophilized kit."),
        overview=[
            ("The GLOW concept pairs GHK-Cu's collagen and copper signalling with BPC-157's angiogenic "
             "profile and TB-500's actin-binding repair biology. It is used in laboratory research where a "
             "single, documented blend simplifies handling."),
            ("Vivalr prepares GLOW from independently synthesized and purified components. The blue colour "
             "of the copper peptide is expected and can vary slightly between batches; the COA reports each "
             "component and the total fill."),
        ],
        research=[
            ("Skin & ECM research", "GHK-Cu contributes copper-peptide collagen and matrix signalling."),
            ("Repair signalling", "BPC-157 and TB-500 add angiogenic and cytoskeletal repair pathways."),
            ("Combination studies", "Used where researchers need a fixed three-peptide ratio."),
            ("Blend characterization", "Component identity and purity are reported individually."),
        ],
        synthesis=("GHK-Cu is synthesized and copper-complexed; BPC-157 and TB-500 are synthesized and "
                    "purified separately. The three components are quantified, blended and co-lyophilized. "
                    "Each component is tested for identity and purity before blending."),
        risks=[
            ("Copper-peptide colour shift", "medium", "The blue complex can shift colour with pH or moisture. Colour variation alone is not a purity indicator; rely on HPLC and MS."),
            ("Oxidation of TB-500", "medium", "TB-500 methionine is oxidation-sensitive. Protect from light and oxygen."),
            ("Component segregation", "medium", "Confirm blend uniformity for the batch, especially when scaling."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Equilibrate before opening. "
                  "Reconstitute under aseptic conditions and aliquot."),
        formulation=("For laboratory research only. Use a pH 5–6 buffer to keep the copper complex stable; "
                     "avoid chelators and strong reducing agents."),
        applications=["Skin-repair research", "Copper-peptide combination studies", "Regenerative-medicine models", "Blend reference standards"],
        faqs=[
            ("What is in the GLOW 70 mg blend?",
             "Each 70 mg vial contains GHK-Cu 50 mg, BPC-157 10 mg and TB-500 10 mg. The components are co-lyophilized and tested individually before blending."),
            ("Can the GLOW ratio be customised?",
             "Yes. Custom ratios and fill weights are available from 10 kits upward, subject to a technical review of co-lyophilization compatibility."),
        ],
        related=["klow", "ghk-cu", "bpc-157", "tb-500"],
        tags=["GLOW", "blend", "GHK-Cu", "BPC-157", "TB-500", "skin"],
        featured=True,
        meta_desc="GLOW 70 mg research blend: GHK-Cu 50 mg + BPC-157 10 mg + TB-500 10 mg. ≥99% HPLC per component, COA, worldwide shipping. Request a quote.",
    ),
    P(
        slug="klow",
        name="KLOW",
        full_name="KLOW Peptide Blend (GHK-Cu + BPC-157 + TB-500 + KPV)",
        title_name="KLOW Peptide Blend",
        cat="blend",
        cas="— (multi-component blend)",
        seq="GHK-Cu 50 mg + BPC-157 10 mg + TB-500 10 mg + KPV 10 mg",
        mol="Components: C14H22N6O4·Cu; C62H98N16O22; C212H350N56O78S; C16H30N4O4",
        mw="403.94 + 1419.53 + 4963.44 + 342.43 Da",
        appearance="Blue to off-white lyophilized cake",
        tagline="GLOW plus KPV: an 80 mg four-peptide blend for repair and inflammation research.",
        intro=("KLOW is an 80 mg research blend of GHK-Cu (50 mg), BPC-157 (10 mg), TB-500 (10 mg) and KPV "
               "(10 mg). It extends the GLOW concept with the anti-inflammatory tripeptide KPV."),
        overview=[
            ("KLOW adds KPV, an alpha-MSH-derived tripeptide studied for NF-κB and inflammatory signalling, "
             "to the GHK-Cu / BPC-157 / TB-500 combination. The result is a four-component blend aimed at "
             "researchers studying repair alongside inflammatory resolution."),
            ("As with GLOW, each component is synthesized and released separately before blending. The "
             "component-level COA is the key documentation advantage of this format."),
        ],
        research=[
            ("Repair + inflammation", "Combines repair peptides with KPV's anti-inflammatory research profile."),
            ("Skin & barrier models", "GHK-Cu and KPV are both studied in skin-barrier and cytokine research."),
            ("Four-component stability", "Evaluated for co-lyophilization and moisture control."),
            ("Fixed-ratio studies", "Designed for reproducible four-peptide experiments."),
        ],
        synthesis=("All four peptides are produced by SPPS and purified independently. GHK-Cu is "
                    "copper-complexed, KPV is converted to its acetate salt, and the four components are "
                    "quantified and co-lyophilized."),
        risks=[
            ("KPV oxidation/hydrolysis", "low", "KPV is a short peptide with good stability; still avoid extreme pH and high heat."),
            ("TB-500 oxidation", "medium", "Protect the blend from oxygen and light to limit methionine oxidation."),
            ("Complex colour shift", "medium", "Copper-peptide colour can vary with pH and moisture; rely on analytical data."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute under aseptic "
                  "conditions and aliquot into single-use volumes."),
        formulation=("Use a pH 5–6 buffer for laboratory handling. Avoid chelators, strong reducing agents "
                     "and prolonged light exposure."),
        applications=["Repair and inflammation research", "Skin-barrier models", "Four-peptide combination studies", "Blend reference standards"],
        faqs=[
            ("How is KLOW different from GLOW?",
             "KLOW is GLOW plus 10 mg KPV, giving 80 mg total per vial. GLOW contains GHK-Cu, BPC-157 and TB-500 only; KLOW adds the anti-inflammatory tripeptide KPV."),
            ("Is KLOW a single peptide?",
             "No. KLOW is a four-component blend. The COA reports each peptide separately, along with total fill weight and moisture."),
        ],
        related=["glow", "kpv", "ghk-cu", "bpc-157"],
        tags=["KLOW", "blend", "KPV", "GHK-Cu", "BPC-157", "TB-500"],
        featured=True,
        meta_desc="KLOW 80 mg research blend: GHK-Cu 50 + BPC-157 10 + TB-500 10 + KPV 10 mg. ≥99% HPLC per component, COA, worldwide shipping. Request a quote.",
    ),
    P(
        slug="epithalon",
        name="Epithalon",
        full_name="Epithalon (Epitalon, AEDG)",
        title_name="Epithalon",
        cat="repair",
        cas="307297-39-8",
        seq="Ala-Glu-Asp-Gly (AEDG)",
        mol="C14H22N4O9",
        mw="390.35 Da",
        tagline="The AEDG tetrapeptide used in telomerase and pineal-aging research.",
        intro=("Epithalon (epitalon) is a synthetic tetrapeptide with the sequence Ala-Glu-Asp-Gly. It is "
               "studied in cellular-aging research, particularly for telomerase-related and pineal "
               "signalling pathways, and is supplied as a high-purity lyophilized powder."),
        overview=[
            ("Epithalon belongs to the short bioregulator peptide family. Its small size, high polarity and "
             "lack of aromatic residues make it analytically straightforward but also highly water-soluble, "
             "which influences how stock solutions should be prepared."),
            ("Vivalr supplies Epithalon as the acetate salt with HPLC purity and MS identity confirmed for "
             "each batch. It is intended for laboratory research only."),
        ],
        research=[
            ("Telomerase research", "Studied for telomerase activity and telomere-length maintenance in cell models."),
            ("Pineal & circadian research", "Investigated for melatonin-related and pineal signalling effects."),
            ("Cellular aging", "Used in senescence and longevity-pathway studies."),
            ("Bioregulator series", "A reference peptide for the Khavinson short-peptide research family."),
        ],
        synthesis=("Epithalon is assembled by Fmoc SPPS, cleaved with TFA, precipitated and purified by "
                    "preparative C18 HPLC. The acetate salt is lyophilized and tested for purity, water "
                    "content and mass identity."),
        risks=[
            ("Hydrolysis at acidic pH", "low", "The peptide is relatively stable but can hydrolyse under strongly acidic or alkaline conditions. Use pH 5–7."),
            ("Moisture uptake", "medium", "The lyophilized powder is hygroscopic; seal with desiccant and equilibrate before opening."),
            ("Microbial growth in stock", "low", "Aqueous stocks support microbial growth; filter sterilise and store cold."),
        ],
        handling=("Store sealed at -20 °C, protected from light and moisture. Reconstitute with sterile "
                  "water or a neutral buffer under aseptic conditions."),
        formulation=("Epithalon is highly water-soluble and suited to aqueous research formulations. Avoid "
                     "extreme pH and repeated freeze–thaw."),
        applications=["Telomerase research", "Cellular-aging studies", "Pineal research", "Bioregulator reference work"],
        faqs=[
            ("Is Epithalon the same as Epitalon?",
             "Yes. Epithalon and Epitalon are alternative spellings for the same AEDG tetrapeptide, CAS 307297-39-8."),
            ("What is the sequence and molecular weight of Epithalon?",
             "The sequence is Ala-Glu-Asp-Gly, formula C14H22N4O9, calculated molecular weight 390.35 Da."),
        ],
        related=["pinealon", "nad-plus", "cortagen"],
        tags=["epithalon", "telomerase", "longevity", "bioregulator", "AEDG"],
        featured=True,
        meta_desc="Bulk Epithalon (Epitalon, AEDG), CAS 307297-39-8, ≥99% HPLC, MS verified. 10/50 mg 10-vial kits, COA, worldwide shipping. Request a quote.",
    ),
    P(
        slug="pinealon",
        name="Pinealon",
        full_name="Pinealon (EDR)",
        title_name="Pinealon",
        cat="repair",
        cas="175175-23-2",
        seq="Glu-Asp-Arg (EDR)",
        mol="C15H26N6O8",
        mw="418.40 Da",
        tagline="The EDR tripeptide studied in neuroprotection and brain-aging models.",
        intro=("Pinealon is a synthetic tripeptide with the sequence Glu-Asp-Arg. It is studied as a "
               "neuroprotective bioregulator peptide in cell and animal models of brain aging, oxidative "
               "stress and neuronal survival."),
        overview=[
            ("Pinealon's charge profile — two acidic residues and a basic arginine — makes it highly "
             "water-soluble and gives it a distinct interaction profile at the cell membrane. It is one of "
             "the most researched short bioregulators in neuro-aging models."),
            ("Vivalr supplies Pinealon as a ≥99% HPLC-purified lyophilized powder with MS identity data."),
        ],
        research=[
            ("Neuroprotection", "Studied for neuronal survival under oxidative and excitotoxic stress."),
            ("Brain-aging models", "Investigated for cognitive and neurotrophic signalling in aging models."),
            ("Oxidative stress", "Evaluated for antioxidant and mitochondrial effects in neural cells."),
            ("Bioregulator research", "A reference tripeptide in the Khavinson peptide family."),
        ],
        synthesis=("Pinealon is produced by Fmoc SPPS, cleaved and purified by preparative C18 HPLC, then "
                    "converted to the acetate salt and lyophilized."),
        risks=[
            ("Arginine side-chain degradation", "low", "Protect from strong alkali and prolonged heat; arginine-containing peptides can degrade at high pH."),
            ("Hygroscopicity", "medium", "Store with desiccant and equilibrate before weighing."),
            ("Peptide hydrolysis", "low", "Use pH 5–7 and avoid autoclaving."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute with sterile water or "
                  "a neutral buffer for laboratory use."),
        formulation=("Pinealon is freely water-soluble. Prepare fresh aqueous stocks and avoid repeated "
                     "freeze–thaw; filter sterilise if required."),
        applications=["Neuroprotection research", "Brain-aging models", "Oxidative-stress studies", "Bioregulator screening"],
        faqs=[
            ("What is the sequence of Pinealon?",
             "Pinealon is Glu-Asp-Arg (EDR), CAS 175175-23-2, with a calculated molecular weight of 418.40 Da."),
            ("How does Pinealon differ from Epithalon?",
             "They are different short peptides: Pinealon is EDR and Epithalon is AEDG. Both belong to the bioregulator family but have distinct research profiles, with Pinealon focused on neural models."),
        ],
        related=["epithalon", "cortagen", "humanin"],
        tags=["pinealon", "neuroprotection", "bioregulator", "brain", "EDR"],
        meta_desc="Bulk Pinealon (EDR), CAS 175175-23-2, ≥99% HPLC, MS verified. 5/10/20 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="kpv",
        name="KPV",
        full_name="KPV (Lys-Pro-Val)",
        title_name="KPV",
        cat="repair",
        cas="67727-97-3",
        seq="Lys-Pro-Val",
        mol="C16H30N4O4",
        mw="342.43 Da",
        tagline="The alpha-MSH tripeptide fragment for inflammation and barrier research.",
        intro=("KPV is the C-terminal tripeptide of alpha-melanocyte-stimulating hormone (α-MSH), with the "
               "sequence Lys-Pro-Val. It is studied for anti-inflammatory and barrier-protective activity, "
               "particularly in skin and intestinal models."),
        overview=[
            ("KPV retains the anti-inflammatory motif of α-MSH without the melanotropic activity of the full "
             "hormone. That selectivity is why it is widely used in inflammation and epithelial-barrier "
             "research."),
            ("Vivalr supplies KPV as a ≥99% HPLC-purified acetate salt. It is also a component of the KLOW "
             "research blend."),
        ],
        research=[
            ("NF-κB signalling", "Studied for inhibition of NF-κB activation and pro-inflammatory cytokine release."),
            ("Skin-barrier models", "Evaluated for barrier protection and inflammatory resolution in keratinocyte models."),
            ("Intestinal inflammation", "Investigated in models of mucosal inflammation."),
            ("Combination research", "Used with repair peptides such as BPC-157 and GHK-Cu."),
        ],
        synthesis=("KPV is synthesized by Fmoc SPPS, cleaved and purified by preparative HPLC. The acetate "
                    "salt is prepared by ion exchange and lyophilized."),
        risks=[
            ("Hydrolysis", "low", "Short peptides are relatively stable; avoid extreme pH and heat."),
            ("Moisture", "medium", "Store desiccated; the powder is hygroscopic."),
            ("Microbial growth", "low", "Aqueous stocks should be filter-sterilised and refrigerated."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute with sterile water or "
                  "buffer under aseptic conditions."),
        formulation=("KPV is highly water-soluble and compatible with aqueous gels and serums. Avoid strong "
                     "oxidizers and extreme pH."),
        applications=["Anti-inflammatory research", "Skin-barrier models", "Intestinal inflammation studies", "KLOW-style blends"],
        faqs=[
            ("What does KPV stand for?",
             "KPV is the tripeptide Lys-Pro-Val, derived from the C-terminus of alpha-MSH. CAS 67727-97-3."),
            ("Is KPV part of the KLOW blend?",
             "Yes. KLOW contains GHK-Cu 50 mg, BPC-157 10 mg, TB-500 10 mg and KPV 10 mg per 80 mg vial."),
        ],
        related=["klow", "bpc-157", "ghk-cu"],
        tags=["KPV", "anti-inflammatory", "barrier", "alpha-MSH", "repair"],
        meta_desc="Bulk KPV (Lys-Pro-Val), CAS 67727-97-3, ≥99% HPLC, MS verified. 5/10 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="thymosin-alpha-1",
        name="Thymosin Alpha-1",
        full_name="Thymosin Alpha-1 (Tα1)",
        title_name="Thymosin Alpha-1",
        cat="repair",
        cas="62304-98-7",
        seq="Ac-Ser-Asp-Ala-Ala-Val-Asp-Thr-Ser-Ser-Glu-Ile-Thr-Thr-Lys-Asp-Leu-Lys-Glu-Lys-Lys-Glu-Val-Val-Glu-Glu-Ala-Glu-Asn (28 aa)",
        mol="C129H215N33O55",
        mw="3108.30 Da",
        tagline="A 28-amino-acid thymic peptide for immune-signalling research.",
        intro=("Thymosin alpha-1 is an N-acetylated 28-amino-acid peptide derived from thymosin fraction 5. "
               "It is studied for T-cell maturation, innate immune signalling and immune-modulation in "
               "preclinical and clinical research."),
        overview=[
            ("Tα1 is one of the most characterized thymic peptides. Its acetylated N-terminus and acidic "
             "C-terminal region contribute to its stability and receptor interactions. It is used widely in "
             "immunology research."),
            ("Vivalr supplies synthetic Tα1 as a lyophilized acetate salt with HPLC and MS release data."),
        ],
        research=[
            ("T-cell maturation", "Studied for T-cell differentiation and thymocyte maturation."),
            ("Innate immunity", "Investigated for Toll-like receptor and dendritic-cell signalling."),
            ("Immune modulation", "Used in models of immunosuppression and chronic infection."),
            ("Vaccine research", "Evaluated as an immunological adjuvant in preclinical studies."),
        ],
        synthesis=("Thymosin alpha-1 is produced by Fmoc SPPS, N-terminally acetylated, cleaved and purified "
                    "by preparative C18 HPLC. The acetate salt is lyophilized and identity-tested by MS."),
        risks=[
            ("Aggregation", "medium", "The 28-mer can aggregate at high concentration; keep stocks dilute and avoid foaming."),
            ("Oxidation", "low", "No methionine or cysteine, but protect from strong oxidizers."),
            ("Proteolysis", "medium", "Use aseptic handling and cold storage for working solutions."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute under aseptic "
                  "conditions and aliquot."),
        formulation=("Use a neutral buffer for laboratory work. Avoid high shear and repeated freeze–thaw."),
        applications=["Immunology research", "T-cell studies", "Dendritic-cell research", "Vaccine-adjuvant models"],
        faqs=[
            ("Is thymosin alpha-1 the same as thymosin beta-4?",
             "No. Thymosin alpha-1 is a 28-amino-acid thymic peptide (CAS 62304-98-7); TB-500 is the 43-amino-acid thymosin beta-4. They have different sequences and research profiles."),
            ("What is the molecular weight of thymosin alpha-1?",
             "The acetylated 28-amino-acid peptide has a calculated molecular weight of 3108.30 Da and formula C129H215N33O55."),
        ],
        related=["thymalin", "kpv", "bpc-157"],
        tags=["immune", "thymosin", "T-cell", "peptide", "repair"],
        meta_desc="Bulk thymosin alpha-1, CAS 62304-98-7, ≥99% HPLC, MS verified. 5/10 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="ara-290",
        name="ARA-290",
        full_name="ARA-290 (Cibinetide)",
        title_name="ARA-290",
        cat="repair",
        cas="1208243-50-8",
        seq="EPO-derived linear 11-mer (Cibinetide)",
        mol="—",
        mw="≈1257 Da",
        tagline="An EPO-derived peptide for innate-repair-receptor research.",
        intro=("ARA-290 (cibinetide) is a synthetic 11-amino-acid peptide derived from the helix-B region "
               "of erythropoietin. It is studied for tissue-protective signalling through the innate repair "
               "receptor without stimulating erythropoiesis."),
        overview=[
            ("ARA-290 was designed to separate erythropoietin's tissue-protective effects from its "
             "erythropoietic activity. It is used in preclinical research on neuropathy, ischemia and "
             "inflammatory injury."),
            ("Vivalr supplies ARA-290 as a high-purity lyophilized acetate salt with MS identity data."),
        ],
        research=[
            ("Innate repair receptor", "Studied as an EPOR/CD131 agonist with tissue-protective signalling."),
            ("Neuropathy models", "Investigated for peripheral-nerve repair and neuropathic pain in preclinical studies."),
            ("Ischemia-reperfusion", "Evaluated in cardiac, renal and retinal injury models."),
            ("Inflammation", "Studied for modulation of inflammatory cascades."),
        ],
        synthesis=("ARA-290 is assembled by Fmoc SPPS, cleaved and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt. Identity is confirmed by ESI-MS."),
        risks=[
            ("Aggregation", "medium", "The 11-mer can self-associate; keep stock solutions dilute and avoid foaming."),
            ("Hydrolysis", "low", "Avoid extreme pH and prolonged heat."),
            ("Moisture", "medium", "Store desiccated and equilibrate before opening."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute under aseptic "
                  "conditions for laboratory use."),
        formulation=("Use a neutral buffer and avoid repeated freeze–thaw. Filter sterilise working "
                     "solutions if required."),
        applications=["Tissue-protection research", "Neuropathy models", "Ischemia research", "Innate-repair-receptor studies"],
        faqs=[
            ("What is ARA-290 also called?",
             "ARA-290 is also known as cibinetide, CAS 1208243-50-8. It is an EPO-derived 11-amino-acid peptide."),
            ("Does ARA-290 stimulate erythropoiesis?",
             "ARA-290 was designed to act through the innate repair receptor rather than the classical erythropoietin receptor. It is used as a research peptide, not a therapeutic."),
        ],
        related=["bpc-157", "ll-37", "thymosin-alpha-1"],
        tags=["ARA-290", "cibinetide", "EPO", "tissue repair", "neuropathy"],
        meta_desc="Bulk ARA-290 (cibinetide), CAS 1208243-50-8, ≥99% HPLC, MS verified. 10/16/40 mg 10-vial kits, COA, worldwide shipping. Request a quote.",
    ),
    P(
        slug="ll-37",
        name="LL-37",
        full_name="LL-37 (Cathelicidin LL-37)",
        title_name="LL-37",
        cat="repair",
        cas="154947-66-7",
        seq="LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES (37 aa)",
        mol="C205H340N60O53",
        mw="4493.30 Da",
        tagline="The human cathelicidin peptide for antimicrobial and wound-repair research.",
        intro=("LL-37 is the only human cathelicidin-derived antimicrobial peptide, a 37-amino-acid "
               "amphipathic helix. It is widely studied for antimicrobial activity, innate immunity, "
               "biofilm disruption and wound-repair signalling."),
        overview=[
            ("LL-37's cationic, amphipathic structure lets it interact with microbial membranes and host "
             "cells. That dual activity makes it a model peptide for innate-immunity and tissue-repair "
             "research, but also a challenging molecule to formulate."),
            ("Vivalr supplies synthetic LL-37 as a ≥99% HPLC-purified lyophilized powder with MS identity."),
        ],
        research=[
            ("Antimicrobial activity", "Studied against bacteria, fungi and biofilm-forming organisms."),
            ("Innate immunity", "Investigated for chemotaxis, cytokine modulation and host-defence signalling."),
            ("Wound repair", "Evaluated for keratinocyte migration, angiogenesis and re-epithelialization."),
            ("Biofilm disruption", "Studied for membrane disruption and biofilm inhibition."),
        ],
        synthesis=("LL-37 is produced by Fmoc SPPS, cleaved and purified by preparative C18 HPLC. The "
                    "acetate salt is lyophilized; identity is confirmed by ESI-MS."),
        risks=[
            ("Aggregation & membrane activity", "high", "The amphipathic peptide self-assembles and can adsorb to surfaces. Use low-binding tubes and avoid foaming."),
            ("Proteolysis", "medium", "Susceptible to proteases; handle aseptically and store working solutions cold."),
            ("pH-dependent charge", "medium", "Activity and solubility depend on pH; use a defined buffer and validate."),
        ],
        handling=("Store at -20 °C, desiccated. Use low-binding tubes, avoid high shear, and prepare "
                  "working solutions in a defined buffer."),
        formulation=("LL-37 adsorbs strongly to glass and some plastics. Use low-binding labware and "
                     "include a compatible carrier protein or surfactant only if your assay allows."),
        applications=["Antimicrobial research", "Innate-immunity studies", "Wound-repair models", "Biofilm research"],
        faqs=[
            ("What is LL-37?",
             "LL-37 is the 37-amino-acid human cathelicidin antimicrobial peptide, CAS 154947-66-7, with the sequence LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES."),
            ("Why does LL-37 adsorb to labware?",
             "Its cationic and amphipathic character promotes surface adsorption and self-assembly. Use low-binding tubes and avoid foaming to improve recovery."),
        ],
        related=["kpv", "ara-290", "bpc-157"],
        tags=["LL-37", "cathelicidin", "antimicrobial", "wound repair", "innate immunity"],
        meta_desc="Bulk LL-37 cathelicidin peptide, CAS 154947-66-7, ≥99% HPLC, MS verified. 5 mg and liquid-format kits, COA, worldwide shipping. Request a quote.",
    ),
    P(
        slug="foxo4-dri",
        name="FOXO4-DRI",
        full_name="FOXO4-DRI (D-Retro-Inverso)",
        title_name="FOXO4-DRI",
        cat="repair",
        cas="2460055-10-9",
        seq="D-retro-inverso FOXO4 p53-binding domain",
        mol="—",
        mw="≈5.0 kDa (sequence-dependent)",
        tagline="A senolytic D-retro-inverso peptide for p53–FOXO4 research.",
        intro=("FOXO4-DRI is a D-retro-inverso peptide designed to disrupt the FOXO4–p53 interaction. It is "
               "used in senescence and senolytic research to study p53-dependent apoptosis in senescent "
               "cells."),
        overview=[
            ("The D-retro-inverso backbone reverses the peptide's handedness, which increases protease "
             "resistance and alters its interaction with the FOXO4–p53 complex. It is a specialised research "
             "tool rather than a general repair peptide."),
            ("Vivalr supplies FOXO4-DRI as a high-purity lyophilized powder with MS identity confirmation."),
        ],
        research=[
            ("Senolytic research", "Studied for selective effects on senescent cells in vitro and in vivo."),
            ("p53–FOXO4 axis", "Designed to disrupt the FOXO4–p53 interaction that sustains senescence."),
            ("Aging models", "Used in preclinical aging and tissue-dysfunction studies."),
            ("D-peptide stability", "The retro-inverso backbone is more resistant to proteases than L-peptides."),
        ],
        synthesis=("FOXO4-DRI is assembled from D-amino acids in retro-inverso order by SPPS, purified by "
                    "preparative HPLC and lyophilized. Identity is confirmed by MS."),
        risks=[
            ("Aggregation", "medium", "D-peptides can aggregate; keep stocks dilute and avoid foaming."),
            ("Batch-specific sequence", "medium", "Confirm the exact retro-inverso sequence and mass with your batch COA."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute under aseptic "
                  "conditions in a defined buffer."),
        formulation=("Use low-binding labware and a neutral buffer. Avoid repeated freeze–thaw."),
        applications=["Senescence research", "Senolytic screening", "Aging models", "Protein-interaction studies"],
        faqs=[
            ("What does D-retro-inverso mean?",
             "The peptide is built from D-amino acids in reverse sequence order. This backbone increases protease resistance and can preserve the shape of the original binding motif."),
            ("Is FOXO4-DRI sequence-specific?",
             "Yes. The exact sequence and mass should be confirmed against the batch COA; small differences in the retro-inverso design change activity and analytical behaviour."),
        ],
        related=["ss-31", "humanin", "nad-plus"],
        tags=["FOXO4", "senolytic", "senescence", "aging", "D-peptide"],
        meta_desc="Bulk FOXO4-DRI senolytic peptide, CAS 2460055-10-9, ≥99% HPLC, MS verified. 2/10 mg kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="ss-31",
        name="SS-31",
        full_name="SS-31 (Elamipretide)",
        title_name="SS-31",
        cat="repair",
        cas="736992-21-5",
        seq="D-Arg-Dmt-Lys-Phe-NH2",
        mol="C32H49N9O5",
        mw="639.80 Da",
        tagline="A mitochondria-targeted tetrapeptide for cardiolipin and bioenergetics research.",
        intro=("SS-31 (elamipretide) is a mitochondria-targeted tetrapeptide that binds cardiolipin on the "
               "inner mitochondrial membrane. It is studied for mitochondrial bioenergetics, oxidative "
               "stress and ischemia-reperfusion injury."),
        overview=[
            ("SS-31 concentrates at the inner mitochondrial membrane through its alternating aromatic and "
             "cationic residues. Its interaction with cardiolipin is the basis of its research use in "
             "mitochondrial dysfunction models."),
            ("Vivalr supplies SS-31 as a ≥99% HPLC-purified lyophilized powder with MS identity data."),
        ],
        research=[
            ("Cardiolipin binding", "Studied for stabilisation of cardiolipin-rich membrane domains."),
            ("Mitochondrial bioenergetics", "Investigated for ATP production and electron-transport efficiency."),
            ("Oxidative stress", "Evaluated for reduction of mitochondrial reactive oxygen species."),
            ("Ischemia-reperfusion", "Used in preclinical cardiac and renal injury models."),
        ],
        synthesis=("SS-31 is produced by Fmoc SPPS with the D-arginine and Dmt residues, C-terminally "
                    "amidated, cleaved and purified by preparative HPLC."),
        risks=[
            ("Oxidation of Dmt", "medium", "The dimethyltyrosine residue is oxidation-sensitive; protect from light and oxygen."),
            ("Aggregation", "low", "Keep stock solutions dilute and avoid foaming."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute under aseptic "
                  "conditions and aliquot."),
        formulation=("Use a neutral buffer and low-binding labware. Avoid strong oxidizers."),
        applications=["Mitochondrial research", "Cardiolipin studies", "Ischemia-reperfusion models", "Bioenergetics assays"],
        faqs=[
            ("What is SS-31 also called?",
             "SS-31 is also known as elamipretide, CAS 736992-21-5. Its sequence is D-Arg-Dmt-Lys-Phe-NH2."),
            ("Why is SS-31 mitochondria-targeted?",
             "The alternating cationic and aromatic residues concentrate the peptide at the inner mitochondrial membrane, where it binds cardiolipin."),
        ],
        related=["mots-c", "humanin", "foxo4-dri"],
        tags=["SS-31", "elamipretide", "mitochondria", "cardiolipin", "aging"],
        meta_desc="Bulk SS-31 (elamipretide), CAS 736992-21-5, ≥99% HPLC, MS verified. 5/10/50 mg kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="mots-c",
        name="MOTS-c",
        full_name="MOTS-c (Mitochondrial Open Reading Frame)",
        title_name="MOTS-c",
        cat="repair",
        cas="1627580-64-6",
        seq="MRWQEMGYIFYPRKLR (16 aa)",
        mol="—",
        mw="≈2174 Da",
        tagline="A mitochondrial-derived peptide for metabolic and AMPK research.",
        intro=("MOTS-c is a 16-amino-acid mitochondrial-derived peptide encoded within the 12S rRNA. It is "
               "studied for metabolic regulation, AMPK activation and mitochondrial stress responses."),
        overview=[
            ("MOTS-c belongs to the mitochondrial-derived peptide family, which signals from the "
             "mitochondrion to the nucleus. Its research profile centres on glucose metabolism, exercise "
             "adaptation and cellular stress."),
            ("Vivalr supplies MOTS-c as a ≥99% HPLC-purified lyophilized powder with MS identity data."),
        ],
        research=[
            ("AMPK activation", "Studied for AMPK-dependent metabolic signalling."),
            ("Glucose metabolism", "Investigated for insulin sensitivity and glucose uptake in models."),
            ("Mitochondrial stress", "Evaluated for mitochondrial-nuclear retrograde signalling."),
            ("Exercise & aging", "Used in metabolic-aging and exercise-adaptation research."),
        ],
        synthesis=("MOTS-c is synthesized by Fmoc SPPS, cleaved and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Methionine oxidation", "high", "The sequence contains methionine; protect from oxygen and light."),
            ("Aggregation", "low", "Keep stocks dilute and avoid foaming."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute under aseptic "
                  "conditions and aliquot."),
        formulation=("Use a neutral buffer. Avoid strong oxidizers and repeated freeze–thaw."),
        applications=["Metabolic research", "AMPK studies", "Mitochondrial biology", "Aging research"],
        faqs=[
            ("What is MOTS-c?",
             "MOTS-c is a 16-amino-acid mitochondrial-derived peptide with the sequence MRWQEMGYIFYPRKLR, CAS 1627580-64-6."),
            ("Why is MOTS-c sensitive to oxidation?",
             "Its methionine residue can oxidise to methionine sulfoxide, changing mass and activity. Protect the powder and solutions from oxygen and light."),
        ],
        related=["ss-31", "humanin", "nad-plus"],
        tags=["MOTS-c", "mitochondria", "AMPK", "metabolism", "aging"],
        meta_desc="Bulk MOTS-c, CAS 1627580-64-6, ≥99% HPLC, MS verified. 10/15/20/40 mg kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="humanin",
        name="Humanin",
        full_name="Humanin (24 aa)",
        title_name="Humanin",
        cat="repair",
        cas="330936-69-1",
        seq="MAPRGFSCLLLLTSEIDLPVKRRA (24 aa)",
        mol="—",
        mw="≈2687 Da",
        tagline="A mitochondrial-derived cytoprotective peptide for stress-response research.",
        intro=("Humanin is a 24-amino-acid mitochondrial-derived peptide with cytoprotective and "
               "stress-response activity. It is studied in neurodegeneration, metabolic stress and "
               "cell-survival models."),
        overview=[
            ("Humanin was one of the first mitochondrial-derived peptides discovered. Its sequence includes "
             "a cysteine and multiple hydrophobic residues, which influence its solubility and its tendency "
             "to associate with membranes."),
            ("Vivalr supplies synthetic Humanin as a ≥99% HPLC-purified lyophilized powder."),
        ],
        research=[
            ("Cytoprotection", "Studied for protection against stress-induced apoptosis."),
            ("Neurodegeneration", "Investigated in neuronal survival and amyloid-toxicity models."),
            ("Metabolic stress", "Evaluated for insulin sensitivity and metabolic signalling."),
            ("Mitochondrial signalling", "A reference mitochondrial-derived peptide in aging research."),
        ],
        synthesis=("Humanin is produced by Fmoc SPPS, cleaved and purified by preparative C18 HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Cysteine oxidation", "high", "The free cysteine can form disulfides or oxidise; use reducing conditions only if your assay permits."),
            ("Aggregation", "medium", "Hydrophobic regions promote self-association; keep stocks dilute."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Avoid repeated freeze–thaw; use "
                  "low-binding tubes."),
        formulation=("Use a defined buffer and low-binding labware. The cysteine residue may require "
                     "careful redox control depending on the assay."),
        applications=["Cytoprotection research", "Neuroscience", "Metabolic studies", "Mitochondrial-derived peptide research"],
        faqs=[
            ("What is the sequence of Humanin?",
             "Humanin is a 24-amino-acid peptide with the sequence MAPRGFSCLLLLTSEIDLPVKRRA, CAS 330936-69-1."),
            ("Why does Humanin require reducing conditions?",
             "The peptide contains a free cysteine that can oxidise or form disulfides. Whether to use a reducing agent depends on your assay and should be validated."),
        ],
        related=["mots-c", "ss-31", "foxo4-dri"],
        tags=["humanin", "mitochondria", "cytoprotection", "neuroprotection", "aging"],
        meta_desc="Bulk Humanin (24 aa), CAS 330936-69-1, ≥99% HPLC, MS verified. 10 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="cortagen",
        name="Cortagen",
        full_name="Cortagen (AEDP)",
        title_name="Cortagen",
        cat="repair",
        cas="335591-03-2",
        seq="Ala-Glu-Asp-Pro (AEDP)",
        mol="C17H26N4O9",
        mw="430.45 Da",
        tagline="A cortical-tissue bioregulator peptide for neuroresearch.",
        intro=("Cortagen is a short synthetic peptide with the sequence Ala-Glu-Asp-Pro, from the "
               "Khavinson bioregulator series. It is studied for cortical-tissue and neuroprotective "
               "signalling in cell and animal models."),
        overview=[
            ("Cortagen is one of a family of short peptides studied for tissue-specific gene-expression "
             "effects. Its acidic, hydrophilic sequence is typical of the series and is highly water-soluble."),
            ("Vivalr supplies Cortagen as a ≥99% HPLC-purified acetate salt with MS identity data."),
        ],
        research=[
            ("Cortical tissue research", "Studied for cortical neuron and brain-tissue signalling."),
            ("Neuroprotection", "Investigated in oxidative-stress and neurodegeneration models."),
            ("Gene-expression research", "A reference peptide in bioregulator transcription studies."),
            ("Peptide screening", "Used alongside other short bioregulators in comparative work."),
        ],
        synthesis=("Cortagen is assembled by Fmoc SPPS, cleaved, purified by preparative HPLC and "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Hydrolysis", "low", "Avoid extreme pH and high heat."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
            ("Microbial growth", "low", "Filter sterilise aqueous stocks and store cold."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute with sterile water or "
                  "neutral buffer."),
        formulation=("Freely water-soluble. Prepare fresh stocks and avoid repeated freeze–thaw."),
        applications=["Neuroscience research", "Cortical-tissue models", "Bioregulator studies", "Neuroprotection screening"],
        faqs=[
            ("What is the Cortagen sequence?",
             "Cortagen is Ala-Glu-Asp-Pro (AEDP), CAS 335591-03-2, with a calculated molecular weight of 430.45 Da."),
            ("How does Cortagen differ from Pinealon?",
             "Cortagen is the AEDP tetrapeptide and Pinealon is the EDR tripeptide. Both are studied in neural models but have different sequences and research profiles."),
        ],
        related=["pinealon", "epithalon", "livagen"],
        tags=["cortagen", "bioregulator", "brain", "neuro", "AEDP"],
        meta_desc="Bulk Cortagen (AEDP), CAS 335591-03-2, ≥99% HPLC, MS verified. 20 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="livagen",
        name="Livagen",
        full_name="Livagen (KEDA)",
        title_name="Livagen",
        cat="repair",
        cas="433257-50-2",
        seq="Lys-Glu-Asp-Ala (KEDA)",
        mol="C18H31N5O9",
        mw="461.52 Da",
        tagline="A chromatin and immune-research bioregulator peptide.",
        intro=("Livagen is a short synthetic peptide with the sequence Lys-Glu-Asp-Ala. It is studied in "
               "chromatin-remodelling, immune-signalling and age-related gene-expression research."),
        overview=[
            ("Livagen's basic lysine residue and acidic Glu-Asp motif give it a mixed charge profile that "
             "distinguishes it from the all-acidic bioregulators. It is used in chromatin and lymphocyte "
             "research."),
            ("Vivalr supplies Livagen as a ≥99% HPLC-purified lyophilized acetate salt."),
        ],
        research=[
            ("Chromatin research", "Studied for effects on chromatin structure and gene accessibility."),
            ("Immune signalling", "Investigated in lymphocyte and cytokine models."),
            ("Age-related gene expression", "A reference peptide in bioregulator transcription studies."),
            ("Cellular stress", "Evaluated for stress-response and senescence markers."),
        ],
        synthesis=("Livagen is produced by Fmoc SPPS, cleaved and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Hydrolysis", "low", "Avoid extreme pH and heat."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
            ("Microbial growth", "low", "Filter sterilise aqueous stocks and store cold."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute with sterile water or "
                  "neutral buffer."),
        formulation=("Freely water-soluble. Use fresh stocks and avoid repeated freeze–thaw."),
        applications=["Chromatin research", "Immune-signalling studies", "Aging research", "Bioregulator screening"],
        faqs=[
            ("What is the Livagen sequence?",
             "Livagen is Lys-Glu-Asp-Ala (KEDA), CAS 433257-50-2, with a calculated molecular weight of 461.52 Da."),
            ("Is Livagen water-soluble?",
             "Yes. The peptide is freely soluble in water and can be reconstituted in a neutral buffer for laboratory use."),
        ],
        related=["cortagen", "crystagen", "epithalon"],
        tags=["livagen", "bioregulator", "chromatin", "immune", "KEDA"],
        meta_desc="Bulk Livagen (KEDA), CAS 433257-50-2, ≥99% HPLC, MS verified. 20 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="crystagen",
        name="Crystagen",
        full_name="Crystagen (EDP)",
        title_name="Crystagen",
        cat="repair",
        cas="Not publicly assigned",
        seq="Glu-Asp-Pro (EDP)",
        mol="C14H21N3O8",
        mw="359.33 Da",
        tagline="An immune-research tripeptide from the bioregulator series.",
        intro=("Crystagen is a synthetic tripeptide with the sequence Glu-Asp-Pro. It is studied in "
               "immune-modulation and thymic-signalling research as part of the short bioregulator peptide "
               "family."),
        overview=[
            ("Crystagen's acidic tripeptide sequence is typical of the bioregulator class. It is highly "
             "water-soluble and analytically straightforward, making it suitable for comparative screening "
             "work."),
            ("Vivalr supplies Crystagen as a ≥99% HPLC-purified lyophilized acetate salt."),
        ],
        research=[
            ("Immune modulation", "Studied for cytokine and immune-cell signalling."),
            ("Thymic research", "Investigated alongside thymic peptides in immune models."),
            ("Gene expression", "A reference tripeptide in bioregulator transcription research."),
            ("Comparative screening", "Used in panels of short bioregulator peptides."),
        ],
        synthesis=("Crystagen is produced by Fmoc SPPS, cleaved, purified by preparative HPLC and "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Hydrolysis", "low", "Avoid extreme pH and high heat."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
            ("Microbial growth", "low", "Filter sterilise aqueous stocks."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute with sterile water or "
                  "neutral buffer."),
        formulation=("Freely water-soluble; prepare fresh stocks and avoid repeated freeze–thaw."),
        applications=["Immune research", "Bioregulator studies", "Thymic-signalling models", "Peptide screening"],
        faqs=[
            ("Does Crystagen have a CAS number?",
             "Crystagen does not have a widely assigned public CAS number. Identity is controlled by the EDP sequence, HPLC purity and MS data on the batch COA."),
            ("What is the Crystagen sequence?",
             "Crystagen is Glu-Asp-Pro (EDP), with a calculated molecular weight of 359.33 Da."),
        ],
        related=["livagen", "thymalin", "cortagen"],
        tags=["crystagen", "bioregulator", "immune", "EDP", "thymic"],
        meta_desc="Bulk Crystagen (EDP) research peptide, ≥99% HPLC, MS verified. 20 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="testagen",
        name="Testagen",
        full_name="Testagen (KEDG)",
        title_name="Testagen",
        cat="repair",
        cas="Not publicly assigned",
        seq="Lys-Glu-Asp-Gly (KEDG)",
        mol="C17H29N5O9",
        mw="447.49 Da",
        tagline="A testicular-tissue bioregulator peptide for endocrine research.",
        intro=("Testagen is a short synthetic peptide with the sequence Lys-Glu-Asp-Gly. It is studied in "
               "testicular-tissue and endocrine-aging research within the bioregulator peptide family."),
        overview=[
            ("Testagen combines a basic lysine with the acidic Glu-Asp-Gly motif. It is used in research on "
             "gonadal tissue and age-related endocrine changes."),
            ("Vivalr supplies Testagen as a ≥99% HPLC-purified lyophilized acetate salt."),
        ],
        research=[
            ("Testicular tissue research", "Studied for gonadal cell and tissue signalling."),
            ("Endocrine aging", "Investigated in age-related hormonal and tissue models."),
            ("Gene-expression research", "A reference peptide in bioregulator transcription studies."),
            ("Comparative screening", "Used in panels of short tissue-specific peptides."),
        ],
        synthesis=("Testagen is produced by Fmoc SPPS, cleaved and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Hydrolysis", "low", "Avoid extreme pH and heat."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
            ("Microbial growth", "low", "Filter sterilise aqueous stocks."),
        ],
        handling=("Store at -20 °C, desiccated. Reconstitute with sterile water or neutral buffer under "
                  "aseptic conditions."),
        formulation=("Freely water-soluble. Prepare fresh stocks and avoid repeated freeze–thaw."),
        applications=["Endocrine research", "Gonadal-tissue models", "Aging research", "Bioregulator screening"],
        faqs=[
            ("Does Testagen have a CAS number?",
             "Testagen does not have a widely assigned public CAS number. Batch identity is controlled by the KEDG sequence, HPLC purity and MS data."),
            ("What is the Testagen sequence?",
             "Testagen is Lys-Glu-Asp-Gly (KEDG), with a calculated molecular weight of 447.49 Da."),
        ],
        related=["livagen", "cortagen", "vesugen"],
        tags=["testagen", "bioregulator", "endocrine", "KEDG", "aging"],
        meta_desc="Bulk Testagen (KEDG) research peptide, ≥99% HPLC, MS verified. 20 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="vesugen",
        name="Vesugen",
        full_name="Vesugen (KED)",
        title_name="Vesugen",
        cat="repair",
        cas="Not publicly assigned",
        seq="Lys-Glu-Asp (KED)",
        mol="C15H26N4O8",
        mw="390.39 Da",
        tagline="A vascular-tissue bioregulator tripeptide.",
        intro=("Vesugen is a synthetic tripeptide with the sequence Lys-Glu-Asp. It is studied in vascular "
               "tissue and endothelial-signalling research as part of the short bioregulator family."),
        overview=[
            ("Vesugen is the tripeptide core shared by several longer bioregulators. It is used in "
             "endothelial and vascular-aging research, often alongside longer tissue-specific peptides."),
            ("Vivalr supplies Vesugen as a ≥99% HPLC-purified lyophilized acetate salt."),
        ],
        research=[
            ("Vascular research", "Studied for endothelial cell and vascular-wall signalling."),
            ("Endothelial function", "Investigated in models of vascular aging and inflammation."),
            ("Gene expression", "A reference tripeptide in bioregulator transcription studies."),
            ("Comparative screening", "Used in panels of short vascular peptides."),
        ],
        synthesis=("Vesugen is produced by Fmoc SPPS, cleaved and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Hydrolysis", "low", "Avoid extreme pH and heat."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
            ("Microbial growth", "low", "Filter sterilise aqueous stocks."),
        ],
        handling=("Store at -20 °C, desiccated. Reconstitute with sterile water or neutral buffer."),
        formulation=("Freely water-soluble; prepare fresh stocks and avoid repeated freeze–thaw."),
        applications=["Vascular research", "Endothelial models", "Aging research", "Bioregulator screening"],
        faqs=[
            ("Does Vesugen have a CAS number?",
             "Vesugen does not have a widely assigned public CAS number. Identity is controlled by the KED sequence, HPLC purity and MS data."),
            ("What is the Vesugen sequence?",
             "Vesugen is Lys-Glu-Asp (KED), with a calculated molecular weight of 370.40 Da."),
        ],
        related=["cardiogen", "testagen", "livagen"],
        tags=["vesugen", "bioregulator", "vascular", "KED", "endothelial"],
        meta_desc="Bulk Vesugen (KED) research peptide, ≥99% HPLC, MS verified. 10 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="cardiogen",
        name="Cardiogen",
        full_name="Cardiogen (AEDR)",
        title_name="Cardiogen",
        cat="repair",
        cas="Not publicly assigned",
        seq="Ala-Glu-Asp-Arg (AEDR)",
        mol="C18H31N7O9",
        mw="489.51 Da",
        tagline="A cardiac-tissue bioregulator peptide for myocardial research.",
        intro=("Cardiogen is a short synthetic peptide with the sequence Ala-Glu-Asp-Arg. It is studied in "
               "cardiac-tissue and myocardial-aging research within the bioregulator peptide family."),
        overview=[
            ("Cardiogen combines the acidic AED motif with a basic arginine, giving it a mixed charge "
             "profile. It is used in cardiac cell and tissue research."),
            ("Vivalr supplies Cardiogen as a ≥99% HPLC-purified lyophilized acetate salt."),
        ],
        research=[
            ("Cardiac tissue research", "Studied for cardiomyocyte and myocardial signalling."),
            ("Cardiac aging", "Investigated in age-related cardiac function models."),
            ("Gene expression", "A reference peptide in bioregulator transcription studies."),
            ("Ischemia models", "Evaluated in preclinical myocardial stress research."),
        ],
        synthesis=("Cardiogen is produced by Fmoc SPPS, cleaved and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Hydrolysis", "low", "Avoid extreme pH and heat."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
            ("Microbial growth", "low", "Filter sterilise aqueous stocks."),
        ],
        handling=("Store at -20 °C, desiccated. Reconstitute with sterile water or neutral buffer."),
        formulation=("Freely water-soluble; prepare fresh stocks and avoid repeated freeze–thaw."),
        applications=["Cardiac research", "Myocardial models", "Aging research", "Bioregulator screening"],
        faqs=[
            ("Does Cardiogen have a CAS number?",
             "Cardiogen does not have a widely assigned public CAS number. Identity is controlled by the AEDR sequence, HPLC purity and MS data."),
            ("What is the Cardiogen sequence?",
             "Cardiogen is Ala-Glu-Asp-Arg (AEDR), with a calculated molecular weight of 489.51 Da."),
        ],
        related=["vesugen", "cortagen", "ss-31"],
        tags=["cardiogen", "bioregulator", "cardiac", "AEDR", "heart"],
        meta_desc="Bulk Cardiogen (AEDR) research peptide, ≥99% HPLC, MS verified. 20 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="cartalax",
        name="Cartalax",
        full_name="Cartalax (AED)",
        title_name="Cartalax",
        cat="repair",
        cas="85806-95-7",
        seq="Ala-Glu-Asp (AED)",
        mol="C12H19N3O8",
        mw="333.30 Da",
        tagline="A cartilage and bone-tissue bioregulator tripeptide.",
        intro=("Cartalax is a synthetic tripeptide with the sequence Ala-Glu-Asp. It is studied in "
               "cartilage, bone and connective-tissue research as part of the short bioregulator family."),
        overview=[
            ("Cartalax is the acidic tripeptide core of several longer bioregulators. It is used in "
             "chondrocyte and osteoblast research and in comparative bioregulator panels."),
            ("Vivalr supplies Cartalax as a ≥99% HPLC-purified lyophilized acetate salt."),
        ],
        research=[
            ("Cartilage research", "Studied for chondrocyte and cartilage-matrix signalling."),
            ("Bone-tissue models", "Investigated for osteoblast and connective-tissue research."),
            ("Gene expression", "A reference tripeptide in bioregulator transcription studies."),
            ("Joint research", "Used in preclinical models of joint and connective-tissue aging."),
        ],
        synthesis=("Cartalax is produced by Fmoc SPPS, cleaved and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Hydrolysis", "low", "Avoid extreme pH and heat."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
            ("Microbial growth", "low", "Filter sterilise aqueous stocks."),
        ],
        handling=("Store at -20 °C, desiccated. Reconstitute with sterile water or neutral buffer."),
        formulation=("Freely water-soluble; prepare fresh stocks and avoid repeated freeze–thaw."),
        applications=["Cartilage research", "Bone-tissue models", "Connective-tissue aging", "Bioregulator screening"],
        faqs=[
            ("Does Cartalax have a CAS number?",
             "Cartalax does not have a widely assigned public CAS number. Identity is controlled by the AED sequence, HPLC purity and MS data."),
            ("What is the Cartalax sequence?",
             "Cartalax is Ala-Glu-Asp (AED), with a calculated molecular weight of 333.30 Da."),
        ],
        related=["cortagen", "vesugen", "livagen"],
        tags=["cartalax", "bioregulator", "cartilage", "bone", "AED"],
        meta_desc="Bulk Cartalax (AED) research peptide, ≥99% HPLC, MS verified. 20 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="pancragen",
        name="Pancragen",
        full_name="Pancragen (KEDW)",
        title_name="Pancragen",
        cat="repair",
        cas="Not publicly assigned",
        seq="Lys-Glu-Asp-Trp (KEDW)",
        mol="C26H36N6O9",
        mw="576.61 Da",
        tagline="A pancreatic-tissue bioregulator peptide.",
        intro=("Pancragen is a short synthetic peptide with the sequence Lys-Glu-Asp-Trp. It is studied in "
               "pancreatic-tissue and metabolic research within the bioregulator peptide family."),
        overview=[
            ("Pancragen adds a tryptophan residue to the KED core, giving it a distinct spectroscopic and "
             "hydrophobic character. It is used in pancreatic-islet and metabolic research."),
            ("Vivalr supplies Pancragen as a ≥99% HPLC-purified lyophilized acetate salt."),
        ],
        research=[
            ("Pancreatic tissue research", "Studied for islet and pancreatic cell signalling."),
            ("Metabolic models", "Investigated in glucose and metabolic-aging research."),
            ("Gene expression", "A reference peptide in bioregulator transcription studies."),
            ("Comparative screening", "Used in panels of tissue-specific short peptides."),
        ],
        synthesis=("Pancragen is produced by Fmoc SPPS, cleaved and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Tryptophan oxidation", "medium", "The Trp residue is oxidation-sensitive; protect from light and oxygen."),
            ("Hydrolysis", "low", "Avoid extreme pH and heat."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Reconstitute with sterile water or "
                  "neutral buffer."),
        formulation=("Protect from light and oxidizers. Prepare fresh stocks and avoid repeated "
                     "freeze–thaw."),
        applications=["Pancreatic research", "Metabolic models", "Bioregulator studies", "Peptide screening"],
        faqs=[
            ("Does Pancragen have a CAS number?",
             "Pancragen does not have a widely assigned public CAS number. Identity is controlled by the KEDW sequence, HPLC purity and MS data."),
            ("What is the Pancragen sequence?",
             "Pancragen is Lys-Glu-Asp-Trp (KEDW), with a calculated molecular weight of 549.63 Da."),
        ],
        related=["livagen", "vesugen", "cortagen"],
        tags=["pancragen", "bioregulator", "pancreas", "metabolic", "KEDW"],
        meta_desc="Bulk Pancragen (KEDW) research peptide, ≥99% HPLC, MS verified. 20 mg 10-vial kits, COA per batch, worldwide shipping. Request a quote.",
    ),
    P(
        slug="prostamax",
        name="Prostamax",
        full_name="Prostamax (KEDP)",
        title_name="Prostamax",
        cat="repair",
        cas="473578-47-1",
        seq="Lys-Glu-Asp-Pro (KEDP)",
        mol="C20H33N5O9",
        mw="487.55 Da",
        tagline="A prostate-tissue bioregulator peptide for urological research.",
        intro=("Prostamax is a short synthetic peptide with the sequence Lys-Glu-Asp-Pro. It is studied in "
               "prostate-tissue and urological-aging research within the bioregulator peptide family."),
        overview=[
            ("Prostamax combines the KED motif with a proline residue, which influences its conformation. "
             "It is used in prostate cell and tissue research."),
            ("Vivalr supplies Prostamax as a ≥99% HPLC-purified lyophilized acetate salt."),
        ],
        research=[
            ("Prostate tissue research", "Studied for prostate cell and tissue signalling."),
            ("Urological aging", "Investigated in age-related prostate models."),
            ("Gene expression", "A reference peptide in bioregulator transcription studies."),
            ("Comparative screening", "Used in panels of tissue-specific short peptides."),
        ],
        synthesis=("Prostamax is produced by Fmoc SPPS, cleaved and purified by preparative HPLC, then "
                    "lyophilized as the acetate salt."),
        risks=[
            ("Hydrolysis", "low", "Avoid extreme pH and heat."),
            ("Moisture", "medium", "Store desiccated at -20 °C."),
            ("Microbial growth", "low", "Filter sterilise aqueous stocks."),
        ],
        handling=("Store at -20 °C, desiccated. Reconstitute with sterile water or neutral buffer."),
        formulation=("Freely water-soluble; prepare fresh stocks and avoid repeated freeze–thaw."),
        applications=["Prostate research", "Urological models", "Aging research", "Bioregulator screening"],
        faqs=[
            ("What is the Prostamax sequence?",
             "Prostamax is Lys-Glu-Asp-Pro (KEDP), CAS 473578-47-1, with a calculated molecular weight of 487.55 Da."),
            ("Is Prostamax water-soluble?",
             "Yes. The peptide dissolves readily in water and neutral buffers for laboratory use."),
        ],
        related=["testagen", "livagen", "cortagen"],
        tags=["prostamax", "bioregulator", "prostate", "KEDP", "urology"],
        meta_desc="Bulk Prostamax (KEDP), CAS 473578-47-1, ≥99% HPLC, MS verified. 20 mg 10-vial kits, COA, worldwide shipping. Request a quote.",
    ),
    P(
        slug="thymalin",
        name="Thymalin",
        full_name="Thymalin (Thymic Polypeptide Complex)",
        title_name="Thymalin",
        cat="repair",
        cas="Not publicly assigned",
        seq="Polypeptide complex (thymic origin)",
        mol="—",
        mw="Variable (polypeptide complex)",
        appearance="White to off-white powder",
        form="Powder (polypeptide complex)",
        purity="HPLC profile (batch-specific)",
        tagline="A thymic polypeptide complex for immune-modulation research.",
        intro=("Thymalin is a polypeptide complex derived from thymic tissue, used in immunology research "
               "on T-cell maturation and immune regulation. Unlike the synthetic single peptides in the "
               "catalogue, it is a heterogeneous polypeptide preparation."),
        overview=[
            ("Thymalin is not a single sequence. Its biological character comes from the mixture of "
             "thymic polypeptides, which is why batch documentation focuses on source material, processing "
             "and bioactivity rather than a single mass."),
            ("Vivalr supplies Thymalin as a research-grade powder with lot-specific documentation. "
             "Because it is a complex biological material, researchers should confirm the assay and "
             "characterization data required for their work."),
        ],
        research=[
            ("T-cell research", "Studied for thymocyte maturation and T-cell differentiation."),
            ("Immune regulation", "Investigated in models of immune suppression and aging."),
            ("Cytokine signalling", "Evaluated for effects on cytokine balance."),
            ("Comparative immunology", "Used alongside synthetic thymic peptides such as thymosin alpha-1."),
        ],
        synthesis=("Thymalin is prepared from thymic tissue by controlled extraction, fractionation and "
                    "drying. It is a polypeptide complex rather than a chemically synthesized single "
                    "peptide; batch documentation covers source, processing and characterization."),
        risks=[
            ("Batch variability", "high", "Biological complexes vary by lot. Review the batch characterization data and retain samples for comparability."),
            ("Moisture & microbial load", "medium", "Store desiccated and handle aseptically; request microbial limits on the COA."),
            ("Stability", "medium", "Keep at -20 °C and protect from light; avoid repeated freeze–thaw."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Handle aseptically and equilibrate "
                  "before opening."),
        formulation=("Use according to your validated laboratory protocol. Because composition is variable, "
                     "do not assume equivalence between lots without characterization."),
        applications=["Immunology research", "T-cell studies", "Immune-aging models", "Thymic-peptide comparison"],
        faqs=[
            ("Is Thymalin a single peptide?",
             "No. Thymalin is a polypeptide complex derived from thymic tissue, so it does not have a single sequence or molecular weight. Batch characterization is the relevant identity control."),
            ("How is Thymalin documented?",
             "The COA covers appearance, moisture, microbial limits and the lot's characterization profile. Request the current batch data before placing a research order."),
        ],
        related=["thymosin-alpha-1", "crystagen", "epithalon"],
        tags=["thymalin", "thymus", "immune", "polypeptide", "bioregulator"],
        meta_desc="Bulk Thymalin thymic polypeptide complex for immune research. 10 mg kits, batch documentation, COA, worldwide shipping. Request a quote.",
    ),

    # ------------------------------------------------------------------ NAD+ / NMN
    P(
        slug="nad-plus",
        name="NAD+",
        full_name="NAD+ (β-Nicotinamide Adenine Dinucleotide)",
        title_name="NAD+",
        cat="nad",
        cas="53-84-9",
        seq="β-Nicotinamide adenine dinucleotide",
        mol="C21H27N7O14P2",
        mw="663.43 Da",
        appearance="White to off-white powder",
        form="Crystalline / lyophilized powder",
        storage="-20 °C, desiccated, protected from light",
        tagline="The central redox coenzyme for sirtuin, PARP and cellular-aging research.",
        intro=("NAD+ (β-nicotinamide adenine dinucleotide) is the central redox coenzyme of cellular "
               "metabolism and the substrate for sirtuins, PARPs and CD38. It is supplied as a high-purity "
               "powder for metabolic, epigenetic and longevity research."),
        overview=[
            ("NAD+ sits at the intersection of energy metabolism and cellular signalling. Its oxidised and "
             "reduced forms (NAD+/NADH) carry electrons in glycolysis, the TCA cycle and oxidative "
             "phosphorylation, while the NAD+ pool also controls sirtuin and PARP activity."),
            ("NAD+ is chemically fragile in aqueous solution: the glycosidic bond hydrolyses, and the "
             "molecule is hygroscopic. Vivalr supplies a high-purity, low-moisture powder with HPLC assay "
             "and batch-specific handling guidance."),
        ],
        research=[
            ("Sirtuin research", "NAD+ is the substrate for SIRT1–SIRT7 deacetylation reactions."),
            ("PARP biology", "Used to study poly(ADP-ribose) polymerase activity and DNA-repair signalling."),
            ("Metabolic research", "Central to glycolysis, TCA-cycle and mitochondrial electron transport studies."),
            ("Cellular aging", "Investigated for NAD+ decline and age-related metabolic dysfunction."),
        ],
        synthesis=("NAD+ is produced by enzymatic synthesis or fermentation and purified by ion-exchange "
                    "chromatography and preparative HPLC. The product is concentrated and dried under "
                    "controlled conditions to a low-moisture powder."),
        risks=[
            ("Hydrolysis in aqueous solution", "high", "The glycosidic bond hydrolyses in water, faster at acidic or alkaline pH. Prepare solutions fresh and keep them cold."),
            ("Hygroscopicity", "high", "The powder absorbs moisture rapidly. Equilibrate sealed vials to room temperature and minimise open time."),
            ("Light & heat sensitivity", "medium", "Protect from light and avoid prolonged heat during handling."),
        ],
        handling=("Store at -20 °C in a sealed, desiccated vial protected from light. Weigh quickly, avoid "
                  "unnecessary aqueous stock, and prepare solutions fresh at a defined pH."),
        formulation=("For laboratory work, prepare NAD+ solutions in a neutral buffer and use them promptly. "
                     "Avoid repeated freeze–thaw of solutions; aliquot single-use volumes."),
        applications=["Sirtuin assays", "PARP research", "Metabolic studies", "NAD+ metabolism research"],
        faqs=[
            ("What is the difference between NAD+ and NADH?",
             "NAD+ is the oxidised form and NADH the reduced form. NAD+ is the substrate for sirtuins and PARPs, while NADH mainly carries electrons in metabolism. This product is NAD+."),
            ("How should NAD+ powder be stored?",
             "Keep it sealed at -20 °C with desiccant, protected from light. NAD+ is hygroscopic and hydrolyses in solution, so weigh quickly and prepare aqueous stocks fresh."),
        ],
        related=["nmn", "aicar", "5-amino-1mq"],
        tags=["NAD+", "coenzyme", "sirtuin", "PARP", "longevity", "metabolism"],
        featured=True,
        meta_desc="Bulk NAD+ (β-nicotinamide adenine dinucleotide), CAS 53-84-9, ≥99% HPLC. 100/500/1000 mg kits, COA, worldwide shipping. Request a quote.",
    ),
    P(
        slug="nmn",
        name="NMN",
        full_name="NMN (β-Nicotinamide Mononucleotide)",
        title_name="NMN",
        cat="nad",
        cas="1094-61-7",
        seq="β-Nicotinamide mononucleotide",
        mol="C11H15N2O8P",
        mw="334.22 Da",
        appearance="White to off-white crystalline powder",
        form="Crystalline powder",
        storage="-20 °C, desiccated, protected from light",
        moq="10 g",
        tagline="The NAD+ precursor for salvage-pathway and longevity research.",
        intro=("NMN (β-nicotinamide mononucleotide) is a naturally occurring NAD+ precursor in the salvage "
               "pathway. It is widely studied in cellular-aging, metabolic and mitochondrial research and is "
               "supplied as a high-purity crystalline powder."),
        overview=[
            ("NMN is converted to NAD+ by nicotinamide mononucleotide adenylyltransferase (NMNAT) inside "
             "cells. Because it sits one step closer to NAD+ than nicotinamide, it is a key tool for "
             "studying NAD+ repletion and its downstream effects."),
            ("NMN is hygroscopic and hydrolyses in aqueous solution to nicotinamide and ribose phosphate. "
             "Vivalr supplies low-moisture powder with HPLC assay and identity data; bulk quantities are "
             "quoted per batch."),
        ],
        research=[
            ("NAD+ salvage pathway", "Converted to NAD+ by NMNAT; used to study NAD+ repletion."),
            ("Metabolic research", "Investigated for glucose metabolism, insulin sensitivity and energy expenditure."),
            ("Mitochondrial function", "Studied for mitochondrial biogenesis and bioenergetics."),
            ("Cellular aging", "Evaluated in senescence and age-related dysfunction models."),
        ],
        synthesis=("NMN is produced by enzymatic synthesis (nicotinamide + PRPP) or by controlled chemical "
                    "routes, then purified by ion-exchange and preparative chromatography. The product is "
                    "dried to a low-moisture crystalline powder and tested by HPLC and MS."),
        risks=[
            ("Hydrolysis", "high", "NMN hydrolyses to nicotinamide and ribose phosphate in aqueous solution. Keep the powder dry and prepare solutions fresh."),
            ("Hygroscopicity", "high", "Store with desiccant and equilibrate before opening; minimise open-vial time."),
            ("Heat sensitivity", "medium", "Avoid prolonged heat; use cool processing conditions."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Weigh quickly in a low-humidity "
                  "environment. Prepare aqueous stocks fresh and keep them cold."),
        formulation=("For laboratory use, dissolve NMN in a neutral buffer and use promptly. Avoid "
                     "alkaline conditions and repeated freeze–thaw."),
        applications=["NAD+ research", "Metabolic studies", "Mitochondrial research", "Longevity screening"],
        faqs=[
            ("Is NMN the same as NAD+?",
             "No. NMN is β-nicotinamide mononucleotide, a precursor that cells convert to NAD+. NAD+ is the larger dinucleotide coenzyme. They are different molecules with different molecular weights."),
            ("Why is NMN sold in gram quantities?",
             "NMN is typically used as a bulk powder in research, so it is quoted from 10 g upward. Vial kits are available on request for smaller studies."),
        ],
        related=["nad-plus", "aicar", "5-amino-1mq"],
        tags=["NMN", "NAD+ precursor", "longevity", "metabolism", "mitochondria"],
        featured=True,
        note="NMN is not listed in the source workbook; it is included as a companion NAD+ precursor and is quote-based.",
        meta_desc="Bulk NMN (β-nicotinamide mononucleotide), CAS 1094-61-7, ≥99% HPLC. 10 g–1 kg quantities, COA and MS verification. Request a quote.",
    ),
    P(
        slug="aicar",
        name="AICAR",
        full_name="AICAR (Acadesine)",
        title_name="AICAR",
        cat="nad",
        cas="2627-69-2",
        seq="5-Aminoimidazole-4-carboxamide riboside",
        mol="C9H14N4O5",
        mw="258.23 Da",
        appearance="White to off-white powder",
        form="Crystalline powder",
        storage="-20 °C, desiccated, protected from light",
        tagline="An AMPK-pathway activator for metabolic and energy-sensing research.",
        intro=("AICAR (acadesine) is a cell-permeable adenosine analogue that is phosphorylated to ZMP and "
               "activates AMPK. It is a standard tool for metabolic, energy-sensing and mitochondrial "
               "research."),
        overview=[
            ("AICAR enters cells and is converted to AICA ribotide (ZMP), which mimics AMP and activates "
             "AMPK. This makes it a widely used chemical tool for studying energy stress and metabolic "
             "adaptation."),
            ("Vivalr supplies AICAR as a high-purity crystalline powder with HPLC and MS data. It is "
             "intended for laboratory research only."),
        ],
        research=[
            ("AMPK activation", "Converted to ZMP, which activates AMPK-dependent signalling."),
            ("Metabolic research", "Studied for glucose uptake, fatty-acid oxidation and energy metabolism."),
            ("Mitochondrial biogenesis", "Investigated for PGC-1α and mitochondrial adaptation."),
            ("Cellular stress", "Used as a tool to mimic energy stress in vitro."),
        ],
        synthesis=("AICAR is produced by chemical synthesis from an imidazole riboside intermediate, "
                    "purified by crystallization and chromatography, and dried to a low-moisture powder."),
        risks=[
            ("Hydrolysis", "medium", "Avoid prolonged aqueous storage; prepare solutions fresh."),
            ("Light sensitivity", "medium", "Protect from light; store in amber glass."),
            ("Hygroscopicity", "medium", "Store desiccated at -20 °C."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Prepare stock solutions fresh and "
                  "filter sterilise if required."),
        formulation=("AICAR is Soluble in aqueous buffers; confirm solubility for your concentration. Avoid "
                     "alkaline conditions and prolonged heat."),
        applications=["AMPK research", "Metabolic assays", "Mitochondrial studies", "Energy-stress models"],
        faqs=[
            ("What is AICAR also called?",
             "AICAR is also known as acadesine, CAS 2627-69-2. It is an adenosine analogue that activates AMPK after intracellular conversion to ZMP."),
            ("Is AICAR the same as AICAR phosphate?",
             "No. This product is AICAR (acadesine) base, CAS 2627-69-2. Phosphate and other salt forms can be quoted separately."),
        ],
        related=["nad-plus", "nmn", "5-amino-1mq"],
        tags=["AICAR", "AMPK", "metabolism", "acadesine", "energy"],
        meta_desc="Bulk AICAR (acadesine), CAS 2627-69-2, ≥99% HPLC. 50/100 mg 10-vial kits, COA and MS verification, worldwide shipping. Request a quote.",
    ),
    P(
        slug="5-amino-1mq",
        name="5-Amino-1MQ",
        full_name="5-Amino-1MQ (NNMT Inhibitor)",
        title_name="5-Amino-1MQ",
        cat="nad",
        cas="42464-96-0",
        seq="5-Amino-1-methylquinolinium iodide",
        mol="C10H11IN2",
        mw="286.11 Da",
        appearance="Yellow to orange powder",
        form="Crystalline powder",
        storage="-20 °C, desiccated, protected from light",
        tagline="An NNMT inhibitor for metabolic and adipocyte research.",
        intro=("5-Amino-1MQ is a small-molecule inhibitor of nicotinamide N-methyltransferase (NNMT). It is "
               "studied in adipocyte, metabolic and NAD+-consumption research, where NNMT activity affects "
               "the cellular NAD+ pool."),
        overview=[
            ("NNMT consumes nicotinamide and SAM to produce 1-methylnicotinamide, influencing both NAD+ "
             "metabolism and methylation capacity. 5-Amino-1MQ is used to probe that axis in metabolic "
             "research."),
            ("The compound is supplied as the iodide salt, a yellow crystalline powder. Vivalr provides "
             "HPLC purity and MS identity for each batch."),
        ],
        research=[
            ("NNMT inhibition", "Studied as a cell-permeable inhibitor of nicotinamide N-methyltransferase."),
            ("Adipocyte research", "Investigated for lipid accumulation and adipocyte metabolism."),
            ("NAD+ metabolism", "Used to probe NNMT-dependent NAD+ consumption."),
            ("Metabolic disease models", "Evaluated in obesity and insulin-resistance research."),
        ],
        synthesis=("5-Amino-1MQ is prepared by quaternization of 5-aminoquinoline with methyl iodide, "
                    "followed by crystallization and drying. Purity is assessed by HPLC and identity by MS."),
        risks=[
            ("Light sensitivity", "high", "The quinolium salt is light-sensitive; store in amber glass and protect from light."),
            ("Hygroscopicity", "medium", "Store desiccated at -20 °C."),
            ("Aqueous stability", "medium", "Prepare fresh solutions and avoid prolonged storage."),
        ],
        handling=("Store at -20 °C, desiccated and protected from light. Weigh in low light and prepare "
                  "solutions fresh."),
        formulation=("Use a compatible aqueous or DMSO stock for laboratory work. Avoid alkaline conditions "
                     "and prolonged light exposure."),
        applications=["NNMT research", "Adipocyte studies", "Metabolic research", "NAD+ metabolism"],
        faqs=[
            ("What does 5-Amino-1MQ inhibit?",
             "5-Amino-1MQ is studied as an inhibitor of nicotinamide N-methyltransferase (NNMT), an enzyme that consumes nicotinamide and SAM."),
            ("Why is 5-Amino-1MQ supplied as an iodide salt?",
             "The iodide salt is the conventional crystalline form of the quinolium compound. Identity and counter-ion are confirmed on the batch COA."),
        ],
        related=["nad-plus", "nmn", "aicar"],
        tags=["5-Amino-1MQ", "NNMT", "metabolism", "adipocyte", "NAD+"],
        meta_desc="Bulk 5-Amino-1MQ (NNMT inhibitor), CAS 42464-96-0, ≥99% HPLC. 5/10/50 mg kits, COA and MS verification. Request a quote.",
    ),
]


# ---------------------------------------------------------------------------
# SKU aggregation: every size of the same molecule lives on one product page.
# ---------------------------------------------------------------------------
KIT = " × 10 vials"
VARIANTS = {
    "ghk-cu": [V("50 mg" + KIT, "VVR-GHK-50"), V("100 mg" + KIT, "VVR-GHK-100")],
    "ahk-cu": [V("50 mg" + KIT, "VVR-AHK-50"), V("100 mg" + KIT, "VVR-AHK-100")],
    "snap-8": [V("10 mg" + KIT, "VVR-SNP-10"), V("100 mg" + KIT, "VVR-SNP-100")],
    "matrixyl": [V("10 mg" + KIT, "VVR-MTX-10")],
    "glutathione": [V("400 mg" + KIT, "VVR-GSH-400"), V("600 mg" + KIT, "VVR-GSH-600"), V("1500 mg" + KIT, "VVR-GSH-1500")],
    "bpc-157": [V("2 mg" + KIT, "VVR-BPC-2"), V("5 mg" + KIT, "VVR-BPC-5"), V("10 mg" + KIT, "VVR-BPC-10"), V("20 mg" + KIT, "VVR-BPC-20")],
    "tb-500": [V("2 mg" + KIT, "VVR-TB5-2"), V("5 mg" + KIT, "VVR-TB5-5"), V("10 mg" + KIT, "VVR-TB5-10")],
    "bpc-157-tb-500-blend": [V("10 mg (5 + 5 mg)" + KIT, "VVR-BTB-10"), V("20 mg (10 + 10 mg)" + KIT, "VVR-BTB-20"), V("30 mg (15 + 15 mg)" + KIT, "VVR-BTB-30")],
    "glow": [V("70 mg (50 + 10 + 10 mg)" + KIT, "VVR-GLW-70")],
    "klow": [V("80 mg (50 + 10 + 10 + 10 mg)" + KIT, "VVR-KLW-80")],
    "epithalon": [V("10 mg" + KIT, "VVR-EPI-10"), V("50 mg" + KIT, "VVR-EPI-50")],
    "pinealon": [V("5 mg" + KIT, "VVR-PIN-5"), V("10 mg" + KIT, "VVR-PIN-10"), V("20 mg" + KIT, "VVR-PIN-20")],
    "kpv": [V("5 mg" + KIT, "VVR-KPV-5"), V("10 mg" + KIT, "VVR-KPV-10")],
    "thymosin-alpha-1": [V("5 mg" + KIT, "VVR-TA1-5"), V("10 mg" + KIT, "VVR-TA1-10")],
    "ara-290": [V("10 mg" + KIT, "VVR-ARA-10"), V("16 mg" + KIT, "VVR-ARA-16"), V("40 mg" + KIT, "VVR-ARA-40")],
    "ll-37": [V("5 mg" + KIT, "VVR-LL37-5"), V("5 mL" + KIT, "VVR-LL37-5ML"), V("10 mL" + KIT, "VVR-LL37-10ML")],
    "foxo4-dri": [V("2 mg" + KIT, "VVR-FOX-2"), V("10 mg" + KIT, "VVR-FOX-10")],
    "ss-31": [V("5 mg" + KIT, "VVR-SS31-5"), V("10 mg" + KIT, "VVR-SS31-10"), V("50 mg" + KIT, "VVR-SS31-50")],
    "mots-c": [V("10 mg" + KIT, "VVR-MOT-10"), V("15 mg" + KIT, "VVR-MOT-15"), V("20 mg" + KIT, "VVR-MOT-20"), V("40 mg" + KIT, "VVR-MOT-40")],
    "humanin": [V("10 mg" + KIT, "VVR-HUM-10")],
    "cortagen": [V("20 mg" + KIT, "VVR-COR-20")],
    "livagen": [V("20 mg" + KIT, "VVR-LIV-20")],
    "crystagen": [V("20 mg" + KIT, "VVR-CRY-20")],
    "testagen": [V("20 mg" + KIT, "VVR-TES-20")],
    "vesugen": [V("10 mg" + KIT, "VVR-VES-10")],
    "cardiogen": [V("20 mg" + KIT, "VVR-CAR-20")],
    "cartalax": [V("20 mg" + KIT, "VVR-CAT-20")],
    "pancragen": [V("20 mg" + KIT, "VVR-PAN-20")],
    "prostamax": [V("20 mg" + KIT, "VVR-PRO-20")],
    "thymalin": [V("10 mg" + KIT, "VVR-THY-10")],
    "nad-plus": [V("100 mg" + KIT, "VVR-NAD-100"), V("500 mg" + KIT, "VVR-NAD-500"), V("1000 mg" + KIT, "VVR-NAD-1000")],
    "nmn": [V("10 g", "VVR-NMN-10G"), V("50 g", "VVR-NMN-50G"), V("100 g", "VVR-NMN-100G"), V("1 kg", "VVR-NMN-1KG")],
    "aicar": [V("50 mg" + KIT, "VVR-AIC-50"), V("100 mg" + KIT, "VVR-AIC-100")],
    "5-amino-1mq": [V("5 mg" + KIT, "VVR-5MQ-5"), V("10 mg" + KIT, "VVR-5MQ-10"), V("50 mg" + KIT, "VVR-5MQ-50")],
}

BY_SLUG = {p["slug"]: p for p in PRODUCTS}
for p in PRODUCTS:
    p["variants"] = VARIANTS[p["slug"]]
    p["cat_label"] = CATEGORIES[p["cat"]]["label"]
    p["cat_short"] = CATEGORIES[p["cat"]]["short"]
    p["url"] = SITE + "/products/" + p["slug"]
    p["path"] = "/products/" + p["slug"]
    p["og_image"] = SITE + "/assets/img/og/" + p["slug"] + ".png"
    p["spec_summary"] = " · ".join(v["label"].replace(KIT, "") for v in p["variants"])
    p["seq_mw"] = p["seq"] + " · " + p["mol"] + " · " + p["mw"]
    p["featured_rank"] = 0
    if p["slug"] in ("ghk-cu", "bpc-157", "glow", "klow", "nad-plus", "nmn", "snap-8", "tb-500", "epithalon"):
        p["featured_rank"] = 1

assert len(PRODUCTS) == 34
assert all(p["variants"] for p in PRODUCTS)

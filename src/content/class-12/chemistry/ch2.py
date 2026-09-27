# Class 12 Chemistry, Chapter 2 - Electrochemistry
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 2,
 "title_en": "Electrochemistry",
 "title_hi": "विद्युत रसायन",
 "tagline": "Galvanic cells, Nernst equation, conductance, Kohlrausch aur Faraday's laws",
 "jee": "HIGH",
 "meta_desc": "Class 12 Chemistry Chapter 2: Electrochemistry — long + short notes in Hindi, English, Hinglish. Galvanic cells, electrode potential, Nernst equation, molar conductivity, Kohlrausch law, Faraday's laws, batteries, corrosion.",
 "video": None,
 "card_tag": "Galvanic cells, Nernst equation, conductance, Kohlrausch aur Faraday's laws",
 "card_topics": [
  "🔋 Galvanic cells + Nernst",
  "⚡ ΔG-E-K triangle",
  "🌊 Conductance + Kohlrausch",
  "⚖️ Faraday's laws + corrosion"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Electrochemical Cells — Chemical Energy Se Current",
    "body": "<ul>\n<li><b>Electrochemistry:</b> chemical energy ↔ electrical energy ka study. Do type ke cells.</li>\n<li><b>Galvanic (voltaic) cell:</b> spontaneous redox reaction se <b>electricity BANTI hai</b> (chemical → electrical). Example: Daniell cell.</li>\n<li><b>Electrolytic cell:</b> electricity laga ke <b>non-spontaneous reaction KARVATE hain</b> (electrical → chemical). Example: electrolysis.</li>\n<li><b>Daniell cell ⭐:</b> Zn rod ZnSO₄ me (anode) + Cu rod CuSO₄ me (cathode). <b>Anode pe oxidation</b> (Zn → Zn²⁺ + 2e⁻), <b>cathode pe reduction</b> (Cu²⁺ + 2e⁻ → Cu). Electrons external circuit me Zn → Cu flow karte hain.</li>\n<li><b>Salt bridge:</b> U-tube me agar/jelly + KCl/KNO₃. Dono half-cells ko jodta hai, <b>charge balance</b> rakhta hai (ions migrate), circuit complete karta hai — lekin solutions mix nahi hone deta.</li>\n<li><b>Cell notation:</b> Zn | Zn²⁺ || Cu²⁺ | Cu — anode (oxidation) left, cathode (reduction) right, || = salt bridge.</li>\n</ul>\n<p class=\"small-note\">💡 Galvanic = \"free me current\" (reaction khud chalti hai). Electrolytic = \"paisa deke reaction\" (current lagani padti hai). Anode = oxidation (A-O yaad rakho)!</p>"
   },
   {
    "h": "2️⃣ Electrode Potential aur SHE — Reference Ka Khel",
    "body": "<ul>\n<li><b>Electrode potential (E):</b> electrode aur uske ion solution ke beech ka potential difference. Oxidation ya reduction dono tarah likh sakte; IUPAC <b>reduction potential</b> use karta hai.</li>\n<li><b>Standard electrode potential (E°):</b> 298 K, 1 bar, 1 M concentration pe measure hota hai.</li>\n<li><b>Standard Hydrogen Electrode (SHE) ⭐:</b> reference electrode jiska E° = <b>0 V</b> (assigned). Pt electrode, H₂ gas 1 bar, H⁺ 1 M. Baaki sab electrodes ka E° SHE ke against measure hota hai.</li>\n<li><b>Electrochemical series ⭐:</b> elements ko standard reduction potential ke order me rank karna. <b>Zyada negative E° = strong reducing agent</b> (jaise Li, Zn — aasani se electron deta), <b>zyada positive E° = strong oxidizing agent</b> (jaise F₂, Cu²⁺ — electron leta).</li>\n<li><b>Cell EMF:</b> E°cell = E°cathode − E°anode. Positive EMF = spontaneous reaction (cell kaam karega).</li>\n</ul>\n<p class=\"small-note\">💡 E° = \"electron khinchne ki power\". Jiska E° zyada positive, woh electron kheenchta hai (oxidizing agent). SHE = sabka zero-point (jaise sea-level for height)!</p>"
   },
   {
    "h": "3️⃣ Nernst Equation — Concentration Ka Asar ⭐⭐",
    "body": "<ul>\n<li>Standard conditions (1 M) pe to E° milta hai — lekin concentration badalne pe EMF badalta hai. Iske liye <b>Nernst equation</b>.</li>\n<li><b>Electrode ke liye:</b> Mⁿ⁺ + ne⁻ → M. <b>E = E° − (RT/nF)·ln(1/[Mⁿ⁺]) = E° − (2.303RT/nF)·log(1/[Mⁿ⁺])</b>.</li>\n<li><b>298 K pe simplified ⭐:</b> 2.303RT/F = 0.059 V. Toh <b>E = E° − (0.059/n)·log(1/[Mⁿ⁺])</b> ya cell ke liye <b>E_cell = E°_cell − (0.059/n)·log Q</b> (Q = reaction quotient).</li>\n<li><b>Concentration badhao/bahao:</b> reactant ([Mⁿ⁺]) zyada → Q kam → E zyada (cell better chalti). Product zyada → E kam. Battery discharge hote hote reactant ghatta → EMF girti.</li>\n<li><b>Equilibrium pe:</b> E_cell = 0, Q = K. Toh <b>E°_cell = (0.059/n)·log K</b> (298 K) — yahan se equilibrium constant K nikalta hai!</li>\n</ul>\n<p class=\"small-note\">💡 Nernst = \"abhi ka mood\" — concentration jaise badlegi, EMF waisa badlega. 0.059/n yaad rakho, numericals me har jagah aayega!</p>"
   },
   {
    "h": "4️⃣ Thermodynamics of Cell — ΔG, E aur K Ka Triangle ⭐",
    "body": "<ul>\n<li><b>Gibbs energy aur EMF:</b> cell ka maximum useful work = electrical work. <b>ΔG = −nF·E_cell</b> (n = moles of electrons, F = Faraday = 96487 C/mol).</li>\n<li><b>Standard:</b> ΔG° = −nF·E°_cell. <b>E° positive → ΔG° negative → spontaneous</b> reaction. Simple link!</li>\n<li><b>Equilibrium constant:</b> ΔG° = −RT·ln K. Dono ko jodo → <b>ln K = nF·E°/RT</b> ya 298 K pe <b>log K = n·E°/0.059</b>.</li>\n<li>Teen quantities (ΔG°, E°_cell, K) ek dusre se judi — koi ek pata ho to baaki nikal lo. Numerical me yahi triangle sabse zyada puchha jaata hai.</li>\n</ul>\n<p class=\"small-note\">💡 ΔG = −nFE = reaction ka \"driving force\". E zyada positive, reaction zyada utsah se chalegi (ΔG zyada negative), K zyada bada!</p>"
   },
   {
    "h": "5️⃣ Conductance — Solution Me Current Kaise Behta Hai",
    "body": "<ul>\n<li><b>Resistance (R):</b> R = ρ·l/A (ρ = resistivity). <b>Conductance (G) = 1/R</b> (unit: siemens, S ya mho).</li>\n<li><b>Conductivity (κ, kappa):</b> κ = 1/ρ = G·(l/A). Unit: S/m ya S/cm. Pure solution ki property.</li>\n<li><b>Molar conductivity (Λm) ⭐:</b> κ ko concentration se normalize kiya — <b>Λm = κ/C</b> (C = molarity, mol/L). Unit: S·cm²/mol (ya S·m²/mol). Formula: Λm = (κ × 1000)/C agar κ S/cm me.</li>\n<li><b>Dilution ka effect ⭐:</b> dilute karne pe <b>κ GHATTI hai</b> (ions per cm³ kam) lekin <b>Λm BADHTI hai</b> (har mole ke liye zyada ions available/interference kam).</li>\n<li><b>Strong electrolyte:</b> Λm dilution pe thodi badhti (Debye-Hückel) — extrapolate karke Λ°m milti. <b>Weak electrolyte:</b> dilution pe Λm tez badhti (dissociation badhta) — Λ°m directly nahi milti.</li>\n</ul>\n<p class=\"small-note\">💡 κ = \"abhi kitna current\" (quantity), Λm = \"per-mole kitna current\" (quality). Paani milao → κ neeche, Λm upar. Dono ka ulta behavior = exam favourite!</p>"
   },
   {
    "h": "6️⃣ Kohlrausch Law — Weak Ka Strong Se Hisaab",
    "body": "<ul>\n<li><b>Kohlrausch law ⭐:</b> infinite dilution pe, electrolyte ki molar conductivity uske ions ki individual conductivities ka <b>sum</b> hoti hai — <b>Λ°m = ν₊·λ°₊ + ν₋·λ°₋</b> (ν = ions ki ginti, λ° = ionic molar conductivity).</li>\n<li><b>Application — weak electrolyte ki Λ°m ⭐:</b> directly measure nahi hoti, par strong electrolytes ke combo se nikal lo. Example: Λ°m(CH₃COOH) = Λ°m(CH₃COONa) + Λ°m(HCl) − Λ°m(NaCl).</li>\n<li><b>Dissociation constant nikalo:</b> degree of dissociation α = Λm/Λ°m, phir Ka = C·α²/(1−α) (weak acid).</li>\n<li>Λ°m bhi Kohlrausch se, Ka bhi usi se — weak electrolytes ka poora hisaab isi law pe tika hai.</li>\n</ul>\n<p class=\"small-note\">💡 Kohlrausch = \"jugaad math\" — weak acid ka data directly nahi milta, to strong salts ko plus-minus karke nikal lo. CH₃COONa + HCl − NaCl yaad rakho!</p>"
   },
   {
    "h": "7️⃣ Electrolysis aur Faraday's Laws ⭐⭐",
    "body": "<ul>\n<li><b>Electrolysis:</b> electrolytic cell me current laga ke chemical reaction karvana. Cathode pe reduction (cation jata), anode pe oxidation.</li>\n<li><b>Faraday's 1st law ⭐:</b> electrode pe deposited/liberated substance ka mass <b>charge (Q) ke proportional</b> — <b>m = Z·Q = Z·I·t</b> (Z = electrochemical equivalent, I = current, t = time).</li>\n<li><b>Faraday's 2nd law ⭐:</b> same charge se, deposited masses unke <b>equivalent weights ke proportional</b> — m₁/m₂ = E₁/E₂.</li>\n<li><b>Faraday constant:</b> 1 mole electron ka charge = <b>96487 C ≈ 96500 C</b>. n-factor yaad rakho: 1 mol Mⁿ⁺ ko n×96487 C chahiye.</li>\n<li><b>Numerical trick:</b> mass nikalo → moles of e⁻ = Q/96487 = (I×t)/96487, phir reaction stoichiometry se mass. Products: cathode pe metal/H₂, anode pe O₂/halogen (solution pe depend).</li>\n</ul>\n<p class=\"small-note\">💡 Faraday 1 = \"jitna charge, utna mass\". Faraday 2 = \"same charge, equivalent weight ke hisaab se\". Q = It, 96500 C per mole e⁻ — bas numerical set!</p>"
   },
   {
    "h": "8️⃣ Batteries aur Corrosion — Real-Life Electrochemistry",
    "body": "<ul>\n<li><b>Primary batteries (non-rechargeable):</b> <b>Dry cell</b> (Zn anode, MnO₂ cathode, NH₄Cl paste — torch), <b>mercury cell</b> (Zn-Hg anode, HgO cathode — hearing aids, watches; steady 1.35 V).</li>\n<li><b>Secondary batteries (rechargeable) ⭐:</b> <b>Lead storage battery</b> (car battery: Pb anode, PbO₂ cathode, 38% H₂SO₄; discharge pe dono PbSO₄ ban jate, recharge pe reverse). <b>Ni-Cd cell</b> (rechargeable, toys/tools).</li>\n<li><b>Fuel cell ⭐:</b> H₂ + O₂ → H₂O + electricity (continuous fuel supply, ~70% efficient, pollution-free). Space missions (Apollo) me use hua; product water peene layak!</li>\n<li><b>Corrosion ⭐:</b> metal ka dheere-dheere oxidation (rusting). Iron rusting: anode pe Fe → Fe²⁺ + 2e⁻, cathode pe O₂ + 2H₂O + 4e⁻ → 4OH⁻, phir Fe²⁺ oxidize hoke <b>Fe₂O₃·xH₂O (rust)</b> banta hai. Pani + oxygen dono chahiye.</li>\n<li><b>Prevention:</b> painting/coating, <b>galvanization</b> (Zn coating — Zn sacrificial anode banke pehle corrode hota), sacrificial protection (Mg/Zn blocks on ships/pipes).</li>\n</ul>\n<p class=\"small-note\">💡 Battery = stored electrochemistry, corrosion = unwanted electrochemistry. Galvanization me Zn \"bali ka bakra\" banta hai taaki iron bache — sacrificial protection!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ विद्युतरासायनिक सेल",
    "body": "<ul>\n<li><b>गैल्वेनिक सेल:</b> spontaneous अभिक्रिया से विद्युत (रासायनिक→विद्युत)। <b>विद्युत-अपघटनी सेल:</b> विद्युत से अभिक्रिया (विद्युत→रासायनिक)।</li>\n<li><b>Daniell सेल:</b> Zn (एनोड, ऑक्सीकरण) + Cu (कैथोड, अपचयन)। लवण सेतु आवेश संतुलन रखता है।</li>\n</ul>\n<p class=\"small-note\">💡 एनोड = ऑक्सीकरण, कैथोड = अपचयन।</p>"
   },
   {
    "h": "2️⃣ इलेक्ट्रोड विभव और SHE",
    "body": "<ul>\n<li><b>मानक इलेक्ट्रोड विभव (E°):</b> 298 K, 1 bar, 1 M पर। <b>SHE:</b> संदर्भ इलेक्ट्रोड, E° = 0 V। <b>E°cell = E°कैथोड − E°एनोड</b>।</li>\n</ul>\n<p class=\"small-note\">💡 अधिक ऋणात्मक E° = प्रबल अपचायक।</p>"
   },
   {
    "h": "3️⃣ Nernst समीकरण ⭐⭐",
    "body": "<ul>\n<li><b>E = E° − (0.059/n)·log(1/[Mⁿ⁺])</b> (298 K)। साम्य पर E°cell = (0.059/n)·log K।</li>\n</ul>\n<p class=\"small-note\">💡 सांद्रता बदली तो EMF बदली।</p>"
   },
   {
    "h": "4️⃣ ΔG, E और K",
    "body": "<ul>\n<li><b>ΔG = −nFE_cell</b>; ΔG° = −nFE° = −RT·lnK; log K = nE°/0.059। E° धनात्मक → spontaneous।</li>\n</ul>\n<p class=\"small-note\">💡 E बड़ा तो K बड़ा, ΔG अधिक ऋणात्मक।</p>"
   },
   {
    "h": "5️⃣ चालकता",
    "body": "<ul>\n<li><b>κ = 1/ρ; Λm = κ/C</b>। तनुकरण पर κ घटती, Λm बढ़ती। दुर्बल विद्युत-अपघट्य में Λm तेज़ी से बढ़ती।</li>\n</ul>\n<p class=\"small-note\">💡 κ नीचे, Λm ऊपर।</p>"
   },
   {
    "h": "6️⃣ Kohlrausch नियम",
    "body": "<ul>\n<li><b>Λ°m = ν₊λ°₊ + ν₋λ°₋</b>। दुर्बल: Λ°m(CH₃COOH) = Λ°m(CH₃COONa) + Λ°m(HCl) − Λ°m(NaCl)।</li>\n</ul>\n<p class=\"small-note\">💡 प्रबल लवणों से दुर्बल का हिसाब।</p>"
   },
   {
    "h": "7️⃣ Faraday के नियम ⭐⭐",
    "body": "<ul>\n<li><b>प्रथम:</b> m = Z·I·t (आवेश के समानुपाती)। <b>द्वितीय:</b> द्रव्यमान तुल्यांकी भार के समानुपाती। 1 F = 96487 C।</li>\n</ul>\n<p class=\"small-note\">💡 जितना आवेश, उतना द्रव्यमान।</p>"
   },
   {
    "h": "8️⃣ बैटरी और संक्षारण",
    "body": "<ul>\n<li><b>Lead storage</b> (car battery), <b>fuel cell</b> (H₂+O₂→H₂O, space)। <b>संक्षारण:</b> Fe का ऑक्सीकरण → Fe₂O₃·xH₂O (जंग)। रोक: galvanization (Zn), sacrificial protection।</li>\n</ul>\n<p class=\"small-note\">💡 Zn बलि का बकरा बनकर लोहे को बचाता है।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Electrochemical Cells",
    "body": "<ul>\n<li><b>Galvanic cell:</b> spontaneous redox produces electricity. <b>Electrolytic cell:</b> electricity drives a non-spontaneous reaction.</li>\n<li><b>Daniell cell:</b> Zn anode (oxidation), Cu cathode (reduction). Salt bridge maintains charge balance. Notation: Zn|Zn²⁺||Cu²⁺|Cu.</li>\n</ul>\n<p class=\"small-note\">💡 Anode = oxidation, cathode = reduction.</p>"
   },
   {
    "h": "2️⃣ Electrode Potential & SHE",
    "body": "<ul>\n<li><b>Standard electrode potential (E°)</b> measured at 298 K, 1 bar, 1 M. <b>SHE:</b> reference, E° = 0 V. <b>E°cell = E°cathode − E°anode</b>. More negative E° = stronger reducing agent.</li>\n</ul>\n<p class=\"small-note\">💡 Positive E°cell = spontaneous.</p>"
   },
   {
    "h": "3️⃣ Nernst Equation ⭐⭐",
    "body": "<ul>\n<li><b>E = E° − (0.059/n)·log(1/[Mⁿ⁺])</b> at 298 K. For a cell: E_cell = E°_cell − (0.059/n)log Q. At equilibrium: E°_cell = (0.059/n)log K.</li>\n</ul>\n<p class=\"small-note\">💡 Concentration change → EMF change.</p>"
   },
   {
    "h": "4️⃣ ΔG, E & K",
    "body": "<ul>\n<li><b>ΔG = −nFE_cell</b>; ΔG° = −nFE° = −RT·lnK; log K = nE°/0.059. Positive E° → negative ΔG° → spontaneous, larger K.</li>\n</ul>\n<p class=\"small-note\">💡 The ΔG–E–K triangle links all three.</p>"
   },
   {
    "h": "5️⃣ Conductance",
    "body": "<ul>\n<li><b>κ = 1/ρ; Λm = κ/C</b> (molar conductivity). On dilution: κ decreases, Λm increases. Weak electrolytes: Λm rises steeply with dilution.</li>\n</ul>\n<p class=\"small-note\">💡 κ down, Λm up on dilution.</p>"
   },
   {
    "h": "6️⃣ Kohlrausch Law",
    "body": "<ul>\n<li><b>Λ°m = ν₊λ°₊ + ν₋λ°₋</b> at infinite dilution. Weak electrolyte: Λ°m(CH₃COOH) = Λ°m(CH₃COONa) + Λ°m(HCl) − Λ°m(NaCl). α = Λm/Λ°m.</li>\n</ul>\n<p class=\"small-note\">💡 Get weak-electrolyte Λ°m from strong salts.</p>"
   },
   {
    "h": "7️⃣ Faraday's Laws ⭐⭐",
    "body": "<ul>\n<li><b>First:</b> m = Z·I·t (mass ∝ charge). <b>Second:</b> masses ∝ equivalent weights for the same charge. 1 F = 96487 C per mole of electrons.</li>\n</ul>\n<p class=\"small-note\">💡 More charge → more mass deposited.</p>"
   },
   {
    "h": "8️⃣ Batteries & Corrosion",
    "body": "<ul>\n<li><b>Lead storage battery</b> (rechargeable car battery), <b>fuel cell</b> (H₂+O₂→H₂O, ~70% efficient, space). <b>Corrosion:</b> iron oxidizes to Fe₂O₃·xH₂O (rust). Prevention: galvanization (Zn), sacrificial protection.</li>\n</ul>\n<p class=\"small-note\">💡 Zn sacrifices itself to protect iron.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Cells",
    "items": [
     "Galvanic: chemical→electrical (spontaneous)",
     "Electrolytic: electrical→chemical",
     "Anode=oxidation, Cathode=reduction",
     "Salt bridge = charge balance"
    ]
   },
   {
    "h": "E° & Series",
    "items": [
     "E°cell = E°cathode − E°anode",
     "SHE = 0 V reference",
     "Negative E° = strong reducing agent",
     "Positive E°cell = spontaneous"
    ]
   },
   {
    "h": "Nernst ⭐",
    "items": [
     "E = E° − (0.059/n)log(1/[Mⁿ⁺])",
     "298 K pe 0.059/n factor",
     "Equilibrium: E°cell=(0.059/n)log K"
    ]
   },
   {
    "h": "ΔG-E-K",
    "items": [
     "ΔG = −nFE_cell",
     "ΔG°=−nFE°=−RT lnK",
     "log K = nE°/0.059"
    ]
   },
   {
    "h": "Conductance",
    "items": [
     "κ = 1/ρ; Λm = κ/C",
     "Dilution: κ ghatti, Λm badhti",
     "Kohlrausch: Λ°m = ν₊λ°₊+ν₋λ°₋"
    ]
   },
   {
    "h": "Faraday",
    "items": [
     "1st: m = ZIt (∝ charge)",
     "2nd: masses ∝ equivalent wt",
     "1 F = 96487 C per mol e⁻"
    ]
   }
  ],
  "hi": [
   {
    "h": "सेल",
    "items": [
     "गैल्वेनिक: रासायनिक→विद्युत",
     "एनोड=ऑक्सीकरण",
     "लवण सेतु = आवेश संतुलन"
    ]
   },
   {
    "h": "E°",
    "items": [
     "E°cell=E°कैथोड−E°एनोड",
     "SHE=0 V",
     "धनात्मक=spontaneous"
    ]
   },
   {
    "h": "Nernst",
    "items": [
     "E=E°−(0.059/n)log(1/[Mⁿ⁺])",
     "E°cell=(0.059/n)log K"
    ]
   },
   {
    "h": "चालकता",
    "items": [
     "Λm=κ/C",
     "तनुकरण: κ↓, Λm↑",
     "Kohlrausch: Λ°m=Σνλ°"
    ]
   },
   {
    "h": "Faraday",
    "items": [
     "m=ZIt",
     "द्रव्यमान∝तुल्यांकी भार",
     "1F=96487 C"
    ]
   }
  ],
  "en": [
   {
    "h": "Cells",
    "items": [
     "Galvanic: chemical→electrical",
     "Anode=oxidation",
     "Salt bridge balances charge"
    ]
   },
   {
    "h": "E°",
    "items": [
     "E°cell=E°cathode−E°anode",
     "SHE=0 V",
     "Positive=spontaneous"
    ]
   },
   {
    "h": "Nernst",
    "items": [
     "E=E°−(0.059/n)log(1/[Mⁿ⁺])",
     "E°cell=(0.059/n)log K"
    ]
   },
   {
    "h": "Conductance",
    "items": [
     "Λm=κ/C",
     "Dilution: κ↓, Λm↑",
     "Kohlrausch: Λ°m=Σνλ°"
    ]
   },
   {
    "h": "Faraday",
    "items": [
     "m=ZIt",
     "mass∝equiv wt",
     "1F=96487 C"
    ]
   }
  ]
 },
 "practice": [
  [
   "Galvanic aur electrolytic cell me farak kya hai?",
   "<b>Galvanic</b> me spontaneous reaction se electricity banti hai; <b>electrolytic</b> me electricity se non-spontaneous reaction karvate hain."
  ],
  [
   "Salt bridge ka kaam kya hai?",
   "Dono half-cells jodna aur <b>charge balance</b> rakhna (ions migrate karke), taaki cell chalta rahe — solutions mix nahi hote."
  ],
  [
   "E°cell ka formula aur spontaneous ka matlab?",
   "<b>E°cell = E°cathode − E°anode</b>. E°cell <b>positive</b> → reaction spontaneous (ΔG° negative)."
  ],
  [
   "298 K pe Nernst equation likho (electrode).",
   "<b>E = E° − (0.059/n)·log(1/[Mⁿ⁺])</b>."
  ],
  [
   "ΔG°, E°cell aur K ko relate karo.",
   "<b>ΔG° = −nF·E°cell = −RT·ln K</b>; ya log K = nE°/0.059."
  ],
  [
   "Dilution karne par κ aur Λm pe kya effect?",
   "<b>κ ghatti</b> hai (ions/cm³ kam), <b>Λm badhti</b> hai (per-mole conductivity)."
  ],
  [
   "Kohlrausch law se CH₃COOH ki Λ°m kaise nikalo?",
   "<b>Λ°m(CH₃COOH) = Λ°m(CH₃COONa) + Λ°m(HCl) − Λ°m(NaCl)</b>."
  ],
  [
   "Faraday ka first law + 1 Faraday ki value.",
   "<b>m = Z·I·t</b> (mass ∝ charge). 1 F = <b>96487 C</b> per mole electrons."
  ],
  [
   "Lead storage battery me cathode aur anode kya hain?",
   "Anode: <b>Pb</b>, Cathode: <b>PbO₂</b>, electrolyte: 38% H₂SO₄. Discharge pe dono PbSO₄ bante hain."
  ],
  [
   "Iron rusting (corrosion) ka product aur ek prevention.",
   "Product: <b>Fe₂O₃·xH₂O (rust)</b>. Prevention: <b>galvanization</b> (Zn coating) ya sacrificial protection."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/chemistry/ch-3/",
  "title": "Chemical Kinetics"
 }
}

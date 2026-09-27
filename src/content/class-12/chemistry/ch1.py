# Class 12 Chemistry, Chapter 1 - Solutions
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 1,
 "title_en": "Solutions",
 "title_hi": "विलयन",
 "tagline": "Concentration units, Raoult's law, colligative properties aur van't Hoff factor",
 "jee": "HIGH",
 "meta_desc": "Class 12 Chemistry Chapter 1: Solutions — long + short notes in Hindi, English, Hinglish. Concentration units, Henry's law, Raoult's law, colligative properties, osmotic pressure, van't Hoff factor.",
 "video": None,
 "card_tag": "Concentration units, Raoult's law, colligative properties aur van't Hoff factor",
 "card_topics": [
  "🧪 Concentration units",
  "⚖️ Raoult's law + azeotropes",
  "📉 Colligative properties",
  "🔢 van't Hoff factor"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Solution Kya Hota Hai — Perfect Mixing Ka Game",
    "body": "<ul>\n<li><b>Solution:</b> do ya zyada substances ka <b>homogeneous mixture</b> — har jagah composition same. (namak paani = solution; mitti paani = nahi, woh suspension hai.)</li>\n<li><b>Solute:</b> jo ghulta hai (kam quantity). <b>Solvent:</b> jo ghulata hai (zyada quantity) — paani sabse common (universal solvent).</li>\n<li><b>Binary solution:</b> sirf 2 components (solute + solvent). Ternary = 3, aur aage.</li>\n<li><b>Types (9 combos):</b> solid/liquid/gas solute × solid/liquid/gas solvent. Jaise — <b>gas in liquid</b> (soda water me CO₂), <b>liquid in liquid</b> (ethanol + water), <b>solid in liquid</b> (namak paani), <b>solid in solid</b> (alloys jaise brass = Cu + Zn), <b>gas in gas</b> (air).</li>\n<li>Solution ke particles bohot chhote (&lt;1 nm) — isliye light scatter nahi hoti (Tyndall effect nahi) aur filter se alag nahi hote.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: solution = aisa mix jisme solute solvent me itna ghul gaya ki alag-alag pehchan hi nahi bachi. Ek dum \"ek ho gaye\" wala scene!</p>"
   },
   {
    "h": "2️⃣ Concentration Units — Kitna Solute, Kitna Solvent ⭐",
    "body": "<ul>\n<li><b>Mass % (w/w):</b> (solute ka mass / solution ka mass) × 100. Temperature se farak NAHI padta.</li>\n<li><b>Mole fraction (x):</b> component ke moles / total moles. x_solute + x_solvent = 1. Unit nahi hoti, temperature-proof.</li>\n<li><b>Molarity (M):</b> solute ke moles / solution ka VOLUME (L). <b>Temperature badhane par M ghatti hai</b> (volume expand hota hai) — yeh iski kami hai!</li>\n<li><b>Molality (m):</b> solute ke moles / solvent ka MASS (kg). <b>Temperature se unaffected</b> (mass constant) — isliye colligative properties me m use hota hai.</li>\n<li><b>Normality (N):</b> gram equivalents / volume (L). <b>ppm:</b> parts per million = (solute mass / solution mass) × 10⁶ — trace quantities ke liye.</li>\n<li><b>Conversion yaad rakho:</b> molarity ↔ molality density ke through judte hain. Dilute solution me (water) m ≈ M × (1000/density).</li>\n</ul>\n<p class=\"small-note\">🎯 Exam favourite: \"Kaunsa unit temperature se independent?\" → mass %, mole fraction, molality. \"Kaunsa dependent?\" → molarity, normality (kyunki volume temperature se badalta hai)!</p>"
   },
   {
    "h": "3️⃣ Solubility aur Henry's Law — Gas Ko Ghulne Do",
    "body": "<ul>\n<li><b>Solubility:</b> kisi temperature pe saturated solution me maximum kitna solute ghul sakta hai. Solid-liquid me: <b>endothermic dissolution (ΔH &gt; 0) pe temperature badhane se solubility badhti hai</b>; exothermic pe ghatti hai.</li>\n<li><b>Pressure ka solid/liquid solubility pe effect negligible</b> (incompressible hain) — lekin <b>gas ki solubility pe pressure ka bada effect!</b></li>\n<li><b>Henry's Law ⭐:</b> constant temperature pe, gas ki solubility us gas ke <b>partial pressure ke directly proportional</b> — <b>p = K_H · x</b> (x = mole fraction of gas in solution). K_H bada → solubility kam.</li>\n<li><b>Applications:</b> soda bottles high pressure pe seal hoti hain (CO₂ zyada ghula), kholte hi pressure girta → fizz! Scuba divers ko <b>bends</b> (N₂ ka blood me ghulna, phir bubbles) — isliye He mix karte hain (He kam soluble). Fish ke liye cold water me O₂ zyada soluble.</li>\n<li>Henry's law sirf <b>low pressure</b> aur jab gas solvent se react NA kare (NH₃/HCl paani me react karte hain — law fail).</li>\n</ul>\n<p class=\"small-note\">💡 Henry's law = \"jitna zor (pressure), utna gas paani me.\" Soda bottle kholo, zor khatam, gas bhaag gayi — simple!</p>"
   },
   {
    "h": "4️⃣ Raoult's Law aur Ideal/Non-Ideal Solutions ⭐⭐",
    "body": "<ul>\n<li><b>Raoult's Law (volatile liquid-liquid):</b> solution me har component ka partial vapour pressure uske <b>mole fraction × pure state ka VP</b> — <b>p₁ = p₁° · x₁</b>. Total VP = p₁°x₁ + p₂°x₂.</li>\n<li><b>Ideal solution:</b> Raoult's law follow karta har concentration pe. A-B interactions ≈ A-A ≈ B-B. <b>ΔH_mix = 0, ΔV_mix = 0.</b> Example: benzene + toluene, hexane + heptane.</li>\n<li><b>Non-ideal — positive deviation ⭐:</b> A-B interactions KAMZOOR → molecules aasani se bhaagte → VP zyada (Raoult se UPAR). <b>ΔH_mix &gt; 0, ΔV_mix &gt; 0.</b> Example: ethanol + water, acetone + CS₂.</li>\n<li><b>Non-ideal — negative deviation ⭐:</b> A-B interactions STRONG → molecules pakde rehte → VP kam (Raoult se NEECHE). <b>ΔH_mix &lt; 0, ΔV_mix &lt; 0.</b> Example: chloroform + acetone (H-bonding), HNO₃ + water.</li>\n<li><b>Trick:</b> positive deviation = \"bhaago\" (kam attraction), negative = \"pakdo\" (zyada attraction). Yaad rakho: ethanol+water = positive (H-bonds tootte).</li>\n</ul>\n<p class=\"small-note\">💡 Ideal = sab barabar pyar (no heat/volume change). Non-ideal = koi zyada chipakta ya zyada bhaagta hai — tabhi VP upar-neeche hota hai!</p>"
   },
   {
    "h": "5️⃣ Azeotropes — Jo Distill Hoke Bhi Alag Na Ho",
    "body": "<ul>\n<li><b>Azeotrope:</b> aisa liquid mixture jo <b>constant boiling point</b> pe ubalta hai aur <b>vapour me bhi same composition</b> — isliye fractional distillation se alag NAHI ho sakta!</li>\n<li><b>Minimum-boiling azeotrope:</b> positive deviation wale. Example: <b>ethanol + water (95.4% ethanol)</b> — isliye pure (100%) ethanol distillation se nahi milta.</li>\n<li><b>Maximum-boiling azeotrope:</b> negative deviation wale. Example: <b>HCl + water (20.2% HCl)</b>, HNO₃ + water (68%).</li>\n<li>Yaad rakhne ka link: positive deviation → VP zyada → BP kam → minimum-boiling azeotrope. Negative → ulta.</li>\n</ul>\n<p class=\"small-note\">💡 Azeotrope = \"jodi pakki\" — ubalne pe bhi saath-saath udte hain, alag karne ka distillation trick fail ho jaata hai!</p>"
   },
   {
    "h": "6️⃣ Colligative Properties (1) — VP, BP, FP ⭐⭐",
    "body": "<ul>\n<li><b>Colligative properties:</b> sirf solute particles ki <b>GINTI (number)</b> pe depend karti hain, unki pehchan (nature) pe NAHI. 4 hain.</li>\n<li><b>(1) Relative lowering of vapour pressure:</b> non-volatile solute daalne se VP girta hai. <b>(p₁° − p₁)/p₁° = x₂</b> (solute ka mole fraction) — yeh Raoult's law hi hai non-volatile ke liye.</li>\n<li><b>(2) Elevation of boiling point ⭐:</b> solute daalne se BP BADHTA hai. <b>ΔT_b = K_b · m</b> (m = molality, K_b = molal elevation constant, solvent ki property). Isliye namak wala paani der se ubalta hai.</li>\n<li><b>(3) Depression of freezing point ⭐:</b> solute daalne se FP GHATTA hai. <b>ΔT_f = K_f · m</b> (K_f = molal depression constant). Isliye barf pe namak (anti-freeze) aur coolant use hota hai.</li>\n<li><b>Molar mass nikalo:</b> ΔT_f = K_f·(w₂×1000)/(M₂×w₁) → yahan se solute ka molar mass M₂ calculate hota hai. K_f (water) = 1.86 K·kg/mol, K_b (water) = 0.52 K·kg/mol.</li>\n</ul>\n<p class=\"small-note\">💡 Colligative = \"headcount game\" — kitne particles, bas wohi matter karta hai. BP upar, FP neeche, VP neeche — teeno ek hi wajah (solute ne solvent ko roka)!</p>"
   },
   {
    "h": "7️⃣ Colligative Properties (2) — Osmotic Pressure ⭐",
    "body": "<ul>\n<li><b>Osmosis:</b> solvent ka <b>semipermeable membrane (SPM)</b> ke through dilute → concentrated side flow karna. SPM sirf solvent ko jaane deta hai, solute ko nahi.</li>\n<li><b>Osmotic pressure (π):</b> osmosis ko rokne ke liye jitna extra pressure lage. <b>π = i·C·R·T = i·(n₂/V)·R·T</b> (C = molarity, T = Kelvin). Sabse ACCURATE colligative property kyunki room temp pe measure hoti hai (biological molecules ke liye best!).</li>\n<li><b>Isotonic solutions ⭐:</b> same osmotic pressure — blood cells 0.9% NaCl (normal saline) me na sikudte na phatte. Hypertonic me cell sikudta, hypotonic me phat-ta hai.</li>\n<li><b>Reverse osmosis (RO):</b> osmotic pressure se ZYADA pressure lagao → solvent ulta behta hai (concentrated → dilute). <b>Sea water desalination</b> me use hota hai — ghar ke RO purifier yahi hain!</li>\n</ul>\n<p class=\"small-note\">💡 Osmosis = \"paani ka bheed-balancing\" — jahan zyada solute (crowded), wahan paani bhaagta hai. RO = bheed ko ulta dhakka!</p>"
   },
   {
    "h": "8️⃣ van't Hoff Factor (i) aur Abnormal Molar Mass ⭐⭐",
    "body": "<ul>\n<li><b>van't Hoff factor (i):</b> actual colligative effect / expected effect — <b>i = observed colligative property / calculated colligative property = normal molar mass / abnormal molar mass.</b></li>\n<li><b>Dissociation (i &gt; 1):</b> electrolyte tootta hai → particles zyada → colligative effect zyada → molar mass KAM aata hai. NaCl → Na⁺ + Cl⁻ (i ≈ 2), CaCl₂ (i ≈ 3), K₄[Fe(CN)₆] (i ≈ 5).</li>\n<li><b>Association (i &lt; 1):</b> particles judte hain → count kam → colligative effect kam → molar mass ZYADA aata hai. <b>Acetic acid benzene me dimerize</b> karta hai (i ≈ 0.5), benzoic acid bhi.</li>\n<li><b>Modified formulas ⭐:</b> ΔT_b = i·K_b·m, ΔT_f = i·K_f·m, π = i·CRT, (Δp/p°) = i·x₂. Degree of dissociation: α = (i−1)/(n−1); association: α = (1−i)/(1−1/n).</li>\n<li>Non-electrolyte (glucose, urea, sugar) ke liye i = 1 — na tootte, na jude.</li>\n</ul>\n<p class=\"small-note\">💡 i = \"asli headcount multiplier\" — tootta hai to zyada (i upar), judta hai to kam (i neeche). Question me \"electrolyte\" dekha to i ka dhyan!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ विलयन क्या है",
    "body": "<ul>\n<li><b>विलयन (Solution):</b> दो या अधिक पदार्थों का <b>समांगी मिश्रण</b> — हर जगह संघटन समान।</li>\n<li><b>विलेय (Solute):</b> जो घुलता है (कम मात्रा)। <b>विलायक (Solvent):</b> जो घुलाता है (अधिक मात्रा)।</li>\n<li><b>प्रकार:</b> solid/liquid/gas विलेय × solid/liquid/gas विलायक — जैसे soda में CO₂ (gas in liquid), नमक-पानी (solid in liquid), पीतल (solid in solid)।</li>\n</ul>\n<p class=\"small-note\">💡 विलयन में कण इतने छोटे (&lt;1 nm) कि फ़िल्टर से अलग नहीं होते।</p>"
   },
   {
    "h": "2️⃣ सांद्रता इकाइयाँ ⭐",
    "body": "<ul>\n<li><b>द्रव्यमान %:</b> (विलेय द्रव्यमान/विलयन द्रव्यमान)×100 — तापमान-मुक्त।</li>\n<li><b>मोल अंश (x):</b> घटक मोल/कुल मोल — इकाई-रहित।</li>\n<li><b>मोलरता (M):</b> मोल/आयतन(L) — तापमान से बदलती है।</li>\n<li><b>मोललता (m):</b> मोल/विलायक द्रव्यमान(kg) — तापमान-मुक्त ⭐ (colligative में यही)।</li>\n</ul>\n<p class=\"small-note\">🎯 तापमान-स्वतंत्र: mass %, mole fraction, molality. तापमान-आश्रित: molarity, normality।</p>"
   },
   {
    "h": "3️⃣ विलेयता और Henry नियम",
    "body": "<ul>\n<li><b>Henry नियम ⭐:</b> p = K_H·x — गैस की विलेयता उसके partial pressure के समानुपाती।</li>\n<li>Soda bottle high pressure पर seal — खोलने पर फ़िज़। Scuba में bends (N₂ घुलना)।</li>\n</ul>\n<p class=\"small-note\">💡 जितना दाब, उतनी गैस घुली।</p>"
   },
   {
    "h": "4️⃣ Raoult नियम और आदर्श/अनादर्श ⭐⭐",
    "body": "<ul>\n<li><b>Raoult:</b> p₁ = p₁°·x₁। <b>आदर्श:</b> ΔH=0, ΔV=0 (benzene+toluene)।</li>\n<li><b>धनात्मक विचलन:</b> A-B कमज़ोर, VP ऊपर (ethanol+water)। <b>ऋणात्मक:</b> A-B मज़बूत, VP नीचे (chloroform+acetone)।</li>\n</ul>\n<p class=\"small-note\">💡 धनात्मक = \"भागो\", ऋणात्मक = \"पकड़ो\"।</p>"
   },
   {
    "h": "5️⃣ ऐज़ियोट्रोप",
    "body": "<ul>\n<li><b>ऐज़ियोट्रोप:</b> स्थिर क्वथनांक, आसवन से अलग नहीं। न्यूनतम-क्वथी: ethanol+water (95.4%); अधिकतम-क्वथी: HCl+water (20.2%)।</li>\n</ul>\n<p class=\"small-note\">💡 उबलने पर भी साथ उड़ते हैं।</p>"
   },
   {
    "h": "6️⃣ अणुसंख्य गुण (VP, BP, FP) ⭐⭐",
    "body": "<ul>\n<li><b>वाष्पदाब अवनमन:</b> (p°−p)/p° = x₂। <b>क्वथनांक उन्नयन:</b> ΔT_b = K_b·m। <b>हिमांक अवनमन:</b> ΔT_f = K_f·m (K_f जल=1.86)।</li>\n</ul>\n<p class=\"small-note\">💡 केवल कणों की संख्या मायने रखती है, प्रकृति नहीं।</p>"
   },
   {
    "h": "7️⃣ परासरण दाब ⭐",
    "body": "<ul>\n<li><b>परासरण:</b> विलायक SPM से dilute→concentrated। <b>π = iCRT</b>। सम-परासरी: 0.9% NaCl (रक्त कोशिका सुरक्षित)। RO = विलोम परासरण (समुद्री जल शुद्धिकरण)।</li>\n</ul>\n<p class=\"small-note\">💡 जहाँ अधिक विलेय, वहाँ पानी भागता है।</p>"
   },
   {
    "h": "8️⃣ van't Hoff गुणक (i) ⭐⭐",
    "body": "<ul>\n<li><b>i = observed/calculated colligative</b>। <b>वियोजन:</b> i&gt;1 (NaCl≈2, CaCl₂≈3)। <b>संघनन:</b> i&lt;1 (acetic acid dimer≈0.5)। सूत्रों में i गुणा करो।</li>\n</ul>\n<p class=\"small-note\">💡 टूटे तो i ऊपर, जुड़े तो i नीचे।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ What is a Solution",
    "body": "<ul>\n<li><b>Solution:</b> a <b>homogeneous mixture</b> of two or more substances — uniform composition throughout.</li>\n<li><b>Solute</b> dissolves (smaller amount); <b>solvent</b> dissolves it (larger amount). 9 type combos (gas/liquid/solid × gas/liquid/solid).</li>\n<li>Particles are tiny (&lt;1 nm) — no Tyndall effect, can't be filtered out.</li>\n</ul>\n<p class=\"small-note\">💡 A solution is a mixture so uniform the solute can't be distinguished anymore.</p>"
   },
   {
    "h": "2️⃣ Concentration Units ⭐",
    "body": "<ul>\n<li><b>Mass %:</b> (solute mass/solution mass)×100. <b>Mole fraction:</b> moles/total moles (unitless).</li>\n<li><b>Molarity (M):</b> moles/volume(L) — temperature DEPENDENT. <b>Molality (m):</b> moles/solvent mass(kg) — temperature INDEPENDENT.</li>\n</ul>\n<p class=\"small-note\">🎯 Temperature-independent: mass %, mole fraction, molality. Dependent: molarity, normality.</p>"
   },
   {
    "h": "3️⃣ Solubility & Henry's Law",
    "body": "<ul>\n<li><b>Henry's Law ⭐:</b> p = K_H·x — a gas's solubility is proportional to its partial pressure. Soda fizz, scuba bends (N₂).</li>\n</ul>\n<p class=\"small-note\">💡 More pressure → more gas dissolves.</p>"
   },
   {
    "h": "4️⃣ Raoult's Law & Ideal/Non-ideal ⭐⭐",
    "body": "<ul>\n<li><b>Raoult:</b> p₁ = p₁°·x₁. <b>Ideal:</b> ΔH=0, ΔV=0 (benzene+toluene). <b>Positive deviation:</b> weaker A-B, VP up (ethanol+water). <b>Negative:</b> stronger A-B, VP down (chloroform+acetone).</li>\n</ul>\n<p class=\"small-note\">💡 Positive = molecules escape, negative = molecules stick.</p>"
   },
   {
    "h": "5️⃣ Azeotropes",
    "body": "<ul>\n<li><b>Azeotrope:</b> constant BP, same vapour composition — can't be separated by distillation. Min-boiling: ethanol+water (95.4%); max-boiling: HCl+water (20.2%).</li>\n</ul>\n<p class=\"small-note\">💡 They boil together and stay together.</p>"
   },
   {
    "h": "6️⃣ Colligative Properties (VP, BP, FP) ⭐⭐",
    "body": "<ul>\n<li>Depend only on the NUMBER of solute particles. <b>RLVP:</b> (p°−p)/p° = x₂. <b>Boiling elevation:</b> ΔT_b = K_b·m. <b>Freezing depression:</b> ΔT_f = K_f·m (K_f water = 1.86).</li>\n</ul>\n<p class=\"small-note\">💡 Only the count matters, not the identity.</p>"
   },
   {
    "h": "7️⃣ Osmotic Pressure ⭐",
    "body": "<ul>\n<li><b>Osmosis:</b> solvent flows through a semipermeable membrane from dilute to concentrated. <b>π = iCRT.</b> Isotonic: 0.9% NaCl. Reverse osmosis = seawater desalination.</li>\n</ul>\n<p class=\"small-note\">💡 Water moves toward the more concentrated side.</p>"
   },
   {
    "h": "8️⃣ van't Hoff Factor (i) ⭐⭐",
    "body": "<ul>\n<li><b>i = observed/calculated colligative property.</b> Dissociation: i&gt;1 (NaCl≈2, CaCl₂≈3). Association: i&lt;1 (acetic acid dimer≈0.5). Multiply all colligative formulas by i.</li>\n</ul>\n<p class=\"small-note\">💡 Dissociation raises i, association lowers it.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Concentration Units",
    "items": [
     "Molarity M = moles/volume(L) — temp dependent",
     "Molality m = moles/solvent(kg) — temp independent ⭐",
     "Mole fraction x — unitless, temp independent",
     "Mass %, ppm — temp independent"
    ]
   },
   {
    "h": "Henry & Raoult",
    "items": [
     "Henry: p = K_H·x (gas solubility ∝ pressure)",
     "Raoult: p₁ = p₁°·x₁",
     "Ideal: ΔH=0, ΔV=0 (benzene+toluene)",
     "Positive deviation: ethanol+water; Negative: chloroform+acetone"
    ]
   },
   {
    "h": "Azeotrope",
    "items": [
     "Constant BP, distill se alag nahi",
     "Min-boiling: ethanol+water (95.4%)",
     "Max-boiling: HCl+water (20.2%)"
    ]
   },
   {
    "h": "Colligative (4)",
    "items": [
     "RLVP: (p°−p)/p° = x₂",
     "ΔT_b = i·K_b·m (BP upar)",
     "ΔT_f = i·K_f·m (FP neeche), K_f water=1.86",
     "π = i·CRT (osmosis; RO = desalination)"
    ]
   },
   {
    "h": "van't Hoff i",
    "items": [
     "i = observed/calculated colligative",
     "Dissociation i>1 (NaCl≈2, CaCl₂≈3)",
     "Association i<1 (acetic acid dimer≈0.5)",
     "Non-electrolyte i=1 (glucose)"
    ]
   }
  ],
  "hi": [
   {
    "h": "सांद्रता",
    "items": [
     "M = मोल/आयतन(L) — तापमान-आश्रित",
     "m = मोल/विलायक(kg) — तापमान-मुक्त",
     "mole fraction — इकाई-रहित"
    ]
   },
   {
    "h": "Henry/Raoult",
    "items": [
     "Henry: p=K_H·x",
     "Raoult: p₁=p₁°·x₁",
     "आदर्श: ΔH=0,ΔV=0"
    ]
   },
   {
    "h": "ऐज़ियोट्रोप",
    "items": [
     "स्थिर BP, अलग नहीं",
     "ethanol+water (95.4%)"
    ]
   },
   {
    "h": "अणुसंख्य",
    "items": [
     "ΔT_b=iK_b·m",
     "ΔT_f=iK_f·m (K_f=1.86)",
     "π=iCRT"
    ]
   },
   {
    "h": "van't Hoff i",
    "items": [
     "वियोजन i>1",
     "संघनन i<1",
     "non-electrolyte i=1"
    ]
   }
  ],
  "en": [
   {
    "h": "Concentration",
    "items": [
     "Molarity = mol/L (temp dependent)",
     "Molality = mol/kg (temp independent)",
     "Mole fraction (unitless)"
    ]
   },
   {
    "h": "Henry/Raoult",
    "items": [
     "Henry: p=K_H·x",
     "Raoult: p₁=p₁°·x₁",
     "Ideal: ΔH=0,ΔV=0"
    ]
   },
   {
    "h": "Azeotrope",
    "items": [
     "Constant BP, not separable",
     "ethanol+water (95.4%)"
    ]
   },
   {
    "h": "Colligative",
    "items": [
     "ΔT_b=iK_b·m",
     "ΔT_f=iK_f·m (K_f=1.86)",
     "π=iCRT"
    ]
   },
   {
    "h": "van't Hoff i",
    "items": [
     "Dissociation i>1",
     "Association i<1",
     "Non-electrolyte i=1"
    ]
   }
  ]
 },
 "practice": [
  [
   "Molarity aur molality me temperature ke hisaab se kya farak hai?",
   "<b>Molarity temperature-dependent</b> hai (volume badalta hai), <b>molality independent</b> (mass constant)."
  ],
  [
   "Henry's law likho aur ek application batao.",
   "<b>p = K_H·x</b>. Application: soda bottle me CO₂ high pressure pe ghula, khulne par fizz."
  ],
  [
   "Ideal solution ke 2 characteristics batao.",
   "Raoult's law follow karta hai; <b>ΔH_mix = 0 aur ΔV_mix = 0</b> (jaise benzene + toluene)."
  ],
  [
   "Ethanol + water kaunsa deviation dikhata hai aur kyun?",
   "<b>Positive deviation</b> — ethanol-water H-bonds tootte hain, A-B kamzor, isliye VP Raoult se zyada."
  ],
  [
   "Azeotrope kya hota hai? Ek example do.",
   "Constant boiling mixture jo distillation se alag nahi hota. Example: <b>ethanol + water (95.4%)</b>."
  ],
  [
   "Freezing point depression ka formula aur K_f (water) ki value.",
   "<b>ΔT_f = i·K_f·m</b>, K_f (water) = <b>1.86 K·kg/mol</b>."
  ],
  [
   "Osmotic pressure ka formula? RO kahan use hota hai?",
   "<b>π = i·C·R·T</b>. Reverse osmosis <b>sea water desalination</b> (RO purifier) me."
  ],
  [
   "NaCl ke liye van't Hoff factor kitna hota hai aur kyun?",
   "<b>i ≈ 2</b> — NaCl → Na⁺ + Cl⁻ me dissociate hota hai, particles double."
  ],
  [
   "Acetic acid ko benzene me dalne par molar mass zyada kyun aata hai?",
   "<b>Association</b> — dimerize hota hai (i ≈ 0.5), particles kam, isliye abnormal (zyada) molar mass."
  ],
  [
   "Isotonic solution kya hai? Blood cells ke liye kaunsa use hota hai?",
   "Same osmotic pressure wale solutions. Blood cells ke liye <b>0.9% NaCl (normal saline)</b>."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/chemistry/ch-2/",
  "title": "Electrochemistry"
 }
}

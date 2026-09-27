# Class 12 Physics, Chapter 3 - Current Electricity
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 3,
 "title_en": "Current Electricity",
 "title_hi": "विद्युत धारा",
 "tagline": "Circuits ka asli khel — Ohm, Kirchhoff, Wheatstone aur power",
 "jee": "HIGH",
 "meta_desc": "Class 12 Physics Chapter 3: Current Electricity — long + short notes in Hindi, English, Hinglish. Ohm's law, drift velocity, Kirchhoff's rules, Wheatstone bridge, power.",
 "video": None,
 "card_tag": "Circuits ka asli khel — Ohm, Kirchhoff, Wheatstone aur power",
 "card_topics": [
  "🔌 Drift velocity I = neAv",
  "📏 Ohm's law + R = ρL/A",
  "🔀 Kirchhoff + Wheatstone",
  "💡 Power P = VI + kWh"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Current aur Drift Velocity — Electron Ka Slow Walk",
    "body": "<ul>\n<li><b>Electric current:</b> charge ka flow — <b>I = Q/t</b>. Unit: ampere (1 A = 1 C/s). Direction conventionally POSITIVE charge ki flow ki taraf (electrons ulta chalte hain!).</li>\n<li><b>Drift velocity ⭐:</b> electrons electric field me bahut DHEERE drift karte hain — sirf ~mm/s! (Signal fast jaata hai kyunki saare electrons ek saath dhakka lagate hain — pipe me paani jaisa.)</li>\n<li><b>Relation ⭐⭐:</b> <b>I = neAv_d</b> — jahan n = electron density, e = charge, A = area, v_d = drift velocity.</li>\n<li><b>Mobility:</b> μ = v_d/E — field per unit kitni speed. <b>Current density:</b> j = I/A = nev_d (vector hai!).</li>\n<li><b>Steady current:</b> constant rate ka flow; instantaneous: I = dQ/dt.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: switch on karte hi light kyun? Electric field light ki speed se establish hota hai, saare electrons ek saath chal padte hain — kisi ek electron ko travel nahi karna!</p>"
   },
   {
    "h": "2️⃣ Ohm's Law aur Resistance ⭐⭐",
    "body": "<ul>\n<li><b>Ohm's law ⭐:</b> <b>V = IR</b> — constant temperature pe current voltage ke proportional. Unit of R: ohm (Ω).</li>\n<li><b>Resistance formula ⭐⭐:</b> <b>R = ρL/A</b> — lamba wire zyada resistance, mota wire kam. ρ = resistivity (material ki property, unit Ω·m).</li>\n<li><b>Conductivity:</b> σ = 1/ρ. Ohm's law vector form: j = σE.</li>\n<li><b>Temperature dependence ⭐:</b> metals me T badhao → R badhta hai (R = R₀(1 + αΔT)); semiconductors me T badhao → R GHATTA hai (zyada free carriers!).</li>\n<li><b>Non-ohmic devices:</b> diode, transistor, electrolytes — V-I graph straight line nahi (Ohm's law follow nahi karte).</li>\n<li><b>Superconductors:</b> kuch materials critical temperature ke neeche R = 0 kar dete hain!</li>\n</ul>\n<p class=\"small-note\">🎯 ρ sirf material pe depend karta hai; R shape pe bhi. Same copper ka lamba patla wire = zyada R, chhota mota = kam R.</p>"
   },
   {
    "h": "3️⃣ Cells, EMF aur Internal Resistance ⭐",
    "body": "<ul>\n<li><b>EMF (ε):</b> cell ka total voltage jab koi current NA ho — chemical energy se charge ko dhakka. Unit: volt. Ye force nahi hai, naam misleading hai!</li>\n<li><b>Internal resistance (r) ⭐:</b> cell ke andar ka apna resistance. Circuit me current behe to terminal voltage <b>V = ε − Ir</b> — discharge me EMF se kam!</li>\n<li><b>Charging me:</b> V = ε + Ir (ulta sign).</li>\n<li><b>Short circuit:</b> R = 0 to I = ε/r — max current (danger!).</li>\n<li><b>Cells in series ⭐:</b> ε_eq = ε₁ + ε₂, r_eq = r₁ + r₂ (zyada voltage chahiye to). Ek cell ulta ho to uska EMF minus.</li>\n<li><b>Cells in parallel ⭐:</b> ε_eq = (ε₁/r₁ + ε₂/r₂)/(1/r₁ + 1/r₂), 1/r_eq = 1/r₁ + 1/r₂ (zyada current/life chahiye to). Identical cells: ε_eq = ε, r_eq = r/n.</li>\n</ul>\n<p class=\"small-note\">💡 Battery weak kyun lagti hai purani hone pe? Internal resistance badh jaata hai — V = ε − Ir me zyada voltage andar hi kho jaata hai!</p>"
   },
   {
    "h": "4️⃣ Kirchhoff's Rules — Circuit Solving Ka Brahmastra ⭐⭐",
    "body": "<ul>\n<li><b>Junction rule (KCL) ⭐:</b> kisi bhi junction pe incoming current = outgoing current. <b>ΣI = 0</b>. Basis: charge conservation (charge junction pe jama nahi ho sakta).</li>\n<li><b>Loop rule (KVL) ⭐:</b> kisi closed loop me saare voltage changes ka sum = 0. <b>ΣV = 0</b>. Basis: energy conservation.</li>\n<li><b>Sign convention:</b> loop direction me resistor cross karo current ke saath → −IR; battery − se + → +ε. Direction ulta to sign ulta.</li>\n<li><b>Method:</b> har branch me current assume karo (direction guess karo — galat ho to answer negative aa jaayega, no problem!), junction equations likho, loops likho, solve karo.</li>\n<li><b>Kab use karo:</b> jab simple series-parallel se circuit na bane — multiple batteries, complex networks.</li>\n</ul>\n<p class=\"small-note\">💡 KCL = charge ki accountancy (jo aaya wo gaya), KVL = energy ki accountancy (jo ghuma, wapas same level pe). Circuit = balance sheet!</p>"
   },
   {
    "h": "5️⃣ Wheatstone Bridge aur Meter Bridge ⭐",
    "body": "<ul>\n<li><b>Wheatstone bridge ⭐⭐:</b> 4 resistors ka diamond circuit + beech me galvanometer. <b>Balanced condition: P/Q = R/S</b> — galvanometer me ZERO current, beech wala resistor ignore kar do!</li>\n<li><b>Balanced hone pe:</b> B aur D points same potential pe — bridge ke through koi current nahi. Circuit simple series-parallel ban jaata hai.</li>\n<li><b>Unbalanced bridge:</b> Kirchhoff se solve karna padta hai — shortcut nahi!</li>\n<li><b>Meter bridge (practical):</b> Wheatstone ka practical form — 1 m uniform wire pe jockey slide karke balance point dhundhte hain. Unknown resistance: S = R(100 − l)/l.</li>\n<li><b>Uses:</b> accurate resistance measurement — unknown R ko known se compare karke.</li>\n</ul>\n<p class=\"small-note\">🎯 Balanced bridge me middle resistor dead weight hai — hata do ya ideal short karo, koi farak nahi. Exam me pehle balance check karo!</p>"
   },
   {
    "h": "6️⃣ Electrical Energy aur Power ⭐",
    "body": "<ul>\n<li><b>Electric power ⭐:</b> <b>P = VI = I²R = V²/R</b> — teeno forms, situation ke hisaab se. Unit: watt.</li>\n<li><b>Heat produced (Joule heating):</b> H = I²Rt — fuse, heater, bulb sab isi pe kaam karte hain.</li>\n<li><b>Electric energy:</b> E = Pt = VIt. Unit: joule; <b>commercial unit: kilowatt-hour (kWh) = 3.6 × 10⁶ J</b> — bijli ka bill isi me aata hai! ⭐</li>\n<li><b>Series me bulbs:</b> zyada R wala zyada glow (P = I²R, I same); <b>parallel me:</b> kam R wala zyada glow (P = V²/R, V same) — dono cases confuse mat karna! ⭐</li>\n<li><b>Max power transfer:</b> source se max power tab milti hai jab external R = internal r.</li>\n<li><b>Efficiency:</b> η = output power/input power; cell ke liye η = R/(R + r).</li>\n</ul>\n<p class=\"small-note\">💡 100 W bulb ka matlab: rated voltage pe 100 J/s energy use. Ghar ka 1 unit = 1 kWh = 1000 W × 3600 s!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ धारा और अनुगमन वेग — इलेक्ट्रॉन की धीमी चाल",
    "body": "<ul>\n<li><b>विद्युत धारा:</b> आवेश का प्रवाह — <b>I = Q/t</b>। मात्रक: एंपियर। दिशा पारंपरिक रूप से धन आवेश के प्रवाह की ओर (इलेक्ट्रॉन विपरीत चलते हैं!)।</li>\n<li><b>अनुगमन वेग ⭐:</b> इलेक्ट्रॉन क्षेत्र में अत्यंत धीरे अनुगमन करते हैं — केवल ~mm/s!</li>\n<li><b>संबंध ⭐⭐:</b> <b>I = neAv_d</b> — n = इलेक्ट्रॉन घनत्व, A = क्षेत्रफल, v_d = अनुगमन वेग।</li>\n<li><b>गतिशीलता:</b> μ = v_d/E। <b>धारा घनत्व:</b> j = I/A = nev_d (सदिश)।</li>\n</ul>\n<p class=\"small-note\">💡 स्विच ऑन करते ही बल्ब क्यों जलता है? क्षेत्र प्रकाश की चाल से स्थापित होता है, सभी इलेक्ट्रॉन एक साथ चल पड़ते हैं!</p>"
   },
   {
    "h": "2️⃣ ओम का नियम और प्रतिरोध ⭐⭐",
    "body": "<ul>\n<li><b>ओम का नियम ⭐:</b> <b>V = IR</b> — नियत ताप पर धारा वोल्टता के समानुपाती। R का मात्रक: ओम (Ω)।</li>\n<li><b>प्रतिरोध सूत्र ⭐⭐:</b> <b>R = ρL/A</b> — लंबा तार अधिक प्रतिरोध, मोटा तार कम। ρ = प्रतिरोधकता (Ω·m)।</li>\n<li><b>चालकता:</b> σ = 1/ρ। सदिश रूप: j = σE।</li>\n<li><b>ताप निर्भरता ⭐:</b> धातुओं में T बढ़ाओ → R बढ़ता है; अर्धचालकों में T बढ़ाओ → R <b>घटता</b> है!</li>\n<li><b>अन-ओमीय युक्तियां:</b> डायोड, ट्रांजिस्टर — V-I ग्राफ सीधी रेखा नहीं।</li>\n<li><b>अतिचालक:</b> क्रांतिक ताप से नीचे R = 0!</li>\n</ul>\n<p class=\"small-note\">🎯 ρ केवल पदार्थ पर निर्भर; R आकृति पर भी।</p>"
   },
   {
    "h": "3️⃣ सेल, विद्युत वाहक बल और आंतरिक प्रतिरोध ⭐",
    "body": "<ul>\n<li><b>वि.वा.बल (ε):</b> सेल का कुल वोल्टता जब धारा न बह रही हो। यह बल नहीं है!</li>\n<li><b>आंतरिक प्रतिरोध (r) ⭐:</b> सेल का अपना प्रतिरोध। धारा बहने पर सीरा वोल्टता <b>V = ε − Ir</b>!</li>\n<li><b>आवेशन में:</b> V = ε + Ir।</li>\n<li><b>लघुपथन:</b> R = 0 तो I = ε/r — अधिकतम धारा (खतरा!)।</li>\n<li><b>श्रेणी में सेल ⭐:</b> ε_कुल = ε₁ + ε₂, r_कुल = r₁ + r₂।</li>\n<li><b>समांतर में ⭐:</b> समान सेल: ε_कुल = ε, r_कुल = r/n।</li>\n</ul>\n<p class=\"small-note\">💡 पुरानी बैटरी कमजोर क्यों? आंतरिक प्रतिरोध बढ़ जाता है — V = ε − Ir में अधिक वोल्टता भीतर खो जाता है!</p>"
   },
   {
    "h": "4️⃣ किरचॉफ के नियम — परिपथ समाधान का ब्रह्मास्त्र ⭐⭐",
    "body": "<ul>\n<li><b>संधि नियम (KCL) ⭐:</b> किसी संधि पर आने वाली धारा = जाने वाली धारा। <b>ΣI = 0</b>। आधार: आवेश संरक्षण।</li>\n<li><b>पाश नियम (KVL) ⭐:</b> बंद पाश में सभी वोल्टता परिवर्तनों का योग = 0। <b>ΣV = 0</b>। आधार: ऊर्जा संरक्षण।</li>\n<li><b>चिह्न परिपाटी:</b> पाश दिशा में धारा के साथ प्रतिरोध → −IR; बैटरी − से + → +ε।</li>\n<li><b>विधि:</b> प्रत्येक शाखा में धारा मानो, संधि समीकरण लिखो, पाश लिखो, हल करो। दिशा गलत हो तो उत्तर ऋणात्मक आएगा — कोई समस्या नहीं!</li>\n</ul>\n<p class=\"small-note\">💡 KCL = आवेश की बही-खाता, KVL = ऊर्जा की बही-खाता।</p>"
   },
   {
    "h": "5️⃣ व्हीटस्टोन सेतु और मीटर सेतु ⭐",
    "body": "<ul>\n<li><b>व्हीटस्टोन सेतु ⭐⭐:</b> 4 प्रतिरोधों का परिपथ + बीच में धारामापी। <b>संतुलन शर्त: P/Q = R/S</b> — धारामापी में शून्य धारा!</li>\n<li><b>संतुलित होने पर:</b> बीच वाला प्रतिरोध निरर्थक — परिपथ सरल श्रेणी-समांतर बन जाता है।</li>\n<li><b>असंतुलित सेतु:</b> किरचॉफ से हल करना पड़ता है।</li>\n<li><b>मीटर सेतु (प्रयोग):</b> 1 m एकसमान तार पर जॉकी से संतुलन बिंदु। अज्ञात प्रतिरोध: S = R(100 − l)/l।</li>\n</ul>\n<p class=\"small-note\">🎯 संतुलित सेतु में मध्य प्रतिरोध हटा दो — कोई फर्क नहीं। परीक्षा में पहले संतुलन जांचो!</p>"
   },
   {
    "h": "6️⃣ विद्युत ऊर्जा और शक्ति ⭐",
    "body": "<ul>\n<li><b>विद्युत शक्ति ⭐:</b> <b>P = VI = I²R = V²/R</b> — तीनों रूप। मात्रक: वाट।</li>\n<li><b>ऊष्मा (जूल तापन):</b> H = I²Rt — फ्यूज, हीटर, बल्ब सब इसी पर।</li>\n<li><b>विद्युत ऊर्जा:</b> E = Pt। <b>वाणिज्यिक मात्रक: किलोवाट-घंटा (kWh) = 3.6 × 10⁶ J</b> — बिजली बिल इसी में! ⭐</li>\n<li><b>श्रेणी में बल्ब:</b> अधिक R वाला अधिक चमके (P = I²R); <b>समांतर में:</b> कम R वाला अधिक (P = V²/R) ⭐</li>\n<li><b>अधिकतम शक्ति स्थानांतरण:</b> जब बाह्य R = आंतरिक r।</li>\n</ul>\n<p class=\"small-note\">💡 घर का 1 यूनिट = 1 kWh = 1000 W × 3600 s!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Current and Drift Velocity — The Electron's Slow Walk",
    "body": "<ul>\n<li><b>Electric current:</b> the flow of charge — <b>I = Q/t</b>. Unit: ampere (1 A = 1 C/s). Conventional direction follows POSITIVE charge flow (electrons actually move the other way!).</li>\n<li><b>Drift velocity ⭐:</b> electrons drift VERY slowly in a field — only ~mm/s! (The signal is fast because all electrons push at once — like water already filling a pipe.)</li>\n<li><b>Relation ⭐⭐:</b> <b>I = neAv_d</b> — where n = electron density, e = charge, A = area, v_d = drift velocity.</li>\n<li><b>Mobility:</b> μ = v_d/E — speed per unit field. <b>Current density:</b> j = I/A = nev_d (it is a vector!).</li>\n<li><b>Steady current:</b> constant rate of flow; instantaneous: I = dQ/dt.</li>\n</ul>\n<p class=\"small-note\">💡 Why does the bulb glow instantly? The electric field sets up at nearly light speed, so ALL electrons start moving together — no single electron needs to travel!</p>"
   },
   {
    "h": "2️⃣ Ohm's Law and Resistance ⭐⭐",
    "body": "<ul>\n<li><b>Ohm's law ⭐:</b> <b>V = IR</b> — at constant temperature, current is proportional to voltage. Unit of R: ohm (Ω).</li>\n<li><b>Resistance formula ⭐⭐:</b> <b>R = ρL/A</b> — longer wire, more resistance; thicker wire, less. ρ = resistivity (a material property, unit Ω·m).</li>\n<li><b>Conductivity:</b> σ = 1/ρ. Vector form of Ohm's law: j = σE.</li>\n<li><b>Temperature dependence ⭐:</b> metals: raise T → R rises (R = R₀(1 + αΔT)); semiconductors: raise T → R FALLS (more free carriers!).</li>\n<li><b>Non-ohmic devices:</b> diode, transistor, electrolytes — the V-I graph is not a straight line.</li>\n<li><b>Superconductors:</b> below a critical temperature some materials drop to R = 0!</li>\n</ul>\n<p class=\"small-note\">🎯 ρ depends only on the material; R also depends on shape. Same copper: long thin wire = high R, short thick wire = low R.</p>"
   },
   {
    "h": "3️⃣ Cells, EMF and Internal Resistance ⭐",
    "body": "<ul>\n<li><b>EMF (ε):</b> the cell's total voltage when NO current flows — chemical energy pushing charges. Unit: volt. It is not a force; the name is misleading!</li>\n<li><b>Internal resistance (r) ⭐:</b> the cell's own resistance. When current flows, terminal voltage <b>V = ε − Ir</b> — less than EMF during discharge!</li>\n<li><b>While charging:</b> V = ε + Ir (opposite sign).</li>\n<li><b>Short circuit:</b> R = 0 gives I = ε/r — maximum current (danger!).</li>\n<li><b>Cells in series ⭐:</b> ε_eq = ε₁ + ε₂, r_eq = r₁ + r₂ (for more voltage). A reversed cell subtracts its EMF.</li>\n<li><b>Cells in parallel ⭐:</b> ε_eq = (ε₁/r₁ + ε₂/r₂)/(1/r₁ + 1/r₂), 1/r_eq = 1/r₁ + 1/r₂ (for more current/life). Identical cells: ε_eq = ε, r_eq = r/n.</li>\n</ul>\n<p class=\"small-note\">💡 Why do old batteries feel weak? Internal resistance grows — in V = ε − Ir, more voltage is lost inside the cell itself!</p>"
   },
   {
    "h": "4️⃣ Kirchhoff's Rules — The Circuit-Solving Weapon ⭐⭐",
    "body": "<ul>\n<li><b>Junction rule (KCL) ⭐:</b> at any junction, incoming current = outgoing current. <b>ΣI = 0</b>. Basis: charge conservation (charge cannot pile up at a junction).</li>\n<li><b>Loop rule (KVL) ⭐:</b> around any closed loop, the sum of all voltage changes = 0. <b>ΣV = 0</b>. Basis: energy conservation.</li>\n<li><b>Sign convention:</b> crossing a resistor along the loop with the current → −IR; battery from − to + → +ε. Reverse direction, reverse sign.</li>\n<li><b>Method:</b> assume a current in every branch (guess the direction — if wrong, the answer just comes out negative, no problem!), write junction equations, write loops, solve.</li>\n<li><b>When to use:</b> when the circuit is not simple series-parallel — multiple batteries, complex networks.</li>\n</ul>\n<p class=\"small-note\">💡 KCL = accounting for charge (what comes in must leave), KVL = accounting for energy (around a loop you return to the same level). A circuit is a balance sheet!</p>"
   },
   {
    "h": "5️⃣ Wheatstone Bridge and Meter Bridge ⭐",
    "body": "<ul>\n<li><b>Wheatstone bridge ⭐⭐:</b> a diamond circuit of 4 resistors with a galvanometer across the middle. <b>Balance condition: P/Q = R/S</b> — ZERO current in the galvanometer, so the middle resistor can be ignored!</li>\n<li><b>When balanced:</b> points B and D are at the same potential — no current crosses the bridge. The circuit reduces to simple series-parallel.</li>\n<li><b>Unbalanced bridge:</b> must be solved with Kirchhoff — no shortcut!</li>\n<li><b>Meter bridge (practical):</b> the practical form of Wheatstone — a jockey slides on a 1 m uniform wire to find the balance point. Unknown resistance: S = R(100 − l)/l.</li>\n<li><b>Uses:</b> accurate resistance measurement by comparing an unknown R against known ones.</li>\n</ul>\n<p class=\"small-note\">🎯 In a balanced bridge the middle resistor is dead weight — remove it or short it ideally, no difference. Check balance first in exams!</p>"
   },
   {
    "h": "6️⃣ Electrical Energy and Power ⭐",
    "body": "<ul>\n<li><b>Electric power ⭐:</b> <b>P = VI = I²R = V²/R</b> — three forms, pick by situation. Unit: watt.</li>\n<li><b>Heat produced (Joule heating):</b> H = I²Rt — fuses, heaters and bulbs all work on this.</li>\n<li><b>Electric energy:</b> E = Pt = VIt. Unit: joule; <b>commercial unit: kilowatt-hour (kWh) = 3.6 × 10⁶ J</b> — your electricity bill counts these! ⭐</li>\n<li><b>Bulbs in series:</b> higher R glows brighter (P = I²R, same I); <b>in parallel:</b> lower R glows brighter (P = V²/R, same V) — do not mix up the two cases! ⭐</li>\n<li><b>Maximum power transfer:</b> a source delivers maximum power when external R = internal r.</li>\n<li><b>Efficiency:</b> η = output/input power; for a cell η = R/(R + r).</li>\n</ul>\n<p class=\"small-note\">💡 A 100 W bulb uses 100 J/s at its rated voltage. One home unit = 1 kWh = 1000 W × 3600 s!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Current + Drift ⭐",
    "items": [
     "I = Q/t, ampere",
     "I = neAv_d, drift ~mm/s",
     "j = I/A = nev_d"
    ]
   },
   {
    "h": "Ohm + Resistance ⭐⭐",
    "items": [
     "V = IR; R = ρL/A",
     "Metal: T↑ R↑; semiconductor: T↑ R↓",
     "j = σE, σ = 1/ρ"
    ]
   },
   {
    "h": "Cells ⭐",
    "items": [
     "V = ε − Ir (discharge)",
     "Series: ε add, r add",
     "Parallel (identical): ε same, r/n"
    ]
   },
   {
    "h": "Kirchhoff ⭐⭐",
    "items": [
     "KCL: ΣI = 0 (charge)",
     "KVL: ΣV = 0 (energy)",
     "Galat direction = negative answer, OK!"
    ]
   },
   {
    "h": "Wheatstone ⭐",
    "items": [
     "Balance: P/Q = R/S",
     "Balanced: galvo current zero",
     "Meter bridge: S = R(100−l)/l"
    ]
   },
   {
    "h": "Power ⭐",
    "items": [
     "P = VI = I²R = V²/R",
     "1 kWh = 3.6×10⁶ J",
     "Max power: R = r"
    ]
   }
  ],
  "hi": [
   {
    "h": "धारा + अनुगमन ⭐",
    "items": [
     "I = Q/t, एंपियर",
     "I = neAv_d, अनुगमन ~mm/s",
     "j = I/A = nev_d"
    ]
   },
   {
    "h": "ओम + प्रतिरोध ⭐⭐",
    "items": [
     "V = IR; R = ρL/A",
     "धातु: T↑ R↑; अर्धचालक: T↑ R↓",
     "j = σE, σ = 1/ρ"
    ]
   },
   {
    "h": "सेल ⭐",
    "items": [
     "V = ε − Ir (निर्वहन)",
     "श्रेणी: ε योग, r योग",
     "समांतर (समान): ε समान, r/n"
    ]
   },
   {
    "h": "किरचॉफ ⭐⭐",
    "items": [
     "KCL: ΣI = 0 (आवेश)",
     "KVL: ΣV = 0 (ऊर्जा)",
     "गलत दिशा = ऋणात्मक उत्तर, ठीक!"
    ]
   },
   {
    "h": "व्हीटस्टोन ⭐",
    "items": [
     "संतुलन: P/Q = R/S",
     "संतुलित: धारामापी शून्य",
     "मीटर सेतु: S = R(100−l)/l"
    ]
   },
   {
    "h": "शक्ति ⭐",
    "items": [
     "P = VI = I²R = V²/R",
     "1 kWh = 3.6×10⁶ J",
     "अधिकतम शक्ति: R = r"
    ]
   }
  ],
  "en": [
   {
    "h": "Current + Drift ⭐",
    "items": [
     "I = Q/t, ampere",
     "I = neAv_d, drift ~mm/s",
     "j = I/A = nev_d"
    ]
   },
   {
    "h": "Ohm + Resistance ⭐⭐",
    "items": [
     "V = IR; R = ρL/A",
     "Metal: T↑ R↑; semiconductor: T↑ R↓",
     "j = σE, σ = 1/ρ"
    ]
   },
   {
    "h": "Cells ⭐",
    "items": [
     "V = ε − Ir (discharge)",
     "Series: ε adds, r adds",
     "Parallel (identical): ε same, r/n"
    ]
   },
   {
    "h": "Kirchhoff ⭐⭐",
    "items": [
     "KCL: ΣI = 0 (charge)",
     "KVL: ΣV = 0 (energy)",
     "Wrong direction = negative answer, fine!"
    ]
   },
   {
    "h": "Wheatstone ⭐",
    "items": [
     "Balance: P/Q = R/S",
     "Balanced: zero galvanometer current",
     "Meter bridge: S = R(100−l)/l"
    ]
   },
   {
    "h": "Power ⭐",
    "items": [
     "P = VI = I²R = V²/R",
     "1 kWh = 3.6×10⁶ J",
     "Max power: R = r"
    ]
   }
  ]
 },
 "practice": [
  [
   "Wire me 10 s me 20 C charge flow hua. Current?",
   "I = Q/t = 20/10 = <b>2 A</b>."
  ],
  [
   "Wire ka length double aur area half kar diya. Naya resistance?",
   "R = ρL/A → L double (×2), A half (×2) → R = <b>4 guna</b>."
  ],
  [
   "Drift velocity ka formula aur uska order of magnitude?",
   "v_d = I/(neA); typical value <b>~10⁻⁴ m/s (mm/s ke order ka)</b> — bahut slow!"
  ],
  [
   "12 V battery, r = 1 Ω, external R = 5 Ω. Terminal voltage?",
   "I = 12/(5+1) = 2 A → V = ε − Ir = 12 − 2 = <b>10 V</b>."
  ],
  [
   "Do cells 1.5 V, r = 0.5 Ω each, series me. Equivalent EMF aur r?",
   "ε = 1.5 + 1.5 = <b>3 V</b>, r = 0.5 + 0.5 = <b>1 Ω</b>."
  ],
  [
   "Kirchhoff ke do rules aur unke physical basis?",
   "KCL: ΣI = 0 — <b>charge conservation</b>; KVL: ΣV = 0 — <b>energy conservation</b>."
  ],
  [
   "Wheatstone bridge me P = 10 Ω, Q = 20 Ω, R = 30 Ω. Balance ke liye S?",
   "P/Q = R/S → S = R × Q/P = 30 × 20/10 = <b>60 Ω</b>."
  ],
  [
   "Balanced bridge me middle resistor ka kya karein?",
   "<b>Kuch nahi</b> — usme zero current hai; hata do ya short karo, circuit same rahega."
  ],
  [
   "100 W bulb 220 V pe. Resistance aur 10 hours ki energy (kWh)?",
   "R = V²/P = 48400/100 = <b>484 Ω</b>; energy = 0.1 kW × 10 h = <b>1 kWh (1 unit)</b>."
  ],
  [
   "Metal aur semiconductor ka temperature coefficient me farak?",
   "Metal: T badhane pe R <b>badhta</b> hai (α positive); semiconductor: T badhane pe R <b>ghatta</b> hai (zyada free carriers)."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/physics/ch-4/",
  "title": "Moving Charges and Magnetism"
 }
}

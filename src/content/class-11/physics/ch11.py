# Class 11 Physics, Chapter 11 - Thermodynamics
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 11,
 "title_en": "Thermodynamics",
 "title_hi": "ऊष्मागतिकी",
 "tagline": "Heat, work aur engines — energy ke flow ke rules",
 "jee": "HIGH",
 "meta_desc": "Class 11 Physics Chapter 11: Thermodynamics — long + short notes in Hindi, English, Hinglish. First law, second law, Carnot engine, isothermal, adiabatic processes, Cp-Cv.",
 "video": {
  "youtube": "6WqhlzygthU",
  "dur": "1 min 16 sec"
 },
 "card_tag": "Heat, work aur engines — energy ke flow ke rules",
 "card_topics": [
  "🔥 Zeroth + first law",
  "⚙️ Isothermal vs adiabatic",
  "🚂 Carnot engine + efficiency",
  "❄️ Refrigerator + COP"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Basics — System, Surroundings aur Zeroth Law",
    "body": "<ul>\n<li><b>System:</b> jo hum study kar rahe hain (gas in cylinder); <b>surroundings:</b> baaki sab. Boundary dono ko separate karti hai.</li>\n<li><b>State variables:</b> P, V, T (aur internal energy U) — system ki \"photo\" kheenchte hain. <b>Equation of state:</b> inka relation (ideal gas: PV = μRT).</li>\n<li><b>Zeroth law ⭐:</b> agar A aur B dono C ke saath thermal equilibrium me hain, to A aur B bhi aapas me equilibrium me — yahi TEMPERATURE ko define karta hai (thermometer isi pe chalta hai!).</li>\n<li><b>Internal energy (U):</b> system ke molecules ki total KE + PE — sirf state pe depend karti hai (<b>state function</b>), path pe nahi!</li>\n<li><b>Heat (Q) aur Work (W):</b> dono energy transfer ke TAREEKE hain — state functions nahi! Same initial-final states, alag path → alag Q aur W (lekin Q − W same, aage dekho).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: U = bank balance (state), Q aur W = deposit/withdrawal ke modes (path). Balance same ho sakta hai, transaction history alag!</p>"
   },
   {
    "h": "2️⃣ First Law of Thermodynamics — Energy Ka Hisaab ⭐",
    "body": "<p><b>ΔU = Q − W</b> — system ko di gayi heat, minus system dwara kiya gaya work = internal energy ka change. (Yehi energy conservation hai thermodynamics me!)</p>\n<ul>\n<li><b>Sign convention ⭐:</b> Q positive jab heat SYSTEM me aaye; W positive jab SYSTEM work kare (gas expand ho). Isme W = ∫P dV.</li>\n<li><b>Isothermal (T constant):</b> ΔU = 0 (ideal gas!) → Q = W. Slow process, piston pe rakh diya heat reservoir.</li>\n<li><b>Adiabatic (Q = 0):</b> ΔU = −W — gas expand kare to THANDI hoti hai (apni energy se work karti hai). Fast process ya insulated.</li>\n<li><b>Isochoric (V constant):</b> W = 0 → ΔU = Q. Sab heat internal energy me.</li>\n<li><b>Isobaric (P constant):</b> W = PΔV; Q = ΔU + PΔV.</li>\n<li><b>Cyclic process:</b> wapas same state → ΔU = 0 → Q_net = W_net (P-V diagram pe area!).</li>\n</ul>\n<p class=\"small-note\">🎯 First law = dukan ka ledger: jo aaya (Q) minus jo gaya (W) = stock change (ΔU).</p>"
   },
   {
    "h": "3️⃣ Specific Heats of Gas — C_p aur C_v ⭐",
    "body": "<ul>\n<li><b>C_v (constant volume):</b> poori heat internal energy me (W=0) → Q = μC_vΔT = ΔU.</li>\n<li><b>C_p (constant pressure):</b> heat = ΔU + work bhi → C_p &gt; C_v. ⭐</li>\n<li><b>Mayer's relation ⭐:</b> C_p − C_v = R (per mole, ideal gas).</li>\n<li><b>γ = C_p/C_v:</b> monatomic 5/3 ≈ 1.67, diatomic 7/5 = 1.4, polyatomic ~1.33.</li>\n<li><b>Adiabatic relations ⭐:</b> PV^γ = constant, TV^(γ−1) = constant, P^(1−γ)T^γ = constant. Adiabatic curve isothermal se STEEP hoti hai!</li>\n<li><b>Work in adiabatic:</b> W = (P₁V₁ − P₂V₂)/(γ − 1) = μR(T₁ − T₂)/(γ − 1).</li>\n</ul>\n<p class=\"small-note\">💡 C_p zyada kyun? Constant pressure me gas ko expand bhi hona padta hai — heat ka ek hissa work me chala jaata hai, isliye same ΔT ke liye zyada heat chahiye!</p>"
   },
   {
    "h": "4️⃣ Second Law — Heat Engines aur Carnot ⭐",
    "body": "<p>First law bolta hai energy conserve hoti hai — lekin DIRECTION nahi batata. Garam chai thandi kyun hoti hai, ulta kyun nahi? Jawab = <b>Second law</b>:</p>\n<ul>\n<li><b>Kelvin-Planck statement ⭐:</b> koi engine 100% heat ko work me nahi badal sakta — kuch heat sink me DENI hi padti hai.</li>\n<li><b>Clausius statement:</b> heat khud-ba-khud cold se hot nahi ja sakti (refrigerator ko work chahiye).</li>\n<li><b>Heat engine:</b> source (T₁) se Q₁ le, W work kare, sink (T₂) ko Q₂ de. <b>Efficiency ⭐:</b> η = W/Q₁ = 1 − Q₂/Q₁.</li>\n<li><b>Carnot engine ⭐:</b> ideal reversible engine — 2 isothermal + 2 adiabatic steps. <b>η_Carnot = 1 − T₂/T₁</b> (temperatures Kelvin me!). Isse zyada efficient engine possible NAHI same temperatures ke beech.</li>\n<li><b>Refrigerator/heat pump:</b> ulta cycle — work daalo, heat cold se hot me pump karo. <b>COP ⭐ = Q₂/W = T₂/(T₁ − T₂)</b> (1 se zyada hota hai!).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: second law = traffic police of energy — energy ka flow hot→cold hi naturally hota hai. Carnot = speed limit; koi bhi engine isse tez nahi!</p>"
   },
   {
    "h": "5️⃣ Processes Ka Comparison aur Quick Tricks",
    "body": "<table class=\"tbl\">\n<tr><th>Process</th><th>Constant</th><th>Q</th><th>W</th><th>ΔU</th></tr>\n<tr><td>Isothermal</td><td>T</td><td>= W</td><td>μRT ln(V₂/V₁)</td><td>0</td></tr>\n<tr><td>Adiabatic</td><td>Q=0</td><td>0</td><td>μRΔT/(1−γ)... −ΔU</td><td>μC_vΔT</td></tr>\n<tr><td>Isochoric</td><td>V</td><td>μC_vΔT</td><td>0</td><td>= Q</td></tr>\n<tr><td>Isobaric</td><td>P</td><td>μC_pΔT</td><td>PΔV</td><td>μC_vΔT</td></tr>\n</table>\n<ul>\n<li><b>P-V diagram pe area = work ⭐</b> — clockwise cycle = positive net work (engine), anticlockwise = negative (refrigerator).</li>\n<li><b>Free expansion:</b> vacuum me expand → W = 0, Q = 0 → ΔU = 0 (ideal gas ka T unchanged!). Lekin irreversible hai.</li>\n<li><b>Reversible process:</b> infinitely slow, quasi-static — har step equilibrium. Real processes irreversible (friction, fast changes).</li>\n<li>Trick: ΔU har process me μC_vΔT hi hai (ideal gas) — C_v sirf isochoric ke liye nahi! ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 Exam hack: pehle process pehchano (kya constant?), phir table se Q/W/ΔU nikalo. Carnot η me temperatures hamesha Kelvin!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ मूल बातें — निकाय, परिवेश और शून्यवां नियम",
    "body": "<ul>\n<li><b>निकाय (system):</b> जिसका अध्ययन कर रहे हैं; <b>परिवेश:</b> शेष सब।</li>\n<li><b>राज्य चर:</b> P, V, T (और आंतरिक ऊर्जा U)। <b>राज्य समीकरण:</b> आदर्श गैस के लिए PV = μRT।</li>\n<li><b>शून्यवां नियम ⭐:</b> यदि A और B दोनों C के साथ तापीय साम्य में हैं, तो A और B भी परस्पर साम्य में — यही <b>तापमान</b> को परिभाषित करता है।</li>\n<li><b>आंतरिक ऊर्जा (U):</b> अणुओं की कुल KE + PE — केवल अवस्था पर निर्भर (<b>अवस्था फलन</b>), पथ पर नहीं!</li>\n<li><b>ऊष्मा (Q) और कार्य (W):</b> ऊर्जा स्थानांतरण के तरीके — अवस्था फलन नहीं!</li>\n</ul>\n<p class=\"small-note\">💡 U = बैंक बैलेंस (अवस्था), Q और W = जमा/निकासी के तरीके (पथ)।</p>"
   },
   {
    "h": "2️⃣ ऊष्मागतिकी का प्रथम नियम — ऊर्जा का हिसाब ⭐",
    "body": "<p><b>ΔU = Q − W</b> — निकाय को दी गई ऊष्मा, ऋण निकाय द्वारा किया कार्य = आंतरिक ऊर्जा परिवर्तन।</p>\n<ul>\n<li><b>चिह्न परिपाटी ⭐:</b> Q धनात्मक जब ऊष्मा निकाय में आए; W धनात्मक जब निकाय कार्य करे। W = ∫P dV।</li>\n<li><b>समतापीय (T नियत):</b> ΔU = 0 → Q = W।</li>\n<li><b>रुद्धोष्म (Q = 0):</b> ΔU = −W — प्रसार पर गैस ठंडी होती है।</li>\n<li><b>समआयतनिक (V नियत):</b> W = 0 → ΔU = Q।</li>\n<li><b>समदाबीय (P नियत):</b> W = PΔV।</li>\n<li><b>चक्रीय प्रक्रम:</b> ΔU = 0 → Q_नेट = W_नेट (P-V आरेख का क्षेत्रफल!)।</li>\n</ul>\n<p class=\"small-note\">🎯 प्रथम नियम = दुकान का बही-खाता: आया (Q) ऋण गया (W) = स्टॉक परिवर्तन (ΔU)।</p>"
   },
   {
    "h": "3️⃣ गैस की विशिष्ट ऊष्माएं — C_p और C_v ⭐",
    "body": "<ul>\n<li><b>C_v (नियत आयतन):</b> सारी ऊष्मा आंतरिक ऊर्जा में → Q = μC_vΔT = ΔU।</li>\n<li><b>C_p (नियत दाब):</b> ऊष्मा = ΔU + कार्य भी → C_p &gt; C_v। ⭐</li>\n<li><b>मेयर संबंध ⭐:</b> C_p − C_v = R (प्रति मोल, आदर्श गैस)।</li>\n<li><b>γ = C_p/C_v:</b> एकपरमाणुक 5/3, द्विपरमाणुक 7/5 = 1.4।</li>\n<li><b>रुद्धोष्म संबंध ⭐:</b> PV^γ = नियतांक, TV^(γ−1) = नियतांक। रुद्धोष्म वक्र समतापीय से अधिक खड़ा!</li>\n<li><b>रुद्धोष्म में कार्य:</b> W = (P₁V₁ − P₂V₂)/(γ − 1)।</li>\n</ul>\n<p class=\"small-note\">💡 C_p अधिक क्यों? नियत दाब पर गैस को प्रसारित भी होना है — ऊष्मा का एक हिस्सा कार्य में चला जाता है!</p>"
   },
   {
    "h": "4️⃣ द्वितीय नियम — ऊष्मा इंजन और कार्नो ⭐",
    "body": "<ul>\n<li><b>केल्विन-प्लांक कथन ⭐:</b> कोई इंजन 100% ऊष्मा को कार्य में नहीं बदल सकता — कुछ ऊष्मा सिंक में देनी ही पड़ती है।</li>\n<li><b>क्लॉसियस कथन:</b> ऊष्मा स्वयं ठंडे से गर्म नहीं जा सकती।</li>\n<li><b>ऊष्मा इंजन:</b> स्रोत (T₁) से Q₁, W कार्य, सिंक (T₂) को Q₂। <b>दक्षता ⭐:</b> η = W/Q₁ = 1 − Q₂/Q₁।</li>\n<li><b>कार्नो इंजन ⭐:</b> आदर्श उत्क्रमणीय इंजन — 2 समतापीय + 2 रुद्धोष्म चरण। <b>η_कार्नो = 1 − T₂/T₁</b> (केल्विन में!)। इससे अधिक दक्ष इंजन संभव नहीं।</li>\n<li><b>रेफ्रिजरेटर:</b> उल्टा चक्र — कार्य डालो, ऊष्मा ठंडे से गर्म में पंप करो। <b>COP ⭐ = Q₂/W = T₂/(T₁ − T₂)</b>।</li>\n</ul>\n<p class=\"small-note\">💡 द्वितीय नियम = ऊर्जा की ट्रैफिक पुलिस — प्रवाह गर्म→ठंडा ही स्वाभाविक। कार्नो = स्पीड लिमिट!</p>"
   },
   {
    "h": "5️⃣ प्रक्रमों की तुलना और शीघ्र सूत्र",
    "body": "<table class=\"tbl\">\n<tr><th>प्रक्रम</th><th>नियत</th><th>Q</th><th>W</th><th>ΔU</th></tr>\n<tr><td>समतापीय</td><td>T</td><td>= W</td><td>μRT ln(V₂/V₁)</td><td>0</td></tr>\n<tr><td>रुद्धोष्म</td><td>Q=0</td><td>0</td><td>−ΔU</td><td>μC_vΔT</td></tr>\n<tr><td>समआयतनिक</td><td>V</td><td>μC_vΔT</td><td>0</td><td>= Q</td></tr>\n<tr><td>समदाबीय</td><td>P</td><td>μC_pΔT</td><td>PΔV</td><td>μC_vΔT</td></tr>\n</table>\n<ul>\n<li><b>P-V आरेख का क्षेत्रफल = कार्य ⭐</b> — दक्षिणावर्त चक्र = धनात्मक कार्य (इंजन)।</li>\n<li><b>मुक्त प्रसार:</b> निर्वात में → W = 0, Q = 0 → ΔU = 0 (पर अनुत्क्रमणीय)।</li>\n<li>ट्रिक: आदर्श गैस में ΔU हमेशा μC_vΔT — C_v केवल समआयतनिक के लिए नहीं! ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 पहले प्रक्रम पहचानो, फिर तालिका से Q/W/ΔU। कार्नो में तापमान हमेशा केल्विन!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Basics — System, Surroundings and the Zeroth Law",
    "body": "<ul>\n<li><b>System:</b> what we are studying (gas in a cylinder); <b>surroundings:</b> everything else. The boundary separates them.</li>\n<li><b>State variables:</b> P, V, T (and internal energy U) — they take a snapshot of the system. <b>Equation of state:</b> PV = μRT for an ideal gas.</li>\n<li><b>Zeroth law ⭐:</b> if A and B are each in thermal equilibrium with C, then A and B are in equilibrium with each other — this is what DEFINES temperature (and why thermometers work!).</li>\n<li><b>Internal energy (U):</b> the total KE + PE of the molecules — depends only on the state (<b>state function</b>), not the path!</li>\n<li><b>Heat (Q) and Work (W):</b> both are WAYS of transferring energy — not state functions! Same endpoints, different path → different Q and W (but Q − W stays the same).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: U = the bank balance (state), Q and W = the deposit/withdrawal modes (path). Same balance, different transaction history!</p>"
   },
   {
    "h": "2️⃣ First Law of Thermodynamics — Energy Accounting ⭐",
    "body": "<p><b>ΔU = Q − W</b> — heat given TO the system minus work done BY the system equals the change in internal energy. (This is energy conservation, thermodynamics style!)</p>\n<ul>\n<li><b>Sign convention ⭐:</b> Q positive when heat enters the system; W positive when the system does work (gas expands). W = ∫P dV.</li>\n<li><b>Isothermal (T constant):</b> ΔU = 0 (ideal gas!) → Q = W.</li>\n<li><b>Adiabatic (Q = 0):</b> ΔU = −W — an expanding gas COOLS (it works using its own energy).</li>\n<li><b>Isochoric (V constant):</b> W = 0 → ΔU = Q. All heat becomes internal energy.</li>\n<li><b>Isobaric (P constant):</b> W = PΔV; Q = ΔU + PΔV.</li>\n<li><b>Cyclic process:</b> back to the same state → ΔU = 0 → Q_net = W_net (the area on the P-V diagram!).</li>\n</ul>\n<p class=\"small-note\">🎯 The first law is a shop ledger: what came in (Q) minus what went out (W) equals the stock change (ΔU).</p>"
   },
   {
    "h": "3️⃣ Specific Heats of a Gas — C_p and C_v ⭐",
    "body": "<ul>\n<li><b>C_v (constant volume):</b> all heat goes into internal energy (W=0) → Q = μC_vΔT = ΔU.</li>\n<li><b>C_p (constant pressure):</b> heat covers ΔU AND expansion work → C_p &gt; C_v. ⭐</li>\n<li><b>Mayer's relation ⭐:</b> C_p − C_v = R (per mole, ideal gas).</li>\n<li><b>γ = C_p/C_v:</b> monatomic 5/3 ≈ 1.67, diatomic 7/5 = 1.4.</li>\n<li><b>Adiabatic relations ⭐:</b> PV^γ = constant, TV^(γ−1) = constant. The adiabatic curve is STEEPER than the isothermal!</li>\n<li><b>Work in adiabatic:</b> W = (P₁V₁ − P₂V₂)/(γ − 1) = μR(T₁ − T₂)/(γ − 1).</li>\n</ul>\n<p class=\"small-note\">💡 Why is C_p bigger? At constant pressure the gas must also expand — part of the heat escapes as work, so more heat is needed for the same ΔT!</p>"
   },
   {
    "h": "4️⃣ The Second Law — Heat Engines and Carnot ⭐",
    "body": "<p>The first law says energy is conserved — but not which WAY it flows. Why does hot tea cool down and never the reverse? The answer is the <b>second law</b>:</p>\n<ul>\n<li><b>Kelvin-Planck statement ⭐:</b> no engine can convert 100% of heat into work — some heat MUST be dumped into a sink.</li>\n<li><b>Clausius statement:</b> heat cannot flow by itself from cold to hot (a refrigerator needs work).</li>\n<li><b>Heat engine:</b> takes Q₁ from a source (T₁), does work W, dumps Q₂ into a sink (T₂). <b>Efficiency ⭐:</b> η = W/Q₁ = 1 − Q₂/Q₁.</li>\n<li><b>Carnot engine ⭐:</b> the ideal reversible engine — 2 isothermal + 2 adiabatic steps. <b>η_Carnot = 1 − T₂/T₁</b> (temperatures in kelvin!). No engine between the same two temperatures can beat it.</li>\n<li><b>Refrigerator/heat pump:</b> the reverse cycle — put in work, pump heat from cold to hot. <b>COP ⭐ = Q₂/W = T₂/(T₁ − T₂)</b> (can exceed 1!).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: the second law is the traffic police of energy — the natural flow is hot→cold. Carnot is the speed limit; no engine goes faster!</p>"
   },
   {
    "h": "5️⃣ Comparing the Processes and Quick Tricks",
    "body": "<table class=\"tbl\">\n<tr><th>Process</th><th>Constant</th><th>Q</th><th>W</th><th>ΔU</th></tr>\n<tr><td>Isothermal</td><td>T</td><td>= W</td><td>μRT ln(V₂/V₁)</td><td>0</td></tr>\n<tr><td>Adiabatic</td><td>Q=0</td><td>0</td><td>−ΔU</td><td>μC_vΔT</td></tr>\n<tr><td>Isochoric</td><td>V</td><td>μC_vΔT</td><td>0</td><td>= Q</td></tr>\n<tr><td>Isobaric</td><td>P</td><td>μC_pΔT</td><td>PΔV</td><td>μC_vΔT</td></tr>\n</table>\n<ul>\n<li><b>Area on the P-V diagram = work ⭐</b> — clockwise cycle = positive net work (engine), anticlockwise = negative (refrigerator).</li>\n<li><b>Free expansion:</b> expanding into a vacuum → W = 0, Q = 0 → ΔU = 0 (ideal gas temperature unchanged!). But it is irreversible.</li>\n<li>Trick: for an ideal gas, ΔU = μC_vΔT in EVERY process — C_v is not just for isochoric! ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 Exam hack: first identify the process (what is constant?), then read Q/W/ΔU off the table. Carnot temperatures are always in kelvin!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics ⭐",
    "items": [
     "Zeroth law → temperature define",
     "U = state function; Q, W = path functions",
     "Ideal gas: PV = μRT"
    ]
   },
   {
    "h": "First Law ⭐",
    "items": [
     "ΔU = Q − W",
     "Q +ve: heat in, W +ve: gas expands",
     "Cyclic: ΔU=0, Q=W=area"
    ]
   },
   {
    "h": "C_p, C_v ⭐",
    "items": [
     "C_p − C_v = R (Mayer)",
     "γ = C_p/C_v: mono 1.67, di 1.4",
     "Adiabatic: PV^γ = const"
    ]
   },
   {
    "h": "Second Law ⭐",
    "items": [
     "100% conversion impossible",
     "η = 1 − Q₂/Q₁",
     "Carnot: η = 1 − T₂/T₁ (max)"
    ]
   },
   {
    "h": "Processes",
    "items": [
     "Isothermal: ΔU=0, Q=W",
     "Adiabatic: Q=0, gas cools on expansion",
     "Isochoric: W=0; Isobaric: W=PΔV"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल ⭐",
    "items": [
     "शून्यवां नियम → तापमान",
     "U अवस्था फलन; Q, W पथ फलन",
     "PV = μRT"
    ]
   },
   {
    "h": "प्रथम नियम ⭐",
    "items": [
     "ΔU = Q − W",
     "Q +ve: ऊष्मा अंदर, W +ve: प्रसार",
     "चक्रीय: Q=W=क्षेत्रफल"
    ]
   },
   {
    "h": "C_p, C_v ⭐",
    "items": [
     "C_p − C_v = R",
     "γ: एकपरमाणुक 1.67, द्वि 1.4",
     "रुद्धोष्म: PV^γ = नियत"
    ]
   },
   {
    "h": "द्वितीय नियम ⭐",
    "items": [
     "100% रूपांतरण असंभव",
     "η = 1 − Q₂/Q₁",
     "कार्नो: η = 1 − T₂/T₁"
    ]
   },
   {
    "h": "प्रक्रम",
    "items": [
     "समतापीय: ΔU=0, Q=W",
     "रुद्धोष्म: प्रसार पर ठंडी",
     "समदाबीय: W=PΔV"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics ⭐",
    "items": [
     "Zeroth law → defines temperature",
     "U = state function; Q, W = path functions",
     "Ideal gas: PV = μRT"
    ]
   },
   {
    "h": "First Law ⭐",
    "items": [
     "ΔU = Q − W",
     "Q +ve: heat in, W +ve: gas expands",
     "Cyclic: ΔU=0, Q=W=area"
    ]
   },
   {
    "h": "C_p, C_v ⭐",
    "items": [
     "C_p − C_v = R (Mayer)",
     "γ = C_p/C_v: mono 1.67, di 1.4",
     "Adiabatic: PV^γ = const"
    ]
   },
   {
    "h": "Second Law ⭐",
    "items": [
     "100% conversion impossible",
     "η = 1 − Q₂/Q₁",
     "Carnot: η = 1 − T₂/T₁ (max)"
    ]
   },
   {
    "h": "Processes",
    "items": [
     "Isothermal: ΔU=0, Q=W",
     "Adiabatic: Q=0, gas cools on expansion",
     "Isochoric: W=0; Isobaric: W=PΔV"
    ]
   }
  ]
 },
 "practice": [
  [
   "Gas ko 500 J heat di, usne 200 J work kiya. ΔU?",
   "ΔU = Q − W = 500 − 200 = <b>300 J</b>."
  ],
  [
   "Isothermal expansion me ideal gas 400 J work karti hai. Kitni heat li?",
   "Isothermal me ΔU = 0 → Q = W = <b>400 J</b>."
  ],
  [
   "Adiabatic expansion me gas thandi kyun hoti hai?",
   "Q = 0, to work ki energy <b>internal energy se</b> aati hai (ΔU = −W) — T girta hai."
  ],
  [
   "Mayer's relation kya hai?",
   "C_p − C_v = <b>R</b> (8.314 J/mol·K) — constant pressure me expansion work bhi karna padta hai."
  ],
  [
   "Diatomic gas ka γ kitna hota hai?",
   "γ = C_p/C_v = 7/5 = <b>1.4</b> (monatomic 5/3 ≈ 1.67)."
  ],
  [
   "Carnot engine 600 K source aur 300 K sink ke beech. Efficiency?",
   "η = 1 − T₂/T₁ = 1 − 300/600 = <b>50%</b>."
  ],
  [
   "Engine 1000 J heat le kar 300 J work karta hai. Sink me kitna gaya?",
   "Q₂ = Q₁ − W = 1000 − 300 = <b>700 J</b> (η = 30%)."
  ],
  [
   "Koi bolta hai usne 100% efficient engine banaya. Possible?",
   "<b>Nahi</b> — Kelvin-Planck statement: kuch heat sink me deni hi padti hai."
  ],
  [
   "Refrigerator ka COP 4 hai, 200 J work lagaya. Freeze se kitni heat nikali?",
   "COP = Q₂/W → Q₂ = 4×200 = <b>800 J</b>."
  ],
  [
   "Cyclic process me net ΔU kitna hota hai?",
   "<b>Zero</b> — wapas same state pe aate hain, U state function hai. Isliye Q_net = W_net = P-V loop ka area."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/physics/ch-12/",
  "title": "Kinetic Theory"
 }
}

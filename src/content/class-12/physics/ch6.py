# Class 12 Physics, Chapter 6 - Electromagnetic Induction
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 6,
 "title_en": "Electromagnetic Induction",
 "title_hi": "विद्युतचुंबकीय प्रेरण",
 "tagline": "Magnet se bijli — Faraday, Lenz, inductance aur generator",
 "jee": "HIGH",
 "meta_desc": "Class 12 Physics Chapter 6: Electromagnetic Induction — long + short notes in Hindi, English, Hinglish. Faraday's law, Lenz's law, motional EMF, inductance, AC generator.",
 "video": None,
 "card_tag": "Magnet se bijli — Faraday, Lenz, inductance aur generator",
 "card_topics": [
  "🌀 Flux + Faraday's law",
  "✋ Lenz's law",
  "🎢 Motional EMF ε = Blv",
  "⚙️ Inductance + AC generator"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Magnetic Flux aur Induction Ka Discovery",
    "body": "<ul>\n<li><b>Magnetic flux ⭐:</b> surface se guzarti magnetic field lines ki measure — <b>Φ_B = B·A = BA cos θ</b>. Unit: weber (Wb). (Electric flux jaisa hi concept!)</li>\n<li><b>Faraday ka experiment:</b> magnet ko coil ke paas move karo → galvanometer deflect! Magnet ruka → koi current nahi. <b>Sirf CHANGE se current banta hai.</b></li>\n<li><b>Teen tareeke flux change karne ke:</b> (1) B change karo; (2) area change karo; (3) angle θ change karo (coil ghumao). Koi bhi ek chalega!</li>\n<li><b>Induced EMF/current tabhi</b> jab coil ka flux change ho — static field me kitna bhi strong B ho, kuch nahi hota.</li>\n<li><b>Henry ka contribution:</b> USA me independently same discovery — inductance ka unit 'henry' unke naam pe.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: flux = field ka 'flow' coil se. Jab tak wo flow badal nahi raha, coil ko koi farak nahi — change hi sab kuch hai!</p>"
   },
   {
    "h": "2️⃣ Faraday's Law aur Lenz's Law ⭐⭐",
    "body": "<ul>\n<li><b>Faraday's law ⭐⭐:</b> induced EMF = flux change ka rate — <b>ε = −dΦ/dt</b>. N turns ke liye <b>ε = −N dΦ/dt</b>. Jitna tez flux change, utna bada EMF!</li>\n<li><b>Lenz's law ⭐⭐:</b> induced current ki direction aisi hoti hai ki wo us CHANGE ka OPPOSE kare jo use paida kar raha hai. (Minus sign ka matlab yehi hai!)</li>\n<li><b>Magnet approaching:</b> coil ka face us pole jaisa ban jaata hai jo aa raha hai (N aata hai → coil ka face N → repel = oppose!). Receding: opposite pole → attract.</li>\n<li><b>Lenz = energy conservation ⭐:</b> agar current change ko SUPPORT karta, to free energy ban jaati — impossible! Magnet move karne me tumhe work karna padta hai, wahi energy current banti hai.</li>\n<li><b>Induced current:</b> I = ε/R = (N/R)|dΦ/dt|; <b>induced charge (magnitude):</b> q = N|ΔΦ|/R (rate pe depend nahi, sirf total change pe!).</li>\n</ul>\n<p class=\"small-note\">🎯 Lenz's law trick: 'Whatever happens, coil says NO!' — flux badhe to oppose, ghate to support (original field ki taraf).</p>"
   },
   {
    "h": "3️⃣ Motional EMF — Rod Ka Slide ⭐⭐",
    "body": "<ul>\n<li><b>Motional EMF ⭐⭐:</b> conductor ko magnetic field me move karo → andar ke charges pe q(v × B) force → electrons ek end pe jama → <b>EMF ε = Blv</b> (rod length l, velocity v, field B — teeno mutually perpendicular).</li>\n<li><b>Direction:</b> Fleming's right-hand rule (Thumb = motion, Forefinger = Field, Middle = induced current). Left-hand force ke liye tha, right-hand INDUCED current ke liye!</li>\n<li><b>Force needed ⭐:</b> induced current field me force feel karta hai F = BIl = B²l²v/R — ye Lenz ka oppose hai! Constant velocity ke liye external force = yahi, power input = Fv = B²l²v²/R = electrical power. Energy conserved! ✓</li>\n<li><b>Rod ka rotation:</b> ek end pe hinge, ω se rotate → ε = ½Bωl².</li>\n<li><b>General case:</b> ε = (v × B)·l — vector form.</li>\n</ul>\n<p class=\"small-note\">💡 ε = Blv aur F = BIl milke F = B²l²v/R dete hain — railgun se train braking tak, yahi physics!</p>"
   },
   {
    "h": "4️⃣ Eddy Currents aur Self Inductance ⭐",
    "body": "<ul>\n<li><b>Eddy currents (extra application):</b> bulk metal me changing flux se bane circulating currents (bhawar jaisa). Heat banate hain — induction stove isi pe kaam karta hai! ⭐</li>\n<li><b>Disadvantages:</b> transformer cores me energy loss → laminated (thin sheets) cores use karte hain taaki eddy currents toot jaayein.</li>\n<li><b>Uses:</b> electromagnetic braking (trains), induction furnace, metal detectors, speedometers.</li>\n<li><b>Self-inductance (L) ⭐⭐:</b> coil ka apna current change → apne hi flux change → apne me EMF! <b>ε = −L dI/dt</b>. Unit: henry (H).</li>\n<li><b>Definition:</b> NΦ = LI → L = NΦ/I. Solenoid ka L = μ₀n²Al — geometry pe depend karta hai.</li>\n<li><b>Energy stored in inductor ⭐:</b> <b>U = ½LI²</b> — magnetic field me stored (capacitor ke ½CV² jaisa!). Energy density u = B²/(2μ₀).</li>\n<li><b>Inductor ka behavior:</b> current ke SUDDEN change ko oppose karta hai — circuit on/off pe spark isi wajah se! DC steady state me inductor = plain wire.</li>\n</ul>\n<p class=\"small-note\">💡 Inductor = current ka inertia. Jaise heavy cheez ko rokna/chalana mushkil, waise inductor current ko achanak badalne nahi deta!</p>"
   },
   {
    "h": "5️⃣ Mutual Inductance aur AC Generator ⭐",
    "body": "<ul>\n<li><b>Mutual inductance (M) ⭐:</b> ek coil ka current change → doosri coil ka flux change → usme EMF! <b>ε₂ = −M dI₁/dt</b>. Transformers isi principle pe!</li>\n<li><b>M kya decide karta hai:</b> dono coils ki geometry, distance, orientation, turns. Solenoid-coil pair: M = μ₀n₁n₂Al.</li>\n<li><b>Coupling:</b> M² ≤ L₁L₂, coupling coefficient k = M/√(L₁L₂) (max 1 = perfect coupling).</li>\n<li><b>AC generator (next chapter, extra) ⭐:</b> coil ko magnetic field me rotate karo → flux linkage NΦ = NBA cos(ωt) continuously change → <b>ε = NBAω sin(ωt) = ε₀ sin ωt</b>. Peak EMF ε₀ = NBAω.</li>\n<li><b>Yehi India ka 50 Hz AC banata hai</b> — turbines (steam/water) coil ghumate hain!</li>\n<li><b>DC generator:</b> same + split-ring commutator jo current ki direction reverse kar deta hai har half-turn pe.</li>\n</ul>\n<p class=\"small-note\">🎯 Generator = mechanical energy → electrical; motor = ulta. ε₀ = NBAω — B badhao, area badhao, ya tez ghumao, EMF badhega!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ चुंबकीय फ्लक्स और प्रेरण की खोज",
    "body": "<ul>\n<li><b>चुंबकीय फ्लक्स ⭐:</b> पृष्ठ से गुजरती चुंबकीय क्षेत्र रेखाओं की माप — <b>Φ_B = BA cos θ</b>। मात्रक: वेबर (Wb)।</li>\n<li><b>फैराडे का प्रयोग:</b> चुंबक को कुंडली के पास गतिमान करो → धारामापी विक्षेपित! चुंबक रुका → कोई धारा नहीं। <b>केवल परिवर्तन से धारा बनती है।</b></li>\n<li><b>फ्लक्स बदलने के तीन तरीके:</b> (1) B बदलो; (2) क्षेत्रफल बदलो; (3) कोण θ बदलो।</li>\n<li><b>प्रेरित EMF तभी</b> जब कुंडली का फ्लक्स बदले — स्थिर क्षेत्र में कुछ नहीं होता।</li>\n</ul>\n<p class=\"small-note\">💡 फ्लक्स = कुंडली से क्षेत्र का 'प्रवाह'। जब तक प्रवाह नहीं बदलता, कुछ नहीं होता — परिवर्तन ही सब कुछ है!</p>"
   },
   {
    "h": "2️⃣ फैराडे का नियम और लेंज़ का नियम ⭐⭐",
    "body": "<ul>\n<li><b>फैराडे का नियम ⭐⭐:</b> प्रेरित EMF = फ्लक्स परिवर्तन की दर — <b>ε = −dΦ/dt</b>। N फेरों के लिए <b>ε = −N dΦ/dt</b>।</li>\n<li><b>लेंज़ का नियम ⭐⭐:</b> प्रेरित धारा की दिशा ऐसी होती है कि वह उस <b>परिवर्तन का विरोध</b> करे जो उसे उत्पन्न कर रहा है।</li>\n<li><b>चुंबक निकट आए:</b> कुंडली का फलक उसी ध्रुव जैसा बन जाता है (प्रतिकर्षण = विरोध!)। दूर जाए: विपरीत ध्रुव (आकर्षण)।</li>\n<li><b>लेंज़ = ऊर्जा संरक्षण ⭐:</b> यदि धारा परिवर्तन का समर्थन करती, तो मुक्त ऊर्जा बन जाती — असंभव!</li>\n<li><b>प्रेरित धारा:</b> I = (N/R)|dΦ/dt|; <b>प्रेरित आवेश का परिमाण:</b> q = N|ΔΦ|/R।</li>\n</ul>\n<p class=\"small-note\">🎯 लेंज़ की युक्ति: 'जो भी हो, कुंडली कहती है NAHI!' — फ्लक्स बढ़े तो विरोध, घटे तो समर्थन।</p>"
   },
   {
    "h": "3️⃣ गतिक EMF — छड़ का सरकना ⭐⭐",
    "body": "<ul>\n<li><b>गतिक EMF ⭐⭐:</b> चालक को क्षेत्र में गतिमान करो → आवेशों पर q(v × B) बल → <b>EMF ε = Blv</b> (l, v, B परस्पर लंबवत)।</li>\n<li><b>दिशा:</b> फ्लेमिंग का दायां हाथ नियम (अंगूठा = गति, तर्जनी = क्षेत्र, मध्यमा = प्रेरित धारा)।</li>\n<li><b>आवश्यक बल ⭐:</b> प्रेरित धारा क्षेत्र में बल अनुभव करती है F = B²l²v/R — यही लेंज़ का विरोध है! बाह्य शक्ति = Fv = B²l²v²/R = विद्युत शक्ति। ऊर्जा संरक्षित! ✓</li>\n<li><b>छड़ का घूर्णन:</b> ε = ½Bωl²।</li>\n</ul>\n<p class=\"small-note\">💡 ε = Blv और F = BIl मिलकर F = B²l²v/R — रेलगन से ट्रेन ब्रेकिंग तक, यही भौतिकी!</p>"
   },
   {
    "h": "4️⃣ भंवर धाराएं और स्व-प्रेरकत्व ⭐",
    "body": "<ul>\n<li><b>भंवर धाराएं (अतिरिक्त अनुप्रयोग):</b> थोक धातु में बदलते फ्लक्स से बनी परिसंचारी धाराएं। ऊष्मा बनाती हैं — इंडक्शन स्टोव इसी पर! ⭐</li>\n<li><b>नुकसान:</b> ट्रांसफॉर्मर क्रोड में ऊर्जा क्षति → पटलित (laminated) क्रोड उपयोग।</li>\n<li><b>उपयोग:</b> विद्युतचुंबकीय ब्रेकिंग, इंडक्शन भट्टी, धातु संसूचक।</li>\n<li><b>स्व-प्रेरकत्व (L) ⭐⭐:</b> कुंडली का अपना धारा परिवर्तन → अपने में EMF! <b>ε = −L dI/dt</b>। मात्रक: हेनरी (H)।</li>\n<li><b>परिभाषा:</b> NΦ = LI। परिनालिका का L = μ₀n²Al।</li>\n<li><b>प्रेरक में संचित ऊर्जा ⭐:</b> <b>U = ½LI²</b> — चुंबकीय क्षेत्र में। ऊर्जा घनत्व u = B²/(2μ₀)।</li>\n<li><b>प्रेरक का व्यवहार:</b> धारा के अचानक परिवर्तन का विरोध — DC स्थायी अवस्था में प्रेरक = साधारण तार।</li>\n</ul>\n<p class=\"small-note\">💡 प्रेरक = धारा का जड़त्व। प्रेरक धारा को अचानक बदलने नहीं देता!</p>"
   },
   {
    "h": "5️⃣ अन्योन्य प्रेरकत्व और AC जनरेटर ⭐",
    "body": "<ul>\n<li><b>अन्योन्य प्रेरकत्व (M) ⭐:</b> एक कुंडली का धारा परिवर्तन → दूसरी में EMF! <b>ε₂ = −M dI₁/dt</b>। ट्रांसफॉर्मर इसी पर!</li>\n<li><b>M निर्भर:</b> दोनों कुंडलियों की ज्यामिति, दूरी, अभिविन्यास, फेरों पर।</li>\n<li><b>युग्मन:</b> M² ≤ L₁L₂, k = M/√(L₁L₂)।</li>\n<li><b>AC जनरेटर (अगला अध्याय, अतिरिक्त) ⭐:</b> कुंडली को क्षेत्र में घुमाओ → कुल फ्लक्स संबद्धता NΦ = NBA cos(ωt) → <b>ε = NBAω sin(ωt) = ε₀ sin ωt</b>। शिखर EMF ε₀ = NBAω।</li>\n<li><b>यही भारत का 50 Hz AC बनाता है</b> — टरबाइन कुंडली घुमाते हैं!</li>\n<li><b>DC जनरेटर:</b> समान + दिक्परिवर्तक (split-ring commutator)।</li>\n</ul>\n<p class=\"small-note\">🎯 जनरेटर = यांत्रिक ऊर्जा → विद्युत; मोटर = विपरीत। ε₀ = NBAω!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Magnetic Flux and the Discovery of Induction",
    "body": "<ul>\n<li><b>Magnetic flux ⭐:</b> the measure of magnetic field lines passing through a surface — <b>Φ_B = B·A = BA cos θ</b>. Unit: weber (Wb). (Same idea as electric flux!)</li>\n<li><b>Faraday's experiment:</b> move a magnet near a coil → the galvanometer deflects! Stop the magnet → no current. <b>Only CHANGE creates current.</b></li>\n<li><b>Three ways to change flux:</b> (1) change B; (2) change the area; (3) change the angle θ (rotate the coil). Any one works!</li>\n<li><b>Induced EMF/current only when</b> the coil's flux changes — in a static field, however strong, nothing happens.</li>\n<li><b>Henry's contribution:</b> discovered the same effect independently in the USA — the unit of inductance, the henry, is named after him.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: flux is the field's 'flow' through the coil. Until that flow changes, the coil does not care — change is everything!</p>"
   },
   {
    "h": "2️⃣ Faraday's Law and Lenz's Law ⭐⭐",
    "body": "<ul>\n<li><b>Faraday's law ⭐⭐:</b> induced EMF = rate of change of flux — <b>ε = −dΦ/dt</b>. For N turns, <b>ε = −N dΦ/dt</b>. The faster the flux changes, the bigger the EMF!</li>\n<li><b>Lenz's law ⭐⭐:</b> the induced current flows in the direction that OPPOSES the change producing it. (That is what the minus sign means!)</li>\n<li><b>Magnet approaching:</b> the coil's face becomes the same pole as the approaching one (N coming → face becomes N → repel = oppose!). Receding: opposite pole → attract.</li>\n<li><b>Lenz = energy conservation ⭐:</b> if the current SUPPORTED the change, energy would appear from nowhere — impossible! You must do work to move the magnet; that work becomes the current's energy.</li>\n<li><b>Induced current:</b> I = ε/R = (N/R)|dΦ/dt|; <b>induced charge (magnitude):</b> q = N|ΔΦ|/R (depends on the total change, not the rate!).</li>\n</ul>\n<p class=\"small-note\">🎯 Lenz's law trick: 'Whatever happens, the coil says NO!' — flux rising, it opposes; flux falling, it supports the original field.</p>"
   },
   {
    "h": "3️⃣ Motional EMF — The Sliding Rod ⭐⭐",
    "body": "<ul>\n<li><b>Motional EMF ⭐⭐:</b> move a conductor through a magnetic field → charges inside feel q(v × B) → electrons pile up at one end → <b>EMF ε = Blv</b> (rod length l, velocity v, field B — all three mutually perpendicular).</li>\n<li><b>Direction:</b> Fleming's right-hand rule (Thumb = motion, Forefinger = Field, Middle = induced current). Left hand was for force, right hand for INDUCED current!</li>\n<li><b>Force needed ⭐:</b> the induced current feels a force F = BIl = B²l²v/R in the field — this is Lenz's opposition! To keep constant velocity you supply exactly this force; input power = Fv = B²l²v²/R = electrical power. Energy conserved! ✓</li>\n<li><b>Rotating rod:</b> hinged at one end, spinning at ω → ε = ½Bωl².</li>\n<li><b>General case:</b> ε = (v × B)·l — the vector form.</li>\n</ul>\n<p class=\"small-note\">💡 ε = Blv and F = BIl combine into F = B²l²v/R — from railguns to train braking, the same physics!</p>"
   },
   {
    "h": "4️⃣ Eddy Currents and Self-Inductance ⭐",
    "body": "<ul>\n<li><b>Eddy currents (extra application):</b> circulating currents induced in bulk metal by changing flux (like whirlpools). They produce heat — the induction stove works on exactly this! ⭐</li>\n<li><b>Disadvantages:</b> energy loss in transformer cores → use laminated (thin-sheet) cores to break the eddy currents.</li>\n<li><b>Uses:</b> electromagnetic braking (trains), induction furnaces, metal detectors, speedometers.</li>\n<li><b>Self-inductance (L) ⭐⭐:</b> a coil's own changing current changes its own flux → EMF in itself! <b>ε = −L dI/dt</b>. Unit: henry (H).</li>\n<li><b>Definition:</b> NΦ = LI → L = NΦ/I. For a solenoid, L = μ₀n²Al — depends on geometry.</li>\n<li><b>Energy stored in an inductor ⭐:</b> <b>U = ½LI²</b> — stored in the magnetic field (like the capacitor's ½CV²!). Energy density u = B²/(2μ₀).</li>\n<li><b>Inductor behaviour:</b> opposes SUDDEN changes of current — the spark when you switch off a circuit comes from this! In DC steady state an inductor is just a wire.</li>\n</ul>\n<p class=\"small-note\">💡 An inductor is current's inertia. Just as a heavy body resists being started or stopped, an inductor resists sudden current changes!</p>"
   },
   {
    "h": "5️⃣ Mutual Inductance and the AC Generator ⭐",
    "body": "<ul>\n<li><b>Mutual inductance (M) ⭐:</b> one coil's changing current changes the other coil's flux → EMF in the second! <b>ε₂ = −M dI₁/dt</b>. Transformers work on exactly this!</li>\n<li><b>What decides M:</b> the geometry, distance, orientation and turns of both coils. Solenoid-coil pair: M = μ₀n₁n₂Al.</li>\n<li><b>Coupling:</b> M² ≤ L₁L₂, coupling coefficient k = M/√(L₁L₂) (max 1 = perfect coupling).</li>\n<li><b>AC generator (next chapter, extra) ⭐:</b> rotate a coil in a magnetic field → flux linkage NΦ = NBA cos(ωt) keeps changing → <b>ε = NBAω sin(ωt) = ε₀ sin ωt</b>. Peak EMF ε₀ = NBAω.</li>\n<li><b>This principle generates grid AC in India (50 Hz)</b> — turbines (steam/water) spin the coil!</li>\n<li><b>DC generator:</b> same, plus a split-ring commutator that reverses connections every half-turn.</li>\n</ul>\n<p class=\"small-note\">🎯 Generator = mechanical energy → electrical; motor = the reverse. ε₀ = NBAω — raise B, area or spin speed and EMF rises!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Flux + Faraday ⭐⭐",
    "items": [
     "Φ = BA cosθ, weber",
     "ε = −N dΦ/dt",
     "Change hi EMF banata hai"
    ]
   },
   {
    "h": "Lenz ⭐⭐",
    "items": [
     "Induced current change ko oppose",
     "Approaching N → face N ban jao",
     "= energy conservation"
    ]
   },
   {
    "h": "Motional EMF ⭐⭐",
    "items": [
     "ε = Blv (3 perpendicular)",
     "F = B²l²v/R",
     "Right-hand rule for current"
    ]
   },
   {
    "h": "Inductance ⭐",
    "items": [
     "Self: ε = −L dI/dt",
     "U = ½LI², u = B²/2μ₀",
     "Mutual: ε₂ = −M dI₁/dt"
    ]
   },
   {
    "h": "AC Generator ⭐",
    "items": [
     "ε = NBAω sin ωt",
     "ε₀ = NBAω",
     "50 Hz = India ka AC"
    ]
   }
  ],
  "hi": [
   {
    "h": "फ्लक्स + फैराडे ⭐⭐",
    "items": [
     "Φ = BA cosθ, वेबर",
     "ε = −N dΦ/dt",
     "परिवर्तन ही EMF बनाता है"
    ]
   },
   {
    "h": "लेंज़ ⭐⭐",
    "items": [
     "प्रेरित धारा परिवर्तन का विरोध",
     "निकट N → फलक N बन जाओ",
     "= ऊर्जा संरक्षण"
    ]
   },
   {
    "h": "गतिक EMF ⭐⭐",
    "items": [
     "ε = Blv (3 लंबवत)",
     "F = B²l²v/R",
     "दायां हाथ नियम"
    ]
   },
   {
    "h": "प्रेरकत्व ⭐",
    "items": [
     "स्व: ε = −L dI/dt",
     "U = ½LI², u = B²/2μ₀",
     "अन्योन्य: ε₂ = −M dI₁/dt"
    ]
   },
   {
    "h": "AC जनरेटर ⭐",
    "items": [
     "ε = NBAω sin ωt",
     "ε₀ = NBAω",
     "50 Hz = भारत का AC"
    ]
   }
  ],
  "en": [
   {
    "h": "Flux + Faraday ⭐⭐",
    "items": [
     "Φ = BA cosθ, weber",
     "ε = −N dΦ/dt",
     "Only change creates EMF"
    ]
   },
   {
    "h": "Lenz ⭐⭐",
    "items": [
     "Induced current opposes the change",
     "Approaching N → face becomes N",
     "= energy conservation"
    ]
   },
   {
    "h": "Motional EMF ⭐⭐",
    "items": [
     "ε = Blv (3 perpendicular)",
     "F = B²l²v/R",
     "Right-hand rule for current"
    ]
   },
   {
    "h": "Inductance ⭐",
    "items": [
     "Self: ε = −L dI/dt",
     "U = ½LI², u = B²/2μ₀",
     "Mutual: ε₂ = −M dI₁/dt"
    ]
   },
   {
    "h": "AC Generator ⭐",
    "items": [
     "ε = NBAω sin ωt",
     "ε₀ = NBAω",
     "50 Hz = India's AC"
    ]
   }
  ]
 },
 "practice": [
  [
   "Coil (N = 100) ka flux 0.05 s me 0.1 Wb se 0.3 Wb ho gaya. Induced EMF?",
   "ε = N ΔΦ/Δt = 100 × 0.2/0.05 = <b>400 V</b>."
  ],
  [
   "Magnet ka N pole coil ki taraf aa raha hai. Induced current ki direction (magnet side se)?",
   "Face N banna chahiye (oppose!) → <b>anticlockwise</b> current (magnet wali side se dekhte hue)."
  ],
  [
   "Lenz's law kaunse conservation principle pe based hai?",
   "<b>Energy conservation</b> — warna current free energy generate karti!"
  ],
  [
   "Rod l = 0.5 m, B = 0.4 T, v = 10 m/s perpendicular. Motional EMF?",
   "ε = Blv = 0.4 × 0.5 × 10 = <b>2 V</b>."
  ],
  [
   "Us rod pe constant velocity ke liye kitna force? (R = 2 Ω)",
   "F = B²l²v/R = (0.16 × 0.25 × 10)/2 = <b>0.2 N</b>."
  ],
  [
   "Self-inductance L = 0.5 H coil me current 0.1 s me 2 A se 6 A. Induced EMF?",
   "ε = L dI/dt = 0.5 × 4/0.1 = <b>20 V</b>."
  ],
  [
   "Inductor (L = 2 H) me 3 A current. Stored energy?",
   "U = ½LI² = ½ × 2 × 9 = <b>9 J</b>."
  ],
  [
   "Induction stove (extra application) kaise kaam karta hai?",
   "Coil ka changing magnetic field pan ke metal base me <b>eddy currents</b> banata hai → resistance se heat → khana pakta hai. (Glass top pan ke contact se garam ho sakta hai!)"
  ],
  [
   "Mutual inductance kya hai aur kahan use hota hai?",
   "Ek coil ke current change se doosri coil me EMF — ε₂ = −M dI₁/dt. <b>Transformers</b> isi principle pe kaam karte hain."
  ],
  [
   "AC generator ka peak EMF formula aur India ki AC frequency?",
   "ε₀ = <b>NBAω</b>; India me <b>50 Hz</b> (coil second me 50 baar full cycle)."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/physics/ch-7/",
  "title": "Alternating Current"
 }
}

# Class 12 Physics, Chapter 4 - Moving Charges and Magnetism
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 4,
 "title_en": "Moving Charges and Magnetism",
 "title_hi": "गतिमान आवेश और चुंबकत्व",
 "tagline": "Current ka magnetic kamaal — Lorentz force, Biot-Savart, solenoid aur galvanometer",
 "jee": "HIGH",
 "meta_desc": "Class 12 Physics Chapter 4: Moving Charges and Magnetism — long + short notes in Hindi, English, Hinglish. Lorentz force, Biot-Savart, Ampere's law, solenoid, galvanometer.",
 "video": None,
 "card_tag": "Current ka magnetic kamaal — Lorentz force, Biot-Savart, solenoid aur galvanometer",
 "card_topics": [
  "🧲 Lorentz force + circular motion",
  "🔁 Biot-Savart + loop field",
  "🧵 Solenoid B = μ₀nI",
  "🧭 Galvanometer conversions"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Magnetic Field aur Lorentz Force ⭐",
    "body": "<ul>\n<li><b>Oersted ka discovery:</b> current-carrying wire ke paas compass needle deflect hoti hai — <b>current magnetic field banata hai!</b> Electricity aur magnetism connected.</li>\n<li><b>Magnetic field (B):</b> moving charges pe force lagane wala field. Unit: tesla (T); chhota unit gauss (1 T = 10⁴ G).</li>\n<li><b>Lorentz force ⭐⭐:</b> moving charge pe force <b>F = q(v × B)</b>, magnitude <b>F = |q|vB sin θ</b>. Direction: <b>right-hand / Fleming's left-hand rule</b> (negative charge ke liye ULTA!).</li>\n<li><b>Total electromagnetic force:</b> F = q(E + v × B) — electric + magnetic dono.</li>\n<li><b>Magnetic force ka kaam ⭐:</b> B pe motion perpendicular ho to force hamesha velocity ke perpendicular → <b>work done ZERO</b>, speed change nahi hoti, sirf direction! (Kinetic energy constant.)</li>\n<li><b>Static charge pe:</b> magnetic force ZERO (v = 0) — magnetic field sirf moving charges ko pakadta hai.</li>\n</ul>\n<p class=\"small-note\">💡 Magnetic force = traffic police jo sirf direction modta hai, speed kabhi nahi badhta. Isliye magnetic field se energy nahi mil sakti seedha!</p>"
   },
   {
    "h": "2️⃣ Magnetic Field Me Motion — Circle aur Helix ⭐",
    "body": "<ul>\n<li><b>v ⊥ B ⭐⭐:</b> charge <b>circle</b> me ghoomta hai — magnetic force centripetal ka kaam karta hai. Radius <b>r = mv/(|q|B)</b>, time period <b>T = 2πm/(|q|B)</b>.</li>\n<li><b>T velocity pe depend nahi karta!</b> Tez particle bada circle, slow chhota — same time me complete. (Cyclotron isi principle pe (extra context)!)</li>\n<li><b>v ∥ B:</b> koi force nahi (sin 0 = 0) — seedhi line me chalta rahe.</li>\n<li><b>Angle θ pe ⭐:</b> velocity ke 2 components — perpendicular circle banata hai, parallel seedha kheenchta hai → path = <b>helix</b> (spring jaisa). Pitch = v cos θ × T.</li>\n<li><b>Frequency:</b> f = |q|B/(2πm) — cyclotron frequency.</li>\n<li><b>Momentum se radius:</b> r = p/(|q|B) — momentum measurement ka tool (particle physics detectors!).</li>\n</ul>\n<p class=\"small-note\">🎯 r = mv/|q|B yaad rakho: zyada momentum = bada circle; zyada B ya zyada charge = tight circle.</p>"
   },
   {
    "h": "3️⃣ Biot-Savart Law aur Circular Loop Ka Field ⭐⭐",
    "body": "<ul>\n<li><b>Biot-Savart law ⭐:</b> chhote current element ka field <b>dB = (μ₀/4π) · I dl sin θ / r²</b>. μ₀/4π = 10⁻⁷ T·m/A. Direction: right-hand rule (dl × r̂).</li>\n<li><b>Circular loop ke center pe ⭐⭐:</b> <b>B = μ₀I/(2R)</b> — N turns ho to B = μ₀NI/(2R).</li>\n<li><b>Loop ke axis pe (distance x):</b> B = μ₀IR²/(2(R² + x²)^(3/2)) — center se door jaake girta hai.</li>\n<li><b>Arc (angle θ) ke center pe:</b> B = (μ₀I/2R) × (θ/2π) — semicircle = aadha, quarter = chautha.</li>\n<li><b>Direction:</b> current anticlockwise → field tumhari TARAF (out of page); clockwise → door (into page). Right-hand curl rule!</li>\n<li><b>Straight wire ka field (Biot-Savart se):</b> B = (μ₀I/4πd)(sin θ₁ + sin θ₂); infinite wire: B = μ₀I/(2πd).</li>\n</ul>\n<p class=\"small-note\">💡 Loop center ka formula μ₀I/2R sabse zyada use hota hai — combinations me har arc/loop ka B alag nikalo, phir vector add karo.</p>"
   },
   {
    "h": "4️⃣ Ampere's Law, Solenoid aur Toroid ⭐",
    "body": "<ul>\n<li><b>Ampere's circuital law ⭐:</b> closed loop pe <b>∮B·dl = μ₀I_enclosed</b> — Gauss's law ka magnetic version (symmetry wale problems ke liye).</li>\n<li><b>Infinite straight wire ⭐:</b> circular Amperian loop se <b>B = μ₀I/(2πr)</b> — distance ke saath 1/r se girta hai. Direction: right-hand thumb rule (thumb current, fingers B ke curl).</li>\n<li><b>Solenoid ⭐⭐:</b> andar field uniform <b>B = μ₀nI</b> (n = turns per unit length); bahar approximately zero. Lamba electromagnet!</li>\n<li><b>Toroid (extra; current theory outline se bahar):</b> gol solenoid — andar B = μ₀NI/(2πr), bahar aur center me zero.</li>\n<li><b>Solenoid ke andar field turns ki total count pe nahi, density pe depend karta hai</b> — same n to same B, chahe kitna bhi lamba.</li>\n</ul>\n<p class=\"small-note\">🎯 μ₀I/2πr (wire), μ₀nI (solenoid), μ₀NI/2R (loop center) — teen B-formulas 80% questions cover karte hain!</p>"
   },
   {
    "h": "5️⃣ Force on Conductor, Parallel Wires aur Torque on Loop ⭐⭐",
    "body": "<ul>\n<li><b>Current-carrying conductor pe force ⭐:</b> <b>F = IL × B</b>, magnitude F = BIL sin θ. Direction: Fleming's left-hand rule (Forefinger = Field, Middle = current, Thumb = motion/force).</li>\n<li><b>Do parallel wires ⭐⭐:</b> force per unit length <b>F/L = μ₀I₁I₂/(2πd)</b> — SAME direction currents <b>attract</b>, opposite <b>repel</b>. (Historical ampere definition isi relation pe based thi!)</li>\n<li><b>Ampere ki definition:</b> historically 1 A used 2 × 10⁻⁷ N/m between 1 m-separated parallel wires; modern SI fixes elementary charge.</li>\n<li><b>Current loop pe torque ⭐⭐:</b> <b>τ = NIAB sin θ; vector: τ = m × B</b> jahan m = NIA (magnetic dipole moment). θ = 90° pe max, θ = 0 pe zero.</li>\n<li><b>Loop = magnetic dipole:</b> current loop ek chhota bar magnet jaisa behave karta hai — m = NIA uska dipole moment.</li>\n<li><b>Potential energy:</b> U = −m·B = −mB cos θ (electric dipole jaisa hi!).</li>\n</ul>\n<p class=\"small-note\">💡 Same-direction currents attract — ulta lagta hai na? Electric charges me like repel karte hain, currents me like ATTRACT. Yaad rakho!</p>"
   },
   {
    "h": "6️⃣ Moving Coil Galvanometer ⭐",
    "body": "<ul>\n<li><b>Galvanometer:</b> chhota current detect/measure karne ka device — coil magnetic field me rakha hota hai, current se torque, spring se restoring torque. Balance: <b>nIAB = kφ</b> → deflection φ ∝ I.</li>\n<li><b>Radial field:</b> poles curved hote hain taaki plane hamesha field ke parallel rahe — τ = nIAB constant (θ = 90° hamesha), linear scale milta hai.</li>\n<li><b>Current sensitivity:</b> φ/I = nAB/k — kitna deflection per ampere.</li>\n<li><b>Ammeter banana ⭐⭐:</b> galvanometer ke parallel me CHHOTA shunt resistance S = I_g·G/(I − I_g) — zyada current bypass ho jaata hai. Ammeter ka resistance bahut LOW (series me lagta hai).</li>\n<li><b>Voltmeter banana ⭐⭐:</b> galvanometer ke series me BADA resistance R = V/I_g − G — voltmeter ka resistance bahut HIGH (parallel me lagta hai).</li>\n<li><b>Ideal ammeter R = 0, ideal voltmeter R = ∞</b> — real me jitne paas utna accha.</li>\n</ul>\n<p class=\"small-note\">🎯 Ammeter ke andar shunt parallel, poora ammeter circuit me series; voltmeter ke andar resistor series, poora voltmeter circuit me parallel. Numericals practice karo!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ चुंबकीय क्षेत्र और लॉरेंट्ज बल ⭐",
    "body": "<ul>\n<li><b>ओर्स्टेड की खोज:</b> धारावाही तार के पास कंपास सुई विक्षेपित होती है — <b>धारा चुंबकीय क्षेत्र बनाती है!</b></li>\n<li><b>चुंबकीय क्षेत्र (B):</b> गतिमान आवेशों पर बल लगाने वाला क्षेत्र। मात्रक: टेस्ला (T)।</li>\n<li><b>लॉरेंट्ज बल ⭐⭐:</b> <b>F = q(v × B)</b>, परिमाण <b>F = |q|vB sin θ</b>। दिशा: दाएं हाथ का नियम (ऋण आवेश के लिए विपरीत!)।</li>\n<li><b>कुल विद्युतचुंबकीय बल:</b> F = q(E + v × B)।</li>\n<li><b>चुंबकीय बल का कार्य ⭐:</b> बल सदैव वेग के लंबवत → <b>कार्य शून्य</b>, चाल अपरिवर्तित, केवल दिशा बदलती है!</li>\n<li><b>स्थिर आवेश पर:</b> चुंबकीय बल शून्य (v = 0)।</li>\n</ul>\n<p class=\"small-note\">💡 चुंबकीय बल = ट्रैफिक पुलिस जो केवल दिशा मोड़ता है, चाल कभी नहीं बदलता!</p>"
   },
   {
    "h": "2️⃣ चुंबकीय क्षेत्र में गति — वृत्त और कुंडलिनी ⭐",
    "body": "<ul>\n<li><b>v ⊥ B ⭐⭐:</b> आवेश <b>वृत्त</b> में घूमता है। त्रिज्या <b>r = mv/(|q|B)</b>, आवर्तकाल <b>T = 2πm/(|q|B)</b>।</li>\n<li><b>T वेग पर निर्भर नहीं!</b> तेज कण बड़ा वृत्त, धीमा छोटा — समान समय में पूर्ण। (साइक्लोट्रॉन इसी पर!)</li>\n<li><b>v ∥ B:</b> कोई बल नहीं — सीधी रेखा में चलता रहे।</li>\n<li><b>कोण θ पर ⭐:</b> लंबवत घटक वृत्त बनाता है, समांतर खींचता है → पथ = <b>कुंडलिनी (helix)</b>।</li>\n<li><b>आवृत्ति:</b> f = |q|B/(2πm) — साइक्लोट्रॉन आवृत्ति।</li>\n<li><b>संवेग से त्रिज्या:</b> r = p/(|q|B)।</li>\n</ul>\n<p class=\"small-note\">🎯 r = mv/|q|B: अधिक संवेग = बड़ा वृत्त; अधिक B = तंग वृत्त।</p>"
   },
   {
    "h": "3️⃣ बायो-सावार नियम और वृत्ताकार लूप का क्षेत्र ⭐⭐",
    "body": "<ul>\n<li><b>बायो-सावार नियम ⭐:</b> लघु धारा अवयव का क्षेत्र <b>dB = (μ₀/4π) · I dl sin θ / r²</b>। μ₀/4π = 10⁻⁷ T·m/A।</li>\n<li><b>वृत्ताकार लूप के केंद्र पर ⭐⭐:</b> <b>B = μ₀I/(2R)</b> — N फेरे हों तो B = μ₀NI/(2R)।</li>\n<li><b>अक्ष पर (दूरी x):</b> B = μ₀IR²/(2(R² + x²)^(3/2))।</li>\n<li><b>चाप (कोण θ) के केंद्र पर:</b> B = (μ₀I/2R) × (θ/2π)।</li>\n<li><b>दिशा:</b> धारा वामावर्त → क्षेत्र बाहर; दक्षिणावर्त → भीतर। दाएं हाथ का कर्ल नियम!</li>\n<li><b>सीधे तार का क्षेत्र:</b> अनंत तार: B = μ₀I/(2πd)।</li>\n</ul>\n<p class=\"small-note\">💡 लूप केंद्र का सूत्र μ₀I/2R सर्वाधिक उपयोगी — संयोजनों में प्रत्येक चाप का B अलग निकालो, फिर सदिश योग।</p>"
   },
   {
    "h": "4️⃣ एंपियर नियम, परिनालिका और टोरॉइड ⭐",
    "body": "<ul>\n<li><b>एंपियर का परिपथीय नियम ⭐:</b> <b>∮B·dl = μ₀I_परिबद्ध</b> — गाउस नियम का चुंबकीय संस्करण।</li>\n<li><b>अनंत सीधा तार ⭐:</b> <b>B = μ₀I/(2πr)</b>। दिशा: दाएं हाथ का अंगूठा नियम।</li>\n<li><b>परिनालिका (solenoid) ⭐⭐:</b> भीतर एकसमान क्षेत्र <b>B = μ₀nI</b> (n = फेरे प्रति इकाई लंबाई); बाहर लगभग शून्य।</li>\n<li><b>टोरॉइड (अतिरिक्त):</b> भीतर B = μ₀NI/(2πr), बाहर और केंद्र में शून्य।</li>\n</ul>\n<p class=\"small-note\">🎯 μ₀I/2πr (तार), μ₀nI (परिनालिका), μ₀NI/2R (लूप केंद्र) — तीन सूत्र 80% प्रश्न हल करते हैं!</p>"
   },
   {
    "h": "5️⃣ चालक पर बल, समांतर तार और लूप पर बलाघूर्ण ⭐⭐",
    "body": "<ul>\n<li><b>धारावाही चालक पर बल ⭐:</b> <b>F = IL × B</b>, परिमाण F = BIL sin θ। दिशा: फ्लेमिंग का बायां हाथ नियम।</li>\n<li><b>दो समांतर तार ⭐⭐:</b> प्रति इकाई लंबाई बल <b>F/L = μ₀I₁I₂/(2πd)</b> — समान दिशा धाराएं <b>आकर्षित</b>, विपरीत <b>प्रतिकर्षित</b>।</li>\n<li><b>एंपियर की परिभाषा:</b> पुराने SI में 1 A की परिभाषा 1 m दूर समांतर तारों के बीच 2 × 10⁻⁷ N/m बल से थी; वर्तमान SI आवेश के नियत मान पर आधारित है।</li>\n<li><b>धारा लूप पर बलाघूर्ण ⭐⭐:</b> <b>τ = NIAB sin θ; vector: τ = m × B</b> जहाँ m = NIA (चुंबकीय द्विध्रुव आघूर्ण)।</li>\n<li><b>स्थितिज ऊर्जा:</b> U = −mB cos θ।</li>\n</ul>\n<p class=\"small-note\">💡 समान-दिशा धाराएं आकर्षित — आवेशों में समान प्रतिकर्षित, धाराओं में समान आकर्षित। याद रखो!</p>"
   },
   {
    "h": "6️⃣ गतिशील कुंडली धारामापी ⭐",
    "body": "<ul>\n<li><b>धारामापी:</b> लघु धारा मापने की युक्ति — संतुलन: <b>nIAB = kφ</b> → विक्षेप φ ∝ I।</li>\n<li><b>त्रिज्यीय क्षेत्र:</b> तल सदैव क्षेत्र के समांतर — रैखिक स्केल।</li>\n<li><b>धारा सुग्राहिता:</b> φ/I = nAB/k।</li>\n<li><b>अमीटर बनाना ⭐⭐:</b> समांतर में छोटा शंट S = I_g·G/(I − I_g) — अमीटर का प्रतिरोध अत्यंत कम (श्रेणी में लगता है)।</li>\n<li><b>वोल्टमीटर बनाना ⭐⭐:</b> श्रेणी में बड़ा प्रतिरोध R = V/I_g − G — वोल्टमीटर का प्रतिरोध अत्यंत उच्च (समांतर में)।</li>\n<li><b>आदर्श अमीटर R = 0, आदर्श वोल्टमीटर R = ∞।</b></li>\n</ul>\n<p class=\"small-note\">🎯 अमीटर के भीतर शंट समांतर, पूरा अमीटर परिपथ में श्रेणी। वोल्टमीटर के भीतर बड़ा R श्रेणी, पूरा वोल्टमीटर परिपथ में समांतर।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Magnetic Field and the Lorentz Force ⭐",
    "body": "<ul>\n<li><b>Oersted's discovery:</b> a compass needle deflects near a current-carrying wire — <b>current creates a magnetic field!</b> Electricity and magnetism are connected.</li>\n<li><b>Magnetic field (B):</b> the field that pushes moving charges. Unit: tesla (T); smaller unit gauss (1 T = 10⁴ G).</li>\n<li><b>Lorentz force ⭐⭐:</b> the force on a moving charge <b>F = q(v × B)</b>, magnitude <b>F = |q|vB sin θ</b>. Direction: <b>right-hand / Fleming's left-hand rule</b> (REVERSED for a negative charge!).</li>\n<li><b>Total electromagnetic force:</b> F = q(E + v × B) — electric and magnetic together.</li>\n<li><b>Work done by magnetic force ⭐:</b> the force is always perpendicular to velocity → <b>work done is ZERO</b>; speed never changes, only direction! (Kinetic energy stays constant.)</li>\n<li><b>On a static charge:</b> magnetic force is ZERO (v = 0) — a magnetic field only grabs moving charges.</li>\n</ul>\n<p class=\"small-note\">💡 Magnetic force is a traffic cop that only turns vehicles, never speeds them up. That is why a magnetic field alone cannot give energy!</p>"
   },
   {
    "h": "2️⃣ Motion in a Magnetic Field — Circles and Helices ⭐",
    "body": "<ul>\n<li><b>v ⊥ B ⭐⭐:</b> the charge moves in a <b>circle</b> — the magnetic force acts as the centripetal force. Radius <b>r = mv/(|q|B)</b>, period <b>T = 2πm/(|q|B)</b>.</li>\n<li><b>T does not depend on velocity!</b> A fast particle makes a big circle, a slow one a small circle — both finish in the same time. (The cyclotron works on this (extra context)!)</li>\n<li><b>v ∥ B:</b> no force (sin 0 = 0) — the charge keeps moving straight.</li>\n<li><b>At angle θ ⭐:</b> the perpendicular component circles, the parallel component drifts straight → the path is a <b>helix</b> (like a spring). Pitch = v cos θ × T.</li>\n<li><b>Frequency:</b> f = |q|B/(2πm) — the cyclotron frequency.</li>\n<li><b>Radius from momentum:</b> r = p/(|q|B) — the momentum-measuring tool of particle detectors!</li>\n</ul>\n<p class=\"small-note\">🎯 Remember r = mv/|q|B: more momentum = bigger circle; stronger B or more charge = tighter circle.</p>"
   },
   {
    "h": "3️⃣ Biot-Savart Law and the Field of a Circular Loop ⭐⭐",
    "body": "<ul>\n<li><b>Biot-Savart law ⭐:</b> the field of a small current element <b>dB = (μ₀/4π) · I dl sin θ / r²</b>. μ₀/4π = 10⁻⁷ T·m/A. Direction: right-hand rule (dl × r̂).</li>\n<li><b>Centre of a circular loop ⭐⭐:</b> <b>B = μ₀I/(2R)</b> — for N turns, B = μ₀NI/(2R).</li>\n<li><b>On the axis (distance x):</b> B = μ₀IR²/(2(R² + x²)^(3/2)) — falls off away from the centre.</li>\n<li><b>Arc of angle θ at the centre:</b> B = (μ₀I/2R) × (θ/2π) — semicircle = half, quarter arc = quarter.</li>\n<li><b>Direction:</b> anticlockwise current → field TOWARD you (out of page); clockwise → away (into page). Right-hand curl rule!</li>\n<li><b>Field of a straight wire (from Biot-Savart):</b> B = (μ₀I/4πd)(sin θ₁ + sin θ₂); infinite wire: B = μ₀I/(2πd).</li>\n</ul>\n<p class=\"small-note\">💡 The loop-centre formula μ₀I/2R is the most used — in combination problems, find each arc/loop's B separately, then add as vectors.</p>"
   },
   {
    "h": "4️⃣ Ampere's Law, Solenoid and Toroid ⭐",
    "body": "<ul>\n<li><b>Ampere's circuital law ⭐:</b> around a closed loop <b>∮B·dl = μ₀I_enclosed</b> — the magnetic version of Gauss's law (for symmetric problems).</li>\n<li><b>Infinite straight wire ⭐:</b> a circular Amperian loop gives <b>B = μ₀I/(2πr)</b> — falls as 1/r. Direction: right-hand thumb rule (thumb = current, curled fingers = B).</li>\n<li><b>Solenoid ⭐⭐:</b> uniform field inside <b>B = μ₀nI</b> (n = turns per unit length); approximately zero outside. A long electromagnet!</li>\n<li><b>Toroid (extra; current theory outline se bahar):</b> a solenoid bent into a ring — inside, B = μ₀NI/(2πr); zero outside and in the hollow centre.</li>\n<li><b>Inside a solenoid the field depends on turn DENSITY, not total turns</b> — same n means same B, however long it is.</li>\n</ul>\n<p class=\"small-note\">🎯 μ₀I/2πr (wire), μ₀nI (solenoid), μ₀NI/2R (loop centre) — these three B-formulas solve 80% of questions!</p>"
   },
   {
    "h": "5️⃣ Force on a Conductor, Parallel Wires and Torque on a Loop ⭐⭐",
    "body": "<ul>\n<li><b>Force on a current-carrying conductor ⭐:</b> <b>F = IL × B</b>, magnitude F = BIL sin θ. Direction: Fleming's left-hand rule (Forefinger = Field, Middle = current, Thumb = motion/force).</li>\n<li><b>Two parallel wires ⭐⭐:</b> force per unit length <b>F/L = μ₀I₁I₂/(2πd)</b> — currents in the SAME direction <b>attract</b>, opposite <b>repel</b>. (This was used in the historical definition of the ampere.)</li>\n<li><b>Definition of the ampere:</b> The historical SI definition used 2 × 10⁻⁷ N/m between parallel wires 1 m apart; the modern SI fixes the elementary charge instead.</li>\n<li><b>Torque on a current loop ⭐⭐:</b> <b>τ = NIAB sin θ; vector: τ = m × B</b> where m = NIA (magnetic dipole moment). Maximum at θ = 90°, zero at θ = 0.</li>\n<li><b>Loop = magnetic dipole:</b> a current loop behaves like a tiny bar magnet — m = NIA is its dipole moment.</li>\n<li><b>Potential energy:</b> U = −m·B = −mB cos θ (just like the electric dipole!).</li>\n</ul>\n<p class=\"small-note\">💡 Same-direction currents attract — sounds backwards, right? Like charges repel, but like currents ATTRACT. Remember it!</p>"
   },
   {
    "h": "6️⃣ Moving Coil Galvanometer ⭐",
    "body": "<ul>\n<li><b>Galvanometer:</b> a device to detect/measure small currents — a coil sits in a magnetic field; current produces torque, a spring gives restoring torque. Balance: <b>nIAB = kφ</b> → deflection φ ∝ I.</li>\n<li><b>Radial field:</b> the poles are curved so the coil plane always stays parallel to the field — τ = nIAB stays constant, giving a linear scale.</li>\n<li><b>Current sensitivity:</b> φ/I = nAB/k — deflection per ampere.</li>\n<li><b>Making an ammeter ⭐⭐:</b> connect a SMALL shunt in parallel: S = I_g·G/(I − I_g) — most current bypasses the coil. An ammeter has very LOW resistance (goes in series).</li>\n<li><b>Making a voltmeter ⭐⭐:</b> connect a LARGE resistance in series: R = V/I_g − G — a voltmeter has very HIGH resistance (goes in parallel).</li>\n<li><b>Ideal ammeter R = 0, ideal voltmeter R = ∞</b> — the closer a real one gets, the better.</li>\n</ul>\n<p class=\"small-note\">🎯 Ammeter ke andar shunt parallel, poora ammeter circuit me series; voltmeter ke andar resistor series, poora voltmeter circuit me parallel. Practice its numerical.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Lorentz Force ⭐",
    "items": [
     "F = qvB sinθ, direction right-hand",
     "v=0 ya v∥B to F=0",
     "Work by B = 0 (speed same)"
    ]
   },
   {
    "h": "Motion ⭐⭐",
    "items": [
     "v⊥B: circle, r = mv/|q|B",
     "T = 2πm/|q|B (v-independent!)",
     "Angle pe: helix"
    ]
   },
   {
    "h": "Field Sources ⭐⭐",
    "items": [
     "Loop center: μ₀I/2R",
     "Wire: μ₀I/2πr",
     "Solenoid: μ₀nI"
    ]
   },
   {
    "h": "Forces ⭐⭐",
    "items": [
     "F = BIL sinθ",
     "Parallel wires: same I attract",
     "τ = NIAB sinθ"
    ]
   },
   {
    "h": "Galvanometer ⭐",
    "items": [
     "φ ∝ I (radial field)",
     "Ammeter: parallel chhota shunt",
     "Voltmeter: series bada R"
    ]
   }
  ],
  "hi": [
   {
    "h": "लॉरेंट्ज बल ⭐",
    "items": [
     "F = qvB sinθ, दाएं हाथ नियम",
     "v=0 या v∥B तो F=0",
     "B का कार्य = 0 (चाल समान)"
    ]
   },
   {
    "h": "गति ⭐⭐",
    "items": [
     "v⊥B: वृत्त, r = mv/|q|B",
     "T = 2πm/|q|B (v-स्वतंत्र!)",
     "कोण पर: कुंडलिनी"
    ]
   },
   {
    "h": "क्षेत्र स्रोत ⭐⭐",
    "items": [
     "लूप केंद्र: μ₀I/2R",
     "तार: μ₀I/2πr",
     "परिनालिका: μ₀nI"
    ]
   },
   {
    "h": "बल ⭐⭐",
    "items": [
     "F = BIL sinθ",
     "समांतर तार: समान I आकर्षण",
     "τ = NIAB sinθ"
    ]
   },
   {
    "h": "धारामापी ⭐",
    "items": [
     "φ ∝ I (त्रिज्यीय क्षेत्र)",
     "अमीटर: समांतर छोटा शंट",
     "वोल्टमीटर: श्रेणी बड़ा R"
    ]
   }
  ],
  "en": [
   {
    "h": "Lorentz Force ⭐",
    "items": [
     "F = qvB sinθ, right-hand rule",
     "v=0 or v∥B means F=0",
     "Work by B = 0 (speed unchanged)"
    ]
   },
   {
    "h": "Motion ⭐⭐",
    "items": [
     "v⊥B: circle, r = mv/|q|B",
     "T = 2πm/|q|B (v-independent!)",
     "At an angle: helix"
    ]
   },
   {
    "h": "Field Sources ⭐⭐",
    "items": [
     "Loop centre: μ₀I/2R",
     "Wire: μ₀I/2πr",
     "Solenoid: μ₀nI"
    ]
   },
   {
    "h": "Forces ⭐⭐",
    "items": [
     "F = BIL sinθ",
     "Parallel wires: same I attracts",
     "τ = NIAB sinθ"
    ]
   },
   {
    "h": "Galvanometer ⭐",
    "items": [
     "φ ∝ I (radial field)",
     "Ammeter: tiny parallel shunt",
     "Voltmeter: huge series R"
    ]
   }
  ]
 },
 "practice": [
  [
   "Electron (1.6×10⁻¹⁹ C, 10⁷ m/s) 0.5 T field me perpendicular enter karta hai. Force?",
   "F = qvB = 1.6×10⁻¹⁹ × 10⁷ × 0.5 = <b>8 × 10⁻¹³ N</b>, direction v × B ke opposite (electron negative hai!)."
  ],
  [
   "Magnetic field charge ki speed badha sakta hai?",
   "<b>Nahi</b> — force hamesha velocity ke perpendicular, work zero, sirf direction badalti hai."
  ],
  [
   "Proton 0.2 T field me perpendicular, r = 2 cm. Speed kitni? (m = 1.67×10⁻²⁷ kg)",
   "v = rqB/m = 0.02 × 1.6×10⁻¹⁹ × 0.2/1.67×10⁻²⁷ ≈ <b>3.8 × 10⁵ m/s</b>."
  ],
  [
   "20 cm radius, 5 A current wali circular loop ke center pe B?",
   "B = μ₀I/2R = (4π×10⁻⁷ × 5)/(2 × 0.2) = <b>1.57 × 10⁻⁵ T</b>."
  ],
  [
   "Ek wire me 10 A, usse 5 cm door B kitna?",
   "B = μ₀I/2πr = 2×10⁻⁷ × 10/0.05 = <b>4 × 10⁻⁵ T</b>."
  ],
  [
   "Do parallel wires me same direction current — attract ya repel?",
   "<b>Attract</b> (F/L = μ₀I₁I₂/2πd). Opposite direction me repel."
  ],
  [
   "Solenoid (n = 1000 turns/m) me 2 A. Andar field?",
   "B = μ₀nI = 4π×10⁻⁷ × 1000 × 2 = <b>2.51 × 10⁻³ T</b>."
  ],
  [
   "N = 50, A = 0.02 m², I = 1 A, B = 0.3 T, θ = 90°. Torque?",
   "τ = NIAB = 50 × 1 × 0.02 × 0.3 = <b>0.3 N·m</b> (max, kyunki sin 90° = 1)."
  ],
  [
   "Galvanometer ko ammeter kaise banate hain?",
   "Parallel me <b>chhota shunt</b> S = I_g·G/(I − I_g) lagao — ammeter ka total resistance bahut low ho jaata hai."
  ],
  [
   "Galvanometer (G = 100 Ω, I_g = 1 mA) se 10 V voltmeter. Kitna series R?",
   "R = V/I_g − G = 10/0.001 − 100 = <b>9900 Ω</b> series me."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/physics/ch-5/",
  "title": "Magnetism and Matter"
 }
}

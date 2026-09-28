# Class 11 Physics, Chapter 6 - System of Particles & Rotational Motion
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 6,
 "title_en": "System of Particles & Rotational Motion",
 "title_hi": "कण निकाय और घूर्णी गति",
 "tagline": "COM, torque, moment of inertia, angular momentum aur rolling ka poora game",
 "jee": "HIGH",
 "meta_desc": "Class 11 Physics Chapter 6: System of Particles and Rotational Motion — long + short notes in Hindi, English, Hinglish. Centre of mass, torque, moment of inertia, angular momentum conservation, rolling motion, equilibrium.",
 "video": {
  "youtube": "ufWc4KnUxzY",
  "dur": "1 min 12 sec"
 },
 "card_tag": "COM, torque, moment of inertia, angular momentum aur rolling ka poora game",
 "card_topics": [
  "🎯 Centre of mass",
  "🔧 Torque + moment of inertia",
  "🌀 Angular momentum conservation",
  "🛞 Rolling motion"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Centre of Mass — System Ka Average Point",
    "body": "<p><b>Centre of mass (COM):</b> woh point jahan poora mass concentrated maan sakte hain — system ka motion usi point ka motion jaisa behave karta hai.</p>\n<ul>\n<li><b>Formula:</b> x<sub>COM</sub> = (m₁x₁ + m₂x₂ + ...)/(m₁ + m₂ + ...) — mass-weighted average position. y, z ke liye bhi same.</li>\n<li>Uniform (same material) symmetric bodies ka COM <b>geometric center</b> pe: ring ke center pe (material wahan hai bhi nahi!), disc ke center, sphere ke center.</li>\n<li><b>External force sirf COM ko accelerate karti hai</b> — internal forces (explosion, push between parts) COM ka motion nahi badalte! ⭐ Firecracker upar explode ho: tukde idhar-udhar, lekin COM wahi parabola follow karta hai.</li>\n<li><b>COM velocity:</b> v<sub>COM</sub> = (m₁v₁ + m₂v₂)/M — total momentum = M × v<sub>COM</sub>.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: danda ghumate hue phenko — dande ka har point ulta-pulta ghoomta hai, lekin uska COM seedhi parabola banata hai!</p>"
   },
   {
    "h": "2️⃣ Torque aur Moment of Inertia — Ghoomne Ka Physics",
    "body": "<p>Rotation me linear quantities ke counterparts hote hain:</p>\n<table class=\"tbl\">\n<tr><th>Linear</th><th>Rotational</th></tr>\n<tr><td>Displacement x</td><td>Angle θ (rad)</td></tr>\n<tr><td>Velocity v</td><td>Angular velocity ω</td></tr>\n<tr><td>Acceleration a</td><td>Angular acceleration α</td></tr>\n<tr><td>Force F</td><td>Torque τ = r × F = rF sinθ</td></tr>\n<tr><td>Mass m</td><td>Moment of inertia I</td></tr>\n<tr><td>Momentum p = mv</td><td>Angular momentum L = Iω</td></tr>\n</table>\n<ul>\n<li><b>Torque:</b> τ = rF sinθ — force × lever arm (perpendicular distance). Darwaza hinge ke paas dhakka = kam torque; handle pe (door) = zyada. Unit: N·m.</li>\n<li><b>Moment of inertia ⭐:</b> I = Σmr² — rotation me \"mass\" ka role. Mass axis se JITNA DOOR, utna ZYADA I, utna mushkil ghumana.</li>\n<li><b>Key values:</b> ring I = MR² • disc/solid cylinder I = ½MR² • solid sphere I = (2/5)MR² • rod (center) I = ML²/12 • rod (end) I = ML²/3.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: ghoomte hue chair pe haath failao = I badhta hai = ω ghatti hai. Haath sameto = tez ghoomte ho (skaters ka trick!).</p>"
   },
   {
    "h": "3️⃣ Angular Momentum Conservation ⭐",
    "body": "<p><b>Angular momentum:</b> L = Iω (particle ke liye L = mvr sinθ = r × p). Jab external torque zero ho, <b>L conserved</b>:</p>\n<ul>\n<li><b>Ice skater ⭐:</b> haath sametne se I kam → ω zyada (L = Iω same rakhne ke liye). Haath failao = slow.</li>\n<li>Diver somersault me body tuck karta hai = fast spin; open karta hai = slow (water entry ke liye).</li>\n<li>Planet orbit me: sun ke paas fast, door slow (Kepler's second law — angular momentum conservation!).</li>\n<li><b>Newton's second law for rotation:</b> τ = dL/dt = Iα (I constant ho toh) — F = ma ka rotational version.</li>\n</ul>\n<p class=\"small-note\">🎯 L = Iω aur L conserved → I aur ω ka product fix. Ek badhao, doosra ghatna padega!</p>"
   },
   {
    "h": "4️⃣ Rolling Motion — Rotation + Translation Ek Saath ⭐",
    "body": "<p><b>Rolling = rotation + translation ka combo.</b> Pure rolling (no slipping): v = ωr — bottom point instant rest pe hota hai!</p>\n<ul>\n<li><b>Total KE:</b> K = ½mv<sub>COM</sub>² + ½Iω² — dono parts! Ring: ½mv² + ½mv² = mv². Disc: ¾mv². Sphere: (7/10)mv².</li>\n<li><b>Incline pe race ⭐:</b> v = √(2gh/(1 + I/MR²)) — I/MR² jitna CHHOTA, utna FAST: solid sphere (2/5) &gt; disc (1/2) &gt; ring (1). Sphere sabse pehle neeche!</li>\n<li><b>Friction rolling me STATIC hai</b> (bottom point rest) — isliye energy waste nahi hoti, lekin friction zaroori hai rolling KE LIYE (bina friction sirf slide hoga!).</li>\n<li><b>Kinetic energy share:</b> ring me half translation, half rotation; sphere me rotation ka share sirf 2/7.</li>\n</ul>\n<p class=\"small-note\">🎯 Race yaad rakho: jitna compact (mass axis ke paas), utna tez winner. Sphere &gt; Disc &gt; Ring!</p>"
   },
   {
    "h": "5️⃣ Equilibrium — Na Ghoomo, Na Hilo",
    "body": "<p><b>Static equilibrium ke 2 conditions:</b></p>\n<ul>\n<li><b>Net force = 0</b> (translation nahi) — ΣF = 0.</li>\n<li><b>Net torque = 0</b> (rotation nahi) — Στ = 0 (kisi bhi point ke about). ⭐ Ladder problems, beam problems dono yahi se.</li>\n<li><b>Stable equilibrium:</b> thoda tilt karo toh wapas aata hai (COM neeche, PE minimum) • <b>unstable:</b> gir jaata hai (COM upar) • <b>neutral:</b> jahan rakho wahan rehta hai (sphere flat surface pe).</li>\n<li><b>Couple:</b> do equal-opposite forces alag lines pe — sirf torque dete hain, net force zero (steering wheel ghumana!).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: book table ke edge pe — COM table ke andar = stable; bahar nikla = giregi. Isliye cheezon ka COM support ke andar rakho!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ द्रव्यमान केंद्र — निकाय का औसत बिंदु",
    "body": "<p><b>द्रव्यमान केंद्र (COM):</b> वह बिंदु जहाँ सम्पूर्ण द्रव्यमान केंद्रित माना जा सकता है — निकाय की गति इसी बिंदु की गति जैसी होती है।</p>\n<ul>\n<li><b>सूत्र:</b> x<sub>COM</sub> = (m₁x₁ + m₂x₂ + ...)/(m₁ + m₂ + ...) — द्रव्यमान-भारित औसत।</li>\n<li>समांग सममित पिंडों का COM <b>ज्यामितीय केंद्र</b> पर: वलय, चकती, गोले के केंद्र पर।</li>\n<li><b>बाह्य बल केवल COM को त्वरित करता है</b> — आंतरिक बल COM की गति नहीं बदलते! ⭐ आकाश में फटा पटाखा: टुकड़े इधर-उधर, पर COM वही परवलय।</li>\n<li><b>COM वेग:</b> v<sub>COM</sub> = (m₁v₁ + m₂v₂)/M — कुल संवेग = M × v<sub>COM</sub>।</li>\n</ul>\n<p class=\"small-note\">💡 घूमती छड़ फेंको — प्रत्येक बिंदु घूमता है, पर COM सीधा परवलय बनाता है!</p>"
   },
   {
    "h": "2️⃣ बलाघूर्ण और जड़त्व आघूर्ण",
    "body": "<p>घूर्णन में रैखिक राशियों के समकक्ष होते हैं:</p>\n<table class=\"tbl\">\n<tr><th>रैखिक</th><th>घूर्णी</th></tr>\n<tr><td>विस्थापन x</td><td>कोण θ (रेडियन)</td></tr>\n<tr><td>वेग v</td><td>कोणीय वेग ω</td></tr>\n<tr><td>त्वरण a</td><td>कोणीय त्वरण α</td></tr>\n<tr><td>बल F</td><td>बलाघूर्ण τ = rF sinθ</td></tr>\n<tr><td>द्रव्यमान m</td><td>जड़त्व आघूर्ण I</td></tr>\n<tr><td>संवेग p = mv</td><td>कोणीय संवेग L = Iω</td></tr>\n</table>\n<ul>\n<li><b>बलाघूर्ण (torque):</b> τ = rF sinθ — बल × भुजा-लंबाई (लंबवत दूरी)। दरवाज़ा हैंडल से = अधिक, कब्ज़े के पास = कम। मात्रक: N·m।</li>\n<li><b>जड़त्व आघूर्ण ⭐:</b> I = Σmr² — घूर्णन में द्रव्यमान की भूमिका। द्रव्यमान अक्ष से जितना दूर, उतना अधिक I, उतना कठिन घुमाना।</li>\n<li><b>प्रमुख मान:</b> वलय MR² • चकती/ठोस बेलन ½MR² • ठोस गोला (2/5)MR² • छड़ (केंद्र) ML²/12 • छड़ (सिरा) ML²/3।</li>\n</ul>\n<p class=\"small-note\">💡 घूमती कुर्सी पर हाथ फैलाओ = I बढ़ता = ω घटती; हाथ समेटो = तेज़ (स्केटर की चाल!)।</p>"
   },
   {
    "h": "3️⃣ कोणीय संवेग संरक्षण ⭐",
    "body": "<p><b>कोणीय संवेग:</b> L = Iω (कण के लिए L = mvr sinθ)। जब बाह्य बलाघूर्ण शून्य हो, <b>L संरक्षित</b>:</p>\n<ul>\n<li><b>आइस स्केटर ⭐:</b> हाथ समेटने से I कम → ω अधिक।</li>\n<li>गोताखोर शरीर समेटता है = तीव्र घूर्णन; खोलता है = मंद।</li>\n<li>ग्रह कक्षा में: सूर्य के पास तीव्र, दूर मंद (केप्लर का द्वितीय नियम!)।</li>\n<li><b>घूर्णन का द्वितीय नियम:</b> τ = dL/dt = Iα — F = ma का घूर्णी रूप।</li>\n</ul>\n<p class=\"small-note\">🎯 L = Iω नियत → एक बढ़े तो दूसरा घटेगा!</p>"
   },
   {
    "h": "4️⃣ लोटनी गति — घूर्णन + स्थानांतरण साथ-साथ ⭐",
    "body": "<p><b>लोटनी = घूर्णन + स्थानांतरण का संयोजन।</b> शुद्ध लोटनी (बिना सर्पण): v = ωr — निम्नतम बिंदु क्षणिक विराम में!</p>\n<ul>\n<li><b>कुल KE:</b> K = ½mv<sub>COM</sub>² + ½Iω²। वलय: mv² • चकती: ¾mv² • गोला: (7/10)mv²।</li>\n<li><b>नत तल पर दौड़ ⭐:</b> v = √(2gh/(1 + I/MR²)) — I/MR² जितना छोटा, उतना तीव्र: ठोस गोला (2/5) &gt; चकती (1/2) &gt; वलय (1)।</li>\n<li><b>लोटनी में घर्षण स्थैतिक है</b> — ऊर्जा व्यर्थ नहीं, परंतु लोटनी के लिए घर्षण आवश्यक (बिना घर्षण केवल सर्पण!)।</li>\n<li><b>KE बँटवारा:</b> वलय में आधा स्थानांतरण, आधा घूर्णन; गोले में घूर्णन का हिस्सा केवल 2/7।</li>\n</ul>\n<p class=\"small-note\">🎯 दौड़ याद रखें: जितना संहत (द्रव्यमान अक्ष के पास), उतना विजेता। गोला &gt; चकती &gt; वलय!</p>"
   },
   {
    "h": "5️⃣ साम्यावस्था — न घूमे, न हिले",
    "body": "<p><b>स्थैतिक साम्य की 2 शर्तें:</b></p>\n<ul>\n<li><b>कुल बल = 0</b> (स्थानांतरण नहीं) — ΣF = 0।</li>\n<li><b>कुल बलाघूर्ण = 0</b> (घूर्णन नहीं) — Στ = 0 (किसी भी बिंदु के सापेक्ष)। ⭐ सीढ़ी और बीम प्रश्न इसी से।</li>\n<li><b>स्थायी साम्य:</b> झुकाने पर वापस (COM नीचे) • <b>अस्थायी:</b> गिर जाता है (COM ऊपर) • <b>तटस्थ:</b> जहाँ रखो वहीं रहता है।</li>\n<li><b>बल-युग्म (couple):</b> दो समान-विपरीत बल भिन्न रेखाओं पर — केवल बलाघूर्ण, कुल बल शून्य (स्टीयरिंग व्हील!)।</li>\n</ul>\n<p class=\"small-note\">💡 मेज़ के किनारे किताब — COM मेज़ के अंदर = स्थायी; बाहर = गिरेगी।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Centre of Mass — The System's Average Point",
    "body": "<p><b>Centre of mass (COM):</b> the point where the whole mass can be treated as concentrated — the system moves as if it were this point.</p>\n<ul>\n<li><b>Formula:</b> x<sub>COM</sub> = (m₁x₁ + m₂x₂ + ...)/(m₁ + m₂ + ...) — the mass-weighted average position (same for y and z).</li>\n<li>Uniform symmetric bodies have the COM at the <b>geometric center</b>: a ring's center (no material there!), disc center, sphere center.</li>\n<li><b>Only external forces accelerate the COM</b> — internal forces (explosions, pushes between parts) never change the COM's motion! ⭐ A firecracker exploding mid-air: fragments fly everywhere, but the COM follows the same parabola.</li>\n<li><b>COM velocity:</b> v<sub>COM</sub> = (m₁v₁ + m₂v₂)/M — total momentum = M × v<sub>COM</sub>.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: throw a spinning stick — every point tumbles, but its COM traces a clean parabola!</p>"
   },
   {
    "h": "2️⃣ Torque and Moment of Inertia — The Physics of Turning",
    "body": "<p>Rotation has a counterpart for every linear quantity:</p>\n<table class=\"tbl\">\n<tr><th>Linear</th><th>Rotational</th></tr>\n<tr><td>Displacement x</td><td>Angle θ (rad)</td></tr>\n<tr><td>Velocity v</td><td>Angular velocity ω</td></tr>\n<tr><td>Acceleration a</td><td>Angular acceleration α</td></tr>\n<tr><td>Force F</td><td>Torque τ = rF sinθ</td></tr>\n<tr><td>Mass m</td><td>Moment of inertia I</td></tr>\n<tr><td>Momentum p = mv</td><td>Angular momentum L = Iω</td></tr>\n</table>\n<ul>\n<li><b>Torque:</b> τ = rF sinθ — force times lever arm (perpendicular distance). Push a door near the hinge = little torque; at the handle = lots. Unit: N·m.</li>\n<li><b>Moment of inertia ⭐:</b> I = Σmr² — the \"mass\" of rotation. The FARTHER the mass from the axis, the BIGGER the I, the harder to spin.</li>\n<li><b>Key values:</b> ring I = MR² • disc/solid cylinder I = ½MR² • solid sphere I = (2/5)MR² • rod (center) I = ML²/12 • rod (end) I = ML²/3.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: on a spinning chair, stretch your arms out = I rises = ω drops. Pull them in = spin faster (the skater's trick!).</p>"
   },
   {
    "h": "3️⃣ Angular Momentum Conservation ⭐",
    "body": "<p><b>Angular momentum:</b> L = Iω (for a particle, L = mvr sinθ = r × p). When external torque is zero, <b>L is conserved</b>:</p>\n<ul>\n<li><b>Ice skater ⭐:</b> pulling arms in lowers I → ω rises (keeping L = Iω the same). Arms out = slower.</li>\n<li>A diver tucks mid-air for a fast spin, opens up to slow down for entry.</li>\n<li>Planets: faster near the sun, slower far away (Kepler's second law — angular momentum conservation!).</li>\n<li><b>Newton's second law for rotation:</b> τ = dL/dt = Iα (for constant I) — the rotational F = ma.</li>\n</ul>\n<p class=\"small-note\">🎯 With L = Iω fixed, raising one forces the other down!</p>"
   },
   {
    "h": "4️⃣ Rolling Motion — Rotation + Translation Together ⭐",
    "body": "<p><b>Rolling = rotation plus translation.</b> Pure rolling (no slipping): v = ωr — the bottom point is instantaneously at rest!</p>\n<ul>\n<li><b>Total KE:</b> K = ½mv<sub>COM</sub>² + ½Iω² — both parts count! Ring: mv². Disc: ¾mv². Sphere: (7/10)mv².</li>\n<li><b>Incline race ⭐:</b> v = √(2gh/(1 + I/MR²)) — the SMALLER the I/MR², the FASTER: solid sphere (2/5) &gt; disc (1/2) &gt; ring (1). The sphere wins!</li>\n<li><b>Rolling friction is STATIC</b> (bottom point at rest) — no energy wasted, yet friction is needed FOR rolling (without it there is only sliding!).</li>\n<li><b>Energy split:</b> ring — half translation, half rotation; sphere — rotation takes only 2/7.</li>\n</ul>\n<p class=\"small-note\">🎯 Race rule: the more compact (mass near the axis), the faster the winner. Sphere &gt; Disc &gt; Ring!</p>"
   },
   {
    "h": "5️⃣ Equilibrium — No Turning, No Moving",
    "body": "<p><b>Two conditions for static equilibrium:</b></p>\n<ul>\n<li><b>Net force = 0</b> (no translation) — ΣF = 0.</li>\n<li><b>Net torque = 0</b> (no rotation) — Στ = 0 about ANY point. ⭐ Ladder and beam problems both start here.</li>\n<li><b>Stable equilibrium:</b> tilt it and it returns (COM low, PE minimum) • <b>unstable:</b> it topples (COM high) • <b>neutral:</b> stays wherever placed (sphere on a flat surface).</li>\n<li><b>Couple:</b> two equal-opposite forces on different lines — pure torque, zero net force (steering wheel!).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: book on a table edge — COM over the table = stable; COM beyond the edge = it falls. Keep the COM inside the support!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "COM",
    "items": [
     "x_COM = Σmx/Σm (mass-weighted avg)",
     "Symmetric body → geometric center",
     "Internal forces COM motion nahi badalte ⭐"
    ]
   },
   {
    "h": "Torque + I",
    "items": [
     "τ = rF sinθ (lever arm!)",
     "I = Σmr² — mass jitna door, utna I",
     "Ring MR², Disc ½MR², Sphere (2/5)MR², Rod center ML²/12"
    ]
   },
   {
    "h": "Angular Momentum ⭐",
    "items": [
     "L = Iω; τ_ext = 0 → L conserved",
     "Skater: haath sameto → I↓, ω↑",
     "τ = Iα (rotational F = ma)"
    ]
   },
   {
    "h": "Rolling ⭐",
    "items": [
     "v = ωr (pure rolling), bottom point rest",
     "K = ½mv² + ½Iω²",
     "Race: sphere > disc > ring (I/MR² chhota = tez)"
    ]
   },
   {
    "h": "Equilibrium",
    "items": [
     "ΣF = 0 AND Στ = 0",
     "Stable: COM neeche; unstable: upar",
     "Couple = sirf torque, force zero"
    ]
   }
  ],
  "hi": [
   {
    "h": "COM",
    "items": [
     "x_COM = Σmx/Σm (द्रव्यमान-भारित औसत)",
     "सममित पिंड → ज्यामितीय केंद्र",
     "आंतरिक बल COM गति नहीं बदलते ⭐"
    ]
   },
   {
    "h": "बलाघूर्ण + I",
    "items": [
     "τ = rF sinθ (भुजा-लंबाई!)",
     "I = Σmr² — द्रव्यमान जितना दूर, उतना I",
     "वलय MR², चकती ½MR², गोला (2/5)MR²"
    ]
   },
   {
    "h": "कोणीय संवेग ⭐",
    "items": [
     "L = Iω; τ_ext = 0 → L संरक्षित",
     "स्केटर: हाथ समेटो → I↓, ω↑",
     "τ = Iα"
    ]
   },
   {
    "h": "लोटनी ⭐",
    "items": [
     "v = ωr (शुद्ध लोटनी), निम्न बिंदु विराम",
     "K = ½mv² + ½Iω²",
     "दौड़: गोला > चकती > वलय"
    ]
   },
   {
    "h": "साम्य",
    "items": [
     "ΣF = 0 और Στ = 0",
     "स्थायी: COM नीचे; अस्थायी: ऊपर",
     "बल-युग्म = केवल बलाघूर्ण"
    ]
   }
  ],
  "en": [
   {
    "h": "COM",
    "items": [
     "x_COM = Σmx/Σm (mass-weighted avg)",
     "Symmetric body → geometric center",
     "Internal forces never change COM motion ⭐"
    ]
   },
   {
    "h": "Torque + I",
    "items": [
     "τ = rF sinθ (lever arm!)",
     "I = Σmr² — farther mass, bigger I",
     "Ring MR², Disc ½MR², Sphere (2/5)MR², Rod center ML²/12"
    ]
   },
   {
    "h": "Angular Momentum ⭐",
    "items": [
     "L = Iω; τ_ext = 0 → L conserved",
     "Skater: arms in → I↓, ω↑",
     "τ = Iα (rotational F = ma)"
    ]
   },
   {
    "h": "Rolling ⭐",
    "items": [
     "v = ωr (pure rolling), bottom point at rest",
     "K = ½mv² + ½Iω²",
     "Race: sphere > disc > ring (small I/MR² wins)"
    ]
   },
   {
    "h": "Equilibrium",
    "items": [
     "ΣF = 0 AND Στ = 0",
     "Stable: COM low; unstable: high",
     "Couple = pure torque, zero force"
    ]
   }
  ]
 },
 "practice": [
  [
   "2 kg ka mass x = 0 pe, 4 kg ka mass x = 6 m pe. COM kahan?",
   "x_COM = (2×0 + 4×6)/6 = <b>4 m</b> (4 kg ke paas — heavy side!)"
  ],
  [
   "10 N ka force 0.5 m ke wrench pe 90° pe lage. Torque?",
   "τ = rF sinθ = 0.5×10×1 = <b>5 N·m</b>. (30° pe hota toh sirf 2.5 N·m!)"
  ],
  [
   "Ring aur disc (same M, R) incline pe race karein. Kaun jeetega aur kyun?",
   "<b>Disc</b> — uska I/MR² = ½ chhota hai ring ke 1 se. Rotation me kam energy jaati hai, translation me zyada."
  ],
  [
   "Skater haath failaye I = 6 kg·m², ω = 2 rad/s se ghoomta hai. Haath sametne pe I = 3 ho jaata hai. New ω?",
   "L conserved: ω₂ = I₁ω₁/I₂ = 6×2/3 = <b>4 rad/s</b> — double speed!"
  ],
  [
   "Solid sphere (I = 2/5 MR²) height h se pure rolling se neeche aaye. Speed?",
   "v = √(2gh/(1+2/5)) = √(10gh/7) = <b>√(10gh/7)</b>."
  ],
  [
   "Rod (L = 2 m, M = 3 kg) ko center ke about ghumao. I? Aur ek end ke about?",
   "Center: ML²/12 = 3×4/12 = <b>1 kg·m²</b>. End: ML²/3 = <b>4 kg·m²</b> — 4x zyada!"
  ],
  [
   "Firecracker projectile ke top pe explode hua. Uske tukdon ka COM kya karega?",
   "<b>Wahi parabola follow karega</b> jo explosion na hota toh hota — internal forces COM ka path nahi badalte."
  ],
  [
   "Uniform beam 10 m, 40 kg, dono ends pe supports. Ek support kitna weight uthata hai?",
   "Symmetry se har support <b>half = 20 kg wt = 200 N</b> (ΣF = 0 aur Στ = 0 dono se)."
  ],
  [
   "Disc ka I = ½MR² aur woh v speed se roll kar raha hai. Total KE?",
   "K = ½mv² + ½(½MR²)(v/R)² = ½mv² + ¼mv² = <b>¾mv²</b>."
  ],
  [
   "Angular momentum L = 20 kg·m²/s constant hai. I double ho jaaye toh ω ka kya hoga?",
   "ω <b>half</b> ho jayega — L = Iω fixed, I↑ → ω↓ (inverse relation)."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/physics/ch-7/",
  "title": "Gravitation"
 }
}

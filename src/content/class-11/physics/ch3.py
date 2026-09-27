# Class 11 Physics, Chapter 3 - Motion in a Plane
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 3,
 "title_en": "Motion in a Plane",
 "title_hi": "समतल में गति",
 "tagline": "2D motion — vectors, projectile aur circular motion ka complete game",
 "jee": "HIGH",
 "meta_desc": "Class 11 Physics Chapter 3: Motion in a Plane — long + short notes in Hindi, English, Hinglish. Vectors, projectile motion, uniform circular motion, relative velocity.",
 "video": None,
 "card_tag": "2D motion — vectors, projectile aur circular motion ka complete game",
 "card_topics": [
  "➕ Vector addition",
  "🎯 Projectile motion",
  "🎡 Uniform circular motion",
  "🧭 Relative velocity"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Vectors — Direction Wali Quantities",
    "body": "<p>1D me sirf +/− kaafi tha, lekin 2D me <b>vectors</b> chahiye — magnitude + direction dono. Displacement, velocity, acceleration, force sab vectors; distance, speed, time, mass scalars.</p>\n<ul>\n<li><b>Addition:</b> triangle/parallelogram law — A aur B ko head-to-tail jodo, resultant R = A + B. Magnitude: |R| = √(A² + B² + 2AB cosθ).</li>\n<li><b>Resolution (components) ⭐:</b> vector A ko x/y me todo: A<sub>x</sub> = A cosθ, A<sub>y</sub> = A sinθ. Reverse: A = √(A<sub>x</sub>² + A<sub>y</sub>²), tanθ = A<sub>y</sub>/A<sub>x</sub>. Components se addition EASY: resultant ka component = components ka sum.</li>\n<li><b>Unit vectors:</b> î, ĵ, k̂ — sirf direction batate hain (magnitude 1). A = A<sub>x</sub>î + A<sub>y</sub>ĵ.</li>\n<li><b>Special cases:</b> same direction θ=0° → R = A+B; opposite θ=180° → R = |A−B|; perpendicular θ=90° → R = √(A²+B²).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: vector addition auto-rickshaw ka meter nahi, seedhi line hai — 3 km east + 4 km north = seedha 5 km (3-4-5 triangle!).</p>"
   },
   {
    "h": "2️⃣ 2D Motion — Position, Velocity, Acceleration (Vector Form)",
    "body": "<p>Plane me motion describe karne ke liye sab vector form me:</p>\n<ul>\n<li><b>Position vector:</b> r = xî + yĵ. <b>Displacement:</b> Δr = r₂ − r₁.</li>\n<li><b>Average velocity:</b> v<sub>avg</sub> = Δr/Δt • <b>instantaneous:</b> v = dr/dt — hamesha path ke TANGENT ke along.</li>\n<li><b>Acceleration:</b> a = dv/dt. 2D me velocity ki direction change hona bhi acceleration hai — speed constant ho tab bhi! (circular motion ka secret) ⭐</li>\n<li><b>Independence of motions ⭐:</b> x aur y motions bilkul independent — x me jo ho raha hai usse y pe koi farak nahi. Isi se projectile solve hota hai!</li>\n</ul>\n<p class=\"small-note\">🎯 Key idea: 2D motion = do 1D motions ek saath. Dono ko alag alag solve karo, time common hai.</p>"
   },
   {
    "h": "3️⃣ Projectile Motion — Upar Phenko, Parabola Bano ⭐",
    "body": "<p>Projectile = sirf gravity ke under free motion (a<sub>x</sub> = 0, a<sub>y</sub> = −g). Initial velocity u angle θ pe: u<sub>x</sub> = u cosθ (constant rehta hai!), u<sub>y</sub> = u sinθ (g se change hota hai).</p>\n<table class=\"tbl\">\n<tr><th>Quantity</th><th>Formula</th><th>Yaad rakhne wali baat</th></tr>\n<tr><td>Time of flight (T)</td><td>2u sinθ / g</td><td>sirf vertical part decide karta hai</td></tr>\n<tr><td>Max height (H)</td><td>u² sin²θ / 2g</td><td>θ = 90° pe maximum</td></tr>\n<tr><td>Range (R)</td><td>u² sin2θ / g</td><td>θ = 45° pe maximum ⭐</td></tr>\n<tr><td>Trajectory</td><td>y = x tanθ − gx²/(2u² cos²θ)</td><td>parabola!</td></tr>\n</table>\n<ul>\n<li><b>Complementary angles:</b> θ aur (90° − θ) same range dete hain (30° aur 60° same!).</li>\n<li>Highest point pe velocity = u cosθ (sirf horizontal), ZERO nahi! ⭐ (exam trap)</li>\n<li><b>Horizontal projection (height h se):</b> T = √(2h/g), R = u√(2h/g).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: cricket ka lofted shot — horizontal speed ball ki kabhi nahi rukti (air na ho toh), gravity sirf upar-neeche ka hisaab karti hai.</p>"
   },
   {
    "h": "4️⃣ Uniform Circular Motion — Ghoomega Toh Acceleration Zaroor",
    "body": "<p>Circle me CONSTANT speed se motion bhi accelerated motion hai — kyunki direction badal rahi hai!</p>\n<ul>\n<li><b>Centripetal (radial) acceleration ⭐:</b> a = v²/r = ω²r — hamesha CENTER ki taraf. Ye resultant acceleration hai, koi naya force nahi.</li>\n<li><b>Angular speed:</b> ω = 2π/T = 2πf • v = ωr. Period T = ek chakkar ka time, frequency f = chakkar per second.</li>\n<li>Examples: fan ka blade, merry-go-round, car circular turn pe (friction centripetal force deta hai), satellite orbit me (gravity deta hai).</li>\n<li>Velocity hamesha tangent, acceleration hamesha center — dono PERPENDICULAR ⭐.</li>\n</ul>\n<p class=\"small-note\">🎯 Yaad rakho: \"uniform circular\" me speed constant, velocity NAHI (direction change). Isliye acceleration zero nahi hai!</p>"
   },
   {
    "h": "5️⃣ Relative Velocity — 2D Me",
    "body": "<p>v<sub>AB</sub> = v<sub>A</sub> − v<sub>B</sub> — ab vectors ke saath. Classic cases:</p>\n<ul>\n<li><b>River-boat ⭐:</b> boat ka velocity (still water me) + river ka velocity = ground velocity. Straight across (shortest path): boat thoda upstream aim karo. Shortest time: boat seedha opposite bank ki taraf aim karo, drift downstream hota hai.</li>\n<li><b>Rain-man:</b> baarish vertical se tilted lagti hai jab aadmi bhagta hai — rain ka velocity − man ka velocity. Umbrella relative velocity ki direction me rakho!</li>\n<li>Wind-aeroplane problems bhi same idea.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: moving walkway pe chalna — tumhari speed + walkway ki speed = ground pe tumhari asli speed.</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ सदिश — दिशा वाली राशियाँ",
    "body": "<p>1D में केवल +/− पर्याप्त था, पर 2D में <b>सदिश (vectors)</b> चाहिए — परिमाण + दिशा दोनों। विस्थापन, वेग, त्वरण, बल सदिश हैं; दूरी, चाल, समय, द्रव्यमान अदिश।</p>\n<ul>\n<li><b>योग:</b> त्रिभुज/समांतर चतुर्भुज नियम — परिणामी R = A + B, |R| = √(A² + B² + 2AB cosθ)।</li>\n<li><b>घटक (components) ⭐:</b> A<sub>x</sub> = A cosθ, A<sub>y</sub> = A sinθ। वापस: A = √(A<sub>x</sub>² + A<sub>y</sub>²), tanθ = A<sub>y</sub>/A<sub>x</sub>। घटकों से योग सरल हो जाता है।</li>\n<li><b>मात्रक सदिश:</b> î, ĵ, k̂ — केवल दिशा (परिमाण 1)। A = A<sub>x</sub>î + A<sub>y</sub>ĵ।</li>\n<li><b>विशेष स्थितियाँ:</b> θ=0° → R = A+B; θ=180° → R = |A−B|; θ=90° → R = √(A²+B²)।</li>\n</ul>\n<p class=\"small-note\">💡 उदाहरण: 3 km पूर्व + 4 km उत्तर = सीधा 5 km (3-4-5 त्रिभुज)।</p>"
   },
   {
    "h": "2️⃣ द्विविमीय गति — स्थिति, वेग, त्वरण (सदिश रूप)",
    "body": "<p>तल में गति का वर्णन सदिश रूप में:</p>\n<ul>\n<li><b>स्थिति सदिश:</b> r = xî + yĵ। <b>विस्थापन:</b> Δr = r₂ − r₁।</li>\n<li><b>औसत वेग:</b> Δr/Δt • <b>तात्क्षणिक:</b> v = dr/dt — सदैव पथ की स्पर्श रेखा के अनुदिश।</li>\n<li><b>त्वरण:</b> a = dv/dt। 2D में वेग की दिशा बदलना भी त्वरण है — चाल नियत हो तब भी! ⭐</li>\n<li><b>गतियों की स्वतंत्रता ⭐:</b> x और y गतियाँ परस्पर स्वतंत्र — समय दोनों में समान।</li>\n</ul>\n<p class=\"small-note\">🎯 मुख्य बिंदु: 2D गति = दो 1D गतियाँ साथ-साथ। अलग-अलग हल करें।</p>"
   },
   {
    "h": "3️⃣ प्रक्षेप्य गति — ऊपर फेंको, परवलय बनो ⭐",
    "body": "<p>प्रक्षेप्य = केवल गुरुत्व के अधीन गति (a<sub>x</sub> = 0, a<sub>y</sub> = −g)। u कोण θ पर: u<sub>x</sub> = u cosθ (नियत रहता है!), u<sub>y</sub> = u sinθ (g से बदलता है)।</p>\n<table class=\"tbl\">\n<tr><th>राशि</th><th>सूत्र</th><th>ध्यान रखें</th></tr>\n<tr><td>उड्डयन काल (T)</td><td>2u sinθ / g</td><td>केवल ऊर्ध्व घटक तय करता है</td></tr>\n<tr><td>अधिकतम ऊँचाई (H)</td><td>u² sin²θ / 2g</td><td>θ = 90° पर अधिकतम</td></tr>\n<tr><td>परास (R)</td><td>u² sin2θ / g</td><td>θ = 45° पर अधिकतम ⭐</td></tr>\n<tr><td>पथ</td><td>y = x tanθ − gx²/(2u² cos²θ)</td><td>परवलय!</td></tr>\n</table>\n<ul>\n<li><b>पूरक कोण:</b> θ और (90° − θ) समान परास (30° और 60° समान!)।</li>\n<li>उच्चतम बिंदु पर वेग = u cosθ (केवल क्षैतिज), शून्य नहीं! ⭐</li>\n<li><b>क्षैतिज प्रक्षेपण (ऊँचाई h से):</b> T = √(2h/g), R = u√(2h/g)।</li>\n</ul>\n<p class=\"small-note\">💡 क्रिकेट का लॉफ्टेड शॉट — क्षैतिज चाल नहीं रुकती, गुरुत्व केवल ऊर्ध्व गति संभालता है।</p>"
   },
   {
    "h": "4️⃣ एकसमान वृत्तीय गति — घूमना भी त्वरण है",
    "body": "<p>वृत्त में नियत चाल से गति भी त्वरित गति है — क्योंकि दिशा बदल रही है!</p>\n<ul>\n<li><b>अभिकेंद्रीय त्वरण ⭐:</b> a = v²/r = ω²r — सदैव केंद्र की ओर। यह कोई नया बल नहीं, परिणामी त्वरण है।</li>\n<li><b>कोणीय चाल:</b> ω = 2π/T = 2πf • v = ωr।</li>\n<li>उदाहरण: पंखे का ब्लेड, मोड़ पर कार (घर्षण अभिकेंद्रीय बल देता है), उपग्रह (गुरुत्व देता है)।</li>\n<li>वेग स्पर्श रेखा के अनुदिश, त्वरण केंद्र की ओर — दोनों परस्पर लंबवत ⭐।</li>\n</ul>\n<p class=\"small-note\">🎯 \"एकसमान वृत्तीय\" में चाल नियत, वेग नहीं — इसलिए त्वरण शून्य नहीं!</p>"
   },
   {
    "h": "5️⃣ सापेक्ष वेग — 2D में",
    "body": "<p>v<sub>AB</sub> = v<sub>A</sub> − v<sub>B</sub> — अब सदिशों के साथ। प्रमुख उदाहरण:</p>\n<ul>\n<li><b>नदी-नाव ⭐:</b> नाव का वेग (स्थिर जल में) + धारा का वेग = भूमि सापेक्ष वेग। न्यूनतम पथ: थोड़ा धारा-प्रतिकूल लक्ष्य। न्यूनतम समय: सीधे सामने किनारे की ओर।</li>\n<li><b>वर्षा-मनुष्य:</b> दौड़ने पर वर्षा तिरछी दिखती है — छाता सापेक्ष वेग की दिशा में रखें।</li>\n</ul>\n<p class=\"small-note\">💡 चलती पट्टी (walkway) पर चलना — आपकी चाल + पट्टी की चाल = वास्तविक चाल।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Vectors — Quantities with Direction",
    "body": "<p>In 1D, +/− was enough, but 2D needs <b>vectors</b> — magnitude plus direction. Displacement, velocity, acceleration and force are vectors; distance, speed, time and mass are scalars.</p>\n<ul>\n<li><b>Addition:</b> triangle/parallelogram law — place A and B head to tail, resultant R = A + B. Magnitude: |R| = √(A² + B² + 2AB cosθ).</li>\n<li><b>Resolution (components) ⭐:</b> split A into x/y: A<sub>x</sub> = A cosθ, A<sub>y</sub> = A sinθ. Back: A = √(A<sub>x</sub>² + A<sub>y</sub>²), tanθ = A<sub>y</sub>/A<sub>x</sub>. Components make addition easy: resultant component = sum of components.</li>\n<li><b>Unit vectors:</b> î, ĵ, k̂ — direction only (magnitude 1). A = A<sub>x</sub>î + A<sub>y</sub>ĵ.</li>\n<li><b>Special cases:</b> θ=0° → R = A+B; θ=180° → R = |A−B|; θ=90° → R = √(A²+B²).</li>\n</ul>\n<p class=\"small-note\">💡 Think: vector addition is the straight line, not the odometer — 3 km east + 4 km north = 5 km straight (3-4-5 triangle!).</p>"
   },
   {
    "h": "2️⃣ Motion in 2D — Position, Velocity, Acceleration (Vector Form)",
    "body": "<p>To describe motion in a plane, everything goes vector:</p>\n<ul>\n<li><b>Position vector:</b> r = xî + yĵ. <b>Displacement:</b> Δr = r₂ − r₁.</li>\n<li><b>Average velocity:</b> Δr/Δt • <b>instantaneous:</b> v = dr/dt — always along the TANGENT to the path.</li>\n<li><b>Acceleration:</b> a = dv/dt. In 2D, merely changing the direction of velocity is acceleration — even at constant speed! ⭐</li>\n<li><b>Independence of motions ⭐:</b> x and y motions are fully independent — time is common to both. This is what makes projectile problems solvable!</li>\n</ul>\n<p class=\"small-note\">🎯 Key idea: 2D motion = two 1D motions happening together. Solve each separately.</p>"
   },
   {
    "h": "3️⃣ Projectile Motion — Throw It, Get a Parabola ⭐",
    "body": "<p>A projectile moves under gravity alone (a<sub>x</sub> = 0, a<sub>y</sub> = −g). With initial velocity u at angle θ: u<sub>x</sub> = u cosθ (stays constant!), u<sub>y</sub> = u sinθ (changed by g).</p>\n<table class=\"tbl\">\n<tr><th>Quantity</th><th>Formula</th><th>Remember</th></tr>\n<tr><td>Time of flight (T)</td><td>2u sinθ / g</td><td>decided by the vertical part only</td></tr>\n<tr><td>Max height (H)</td><td>u² sin²θ / 2g</td><td>maximum at θ = 90°</td></tr>\n<tr><td>Range (R)</td><td>u² sin2θ / g</td><td>maximum at θ = 45° ⭐</td></tr>\n<tr><td>Trajectory</td><td>y = x tanθ − gx²/(2u² cos²θ)</td><td>a parabola!</td></tr>\n</table>\n<ul>\n<li><b>Complementary angles:</b> θ and (90° − θ) give the same range (30° and 60° match!).</li>\n<li>At the highest point, velocity = u cosθ (horizontal only) — NOT zero! ⭐ (exam trap)</li>\n<li><b>Horizontal projection (from height h):</b> T = √(2h/g), R = u√(2h/g).</li>\n</ul>\n<p class=\"small-note\">💡 Think of a lofted cricket shot — the horizontal speed never stops (without air); gravity only handles the up-down part.</p>"
   },
   {
    "h": "4️⃣ Uniform Circular Motion — Turning Is Accelerating",
    "body": "<p>Motion in a circle at CONSTANT speed is still accelerated motion — because the direction keeps changing!</p>\n<ul>\n<li><b>Centripetal (radial) acceleration ⭐:</b> a = v²/r = ω²r — always toward the CENTER. It is the resultant acceleration, not a new force.</li>\n<li><b>Angular speed:</b> ω = 2π/T = 2πf • v = ωr. T = time of one revolution, f = revolutions per second.</li>\n<li>Examples: fan blade, merry-go-round, car on a circular turn (friction provides the centripetal force), satellite in orbit (gravity does).</li>\n<li>Velocity is along the tangent, acceleration toward the center — the two are PERPENDICULAR ⭐.</li>\n</ul>\n<p class=\"small-note\">🎯 Remember: in \"uniform circular\" motion, speed is constant but velocity is NOT — so acceleration is not zero!</p>"
   },
   {
    "h": "5️⃣ Relative Velocity — In 2D",
    "body": "<p>v<sub>AB</sub> = v<sub>A</sub> − v<sub>B</sub> — now with vectors. Classic cases:</p>\n<ul>\n<li><b>River-boat ⭐:</b> boat's velocity (in still water) + river's velocity = ground velocity. Shortest path: aim slightly upstream. Shortest time: aim straight across and accept downstream drift.</li>\n<li><b>Rain-man:</b> rain appears tilted when you run — hold the umbrella along the relative velocity!</li>\n<li>Wind-aeroplane problems use the same idea.</li>\n</ul>\n<p class=\"small-note\">💡 Think of walking on a moving walkway — your speed + walkway speed = your real ground speed.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Vectors",
    "items": [
     "|R| = √(A² + B² + 2AB cosθ)",
     "Components: A cosθ (x), A sinθ (y)",
     "θ=90° → R = √(A²+B²)"
    ]
   },
   {
    "h": "2D Motion",
    "items": [
     "v path ke tangent along",
     "Speed constant ho tab bhi acceleration ho sakta hai (direction change)",
     "x aur y motions independent ⭐"
    ]
   },
   {
    "h": "Projectile ⭐",
    "items": [
     "R = u² sin2θ/g (max at 45°)",
     "H = u² sin²θ/2g",
     "T = 2u sinθ/g",
     "Top pe v = u cosθ ≠ 0",
     "θ aur 90−θ same range"
    ]
   },
   {
    "h": "Circular Motion",
    "items": [
     "a = v²/r = ω²r (center ki taraf)",
     "v = ωr, ω = 2π/T",
     "Velocity ⊥ acceleration"
    ]
   },
   {
    "h": "Relative Velocity",
    "items": [
     "v_AB = v_A − v_B (vectors)",
     "River-boat: shortest time = seedha across",
     "Rain tilted dikhti hai bhaagne pe"
    ]
   }
  ],
  "hi": [
   {
    "h": "सदिश",
    "items": [
     "|R| = √(A² + B² + 2AB cosθ)",
     "घटक: A cosθ (x), A sinθ (y)",
     "θ=90° → R = √(A²+B²)"
    ]
   },
   {
    "h": "2D गति",
    "items": [
     "v स्पर्श रेखा के अनुदिश",
     "चाल नियत हो तब भी त्वरण संभव",
     "x व y गतियाँ स्वतंत्र ⭐"
    ]
   },
   {
    "h": "प्रक्षेप्य ⭐",
    "items": [
     "R = u² sin2θ/g (45° पर अधिकतम)",
     "H = u² sin²θ/2g",
     "T = 2u sinθ/g",
     "शीर्ष पर v = u cosθ ≠ 0"
    ]
   },
   {
    "h": "वृत्तीय गति",
    "items": [
     "a = v²/r = ω²r (केंद्र की ओर)",
     "v = ωr, ω = 2π/T",
     "वेग ⊥ त्वरण"
    ]
   },
   {
    "h": "सापेक्ष वेग",
    "items": [
     "v_AB = v_A − v_B (सदिश)",
     "नदी-नाव: न्यूनतम समय = सीधे पार",
     "दौड़ने पर वर्षा तिरछी"
    ]
   }
  ],
  "en": [
   {
    "h": "Vectors",
    "items": [
     "|R| = √(A² + B² + 2AB cosθ)",
     "Components: A cosθ (x), A sinθ (y)",
     "θ=90° → R = √(A²+B²)"
    ]
   },
   {
    "h": "2D Motion",
    "items": [
     "v along the tangent",
     "Acceleration possible at constant speed (direction change)",
     "x and y motions independent ⭐"
    ]
   },
   {
    "h": "Projectile ⭐",
    "items": [
     "R = u² sin2θ/g (max at 45°)",
     "H = u² sin²θ/2g",
     "T = 2u sinθ/g",
     "At top: v = u cosθ ≠ 0",
     "θ and 90−θ give same range"
    ]
   },
   {
    "h": "Circular Motion",
    "items": [
     "a = v²/r = ω²r (toward center)",
     "v = ωr, ω = 2π/T",
     "Velocity ⊥ acceleration"
    ]
   },
   {
    "h": "Relative Velocity",
    "items": [
     "v_AB = v_A − v_B (vectors)",
     "River-boat: shortest time = straight across",
     "Rain tilts when you run"
    ]
   }
  ]
 },
 "practice": [
  [
   "Vector A = 3 units east, B = 4 units north. Resultant ka magnitude aur direction?",
   "θ=90° → R = √(9+16) = <b>5 units</b>. Direction: tanθ = 4/3 → θ = 53° north of east."
  ],
  [
   "Do vectors 5 N aur 5 N ke beech angle 60° hai. Resultant?",
   "R = √(25 + 25 + 2×25×cos60°) = √(50 + 25) = √75 = <b>5√3 N ≈ 8.66 N</b>."
  ],
  [
   "Projectile 50 m/s se 30° pe phenka (g = 10). Time of flight aur range?",
   "T = 2×50×sin30°/10 = <b>5 s</b>. R = 50²×sin60°/10 = 250×(√3/2) = <b>216.5 m ≈ 125√3 m</b>."
  ],
  [
   "Same initial speed se 30° aur 60° pe phenke projectiles ki range ka relation?",
   "<b>Same range</b> — complementary angles (sin2×30° = sin60° = sin2×60°). Heights alag hongi!"
  ],
  [
   "Projectile ke highest point pe uski speed ka minimum value kya hoti hai (u, θ diya ho)?",
   "<b>u cosθ</b> — vertical component zero, horizontal unchanged. Speed ZERO nahi hoti!"
  ],
  [
   "Ek stone 20 m/s se horizontally 80 m ki building se phenka (g = 10). Zameen tak time aur range?",
   "T = √(2h/g) = √(160/10) = <b>4 s</b>. R = u×T = 20×4 = <b>80 m</b>."
  ],
  [
   "Car 10 m radius ke circular turn pe 36 km/h se. Centripetal acceleration?",
   "v = 10 m/s. a = v²/r = 100/10 = <b>10 m/s²</b> (center ki taraf)."
  ],
  [
   "Fan 600 rpm pe ghoomta hai, blade tip 0.5 m radius pe. ω aur tip speed?",
   "ω = 2π×(600/60) = 20π = <b>62.8 rad/s</b>. v = ωr = 20π×0.5 = <b>31.4 m/s</b>."
  ],
  [
   "Nadi 3 km/h se behti hai, boat still water me 5 km/h. Shortest TIME me cross karne ke liye boat kahan aim kare?",
   "<b>Seedha opposite bank ki taraf</b> (perpendicular). Crossing time = width/5; boat 3 km/h se downstream drift hogi."
  ],
  [
   "Uniform circular motion me velocity aur acceleration ke beech angle?",
   "<b>90°</b> — velocity tangent pe, acceleration center ki taraf. Isliye speed nahi badhti, sirf direction badalti hai."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/physics/ch-4/",
  "title": "Laws of Motion"
 }
}

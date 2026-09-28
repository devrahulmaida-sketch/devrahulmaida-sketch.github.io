# Class 11 Physics, Chapter 13 - Oscillations
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 13,
 "title_en": "Oscillations",
 "title_hi": "दोलन",
 "tagline": "SHM, pendulum aur resonance — jhoolne ka pura physics",
 "jee": "HIGH",
 "meta_desc": "Class 11 Physics Chapter 13: Oscillations — long + short notes in Hindi, English, Hinglish. Simple harmonic motion, spring-mass, pendulum, energy in SHM, damped and forced oscillations, resonance.",
  "video": {
  "youtube": "TwK7W6Wh2i8",
  "dur": "1 min 20 sec"
 },
 "card_tag": "SHM, pendulum aur resonance — jhoolne ka pura physics",
 "card_topics": [
  "🔄 SHM + equations",
  "⚡ Velocity, acceleration, energy",
  "🕰️ Pendulum T = 2π√(L/g)",
  "📳 Resonance"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Periodic Motion aur SHM — Jhoolne Ka Physics",
    "body": "<ul>\n<li><b>Periodic motion:</b> jo motion fixed time baad repeat ho — clock ki needle, Earth's orbit. Us time ko <b>period (T)</b> kehte hain.</li>\n<li><b>Oscillatory (to-and-fro) motion:</b> mean position ke dono taraf repeat — pendulum, spring. Har oscillatory periodic hai, har periodic oscillatory nahi! ⭐</li>\n<li><b>Frequency:</b> ν = 1/T (Hz); <b>angular frequency:</b> ω = 2πν = 2π/T (rad/s).</li>\n<li><b>Simple Harmonic Motion (SHM) ⭐:</b> jab restoring force displacement ke proportional aur OPPOSITE ho — F = −kx. Acceleration a = −ω²x.</li>\n<li><b>SHM ka equation:</b> x(t) = A sin(ωt + φ) — A = amplitude (max displacement), φ = phase constant (starting point batata hai).</li>\n<li>Examples: spring-mass, pendulum (chhote angle), liquid in U-tube, floating cylinder — sab SHM!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: SHM = perfect jhoola — jitna door kheencho, utna zor se wapas kheenchi jaati hai. Mean position pe speed max, ends pe zero!</p>"
   },
   {
    "h": "2️⃣ SHM Ki Velocity aur Acceleration ⭐",
    "body": "<ul>\n<li><b>Displacement:</b> x = A sin(ωt + φ)</li>\n<li><b>Velocity:</b> v = Aω cos(ωt + φ) = ±ω√(A² − x²) — <b>mean position (x=0) pe max = Aω</b>, extremes pe zero. ⭐</li>\n<li><b>Acceleration:</b> a = −ω²A sin(ωt + φ) = <b>−ω²x</b> — extremes pe max (ω²A), mean pe zero. Hamesha mean ki taraf point!</li>\n<li><b>Phase relationships ⭐:</b> velocity displacement se 90° aage, acceleration 180° opposite (displacement ke).</li>\n<li><b>Uniform circular motion ka projection = SHM!</b> Circle pe chalta particle ki shadow diameter pe SHM karti hai — ω circle ki angular velocity hi hai.</li>\n<li><b>ω ka formula:</b> spring ke liye ω = √(k/m) → <b>T = 2π√(m/k)</b> ⭐ (mass badhao, slow; stiff spring, fast).</li>\n</ul>\n<p class=\"small-note\">🎯 Yaad rakho: a = −ω²x SHM ki PEHCHAAN hai — kisi bhi motion me ye relation dikhe, wo SHM hai!</p>"
   },
   {
    "h": "3️⃣ Energy in SHM — KE aur PE Ka Jhoola ⭐",
    "body": "<ul>\n<li><b>Kinetic energy:</b> KE = ½mv² = ½mω²(A² − x²) — mean pe max (½mω²A²), extremes pe zero.</li>\n<li><b>Potential energy:</b> PE = ½kx² = ½mω²x² — extremes pe max, mean pe zero.</li>\n<li><b>Total energy ⭐:</b> E = KE + PE = ½mω²A² = ½kA² — <b>CONSTANT</b>! Energy bas KE↔PE me convert hoti rehti hai.</li>\n<li>E ∝ A² — amplitude double, energy 4 guna! ⭐</li>\n<li><b>Average values:</b> time-average KE = time-average PE = E/2 (ek poore cycle me barabar share!).</li>\n<li>Graph: PE parabola (x²), KE inverted parabola — dono ka sum flat line.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: jhoole pe energy ka ping-pong — sabse neeche (mean) poori KE, sabse upar (extreme) poori PE, beech me mix!</p>"
   },
   {
    "h": "4️⃣ Simple Pendulum aur Other Oscillators ⭐",
    "body": "<ul>\n<li><b>Simple pendulum:</b> chhote oscillations ke liye <b>T = 2π√(L/g)</b> ⭐ — sirf length aur g pe depend, mass pe NAHI!</li>\n<li><b>Seconds pendulum:</b> T = 2 sec wala — L ≈ 1 m (exactly 99.4 cm).</li>\n<li><b>Applications:</b> g measure karna (T aur L se!), pendulum clocks — lift me ya pahaad pe g change to clock ki timing bhi change!</li>\n<li><b>Spring combinations:</b> series me 1/k_eff = 1/k₁ + 1/k₂ (soft ho jaati hai), parallel me k_eff = k₁ + k₂ (stiff).</li>\n<li><b>Spring kaatne pe:</b> k ∝ 1/length — aadhi kaato to k double, T → T/√2!</li>\n<li><b>Vertical spring:</b> gravity sirf mean position shift karti hai, T same rehta hai (2π√(m/k))! ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 Exam hack: pendulum = √(L/g), spring = √(m/k) — dono 2π ke saath. g ghate (lift upar accelerate) to T badhta hai!</p>"
   },
   {
    "h": "5️⃣ Damped, Forced Oscillations aur Resonance",
    "body": "<ul>\n<li><b>Free oscillation:</b> ek baar disturb karo, natural frequency pe oscillate karta rahe (ideal me forever).</li>\n<li><b>Damped oscillation:</b> friction/air resistance se amplitude exponentially GHATTA hai — A(t) = A₀e^(−bt/2m). Energy bhi decay. (Real world: har jhoola eventually rukta hai!)</li>\n<li><b>Forced oscillation:</b> bahar se periodic force lagao — system FORCE ki frequency pe oscillate karta hai (apni natural pe nahi!).</li>\n<li><b>Resonance ⭐:</b> jab driving frequency = natural frequency → amplitude MAXIMUM. Isliye: troops bridge pe march break karti hain, swing ko perfect timing pe dhakka, radio tuning, microwave me water molecules!</li>\n<li>Sharp resonance = kam damping; heavy damping = flat, wide resonance.</li>\n</ul>\n<p class=\"small-note\">💡 Resonance = perfect timing ka dhakka — chhota chhota push, right rhythm me, giant swing! (1940 Tacoma bridge collapse bhi resonance se hi hua.)</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ आवर्ती गति और सरल आवर्त गति — झूलने का भौतिकी",
    "body": "<ul>\n<li><b>आवर्ती गति:</b> निश्चित समय बाद दोहरने वाली गति — घड़ी की सुई। समय = <b>आवर्तकाल (T)</b>।</li>\n<li><b>दोलनी गति:</b> माध्य स्थिति के दोनों ओर आवृत्ति — झूला, स्प्रिंग। हर दोलनी आवर्ती है, हर आवर्ती दोलनी नहीं! ⭐</li>\n<li><b>आवृत्ति:</b> ν = 1/T (Hz); <b>कोणीय आवृत्ति:</b> ω = 2πν।</li>\n<li><b>सरल आवर्त गति (SHM) ⭐:</b> प्रत्यानयन बल विस्थापन के समानुपाती और विपरीत — F = −kx। त्वरण a = −ω²x।</li>\n<li><b>SHM समीकरण:</b> x(t) = A sin(ωt + φ) — A = आयाम, φ = कला स्थिरांक।</li>\n</ul>\n<p class=\"small-note\">💡 SHM = आदर्श झूला — जितना दूर खींचो, उतना ज़ोर से वापस। माध्य पर चाल अधिकतम, सिरों पर शून्य!</p>"
   },
   {
    "h": "2️⃣ SHM का वेग और त्वरण ⭐",
    "body": "<ul>\n<li><b>विस्थापन:</b> x = A sin(ωt + φ)</li>\n<li><b>वेग:</b> v = ±ω√(A² − x²) — <b>माध्य स्थिति पर अधिकतम = Aω</b>, चरम पर शून्य। ⭐</li>\n<li><b>त्वरण:</b> a = <b>−ω²x</b> — चरम पर अधिकतम, माध्य पर शून्य। सदैव माध्य की ओर!</li>\n<li><b>कला संबंध ⭐:</b> वेग विस्थापन से 90° आगे, त्वरण 180° विपरीत।</li>\n<li><b>एकसमान वृत्तीय गति का प्रक्षेप = SHM!</b> ω वही कोणीय वेग है।</li>\n<li><b>स्प्रिंग के लिए:</b> ω = √(k/m) → <b>T = 2π√(m/k)</b> ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 a = −ω²x SHM की पहचान है — यह संबंध दिखे तो SHM!</p>"
   },
   {
    "h": "3️⃣ SHM में ऊर्जा — KE और PE का झूला ⭐",
    "body": "<ul>\n<li><b>गतिज ऊर्जा:</b> KE = ½mω²(A² − x²) — माध्य पर अधिकतम, चरम पर शून्य।</li>\n<li><b>स्थितिज ऊर्जा:</b> PE = ½mω²x² — चरम पर अधिकतम, माध्य पर शून्य।</li>\n<li><b>कुल ऊर्जा ⭐:</b> E = ½mω²A² = ½kA² — <b>नियत</b>! ऊर्जा केवल KE↔PE में बदलती रहती है।</li>\n<li>E ∝ A² — आयाम दोगुना, ऊर्जा चार गुना! ⭐</li>\n<li><b>औसत मान:</b> समय-औसत KE = PE = E/2 (पूरे चक्र में बराबर हिस्सा!)।</li>\n</ul>\n<p class=\"small-note\">💡 ऊर्जा का पिंग-पॉन्ग — माध्य पर पूरी KE, चरम पर पूरी PE, बीच में मिश्रण!</p>"
   },
   {
    "h": "4️⃣ सरल लोलक और अन्य दोलक ⭐",
    "body": "<ul>\n<li><b>सरल लोलक:</b> छोटे दोलनों के लिए <b>T = 2π√(L/g)</b> ⭐ — द्रव्यमान पर निर्भर नहीं!</li>\n<li><b>सेकंड लोलक:</b> T = 2 sec, L ≈ 1 m।</li>\n<li><b>उपयोग:</b> g मापना, पेंडुलम घड़ियां — पहाड़ पर g कम तो घड़ी धीमी!</li>\n<li><b>स्प्रिंग संयोजन:</b> श्रेणी में 1/k_eff = 1/k₁ + 1/k₂, समांतर में k_eff = k₁ + k₂।</li>\n<li><b>स्प्रिंग काटने पर:</b> k ∝ 1/लंबाई — आधी काटो तो k दोगुना, T → T/√2!</li>\n<li><b>ऊर्ध्व स्प्रिंग:</b> गुरुत्व केवल माध्य स्थिति खिसकाता है, T वही रहता है! ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 लोलक = √(L/g), स्प्रिंग = √(m/k) — दोनों 2π के साथ।</p>"
   },
   {
    "h": "5️⃣ अवमंदित, प्रणोदित दोलन और अनुनाद",
    "body": "<ul>\n<li><b>मुक्त दोलन:</b> एक बार विचलित करो, प्राकृतिक आवृत्ति पर दोलन।</li>\n<li><b>अवमंदित दोलन:</b> घर्षण से आयाम चरघातांकी घटता है — A(t) = A₀e^(−bt/2m)।</li>\n<li><b>प्रणोदित दोलन:</b> बाहरी आवर्ती बल लगाओ — निकाय बल की आवृत्ति पर दोलन करता है।</li>\n<li><b>अनुनाद ⭐:</b> चालक आवृत्ति = प्राकृतिक आवृत्ति → आयाम अधिकतम। उदाहरण: झूले को सही समय पर धक्का, रेडियो ट्यूनिंग, पुल पर कदमताल बंद!</li>\n<li>कम अवमंदन = तीखा अनुनाद; अधिक अवमंदन = चपटा, चौड़ा।</li>\n</ul>\n<p class=\"small-note\">💡 अनुनाद = सही लय का धक्का — छोटे-छोटे धक्के, सही रिदम में, विशाल झूला!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Periodic Motion and SHM — The Physics of Swinging",
    "body": "<ul>\n<li><b>Periodic motion:</b> motion that repeats after a fixed time — the hands of a clock, Earth's orbit. That time is the <b>period (T)</b>.</li>\n<li><b>Oscillatory motion:</b> to-and-fro about a mean position — a pendulum, a spring. Every oscillatory motion is periodic, but not every periodic motion is oscillatory! ⭐</li>\n<li><b>Frequency:</b> ν = 1/T (Hz); <b>angular frequency:</b> ω = 2πν = 2π/T (rad/s).</li>\n<li><b>Simple Harmonic Motion (SHM) ⭐:</b> when the restoring force is proportional to displacement and OPPOSITE — F = −kx. Acceleration a = −ω²x.</li>\n<li><b>The SHM equation:</b> x(t) = A sin(ωt + φ) — A = amplitude, φ = phase constant (tells where it starts).</li>\n<li>Examples: spring-mass, pendulum (small angles), liquid in a U-tube — all SHM!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: SHM is a perfect swing — the farther you pull, the harder it pulls back. Speed is maximum at the mean, zero at the ends!</p>"
   },
   {
    "h": "2️⃣ Velocity and Acceleration in SHM ⭐",
    "body": "<ul>\n<li><b>Displacement:</b> x = A sin(ωt + φ)</li>\n<li><b>Velocity:</b> v = Aω cos(ωt + φ) = ±ω√(A² − x²) — <b>maximum = Aω at the mean</b>, zero at the extremes. ⭐</li>\n<li><b>Acceleration:</b> a = −ω²A sin(ωt + φ) = <b>−ω²x</b> — maximum (ω²A) at the extremes, zero at the mean. Always points toward the mean!</li>\n<li><b>Phase relationships ⭐:</b> velocity leads displacement by 90°, acceleration is 180° opposite to displacement.</li>\n<li><b>The projection of uniform circular motion is SHM!</b> The shadow of a particle on a circle sweeps SHM along the diameter — ω is the same angular velocity.</li>\n<li><b>For a spring:</b> ω = √(k/m) → <b>T = 2π√(m/k)</b> ⭐ (more mass, slower; stiffer spring, faster).</li>\n</ul>\n<p class=\"small-note\">🎯 Remember: a = −ω²x is the SIGNATURE of SHM — spot this relation and the motion is SHM!</p>"
   },
   {
    "h": "3️⃣ Energy in SHM — The Seesaw of KE and PE ⭐",
    "body": "<ul>\n<li><b>Kinetic energy:</b> KE = ½mv² = ½mω²(A² − x²) — maximum at the mean (½mω²A²), zero at the extremes.</li>\n<li><b>Potential energy:</b> PE = ½kx² = ½mω²x² — maximum at the extremes, zero at the mean.</li>\n<li><b>Total energy ⭐:</b> E = KE + PE = ½mω²A² = ½kA² — <b>CONSTANT</b>! Energy just keeps converting between KE and PE.</li>\n<li>E ∝ A² — double the amplitude, four times the energy! ⭐</li>\n<li><b>Average values:</b> time-average KE = time-average PE = E/2 (an equal split over a full cycle!).</li>\n<li>Graph: PE is a parabola (x²), KE an inverted parabola — their sum is a flat line.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: on a swing, energy plays ping-pong — all KE at the bottom, all PE at the top, a mix in between!</p>"
   },
   {
    "h": "4️⃣ The Simple Pendulum and Other Oscillators ⭐",
    "body": "<ul>\n<li><b>Simple pendulum:</b> for small oscillations <b>T = 2π√(L/g)</b> ⭐ — depends only on length and g, NOT on mass!</li>\n<li><b>Seconds pendulum:</b> the one with T = 2 sec — L ≈ 1 m (exactly 99.4 cm).</li>\n<li><b>Applications:</b> measuring g (from T and L!), pendulum clocks — g changes on a hill or in a lift and the clock's timing changes too!</li>\n<li><b>Spring combinations:</b> in series 1/k_eff = 1/k₁ + 1/k₂ (softer), in parallel k_eff = k₁ + k₂ (stiffer).</li>\n<li><b>Cutting a spring:</b> k ∝ 1/length — cut in half, k doubles, T → T/√2!</li>\n<li><b>Vertical spring:</b> gravity only shifts the mean position; T stays 2π√(m/k)! ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 Exam hack: pendulum = √(L/g), spring = √(m/k) — both with 2π. g drops (lift accelerating up... wait, down!) and T rises!</p>"
   },
   {
    "h": "5️⃣ Damped, Forced Oscillations and Resonance",
    "body": "<ul>\n<li><b>Free oscillation:</b> disturb once and it oscillates at its natural frequency (forever, ideally).</li>\n<li><b>Damped oscillation:</b> friction/air resistance makes the amplitude decay exponentially — A(t) = A₀e^(−bt/2m). Energy decays too. (In the real world every swing stops eventually!)</li>\n<li><b>Forced oscillation:</b> apply an external periodic force — the system oscillates at the FORCE's frequency, not its own!</li>\n<li><b>Resonance ⭐:</b> when driving frequency = natural frequency → amplitude is MAXIMUM. That is why soldiers break step on bridges, why you push a swing at the perfect moment, radio tuning, microwaves exciting water!</li>\n<li>Sharp resonance = light damping; heavy damping = a flat, wide peak.</li>\n</ul>\n<p class=\"small-note\">💡 Resonance = perfectly timed pushes — small pushes in the right rhythm build a giant swing! (The 1940 Tacoma bridge collapse was resonance too.)</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "SHM Basics ⭐",
    "items": [
     "F = −kx, a = −ω²x",
     "x = A sin(ωt + φ)",
     "ω = 2π/T, ν = 1/T"
    ]
   },
   {
    "h": "Velocity/Accel",
    "items": [
     "v = ±ω√(A²−x²), max Aω mean pe",
     "a max = ω²A extremes pe",
     "Circle ka projection = SHM"
    ]
   },
   {
    "h": "Energy ⭐",
    "items": [
     "E = ½kA² = constant",
     "KE max mean pe, PE max ends pe",
     "E ∝ A²"
    ]
   },
   {
    "h": "Pendulum/Spring ⭐",
    "items": [
     "T = 2π√(L/g) — mass independent",
     "T = 2π√(m/k)",
     "Spring series: 1/k₁+1/k₂"
    ]
   },
   {
    "h": "Resonance",
    "items": [
     "Damped: A = A₀e^(−bt/2m)",
     "Forced: driver ki frequency",
     "Driving = natural → max amplitude"
    ]
   }
  ],
  "hi": [
   {
    "h": "SHM मूल ⭐",
    "items": [
     "F = −kx, a = −ω²x",
     "x = A sin(ωt+φ)",
     "ω = 2π/T"
    ]
   },
   {
    "h": "वेग/त्वरण",
    "items": [
     "v अधिकतम Aω माध्य पर",
     "a अधिकतम ω²A चरम पर",
     "वृत्त का प्रक्षेप = SHM"
    ]
   },
   {
    "h": "ऊर्जा ⭐",
    "items": [
     "E = ½kA² = नियत",
     "KE माध्य पर, PE चरम पर",
     "E ∝ A²"
    ]
   },
   {
    "h": "लोलक/स्प्रिंग ⭐",
    "items": [
     "T = 2π√(L/g)",
     "T = 2π√(m/k)",
     "श्रेणी: 1/k₁+1/k₂"
    ]
   },
   {
    "h": "अनुनाद",
    "items": [
     "अवमंदित: A = A₀e^(−bt/2m)",
     "प्रणोदित: चालक की आवृत्ति",
     "आवृत्तियां बराबर → अधिकतम आयाम"
    ]
   }
  ],
  "en": [
   {
    "h": "SHM Basics ⭐",
    "items": [
     "F = −kx, a = −ω²x",
     "x = A sin(ωt + φ)",
     "ω = 2π/T, ν = 1/T"
    ]
   },
   {
    "h": "Velocity/Accel",
    "items": [
     "v = ±ω√(A²−x²), max Aω at mean",
     "a max = ω²A at extremes",
     "Circle's projection = SHM"
    ]
   },
   {
    "h": "Energy ⭐",
    "items": [
     "E = ½kA² = constant",
     "KE max at mean, PE max at ends",
     "E ∝ A²"
    ]
   },
   {
    "h": "Pendulum/Spring ⭐",
    "items": [
     "T = 2π√(L/g) — mass independent",
     "T = 2π√(m/k)",
     "Spring series: 1/k₁+1/k₂"
    ]
   },
   {
    "h": "Resonance",
    "items": [
     "Damped: A = A₀e^(−bt/2m)",
     "Forced: driver's frequency",
     "Driving = natural → max amplitude"
    ]
   }
  ]
 },
 "practice": [
  [
   "Spring (k = 100 N/m) pe 0.25 kg mass. Time period?",
   "T = 2π√(m/k) = 2π√(0.25/100) = 2π×0.05 = <b>0.314 s</b>."
  ],
  [
   "SHM ka signature relation kya hai?",
   "a = <b>−ω²x</b> — acceleration displacement ke proportional aur opposite (F = −kx)."
  ],
  [
   "Amplitude 5 cm, ω = 10 rad/s. Maximum velocity?",
   "v_max = Aω = 0.05×10 = <b>0.5 m/s</b> (mean position pe)."
  ],
  [
   "Mean position pe oscillator ki energy kis form me?",
   "Poori <b>kinetic</b> (PE = 0 wahan). Total E = ½kA² har jagah same."
  ],
  [
   "Amplitude double kar diya. Total energy?",
   "E ∝ A² → <b>4 guna</b>."
  ],
  [
   "Pendulum ki length 4 guna kar do. Period?",
   "T ∝ √L → √4 = <b>double</b> ho jaayega."
  ],
  [
   "Pendulum ko moon pe le jaayein (g_moon = g/6). Period?",
   "T ∝ 1/√g → T_moon = T√6 ≈ <b>2.45 T</b> — slow oscillation!"
  ],
  [
   "Do springs (k aur 2k) series me. Effective k?",
   "1/k_eff = 1/k + 1/2k = 3/2k → k_eff = <b>2k/3</b> (series = softer)."
  ],
  [
   "Swing ko dhakka lagate ho aur amplitude badhta jaata hai. Ye kya hai?",
   "<b>Resonance</b> — driving frequency (aapke dhakke) natural frequency se match kar gayi."
  ],
  [
   "Damped oscillator me amplitude 1/4 reh gaya. Energy kitni?",
   "E ∝ A² → (1/4)² = <b>1/16</b> — energy aur bhi tezi se decay karti hai!"
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/physics/ch-14/",
  "title": "Waves"
 }
}

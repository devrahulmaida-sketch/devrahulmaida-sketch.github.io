# Class 12 Physics, Chapter 7 - Alternating Current
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 7,
 "title_en": "Alternating Current",
 "title_hi": "प्रत्यावर्ती धारा",
 "tagline": "AC ka rhythm: RMS, LCR, resonance aur transformer",
 "jee": "HIGH",
 "meta_desc": "Class 12 Physics Chapter 7: Alternating Current. Long and short notes in Hinglish, Hindi and English, with 10 solved practice questions.",
 "video": None,
 "card_tag": "AC ka rhythm: RMS, LCR, resonance aur transformer",
 "card_topics": [
  "〰️ AC + RMS",
  "🌀 Reactance + impedance",
  "🎯 Resonance + power factor",
  "🔌 Transformer"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ AC signal aur RMS ⭐",
    "body": "<ul>\n<li><b>Alternating current:</b> i(t)=I₀ sin ωt; har half-cycle me direction reverse. ω=2πf, India me f=50 Hz.</li>\n<li><b>RMS ⭐:</b> I_rms=I₀/√2, V_rms=V₀/√2; 230 V household AC RMS hota hai, peak 230√2 V.</li>\n<li><b>Average:</b> pure cycle me sinusoidal current ka average zero; half-cycle average 2I₀/π.</li>\n</ul>\n<p class=\"small-note\">💡 RMS woh DC value hai jo same resistor me utni hi heating kare.</p>"
   },
   {
    "h": "2️⃣ R, L aur C ka AC response ⭐",
    "body": "<ul>\n<li><b>Resistor:</b> V aur I same phase me; impedance R, average power V_rms I_rms.</li>\n<li><b>Inductor ⭐:</b> X_L=ωL; current voltage se 90° peeche (lag). Frequency badhao to opposition badhta hai.</li>\n<li><b>Capacitor ⭐:</b> X_C=1/(ωC); current voltage se 90° aage (lead). Frequency badhao to opposition ghatta hai.</li>\n</ul>\n<p class=\"small-note\">🎯 ELI the ICE man: E leads I in L; I leads E in C.</p>"
   },
   {
    "h": "3️⃣ Series LCR aur resonance ⭐⭐",
    "body": "<ul>\n<li><b>Phasor:</b> R voltage current ke saath; L voltage +90°, C voltage −90°. Vector add karo, arithmetic nahi.</li>\n<li><b>Impedance ⭐:</b> Z=√[R²+(X_L−X_C)²], I_rms=V_rms/Z; tanφ=(X_L−X_C)/R.</li>\n<li><b>Resonance ⭐⭐:</b> X_L=X_C, ω₀=1/√(LC); Z=R minimum, current maximum, φ=0.</li>\n</ul>\n<p class=\"small-note\">💡 Resonance pe L aur C ke opposite effects cancel, lekin unke voltages bade ho sakte hain.</p>"
   },
   {
    "h": "4️⃣ Power factor aur wattless current ⭐",
    "body": "<ul>\n<li><b>Average power ⭐:</b> P=V_rms I_rms cosφ=I_rms²R; cosφ=R/Z power factor.</li>\n<li><b>Pure L/C:</b> φ=90°, cosφ=0 → cycle-average power zero: energy store aur return hoti hai.</li>\n<li><b>Wattless component:</b> I_rms sinφ; useful/in-phase component I_rms cosφ. Low power factor pe same power ke liye zyada current lagta hai.</li>\n</ul>\n<p class=\"small-note\">🎯 Apparent power VI (VA) aur real power VI cosφ (W) confuse mat karo.</p>"
   },
   {
    "h": "5️⃣ Generator aur transformer ⭐",
    "body": "<ul>\n<li><b>AC generator:</b> rotating coil me NNNΦ=NBA cosωt, induced emf ε=NBAω sinωt. Peak ε₀=NBAω.</li>\n<li><b>Transformer ⭐:</b> mutual induction se AC voltage badlo; ideal V_s/V_p=N_s/N_p, I_s/I_p=N_p/N_s, input power = output power.</li>\n<li><b>Step-up:</b> N_s&gt;N_p, voltage badhe aur current ghate. <b>Step-down:</b> ulta. Transformer steady DC pe kaam nahi karta.</li>\n</ul>\n<p class=\"small-note\">💡 Power lines high voltage rakhti hain taaki given power ke liye I kam aur I²R loss kam ho.</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ AC संकेत और RMS ⭐",
    "body": "<ul>\n<li><b>प्रत्यावर्ती धारा:</b> i(t)=I₀ sin ωt; हर अर्धचक्र में दिशा बदलती है। ω=2πf; भारत में f=50 Hz।</li>\n<li><b>प्रभावी मान ⭐:</b> I_rms=I₀/√2, V_rms=V₀/√2; घरेलू 230 V प्रभावी है, शिखर 230√2 V।</li>\n<li><b>औसत:</b> पूरे चक्र में धारा का औसत शून्य; आधे चक्र में 2I₀/π।</li>\n</ul>\n<p class=\"small-note\">💡 प्रभावी मान वही DC मान है जो बराबर ऊष्मा उत्पन्न करे।</p>"
   },
   {
    "h": "2️⃣ R, L और C का AC व्यवहार ⭐",
    "body": "<ul>\n<li><b>प्रतिरोधक:</b> V और I समान कला में; प्रतिबाधा R।</li>\n<li><b>प्रेरक ⭐:</b> X_L=ωL; धारा वोल्टता से 90° पीछे। आवृत्ति बढ़ने पर विरोध बढ़ता है।</li>\n<li><b>संधारित्र ⭐:</b> X_C=1/(ωC); धारा वोल्टता से 90° आगे। आवृत्ति बढ़ने पर विरोध घटता है।</li>\n</ul>\n<p class=\"small-note\">🎯 प्रेरक में धारा पीछे, संधारित्र में आगे।</p>"
   },
   {
    "h": "3️⃣ श्रेणी LCR और अनुनाद ⭐⭐",
    "body": "<ul>\n<li><b>फेजर:</b> R की वोल्टता धारा के साथ; L +90°, C −90°। सदिश जोड़ो।</li>\n<li><b>प्रतिबाधा ⭐:</b> Z=√[R²+(X_L−X_C)²], I_rms=V_rms/Z; tanφ=(X_L−X_C)/R।</li>\n<li><b>अनुनाद ⭐⭐:</b> X_L=X_C, ω₀=1/√(LC); Z न्यूनतम R, धारा अधिकतम, φ=0।</li>\n</ul>\n<p class=\"small-note\">💡 अनुनाद पर L और C का प्रभाव निरस्त; उनकी अलग-अलग वोल्टताएँ फिर भी बड़ी हो सकती हैं।</p>"
   },
   {
    "h": "4️⃣ शक्ति गुणांक और शक्तिहीन धारा ⭐",
    "body": "<ul>\n<li><b>औसत शक्ति ⭐:</b> P=V_rms I_rms cosφ=I_rms²R; cosφ=R/Z शक्ति गुणांक।</li>\n<li><b>शुद्ध L/C:</b> φ=90°, औसत शक्ति शून्य; ऊर्जा संचित होकर लौटती है।</li>\n<li><b>शक्तिहीन घटक:</b> I_rms sinφ; उपयोगी समकला घटक I_rms cosφ।</li>\n</ul>\n<p class=\"small-note\">🎯 आभासी शक्ति VI (VA) और वास्तविक शक्ति VI cosφ (W) अलग हैं।</p>"
   },
   {
    "h": "5️⃣ जनरेटर और ट्रांसफॉर्मर ⭐",
    "body": "<ul>\n<li><b>AC जनरेटर:</b> घूमती कुंडली में NNNΦ=NBA cosωt, ε=NBAω sinωt।</li>\n<li><b>ट्रांसफॉर्मर ⭐:</b> अन्योन्य प्रेरण; आदर्श V_s/V_p=N_s/N_p, I_s/I_p=N_p/N_s, आगत शक्ति = निर्गत शक्ति।</li>\n<li><b>अपचायी/उच्चायी:</b> N_s&gt;N_p तो वोल्टता बढ़ती, धारा घटती। स्थिर DC पर ट्रांसफॉर्मर नहीं चलता।</li>\n</ul>\n<p class=\"small-note\">💡 संचरण में अधिक वोल्टता से धारा और I²R हानि घटती है।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ AC signal and RMS ⭐",
    "body": "<ul>\n<li><b>Alternating current:</b> i(t)=I₀ sin ωt reverses every half-cycle. ω=2πf; mains frequency in India is 50 Hz.</li>\n<li><b>RMS ⭐:</b> I_rms=I₀/√2 and V_rms=V₀/√2. A 230 V mains rating is RMS; peak voltage is 230√2 V.</li>\n<li><b>Average:</b> sinusoidal current averages zero over a full cycle; its half-cycle average is 2I₀/π.</li>\n</ul>\n<p class=\"small-note\">💡 RMS is the DC value that would produce the same heating in a resistor.</p>"
   },
   {
    "h": "2️⃣ AC response of R, L and C ⭐",
    "body": "<ul>\n<li><b>Resistor:</b> current and voltage are in phase; impedance is R.</li>\n<li><b>Inductor ⭐:</b> X_L=ωL; current lags voltage by 90°. Opposition rises with frequency.</li>\n<li><b>Capacitor ⭐:</b> X_C=1/(ωC); current leads voltage by 90°. Opposition falls with frequency.</li>\n</ul>\n<p class=\"small-note\">🎯 ELI the ICE man: voltage leads current in L, current leads voltage in C.</p>"
   },
   {
    "h": "3️⃣ Series LCR and resonance ⭐⭐",
    "body": "<ul>\n<li><b>Phasors:</b> resistor voltage follows current, inductor voltage leads by 90°, capacitor voltage lags by 90°. Add vectors.</li>\n<li><b>Impedance ⭐:</b> Z=√[R²+(X_L−X_C)²], I_rms=V_rms/Z and tanφ=(X_L−X_C)/R.</li>\n<li><b>Resonance ⭐⭐:</b> X_L=X_C at ω₀=1/√(LC); Z reaches R, current peaks and φ=0.</li>\n</ul>\n<p class=\"small-note\">💡 At resonance L and C cancel in net impedance, but their individual voltages can still be large.</p>"
   },
   {
    "h": "4️⃣ Power factor and wattless current ⭐",
    "body": "<ul>\n<li><b>Average power ⭐:</b> P=V_rms I_rms cosφ=I_rms²R; the power factor is cosφ=R/Z.</li>\n<li><b>Pure L or C:</b> φ=90°, average power zero: energy is stored and returned each cycle.</li>\n<li><b>Wattless component:</b> I_rms sinφ; in-phase component I_rms cosφ. A poor power factor needs more current for the same useful power.</li>\n</ul>\n<p class=\"small-note\">🎯 Do not confuse apparent power VI (VA) with real power VI cosφ (W).</p>"
   },
   {
    "h": "5️⃣ Generator and transformer ⭐",
    "body": "<ul>\n<li><b>AC generator:</b> a rotating coil has NNNΦ=NBA cosωt and emf ε=NBAω sinωt.</li>\n<li><b>Transformer ⭐:</b> mutual induction changes AC voltage; ideally V_s/V_p=N_s/N_p and I_s/I_p=N_p/N_s, with equal input/output power.</li>\n<li><b>Step-up:</b> N_s&gt;N_p increases voltage and lowers current. Step-down reverses it. A transformer does not operate on steady DC.</li>\n</ul>\n<p class=\"small-note\">💡 High-voltage transmission keeps current and I²R loss low for a given power.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "AC signal aur RMS ⭐",
    "items": [
     "Alternating current: i(t)=I₀ sin ωt; har half-cycle me direction reverse. ω=2πf, India me f=50 Hz.",
     "RMS ⭐: I_rms=I₀/√2, V_rms=V₀/√2; 230 V household AC RMS hota hai, peak 230√2 V.",
     "Average: pure cycle me sinusoidal current ka average zero; half-cycle average 2I₀/π."
    ]
   },
   {
    "h": "R, L aur C ka AC response ⭐",
    "items": [
     "Resistor: V aur I same phase me; impedance R, average power V_rms I_rms.",
     "Inductor ⭐: X_L=ωL; current voltage se 90° peeche (lag). Frequency badhao to opposition badhta hai.",
     "Capacitor ⭐: X_C=1/(ωC); current voltage se 90° aage (lead). Frequency badhao to opposition ghatta hai."
    ]
   },
   {
    "h": "Series LCR aur resonance ⭐⭐",
    "items": [
     "Phasor: R voltage current ke saath; L voltage +90°, C voltage −90°. Vector add karo, arithmetic nahi.",
     "Impedance ⭐: Z=√[R²+(X_L−X_C)²], I_rms=V_rms/Z; tanφ=(X_L−X_C)/R.",
     "Resonance ⭐⭐: X_L=X_C, ω₀=1/√(LC); Z=R minimum, current maximum, φ=0."
    ]
   },
   {
    "h": "Power factor aur wattless current ⭐",
    "items": [
     "Average power ⭐: P=V_rms I_rms cosφ=I_rms²R; cosφ=R/Z power factor.",
     "Pure L/C: φ=90°, cosφ=0 → cycle-average power zero: energy store aur return hoti hai.",
     "Wattless component: I_rms sinφ; useful/in-phase component I_rms cosφ. Low power factor pe same power ke liye zyada current lagta hai."
    ]
   },
   {
    "h": "Generator aur transformer ⭐",
    "items": [
     "AC generator: rotating coil me NNNΦ=NBA cosωt, induced emf ε=NBAω sinωt. Peak ε₀=NBAω.",
     "Transformer ⭐: mutual induction se AC voltage badlo; ideal V_s/V_p=N_s/N_p, I_s/I_p=N_p/N_s, input power = output power.",
     "Step-up: N_s>N_p, voltage badhe aur current ghate. Step-down: ulta. Transformer steady DC pe kaam nahi karta."
    ]
   }
  ],
  "hi": [
   {
    "h": "AC संकेत और RMS ⭐",
    "items": [
     "प्रत्यावर्ती धारा: i(t)=I₀ sin ωt; हर अर्धचक्र में दिशा बदलती है। ω=2πf; भारत में f=50 Hz।",
     "प्रभावी मान ⭐: I_rms=I₀/√2, V_rms=V₀/√2; घरेलू 230 V प्रभावी है, शिखर 230√2 V।",
     "औसत: पूरे चक्र में धारा का औसत शून्य; आधे चक्र में 2I₀/π।"
    ]
   },
   {
    "h": "R, L और C का AC व्यवहार ⭐",
    "items": [
     "प्रतिरोधक: V और I समान कला में; प्रतिबाधा R।",
     "प्रेरक ⭐: X_L=ωL; धारा वोल्टता से 90° पीछे। आवृत्ति बढ़ने पर विरोध बढ़ता है।",
     "संधारित्र ⭐: X_C=1/(ωC); धारा वोल्टता से 90° आगे। आवृत्ति बढ़ने पर विरोध घटता है।"
    ]
   },
   {
    "h": "श्रेणी LCR और अनुनाद ⭐⭐",
    "items": [
     "फेजर: R की वोल्टता धारा के साथ; L +90°, C −90°। सदिश जोड़ो।",
     "प्रतिबाधा ⭐: Z=√[R²+(X_L−X_C)²], I_rms=V_rms/Z; tanφ=(X_L−X_C)/R।",
     "अनुनाद ⭐⭐: X_L=X_C, ω₀=1/√(LC); Z न्यूनतम R, धारा अधिकतम, φ=0।"
    ]
   },
   {
    "h": "शक्ति गुणांक और शक्तिहीन धारा ⭐",
    "items": [
     "औसत शक्ति ⭐: P=V_rms I_rms cosφ=I_rms²R; cosφ=R/Z शक्ति गुणांक।",
     "शुद्ध L/C: φ=90°, औसत शक्ति शून्य; ऊर्जा संचित होकर लौटती है।",
     "शक्तिहीन घटक: I_rms sinφ; उपयोगी समकला घटक I_rms cosφ।"
    ]
   },
   {
    "h": "जनरेटर और ट्रांसफॉर्मर ⭐",
    "items": [
     "AC जनरेटर: घूमती कुंडली में NNNΦ=NBA cosωt, ε=NBAω sinωt।",
     "ट्रांसफॉर्मर ⭐: अन्योन्य प्रेरण; आदर्श V_s/V_p=N_s/N_p, I_s/I_p=N_p/N_s, आगत शक्ति = निर्गत शक्ति।",
     "अपचायी/उच्चायी: N_s>N_p तो वोल्टता बढ़ती, धारा घटती। स्थिर DC पर ट्रांसफॉर्मर नहीं चलता।"
    ]
   }
  ],
  "en": [
   {
    "h": "AC signal and RMS ⭐",
    "items": [
     "Alternating current: i(t)=I₀ sin ωt reverses every half-cycle. ω=2πf; mains frequency in India is 50 Hz.",
     "RMS ⭐: I_rms=I₀/√2 and V_rms=V₀/√2. A 230 V mains rating is RMS; peak voltage is 230√2 V.",
     "Average: sinusoidal current averages zero over a full cycle; its half-cycle average is 2I₀/π."
    ]
   },
   {
    "h": "AC response of R, L and C ⭐",
    "items": [
     "Resistor: current and voltage are in phase; impedance is R.",
     "Inductor ⭐: X_L=ωL; current lags voltage by 90°. Opposition rises with frequency.",
     "Capacitor ⭐: X_C=1/(ωC); current leads voltage by 90°. Opposition falls with frequency."
    ]
   },
   {
    "h": "Series LCR and resonance ⭐⭐",
    "items": [
     "Phasors: resistor voltage follows current, inductor voltage leads by 90°, capacitor voltage lags by 90°. Add vectors.",
     "Impedance ⭐: Z=√[R²+(X_L−X_C)²], I_rms=V_rms/Z and tanφ=(X_L−X_C)/R.",
     "Resonance ⭐⭐: X_L=X_C at ω₀=1/√(LC); Z reaches R, current peaks and φ=0."
    ]
   },
   {
    "h": "Power factor and wattless current ⭐",
    "items": [
     "Average power ⭐: P=V_rms I_rms cosφ=I_rms²R; the power factor is cosφ=R/Z.",
     "Pure L or C: φ=90°, average power zero: energy is stored and returned each cycle.",
     "Wattless component: I_rms sinφ; in-phase component I_rms cosφ. A poor power factor needs more current for the same useful power."
    ]
   },
   {
    "h": "Generator and transformer ⭐",
    "items": [
     "AC generator: a rotating coil has NNNΦ=NBA cosωt and emf ε=NBAω sinωt.",
     "Transformer ⭐: mutual induction changes AC voltage; ideally V_s/V_p=N_s/N_p and I_s/I_p=N_p/N_s, with equal input/output power.",
     "Step-up: N_s>N_p increases voltage and lowers current. Step-down reverses it. A transformer does not operate on steady DC."
    ]
   }
  ]
 },
 "practice": [
  [
   "Peak current 10 A hai. RMS?",
   "I_rms=10/√2≈<b>7.07 A</b>."
  ],
  [
   "230 V RMS mains ka peak voltage?",
   "V₀=√2×230≈<b>325 V</b>."
  ],
  [
   "50 Hz AC ki angular frequency?",
   "ω=2πf=100π≈<b>314 rad/s</b>."
  ],
  [
   "L=0.2 H aur f=50 Hz. X_L?",
   "X_L=2πfL=20π≈<b>62.8 Ω</b>."
  ],
  [
   "C=100 μF aur f=50 Hz. X_C?",
   "X_C=1/(2πfC)≈<b>31.8 Ω</b>."
  ],
  [
   "R=3 Ω, X_L=5 Ω, X_C=1 Ω. Impedance?",
   "Z=√(3²+4²)=<b>5 Ω</b>."
  ],
  [
   "L=1 H, C=100 μF. Resonance angular frequency?",
   "ω₀=1/√(LC)=1/√10⁻⁴=<b>100 rad/s</b>."
  ],
  [
   "V_rms=100 V, I_rms=2 A, cosφ=0.8. Average power?",
   "P=VI cosφ=100×2×0.8=<b>160 W</b>."
  ],
  [
   "Pure capacitor average AC power?",
   "φ=90°, cosφ=0 → <b>0 W</b> cycle-average."
  ],
  [
   "Ideal transformer N_p=1000, N_s=100, V_p=230 V. V_s?",
   "V_s=230×100/1000=<b>23 V</b>."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/physics/ch-8/",
  "title": "Electromagnetic Waves"
 }
}

# Class 11 Maths, Chapter 8 - Sequences and Series
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 8,
 "title_en": "Sequences and Series",
 "title_hi": "श्रेणी तथा श्रेढ़ी",
 "tagline": "AP, GP aur special sums — pattern pehchano, formula lagao",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 8: Sequences and Series — long + short notes in Hindi, English, Hinglish. AP, GP, AM-GM, sum of squares and cubes, infinite series.",
  "video": {
  "youtube": "TTn5df_h88k",
  "dur": "1 min 12 sec"
 },
 "card_tag": "AP, GP aur special sums — pattern pehchano, formula lagao",
 "card_topics": [
  "➕ AP: aₙ aur Sₙ",
  "✖️ GP + infinite sums",
  "∑ Squares & cubes formulas",
  "⚖️ AM-GM inequality"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Sequence aur Series — Numbers ka Pattern Game",
    "body": "<p>Numbers ko ek rule ke saath line me lagao — wohi <b>sequence</b> hai: 2, 4, 6, 8... (even numbers) ya 3, 6, 12, 24... (har baar double). Aur jab sequence ke terms ko <b>jodne (+)</b> lagein, wo ban jaata hai <b>series</b>: 2 + 4 + 6 + 8 + ...</p>\n<ul>\n<li><b>Sequence:</b> ordered list of numbers following a rule — har term ka ek position hota hai (a₁, a₂, a₃... aₙ).</li>\n<li><b>Finite sequence:</b> limited terms (jaise 1 se 10 tak ke squares). <b>Infinite:</b> chalti rehti hai...</li>\n<li><b>Series = sum of sequence terms</b> — Sₙ = a₁ + a₂ + ... + aₙ.</li>\n<li><b>Fibonacci ⭐:</b> 1, 1, 2, 3, 5, 8, 13... — har term pichli do ka sum. Nature me har jagah milta hai (sunflower, pinecone, shells)!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: sequence = Spotify playlist (order matter karta hai), series = puri playlist ka total playtime!</p>"
   },
   {
    "h": "2️⃣ AP — Arithmetic Progression (Same Difference) ⭐",
    "body": "<p>Jab har term pichli term me <b>ek fixed number add</b> karke bane, wo <b>AP</b> hai: 5, 9, 13, 17... (difference 4).</p>\n<ul>\n<li><b>First term = a, common difference = d.</b> d = kisi bhi term − pichli term.</li>\n<li><b>n-th term ⭐:</b> aₙ = a + (n − 1)d — AP ka sabse zyada use hone wala formula!</li>\n<li><b>Sum of n terms ⭐:</b> Sₙ = n/2 [2a + (n−1)d] = n/2 (a + aₙ) — average of first &amp; last × count.</li>\n<li><b>Arithmetic Mean (AM):</b> a aur b ke beech ka AM = (a+b)/2. k AMs insert karne hon to d = (b−a)/(k+1).</li>\n<li><b>Property:</b> AP ke terms ka sum jo equidistant ends se hain, hamesha same: a₁ + aₙ = a₂ + aₙ₋₁ = ...</li>\n</ul>\n<p class=\"small-note\">💡 Gauss wala trick: 1+2+...+100 = (1+100)×100/2 = 5050 — pair karke jodo!</p>"
   },
   {
    "h": "3️⃣ GP — Geometric Progression (Same Ratio) ⭐",
    "body": "<p>Jab har term pichli term se <b>ek fixed number MULTIPLY</b> karke bane, wo <b>GP</b> hai: 3, 6, 12, 24... (ratio 2).</p>\n<ul>\n<li><b>First term = a, common ratio = r.</b> r = koi bhi term ÷ pichli term.</li>\n<li><b>n-th term ⭐:</b> aₙ = arⁿ⁻¹</li>\n<li><b>Sum of n terms ⭐:</b> Sₙ = a(rⁿ − 1)/(r − 1) jab r ≠ 1. (r = 1 ho to Sₙ = na.)</li>\n<li><b>Infinite GP ka sum ⭐:</b> S = a/(1 − r), sirf jab |r| &lt; 1. Example: 1 + 1/2 + 1/4 + ... = 1/(1−1/2) = 2!</li>\n<li><b>Geometric Mean (GM):</b> a aur b ka GM = √(ab). Hamesha AM ≥ GM ⭐ (positive numbers ke liye).</li>\n<li><b>GP ki property:</b> equidistant terms ka PRODUCT same: a₁·aₙ = a₂·aₙ₋₁</li>\n</ul>\n<p class=\"small-note\">💡 Compound interest, population growth, viral videos — sab GP hain! Paisa double har saal = ratio 2.</p>"
   },
   {
    "h": "4️⃣ Special Series — Sum Formulas ⭐",
    "body": "<ul>\n<li><b>First n naturals:</b> 1 + 2 + ... + n = <b>n(n+1)/2</b></li>\n<li><b>Squares ka sum:</b> 1² + 2² + ... + n² = <b>n(n+1)(2n+1)/6</b></li>\n<li><b>Cubes ka sum ⭐:</b> 1³ + 2³ + ... + n³ = <b>[n(n+1)/2]²</b> — natural sum ka SQUARE! Beautiful!</li>\n<li><b>Σ notation:</b> Σ (sigma) matlab \"sum karo\" — Σk (k=1 to n) = 1+2+...+n.</li>\n<li><b>Sigma ke rules:</b> Σ(a + b) = Σa + Σb; Σ(ca) = c·Σa; Σc = nc.</li>\n<li><b>Arithmetico-Geometric series:</b> AP × GP ka mix (1 + 2x + 3x² + ...) — multiply-shift-subtract trick se solve.</li>\n</ul>\n<p class=\"small-note\">🎯 Cubes wala formula yaad rakhne ka tareeka: (1+2+...+n)² = 1³+2³+...+n³ — ek hi cheez do roop!</p>"
   },
   {
    "h": "5️⃣ AM-GM aur Mixed Problems",
    "body": "<ul>\n<li><b>AM ≥ GM ⭐:</b> (a+b)/2 ≥ √(ab) — equality sirf jab a = b. Minimization/maximization problems me kaam aata hai.</li>\n<li><b>n numbers ke liye bhi:</b> (a₁+a₂+...+aₙ)/n ≥ (a₁·a₂...aₙ)^(1/n).</li>\n<li><b>AP aur GP dono ho:</b> a, b, c AP me → 2b = a + c; GP me → b² = ac. ⭐ Conditions yaad rakho!</li>\n<li><b>Hidden pattern:</b> kabhi sequence directly AP/GP nahi hota — differences dekho! 2, 5, 10, 17... differences 3, 5, 7 (AP me) → aₙ = n² + 1.</li>\n<li><b>Recurring decimals:</b> 0.333... = 3/10 + 3/100 + ... = infinite GP = 1/3.</li>\n</ul>\n<p class=\"small-note\">💡 Series dekh ke pehchano: fixed + (AP), fixed × (GP), squares/cubes (special), kuch na chale to differences likho!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ श्रेणी और श्रेढ़ी — संख्याओं का पैटर्न",
    "body": "<p>संख्याओं को एक नियम से क्रम में लगाओ — वही <b>श्रेणी (sequence)</b> है: 2, 4, 6, 8... और जब श्रेणी के पदों को <b>जोड़ने (+)</b> लगें, वह बन जाती है <b>श्रेढ़ी (series)</b>: 2 + 4 + 6 + 8 + ...</p>\n<ul>\n<li><b>श्रेणी:</b> नियम से बनी संख्याओं की क्रमबद्ध सूची — हर पद की स्थिति निश्चित (a₁, a₂, a₃...)।</li>\n<li><b>परिमित श्रेणी:</b> सीमित पद। <b>अपरिमित:</b> अनंत तक चलती है।</li>\n<li><b>श्रेढ़ी = श्रेणी के पदों का योग</b> — Sₙ = a₁ + a₂ + ... + aₙ।</li>\n<li><b>फिबोनाचि ⭐:</b> 1, 1, 2, 3, 5, 8, 13... — हर पद पिछले दो का योग। प्रकृति में सर्वत्र!</li>\n</ul>\n<p class=\"small-note\">💡 श्रेणी = क्रम से सजी पंक्ति, श्रेढ़ी = उस पंक्ति का कुल योग!</p>"
   },
   {
    "h": "2️⃣ समांतर श्रेढ़ी (AP) — समान अंतर ⭐",
    "body": "<p>जब हर पद पिछले पद में <b>एक निश्चित संख्या जोड़ने</b> से बने, वह <b>समांतर श्रेढ़ी</b> है: 5, 9, 13, 17... (अंतर 4)।</p>\n<ul>\n<li><b>प्रथम पद = a, सार्व अंतर = d.</b> d = कोई पद − पिछला पद।</li>\n<li><b>n-वाँ पद ⭐:</b> aₙ = a + (n − 1)d — AP का सबसे महत्वपूर्ण सूत्र!</li>\n<li><b>n पदों का योग ⭐:</b> Sₙ = n/2 [2a + (n−1)d] = n/2 (a + aₙ)।</li>\n<li><b>समांतर माध्य (AM):</b> a और b का AM = (a+b)/2। k AM रखने हों तो d = (b−a)/(k+1)।</li>\n<li><b>गुण:</b> सिरों से समदूर पदों का योग समान: a₁ + aₙ = a₂ + aₙ₋₁।</li>\n</ul>\n<p class=\"small-note\">💡 गॉस की तरकीब: 1+2+...+100 = (1+100)×100/2 = 5050 — जोड़े बनाकर जोड़ो!</p>"
   },
   {
    "h": "3️⃣ गुणोत्तर श्रेढ़ी (GP) — समान अनुपात ⭐",
    "body": "<p>जब हर पद पिछले पद से <b>एक निश्चित संख्या का गुणा</b> करने से बने, वह <b>गुणोत्तर श्रेढ़ी</b> है: 3, 6, 12, 24... (अनुपात 2)।</p>\n<ul>\n<li><b>प्रथम पद = a, सार्व अनुपात = r.</b> r = कोई पद ÷ पिछला पद।</li>\n<li><b>n-वाँ पद ⭐:</b> aₙ = arⁿ⁻¹</li>\n<li><b>n पदों का योग ⭐:</b> Sₙ = a(rⁿ − 1)/(r − 1), जब r ≠ 1। (r = 1 हो तो Sₙ = na।)</li>\n<li><b>अनंत GP का योग ⭐:</b> S = a/(1 − r), केवल जब |r| &lt; 1। उदाहरण: 1 + 1/2 + 1/4 + ... = 2!</li>\n<li><b>गुणोत्तर माध्य (GM):</b> a और b का GM = √(ab)। सदैव AM ≥ GM ⭐</li>\n<li><b>गुण:</b> सिरों से समदूर पदों का गुणनफल समान: a₁·aₙ = a₂·aₙ₋₁।</li>\n</ul>\n<p class=\"small-note\">💡 चक्रवृद्धि ब्याज, जनसंख्या वृद्धि — सब GP हैं!</p>"
   },
   {
    "h": "4️⃣ विशेष श्रेढ़ियाँ — योग सूत्र ⭐",
    "body": "<ul>\n<li><b>प्रथम n प्राकृत संख्याएँ:</b> 1 + 2 + ... + n = <b>n(n+1)/2</b></li>\n<li><b>वर्गों का योग:</b> 1² + 2² + ... + n² = <b>n(n+1)(2n+1)/6</b></li>\n<li><b>घनों का योग ⭐:</b> 1³ + 2³ + ... + n³ = <b>[n(n+1)/2]²</b> — प्राकृत योग का वर्ग!</li>\n<li><b>Σ संकेत:</b> Σ (सिग्मा) का अर्थ \"योग करो\" — Σk (k=1 से n) = 1+2+...+n।</li>\n<li><b>सिग्मा नियम:</b> Σ(a + b) = Σa + Σb; Σ(ca) = c·Σa; Σc = nc।</li>\n<li><b>समांतर-गुणोत्तर श्रेढ़ी:</b> AP × GP का मिश्रण (1 + 2x + 3x² + ...) — गुणा-स्थानांतरण-घटाव तरकीब से।</li>\n</ul>\n<p class=\"small-note\">🎯 घनों का सूत्र: (1+2+...+n)² = 1³+2³+...+n³ — एक ही बात दो रूप!</p>"
   },
   {
    "h": "5️⃣ AM-GM और मिश्रित प्रश्न",
    "body": "<ul>\n<li><b>AM ≥ GM ⭐:</b> (a+b)/2 ≥ √(ab) — समानता केवल जब a = b।</li>\n<li><b>AP/GP शर्तें:</b> a, b, c AP में → 2b = a + c; GP में → b² = ac। ⭐</li>\n<li><b>छिपा पैटर्न:</b> श्रेणी सीधे AP/GP न हो तो अंतर देखो! 2, 5, 10, 17... अंतर 3, 5, 7 (AP) → aₙ = n² + 1।</li>\n<li><b>आवर्ती दशमलव:</b> 0.333... = 3/10 + 3/100 + ... = अनंत GP = 1/3।</li>\n</ul>\n<p class=\"small-note\">💡 पहचानो: निश्चित + (AP), निश्चित × (GP), वर्ग/घन (विशेष), कुछ न चले तो अंतर लिखो!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Sequences and Series — the Pattern Game of Numbers",
    "body": "<p>Line numbers up by a rule and you get a <b>sequence</b>: 2, 4, 6, 8... (even numbers) or 3, 6, 12, 24... (doubling). Start <b>adding (+)</b> the terms and you get a <b>series</b>: 2 + 4 + 6 + 8 + ...</p>\n<ul>\n<li><b>Sequence:</b> an ordered list of numbers following a rule — every term has a fixed position (a₁, a₂, a₃... aₙ).</li>\n<li><b>Finite sequence:</b> limited terms (like squares from 1 to 10). <b>Infinite:</b> goes on forever...</li>\n<li><b>Series = sum of the sequence's terms</b> — Sₙ = a₁ + a₂ + ... + aₙ.</li>\n<li><b>Fibonacci ⭐:</b> 1, 1, 2, 3, 5, 8, 13... — each term is the sum of the previous two. Found everywhere in nature (sunflowers, pinecones, shells)!</li>\n</ul>\n<p class=\"small-note\">💡 Feel it: a sequence is a playlist (order matters); a series is the playlist's total playtime!</p>"
   },
   {
    "h": "2️⃣ AP — Arithmetic Progression (Same Difference) ⭐",
    "body": "<p>When each term is formed by <b>adding a fixed number</b> to the previous term, it's an <b>AP</b>: 5, 9, 13, 17... (difference 4).</p>\n<ul>\n<li><b>First term = a, common difference = d.</b> d = any term − previous term.</li>\n<li><b>n-th term ⭐:</b> aₙ = a + (n − 1)d — the most-used AP formula!</li>\n<li><b>Sum of n terms ⭐:</b> Sₙ = n/2 [2a + (n−1)d] = n/2 (a + aₙ) — average of first and last, times the count.</li>\n<li><b>Arithmetic Mean (AM):</b> the AM of a and b is (a+b)/2. To insert k AMs between them, d = (b−a)/(k+1).</li>\n<li><b>Property:</b> terms equidistant from the ends sum to the same value: a₁ + aₙ = a₂ + aₙ₋₁ = ...</li>\n</ul>\n<p class=\"small-note\">💡 The Gauss trick: 1+2+...+100 = (1+100)×100/2 = 5050 — pair and add!</p>"
   },
   {
    "h": "3️⃣ GP — Geometric Progression (Same Ratio) ⭐",
    "body": "<p>When each term is formed by <b>MULTIPLYING the previous term by a fixed number</b>, it's a <b>GP</b>: 3, 6, 12, 24... (ratio 2).</p>\n<ul>\n<li><b>First term = a, common ratio = r.</b> r = any term ÷ previous term.</li>\n<li><b>n-th term ⭐:</b> aₙ = arⁿ⁻¹</li>\n<li><b>Sum of n terms ⭐:</b> Sₙ = a(rⁿ − 1)/(r − 1) when r ≠ 1. (If r = 1, then Sₙ = na.)</li>\n<li><b>Infinite GP sum ⭐:</b> S = a/(1 − r), only when |r| &lt; 1. Example: 1 + 1/2 + 1/4 + ... = 1/(1−1/2) = 2!</li>\n<li><b>Geometric Mean (GM):</b> the GM of a and b is √(ab). Always AM ≥ GM ⭐ (for positive numbers).</li>\n<li><b>GP property:</b> terms equidistant from the ends have equal PRODUCTS: a₁·aₙ = a₂·aₙ₋₁.</li>\n</ul>\n<p class=\"small-note\">💡 Compound interest, population growth, viral videos — all GPs! Money doubling yearly = ratio 2.</p>"
   },
   {
    "h": "4️⃣ Special Series — Sum Formulas ⭐",
    "body": "<ul>\n<li><b>First n naturals:</b> 1 + 2 + ... + n = <b>n(n+1)/2</b></li>\n<li><b>Sum of squares:</b> 1² + 2² + ... + n² = <b>n(n+1)(2n+1)/6</b></li>\n<li><b>Sum of cubes ⭐:</b> 1³ + 2³ + ... + n³ = <b>[n(n+1)/2]²</b> — the SQUARE of the natural sum! Beautiful!</li>\n<li><b>Σ notation:</b> Σ (sigma) means \"add up\" — Σk (k=1 to n) = 1+2+...+n.</li>\n<li><b>Sigma rules:</b> Σ(a + b) = Σa + Σb; Σ(ca) = c·Σa; Σc = nc.</li>\n<li><b>Arithmetico-Geometric series:</b> an AP × GP mix (1 + 2x + 3x² + ...) — solved by the multiply-shift-subtract trick.</li>\n</ul>\n<p class=\"small-note\">🎯 Memory hook for cubes: (1+2+...+n)² = 1³+2³+...+n³ — one fact, two forms!</p>"
   },
   {
    "h": "5️⃣ AM-GM and Mixed Problems",
    "body": "<ul>\n<li><b>AM ≥ GM ⭐:</b> (a+b)/2 ≥ √(ab) — equality only when a = b. Used in max/min problems.</li>\n<li><b>For n numbers:</b> (a₁+a₂+...+aₙ)/n ≥ (a₁·a₂...aₙ)^(1/n).</li>\n<li><b>AP/GP conditions:</b> a, b, c in AP → 2b = a + c; in GP → b² = ac. ⭐ Memorise these!</li>\n<li><b>Hidden patterns:</b> sometimes a sequence is neither AP nor GP — check the differences! 2, 5, 10, 17... differences 3, 5, 7 (an AP) → aₙ = n² + 1.</li>\n<li><b>Recurring decimals:</b> 0.333... = 3/10 + 3/100 + ... = infinite GP = 1/3.</li>\n</ul>\n<p class=\"small-note\">💡 Spot the type: fixed + (AP), fixed × (GP), squares/cubes (special), stuck? Write the differences!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "AP ⭐",
    "items": [
     "aₙ = a + (n−1)d",
     "Sₙ = n/2 [2a + (n−1)d] = n/2 (a + aₙ)",
     "AM = (a+b)/2"
    ]
   },
   {
    "h": "GP ⭐",
    "items": [
     "aₙ = arⁿ⁻¹",
     "Sₙ = a(rⁿ−1)/(r−1)",
     "Infinite: a/(1−r), |r|&lt;1",
     "GM = √(ab)"
    ]
   },
   {
    "h": "Sums ⭐",
    "items": [
     "Σn = n(n+1)/2",
     "Σn² = n(n+1)(2n+1)/6",
     "Σn³ = [n(n+1)/2]²"
    ]
   },
   {
    "h": "Relations ⭐",
    "items": [
     "AP: 2b = a+c",
     "GP: b² = ac",
     "AM ≥ GM (equal jab a=b)"
    ]
   },
   {
    "h": "Tricks",
    "items": [
     "Gauss pairing: first+last × n/2",
     "Differences se pattern pehchano",
     "0.333... = infinite GP = 1/3"
    ]
   }
  ],
  "hi": [
   {
    "h": "AP ⭐",
    "items": [
     "aₙ = a + (n−1)d",
     "Sₙ = n/2 [2a + (n−1)d]",
     "AM = (a+b)/2"
    ]
   },
   {
    "h": "GP ⭐",
    "items": [
     "aₙ = arⁿ⁻¹",
     "Sₙ = a(rⁿ−1)/(r−1)",
     "अनंत: a/(1−r), |r|&lt;1",
     "GM = √(ab)"
    ]
   },
   {
    "h": "योग ⭐",
    "items": [
     "Σn = n(n+1)/2",
     "Σn² = n(n+1)(2n+1)/6",
     "Σn³ = [n(n+1)/2]²"
    ]
   },
   {
    "h": "संबंध ⭐",
    "items": [
     "AP: 2b = a+c",
     "GP: b² = ac",
     "AM ≥ GM"
    ]
   },
   {
    "h": "तरकीबें",
    "items": [
     "गॉस: (प्रथम+अंतिम) × n/2",
     "अंतर से पैटर्न",
     "0.333... = 1/3"
    ]
   }
  ],
  "en": [
   {
    "h": "AP ⭐",
    "items": [
     "aₙ = a + (n−1)d",
     "Sₙ = n/2 [2a + (n−1)d] = n/2 (a + aₙ)",
     "AM = (a+b)/2"
    ]
   },
   {
    "h": "GP ⭐",
    "items": [
     "aₙ = arⁿ⁻¹",
     "Sₙ = a(rⁿ−1)/(r−1)",
     "Infinite: a/(1−r), |r|&lt;1",
     "GM = √(ab)"
    ]
   },
   {
    "h": "Sums ⭐",
    "items": [
     "Σn = n(n+1)/2",
     "Σn² = n(n+1)(2n+1)/6",
     "Σn³ = [n(n+1)/2]²"
    ]
   },
   {
    "h": "Relations ⭐",
    "items": [
     "AP: 2b = a+c",
     "GP: b² = ac",
     "AM ≥ GM (equal iff a=b)"
    ]
   },
   {
    "h": "Tricks",
    "items": [
     "Gauss pairing: (first+last) × n/2",
     "Spot patterns via differences",
     "0.333... = infinite GP = 1/3"
    ]
   }
  ]
 },
 "practice": [
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/maths/ch-9/",
  "title": "Straight Lines"
 }
}

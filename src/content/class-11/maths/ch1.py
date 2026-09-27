# Class 11 Maths, Chapter 1 - Sets
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 1,
 "title_en": "Sets",
 "title_hi": "समुच्चय",
 "tagline": "Collections ka ganit — subsets, Venn diagrams aur De Morgan",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 1: Sets — long + short notes in Hindi, English, Hinglish. Sets, subsets, power set, Venn diagrams, union, intersection, De Morgan's laws.",
 "video": None,
 "card_tag": "Collections ka ganit — subsets, Venn diagrams aur De Morgan",
 "card_topics": [
  "📦 Sets + roster/set-builder",
  "🔄 Union, intersection, complement",
  "🎨 Venn diagrams + counting",
  "⚖️ De Morgan's laws"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Set Kya Hota Hai — Collection Ka Rulebook",
    "body": "<ul>\n<li><b>Set:</b> well-defined objects ka collection — \"well-defined\" matlab kisi ko bhi pata chale kaun andar hai, kaun bahar. (\"5 vowels\" = set; \"5 achhe students\" = set NAHI — subjective!)</li>\n<li><b>Elements/members:</b> set ke objects. a ∈ A (a belongs to A), b ∉ A.</li>\n<li><b>Roster form:</b> saare elements list karo — V = {a, e, i, o, u}. <b>Set-builder form ⭐:</b> property likho — V = {x : x is a vowel in English alphabet}.</li>\n<li><b>Order matter nahi karta</b> — {1, 2, 3} = {3, 2, 1}. Repetition ka koi matlab nahi — {1, 1, 2} = {1, 2}.</li>\n<li><b>Important sets ⭐:</b> N (natural: 1, 2, 3...), W (whole: 0, 1, 2...), Z (integers: ...−2, −1, 0, 1...), Q (rationals: p/q form), R (reals: sab kuch number line pe).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: set = club with clear membership rules. Rule clear hai to set hai, rule fuzzy hai to nahi!</p>"
   },
   {
    "h": "2️⃣ Sets Ke Types — Empty Se Universal Tak ⭐",
    "body": "<ul>\n<li><b>Empty/null set (φ ya {}):</b> koi element nahi — {x : x even prime &gt; 2} = φ. (Sirf ek hi empty set hai!)</li>\n<li><b>Finite set:</b> elements count ho jaate hain — {days of week} (7). <b>Infinite set:</b> count khatam nahi hota — N, Z, R.</li>\n<li><b>Equal sets ⭐:</b> SAME elements — {1,2,3} = {3,2,1}. <b>Equivalent sets:</b> same COUNT (cardinality), elements alag ho sakte hain — {1,2,3} aur {a,b,c}.</li>\n<li><b>Singleton set:</b> sirf 1 element — {0}, {5}.</li>\n<li><b>Universal set (U):</b> context ka sabse bada set jisme sab aa jaaye — numbers ki baat ho to U = R.</li>\n<li><b>Cardinal number:</b> set me kitne elements — n(A). n(φ) = 0.</li>\n</ul>\n<p class=\"small-note\">🎯 Equal vs equivalent = exam favourite confusion! Equal = same members; equivalent = same count only.</p>"
   },
   {
    "h": "3️⃣ Subsets aur Power Set ⭐",
    "body": "<ul>\n<li><b>Subset (⊆):</b> A ke saare elements B me hon → A ⊆ B. Har set apna subset hota hai; φ HAR set ka subset hai! ⭐</li>\n<li><b>Proper subset (⊂):</b> A ⊆ B lekin A ≠ B — B me kuch extra hai.</li>\n<li><b>Intervals bhi subsets hain R ke:</b> (a, b) = open (endpoints excluded), [a, b] = closed (included), (a, b] = half-open.</li>\n<li><b>Power set P(A) ⭐:</b> A ke SAARE subsets ka set. Agar n(A) = n → <b>n(P(A)) = 2ⁿ</b>. {a, b} ka power set: {φ, {a}, {b}, {a,b}} — 4 = 2²!</li>\n<li>Proper subsets ka count: 2ⁿ − 1; non-empty proper: 2ⁿ − 2.</li>\n</ul>\n<p class=\"small-note\">💡 2ⁿ kyun? Har element ke paas 2 choice — subset me aao ya na aao. n elements → 2×2×... (n baar) = 2ⁿ!</p>"
   },
   {
    "h": "4️⃣ Venn Diagrams aur Operations — Union, Intersection ⭐",
    "body": "<ul>\n<li><b>Venn diagram:</b> sets ko circles se dikhana, universal set rectangle — visualize karne ka best tool!</li>\n<li><b>Union (A ∪ B):</b> jo A me YA B me YA dono me — sab elements mila do (repeat mat likho!).</li>\n<li><b>Intersection (A ∩ B):</b> jo DONO me common ho — overlap wala hissa.</li>\n<li><b>Disjoint sets ⭐:</b> A ∩ B = φ — kuch common nahi (even aur odd numbers).</li>\n<li><b>Difference (A − B):</b> jo A me ho par B me NA ho. A − B ≠ B − A generally!</li>\n<li><b>Complement (A′ ya Aᶜ) ⭐:</b> U me jo A me NAHI — U − A. (A′)′ = A — double negative!</li>\n<li><b>Counting formula ⭐:</b> n(A ∪ B) = n(A) + n(B) − n(A ∩ B) — intersection double-count ho jaata hai, isliye minus!</li>\n</ul>\n<p class=\"small-note\">💡 Union = OR (kisi me bhi), Intersection = AND (dono me), Complement = NOT (uske bahar sab).</p>"
   },
   {
    "h": "5️⃣ Laws of Set Operations — Algebra Jaisa Game",
    "body": "<ul>\n<li><b>Commutative:</b> A ∪ B = B ∪ A, A ∩ B = B ∩ A.</li>\n<li><b>Associative:</b> (A ∪ B) ∪ C = A ∪ (B ∪ C); same intersection ke liye.</li>\n<li><b>Distributive ⭐:</b> A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C); A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).</li>\n<li><b>De Morgan's laws ⭐⭐:</b> (A ∪ B)′ = A′ ∩ B′ aur (A ∩ B)′ = A′ ∪ B′ — complement andar jaake sign FLIP kar deta hai (∪ ↔ ∩)!</li>\n<li><b>Identity laws:</b> A ∪ φ = A, A ∩ U = A, A ∪ U = U, A ∩ φ = φ.</li>\n<li><b>Idempotent:</b> A ∪ A = A, A ∩ A = A.</li>\n<li><b>Three sets counting:</b> n(A∪B∪C) = n(A)+n(B)+n(C) − n(A∩B) − n(B∩C) − n(A∩C) + n(A∩B∩C) ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 De Morgan = sabse zyada pucha jaane wala law: \"union ka complement = complements ka intersection\" (aur vice versa).</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ समुच्चय क्या है — संग्रह का नियम",
    "body": "<ul>\n<li><b>समुच्चय (set):</b> सुपरिभाषित वस्तुओं का संग्रह — \"सुपरिभाषित\" यानी स्पष्ट हो कौन सदस्य है, कौन नहीं। (\"5 स्वर\" = समुच्चय; \"5 अच्छे विद्यार्थी\" = नहीं!)</li>\n<li><b>अवयव:</b> समुच्चय की वस्तुएं। a ∈ A, b ∉ A।</li>\n<li><b>रोस्टर रूप:</b> सभी अवयव सूचीबद्ध — V = {a, e, i, o, u}। <b>समुच्चय-निर्माता रूप ⭐:</b> गुण लिखो — V = {x : x अंग्रेजी वर्णमाला का स्वर है}।</li>\n<li><b>क्रम महत्वहीन</b> — {1,2,3} = {3,2,1}। पुनरावृत्ति का अर्थ नहीं।</li>\n<li><b>महत्वपूर्ण समुच्चय ⭐:</b> N (प्राकृत), W (पूर्ण), Z (पूर्णांक), Q (परिमेय), R (वास्तविक)।</li>\n</ul>\n<p class=\"small-note\">💡 समुच्चय = स्पष्ट सदस्यता नियमों वाला क्लब। नियम स्पष्ट → समुच्चय!</p>"
   },
   {
    "h": "2️⃣ समुच्चयों के प्रकार — रिक्त से सार्वत्रिक तक ⭐",
    "body": "<ul>\n<li><b>रिक्त समुच्चय (φ):</b> कोई अवयव नहीं। (केवल एक ही रिक्त समुच्चय है!)</li>\n<li><b>परिमित:</b> अवयव गिने जा सकें। <b>अपरिमित:</b> गिनती समाप्त न हो — N, Z, R।</li>\n<li><b>समान समुच्चय ⭐:</b> समान अवयव। <b>तुल्य समुच्चय:</b> समान संख्या (कार्डिनैलिटी), अवयव भिन्न हो सकते हैं।</li>\n<li><b>एकल समुच्चय:</b> केवल 1 अवयव — {0}।</li>\n<li><b>सार्वत्रिक समुच्चय (U):</b> संदर्भ का सबसे बड़ा समुच्चय।</li>\n<li><b>परिणाम संख्या:</b> n(A) — अवयवों की संख्या।</li>\n</ul>\n<p class=\"small-note\">🎯 समान बनाम तुल्य — परीक्षा प्रिय! समान = समान अवयव; तुल्य = केवल समान संख्या।</p>"
   },
   {
    "h": "3️⃣ उपसमुच्चय और घात समुच्चय ⭐",
    "body": "<ul>\n<li><b>उपसमुच्चय (⊆):</b> A के सभी अवयव B में हों → A ⊆ B। प्रत्येक समुच्चय स्वयं का उपसमुच्चय; φ <b>प्रत्येक</b> समुच्चय का उपसमुच्चय! ⭐</li>\n<li><b>उचित उपसमुच्चय (⊂):</b> A ⊆ B परंतु A ≠ B।</li>\n<li><b>अंतराल:</b> (a, b) = खुला, [a, b] = बंद, (a, b] = अर्ध-खुला।</li>\n<li><b>घात समुच्चय P(A) ⭐:</b> A के सभी उपसमुच्चयों का समुच्चय। n(A) = n → <b>n(P(A)) = 2ⁿ</b>।</li>\n<li>उचित उपसमुच्चय: 2ⁿ − 1; अरिक्त उचित: 2ⁿ − 2।</li>\n</ul>\n<p class=\"small-note\">💡 2ⁿ क्यों? प्रत्येक अवयव के 2 विकल्प — आए या न आए। n अवयव → 2ⁿ!</p>"
   },
   {
    "h": "4️⃣ वेन आरेख और संक्रियाएं — संघ, सर्वनिष्ठ ⭐",
    "body": "<ul>\n<li><b>वेन आरेख:</b> समुच्चयों को वृत्तों से, सार्वत्रिक को आयत से दर्शाना।</li>\n<li><b>संघ (A ∪ B):</b> जो A में या B में या दोनों में।</li>\n<li><b>सर्वनिष्ठ (A ∩ B):</b> जो दोनों में उभयनिष्ठ हों।</li>\n<li><b>असंयुक्त समुच्चय ⭐:</b> A ∩ B = φ — कुछ उभयनिष्ठ नहीं।</li>\n<li><b>अंतर (A − B):</b> जो A में हों पर B में नहीं।</li>\n<li><b>पूरक (A′) ⭐:</b> U में जो A में नहीं। (A′)′ = A।</li>\n<li><b>गिनती सूत्र ⭐:</b> n(A ∪ B) = n(A) + n(B) − n(A ∩ B)।</li>\n</ul>\n<p class=\"small-note\">💡 संघ = OR, सर्वनिष्ठ = AND, पूरक = NOT।</p>"
   },
   {
    "h": "5️⃣ संक्रियाओं के नियम — बीजगणित जैसा खेल",
    "body": "<ul>\n<li><b>क्रमविनिमेय:</b> A ∪ B = B ∪ A।</li>\n<li><b>साहचर्य:</b> (A ∪ B) ∪ C = A ∪ (B ∪ C)।</li>\n<li><b>वितरण ⭐:</b> A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)।</li>\n<li><b>डी मॉर्गन नियम ⭐⭐:</b> (A ∪ B)′ = A′ ∩ B′ और (A ∩ B)′ = A′ ∪ B′ — पूरक अंदर जाकर चिह्न बदल देता है!</li>\n<li><b>तत्समक:</b> A ∪ φ = A, A ∩ U = A।</li>\n<li><b>तीन समुच्चयों की गिनती:</b> n(A∪B∪C) = n(A)+n(B)+n(C) − n(A∩B) − n(B∩C) − n(A∩C) + n(A∩B∩C) ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 डी मॉर्गन = सबसे अधिक पूछा जाने वाला नियम!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ What Is a Set — The Rulebook of Collections",
    "body": "<ul>\n<li><b>Set:</b> a well-defined collection of objects — \"well-defined\" means anyone can tell what is in and what is out. (\"The 5 vowels\" = a set; \"5 good students\" = NOT a set — subjective!)</li>\n<li><b>Elements/members:</b> the objects in the set. a ∈ A (a belongs to A), b ∉ A.</li>\n<li><b>Roster form:</b> list all elements — V = {a, e, i, o, u}. <b>Set-builder form ⭐:</b> state the property — V = {x : x is a vowel in the English alphabet}.</li>\n<li><b>Order does not matter</b> — {1, 2, 3} = {3, 2, 1}. Repetition means nothing — {1, 1, 2} = {1, 2}.</li>\n<li><b>Important sets ⭐:</b> N (natural: 1, 2, 3...), W (whole: 0, 1, 2...), Z (integers), Q (rationals: p/q form), R (reals).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: a set is a club with clear membership rules. Clear rule, valid set; fuzzy rule, no set!</p>"
   },
   {
    "h": "2️⃣ Types of Sets — From Empty to Universal ⭐",
    "body": "<ul>\n<li><b>Empty/null set (φ or {}):</b> no elements — {x : x is an even prime &gt; 2} = φ. (There is only ONE empty set!)</li>\n<li><b>Finite set:</b> elements can be counted — {days of the week} (7). <b>Infinite set:</b> counting never ends — N, Z, R.</li>\n<li><b>Equal sets ⭐:</b> the SAME elements — {1,2,3} = {3,2,1}. <b>Equivalent sets:</b> the same COUNT (cardinality), possibly different elements — {1,2,3} and {a,b,c}.</li>\n<li><b>Singleton set:</b> exactly 1 element — {0}, {5}.</li>\n<li><b>Universal set (U):</b> the biggest set in the context, holding everything under discussion.</li>\n<li><b>Cardinal number:</b> how many elements — n(A). n(φ) = 0.</li>\n</ul>\n<p class=\"small-note\">🎯 Equal vs equivalent is a favourite exam confusion! Equal = same members; equivalent = same count only.</p>"
   },
   {
    "h": "3️⃣ Subsets and the Power Set ⭐",
    "body": "<ul>\n<li><b>Subset (⊆):</b> every element of A is in B → A ⊆ B. Every set is its own subset; φ is a subset of EVERY set! ⭐</li>\n<li><b>Proper subset (⊂):</b> A ⊆ B but A ≠ B — B has something extra.</li>\n<li><b>Intervals are subsets of R:</b> (a, b) = open (endpoints excluded), [a, b] = closed (included), (a, b] = half-open.</li>\n<li><b>Power set P(A) ⭐:</b> the set of ALL subsets of A. If n(A) = n → <b>n(P(A)) = 2ⁿ</b>. The power set of {a, b}: {φ, {a}, {b}, {a,b}} — 4 = 2²!</li>\n<li>Proper subsets: 2ⁿ − 1; non-empty proper subsets: 2ⁿ − 2.</li>\n</ul>\n<p class=\"small-note\">💡 Why 2ⁿ? Every element has 2 choices — be in the subset or not. n elements → 2×2×... (n times) = 2ⁿ!</p>"
   },
   {
    "h": "4️⃣ Venn Diagrams and Operations — Union, Intersection ⭐",
    "body": "<ul>\n<li><b>Venn diagram:</b> sets as circles inside a universal-set rectangle — the best visualization tool!</li>\n<li><b>Union (A ∪ B):</b> whatever is in A OR B OR both — merge everything (no repeats!).</li>\n<li><b>Intersection (A ∩ B):</b> whatever is in BOTH — the overlap.</li>\n<li><b>Disjoint sets ⭐:</b> A ∩ B = φ — nothing in common (even and odd numbers).</li>\n<li><b>Difference (A − B):</b> what is in A but NOT in B. Generally A − B ≠ B − A!</li>\n<li><b>Complement (A′ or Aᶜ) ⭐:</b> everything in U NOT in A — U − A. (A′)′ = A — a double negative!</li>\n<li><b>Counting formula ⭐:</b> n(A ∪ B) = n(A) + n(B) − n(A ∩ B) — the intersection gets double-counted, so subtract it!</li>\n</ul>\n<p class=\"small-note\">💡 Union = OR (in either), Intersection = AND (in both), Complement = NOT (everything outside).</p>"
   },
   {
    "h": "5️⃣ Laws of Set Operations — An Algebra-like Game",
    "body": "<ul>\n<li><b>Commutative:</b> A ∪ B = B ∪ A, A ∩ B = B ∩ A.</li>\n<li><b>Associative:</b> (A ∪ B) ∪ C = A ∪ (B ∪ C); same for intersection.</li>\n<li><b>Distributive ⭐:</b> A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C); A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).</li>\n<li><b>De Morgan's laws ⭐⭐:</b> (A ∪ B)′ = A′ ∩ B′ and (A ∩ B)′ = A′ ∪ B′ — the complement flips the sign as it moves in (∪ ↔ ∩)!</li>\n<li><b>Identity laws:</b> A ∪ φ = A, A ∩ U = A, A ∪ U = U, A ∩ φ = φ.</li>\n<li><b>Three-set counting:</b> n(A∪B∪C) = n(A)+n(B)+n(C) − n(A∩B) − n(B∩C) − n(A∩C) + n(A∩B∩C) ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 De Morgan is the most-asked law: \"the complement of a union is the intersection of the complements\" (and vice versa).</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics",
    "items": [
     "Set = well-defined collection",
     "Roster: {a,e,i,o,u}; Set-builder: {x: property}",
     "Order/repetition matter nahi"
    ]
   },
   {
    "h": "Types ⭐",
    "items": [
     "φ = empty; singleton = 1 element",
     "Equal = same elements; equivalent = same count",
     "N ⊂ W ⊂ Z ⊂ Q ⊂ R"
    ]
   },
   {
    "h": "Subsets ⭐",
    "items": [
     "φ har set ka subset",
     "Power set: 2ⁿ subsets",
     "Proper subsets: 2ⁿ − 1"
    ]
   },
   {
    "h": "Operations ⭐",
    "items": [
     "∪ = OR, ∩ = AND, ′ = NOT",
     "A−B: A me, B me nahi",
     "n(A∪B) = n(A)+n(B)−n(A∩B)"
    ]
   },
   {
    "h": "Laws ⭐",
    "items": [
     "De Morgan: (A∪B)′ = A′∩B′",
     "(A∩B)′ = A′∪B′",
     "Distributive dono taraf"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल",
    "items": [
     "समुच्चय = सुपरिभाषित संग्रह",
     "रोस्टर vs समुच्चय-निर्माता",
     "क्रम/पुनरावृत्ति महत्वहीन"
    ]
   },
   {
    "h": "प्रकार ⭐",
    "items": [
     "φ = रिक्त; एकल = 1 अवयव",
     "समान = समान अवयव; तुल्य = समान संख्या",
     "N ⊂ W ⊂ Z ⊂ Q ⊂ R"
    ]
   },
   {
    "h": "उपसमुच्चय ⭐",
    "items": [
     "φ प्रत्येक का उपसमुच्चय",
     "घात समुच्चय: 2ⁿ",
     "उचित: 2ⁿ − 1"
    ]
   },
   {
    "h": "संक्रियाएं ⭐",
    "items": [
     "∪ = OR, ∩ = AND, ′ = NOT",
     "A−B: A में, B में नहीं",
     "n(A∪B) = n(A)+n(B)−n(A∩B)"
    ]
   },
   {
    "h": "नियम ⭐",
    "items": [
     "डी मॉर्गन: (A∪B)′ = A′∩B′",
     "(A∩B)′ = A′∪B′",
     "वितरण दोनों ओर"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics",
    "items": [
     "Set = well-defined collection",
     "Roster: {a,e,i,o,u}; Set-builder: {x: property}",
     "Order/repetition do not matter"
    ]
   },
   {
    "h": "Types ⭐",
    "items": [
     "φ = empty; singleton = 1 element",
     "Equal = same elements; equivalent = same count",
     "N ⊂ W ⊂ Z ⊂ Q ⊂ R"
    ]
   },
   {
    "h": "Subsets ⭐",
    "items": [
     "φ is a subset of every set",
     "Power set: 2ⁿ subsets",
     "Proper subsets: 2ⁿ − 1"
    ]
   },
   {
    "h": "Operations ⭐",
    "items": [
     "∪ = OR, ∩ = AND, ′ = NOT",
     "A−B: in A, not in B",
     "n(A∪B) = n(A)+n(B)−n(A∩B)"
    ]
   },
   {
    "h": "Laws ⭐",
    "items": [
     "De Morgan: (A∪B)′ = A′∩B′",
     "(A∩B)′ = A′∪B′",
     "Distributive both ways"
    ]
   }
  ]
 },
 "practice": [
  [
   "{x : x² = 9, x ∈ Z} ko roster form me likho.",
   "x² = 9 → x = 3 ya −3 → <b>{−3, 3}</b>."
  ],
  [
   "'5 achhe cricket players' set hai ya nahi?",
   "<b>Nahi</b> — 'achhe' subjective hai, well-defined nahi. Set ke liye rule clear hona chahiye."
  ],
  [
   "A = {1, 2, 3, 4}. Power set me kitne elements?",
   "n(P(A)) = 2⁴ = <b>16</b>."
  ],
  [
   "φ kya har set ka subset hota hai?",
   "<b>Haan</b> — empty set har set ka subset hai (aur har set apna bhi subset hai)."
  ],
  [
   "n(A) = 15, n(B) = 12, n(A∩B) = 5. n(A∪B)?",
   "n(A∪B) = 15 + 12 − 5 = <b>22</b>."
  ],
  [
   "A = {1, 2, 3}, B = {3, 4, 5}. A − B aur B − A?",
   "A − B = <b>{1, 2}</b>, B − A = <b>{4, 5}</b> — barabar nahi hote!"
  ],
  [
   "De Morgan ka first law bolo.",
   "(A ∪ B)′ = <b>A′ ∩ B′</b> — union ka complement = complements ka intersection."
  ],
  [
   "U = {1..10}, A = {1, 3, 5, 7, 9}. A′ kya hai?",
   "A′ = <b>{2, 4, 6, 8, 10}</b> — U me jo A me nahi."
  ],
  [
   "Do sets disjoint kab hote hain?",
   "Jab <b>A ∩ B = φ</b> — kuch bhi common na ho (jaise even aur odd numbers)."
  ],
  [
   "50 students me 30 cricket, 25 football, 10 dono khelte hain. Kitne koi bhi nahi khelte?",
   "n(C∪F) = 30 + 25 − 10 = 45 → koi nahi = 50 − 45 = <b>5</b>."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/maths/ch-2/",
  "title": "Relations and Functions"
 }
}

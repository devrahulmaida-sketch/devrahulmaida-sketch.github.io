# Class 12 Maths, Chapter 1 - Relations and Functions
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 1,
 "title_en": "Relations and Functions",
 "title_hi": "संबंध एवं फलन",
 "tagline": "Relations ke types, equivalence classes aur one-one/onto ka full game",
 "jee": "MEDIUM",
 "meta_desc": "Class 12 Maths Chapter 1: Relations and Functions — long + short notes in Hindi, English, Hinglish. Reflexive, symmetric, transitive, equivalence relations, one-one, onto, bijective functions.",
 "video": None,
 "card_tag": "Relations ke types, equivalence classes aur one-one/onto ka full game",
 "card_topics": [
  "🔗 Relations + types (R/S/T)",
  "⭐ Equivalence relations & classes",
  "🎯 One-one, onto, bijective",
  "🔢 Counting functions"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Relation Kya Hota Hai — Sets Ke Beech Connection",
    "body": "<ul>\n<li><b>Relation:</b> do sets A aur B ke elements ke beech connection — mathematically, A × B (Cartesian product) ka koi bhi subset ek relation hai. (a, b) ∈ R matlab \"a ka b se relation hai\".</li>\n<li><b>Cartesian product A × B:</b> saare ordered pairs (a, b) jahan a ∈ A, b ∈ B. n(A × B) = n(A) × n(B).</li>\n<li><b>Domain:</b> relation me aa rahe saare first elements. <b>Range:</b> saare second elements. <b>Codomain:</b> poora B set (range ⊆ codomain!).</li>\n<li>A set pe total relations: agar n(A) = n, to A × A ke 2^(n²) subsets → <b>2^(n²) possible relations</b>!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: relation = pairing ka rule. \"Is brother of\" bhi ek relation hai logon ke set pe!</p>"
   },
   {
    "h": "2️⃣ Relations Ke Types — Reflexive, Symmetric, Transitive ⭐",
    "body": "<ul>\n<li><b>Empty relation:</b> koi pair nahi. <b>Universal relation:</b> saare pairs (poora A × A).</li>\n<li><b>Reflexive ⭐:</b> HAR element ka khud se relation — (a, a) ∈ R sab a ke liye. (\"Is equal to\" reflexive hai; \"is sister of\" nahi!)</li>\n<li><b>Symmetric ⭐:</b> (a, b) ∈ R → (b, a) ∈ R — relation dono taraf chale. (a ⊥ b symmetric hai.)</li>\n<li><b>Transitive ⭐:</b> (a, b) ∈ R aur (b, c) ∈ R → (a, c) ∈ R — chain complete ho. (a &gt; b, b &gt; c → a &gt; c: transitive!)</li>\n<li>Check karte time: <b>ek bhi counterexample kaafi hai</b> relation todne ke liye; prove karne ke liye SAB pairs check karo.</li>\n</ul>\n<p class=\"small-note\">🎯 Symmetric + Transitive ≠ Reflexive zaroori nahi! Empty relation symmetric aur transitive dono hai, par reflexive nahi. Classic trap!</p>"
   },
   {
    "h": "3️⃣ Equivalence Relation aur Equivalence Classes ⭐",
    "body": "<ul>\n<li><b>Equivalence relation ⭐⭐:</b> jo relation REFLEXIVE + SYMMETRIC + TRANSITIVE teeno ho. Example: \"is congruent to\" triangles pe, \"a − b even hai\" integers pe.</li>\n<li><b>Equivalence class [a]:</b> a se related SAARE elements ka set — [a] = {x : (x, a) ∈ R}. Equivalence classes ya to barabar hoti hain ya disjoint — kabhi partial overlap nahi!</li>\n<li>Equivalence relation set ko <b>partitions</b> me tod deta hai — har element exactly ek class me.</li>\n<li>Example: Z pe R = {(a, b) : a − b, 3 se divisible hai} → classes [0], [1], [2] (remainders!). Yehi modulo arithmetic ka base hai.</li>\n</ul>\n<p class=\"small-note\">💡 Equivalence relation = \"same category\" ka formal version. Classes = alag-alag dabbe jisme samaan sort ho jaata hai.</p>"
   },
   {
    "h": "4️⃣ Functions — One-One aur Onto ⭐",
    "body": "<ul>\n<li><b>Function f : A → B:</b> har input ka EXACTLY ek output. Har element of A use hona chahiye, aur sirf ek baar map ho.</li>\n<li><b>One-one (injective) ⭐:</b> alag inputs → alag outputs. f(x₁) = f(x₂) → x₁ = x₂. Horizontal line test: koi horizontal line graph ko ek se zyada baar na kaate.</li>\n<li><b>Onto (surjective) ⭐:</b> codomain ka HAR element kisi ka image ho — range = codomain. Koi bhi b ∈ B ke liye f(a) = b ka solution mile.</li>\n<li><b>Bijective ⭐⭐:</b> one-one + onto dono — perfect matching! Tabhi inverse ban sakta hai (par NCERT me inverse function ab deleted hai — bas concept samjho).</li>\n<li>Many-one: multiple inputs same output (f(x) = x² pe 2 aur −2 dono → 4). Into: kuch codomain elements unused.</li>\n</ul>\n<p class=\"small-note\">🎯 f(x) = x²: R → R me one-one NAHI (±2 same image), onto NAHI (negatives ka preimage nahi). Domain/codomain badalte hi answer badal jaata hai — hamesha dono padho!</p>"
   },
   {
    "h": "5️⃣ Functions Ginna aur Smart Checks",
    "body": "<ul>\n<li>n(A) = m, n(B) = n → total functions A → B: <b>n^m</b> (har element ke n choices).</li>\n<li>One-one functions (m ≤ n): <b>ⁿPₘ = n!/(n−m)!</b>. m &gt; n ho to ZERO one-one functions!</li>\n<li>Bijections jab n(A) = n(B) = n: <b>n!</b> — aur tab har onto function apne aap one-one bhi hota hai. ⭐</li>\n<li>Strictly increasing/decreasing function hamesha <b>one-one</b> hota hai (calculus me yahi use hota hai).</li>\n<li>Odd function ya even ho sakta hai: f(−x) = −f(x) (odd), f(−x) = f(x) (even) — one-one check me kaam aata hai.</li>\n</ul>\n<p class=\"small-note\">💡 Finite sets pe: one-one ⟺ onto ⟺ bijective. Infinite pe ye nahi chalta (f(n) = 2n pe N → even numbers: one-one hai par... socho!)</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ संबंध क्या है — समुच्चयों के बीच कनेक्शन",
    "body": "<ul>\n<li><b>संबंध (relation):</b> दो समुच्चयों A और B के अवयवों के बीच संबंध — A × B का कोई भी उपसमुच्चय एक संबंध है।</li>\n<li><b>कार्तीय गुणन A × B:</b> सभी क्रमित युग्म (a, b) जहां a ∈ A, b ∈ B। n(A × B) = n(A) × n(B)।</li>\n<li><b>प्रांत (domain):</b> सभी प्रथम अवयव। <b>परिसर (range):</b> सभी द्वितीय अवयव। <b>सहप्रांत (codomain):</b> पूरा B।</li>\n<li>n अवयवों वाले समुच्चय पर कुल संबंध: <b>2^(n²)</b>।</li>\n</ul>\n<p class=\"small-note\">💡 संबंध = युग्म बनाने का नियम।</p>"
   },
   {
    "h": "2️⃣ संबंधों के प्रकार — स्वतुल्य, सममित, संक्रामक ⭐",
    "body": "<ul>\n<li><b>रिक्त संबंध:</b> कोई युग्म नहीं। <b>सार्वत्रिक संबंध:</b> सभी युग्म।</li>\n<li><b>स्वतुल्य ⭐:</b> प्रत्येक अवयव का स्वयं से संबंध — सभी a के लिए (a, a) ∈ R।</li>\n<li><b>सममित ⭐:</b> (a, b) ∈ R → (b, a) ∈ R — संबंध दोनों ओर चले।</li>\n<li><b>संक्रामक ⭐:</b> (a, b) ∈ R और (b, c) ∈ R → (a, c) ∈ R।</li>\n<li>खंडन के लिए <b>एक प्रत्युदाहरण पर्याप्त</b> है; सिद्ध करने के लिए सभी युग्म जांचें।</li>\n</ul>\n<p class=\"small-note\">🎯 सममित + संक्रामक ≠ स्वतुल्य आवश्यक नहीं! रिक्त संबंध सममित और संक्रामक है, पर स्वतुल्य नहीं।</p>"
   },
   {
    "h": "3️⃣ तुल्यता संबंध और तुल्यता वर्ग ⭐",
    "body": "<ul>\n<li><b>तुल्यता संबंध ⭐⭐:</b> जो स्वतुल्य + सममित + संक्रामक तीनों हो। उदाहरण: \"a − b सम है\" पूर्णांकों पर।</li>\n<li><b>तुल्यता वर्ग [a]:</b> a से संबंधित सभी अवयव — [a] = {x : (x, a) ∈ R}। वर्ग या तो समान होते हैं या असंयुक्त।</li>\n<li>तुल्यता संबंध समुच्चय को <b>विभाजनों</b> में बांटता है — प्रत्येक अवयव ठीक एक वर्ग में।</li>\n<li>उदाहरण: Z पर R = {(a, b) : a − b, 3 से विभाज्य} → वर्ग [0], [1], [2]।</li>\n</ul>\n<p class=\"small-note\">💡 तुल्यता संबंध = \"समान श्रेणी\" का औपचारिक रूप।</p>"
   },
   {
    "h": "4️⃣ फलन — एकैकी और आच्छादक ⭐",
    "body": "<ul>\n<li><b>फलन f : A → B:</b> प्रत्येक इनपुट का ठीक एक आउटपुट।</li>\n<li><b>एकैकी (injective) ⭐:</b> भिन्न इनपुट → भिन्न आउटपुट। f(x₁) = f(x₂) → x₁ = x₂।</li>\n<li><b>आच्छादक (surjective) ⭐:</b> सहप्रांत का प्रत्येक अवयव किसी का प्रतिबिंब हो — परिसर = सहप्रांत।</li>\n<li><b>एकैकी आच्छादक (bijective) ⭐⭐:</b> एकैकी + आच्छादक दोनों — पूर्ण मिलान!</li>\n<li>बहु-एकैकी: कई इनपुट एक ही आउटपुट। अंतःक्षेपी: कुछ सहप्रांत अवयव अप्रयुक्त।</li>\n</ul>\n<p class=\"small-note\">🎯 f(x) = x², R → R: एकैकी नहीं, आच्छादक नहीं। प्रांत/सहप्रांत बदलते ही उत्तर बदल जाता है!</p>"
   },
   {
    "h": "5️⃣ फलनों की गिनती और स्मार्ट जांच",
    "body": "<ul>\n<li>n(A) = m, n(B) = n → कुल फलन: <b>n^m</b>।</li>\n<li>एकैकी फलन (m ≤ n): <b>ⁿPₘ = n!/(n−m)!</b>। m &gt; n हो तो शून्य!</li>\n<li>एकैकी आच्छादक (जब n(A) = n(B) = n): <b>n!</b> — तब प्रत्येक आच्छादक फलन स्वतः एकैकी। ⭐</li>\n<li>निरंतर वर्धमान/ह्रासमान फलन सदैव <b>एकैकी</b>।</li>\n<li>विषम फलन: f(−x) = −f(x); सम फलन: f(−x) = f(x)।</li>\n</ul>\n<p class=\"small-note\">💡 परिमित समुच्चयों पर: एकैकी ⟺ आच्छादक ⟺ एकैकी आच्छादक।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ What Is a Relation — Connecting Two Sets",
    "body": "<ul>\n<li><b>Relation:</b> a connection between elements of sets A and B — mathematically, any subset of A × B (the Cartesian product) is a relation. (a, b) ∈ R means \"a is related to b\".</li>\n<li><b>Cartesian product A × B:</b> all ordered pairs (a, b) with a ∈ A, b ∈ B. n(A × B) = n(A) × n(B).</li>\n<li><b>Domain:</b> all first elements in the relation. <b>Range:</b> all second elements. <b>Codomain:</b> the whole set B (range ⊆ codomain!).</li>\n<li>Relations on a set with n elements: A × A has 2^(n²) subsets → <b>2^(n²) possible relations</b>!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: a relation is a pairing rule. \"Is a brother of\" is a relation on a set of people!</p>"
   },
   {
    "h": "2️⃣ Types of Relations — Reflexive, Symmetric, Transitive ⭐",
    "body": "<ul>\n<li><b>Empty relation:</b> no pairs. <b>Universal relation:</b> all pairs (the full A × A).</li>\n<li><b>Reflexive ⭐:</b> EVERY element relates to itself — (a, a) ∈ R for all a. (\"Is equal to\" is reflexive; \"is sister of\" is not!)</li>\n<li><b>Symmetric ⭐:</b> (a, b) ∈ R → (b, a) ∈ R — the relation runs both ways.</li>\n<li><b>Transitive ⭐:</b> (a, b) ∈ R and (b, c) ∈ R → (a, c) ∈ R — the chain must complete.</li>\n<li>While checking: <b>one counterexample is enough</b> to break a property; to prove it, check ALL pairs.</li>\n</ul>\n<p class=\"small-note\">🎯 Symmetric + Transitive does NOT force Reflexive! The empty relation is symmetric and transitive, but not reflexive. Classic trap!</p>"
   },
   {
    "h": "3️⃣ Equivalence Relations and Classes ⭐",
    "body": "<ul>\n<li><b>Equivalence relation ⭐⭐:</b> one that is REFLEXIVE + SYMMETRIC + TRANSITIVE — all three. Example: \"a − b is even\" on integers.</li>\n<li><b>Equivalence class [a]:</b> ALL elements related to a — [a] = {x : (x, a) ∈ R}. Two classes are either equal or disjoint — never partially overlapping!</li>\n<li>An equivalence relation splits the set into <b>partitions</b> — every element lands in exactly one class.</li>\n<li>Example: R = {(a, b) : a − b divisible by 3} on Z → classes [0], [1], [2] (the remainders!). This is the base of modular arithmetic.</li>\n</ul>\n<p class=\"small-note\">💡 An equivalence relation formalizes \"same category\". Classes = separate boxes into which everything gets sorted.</p>"
   },
   {
    "h": "4️⃣ Functions — One-One and Onto ⭐",
    "body": "<ul>\n<li><b>Function f : A → B:</b> every input has EXACTLY one output. Every element of A must be used, exactly once.</li>\n<li><b>One-one (injective) ⭐:</b> different inputs → different outputs. f(x₁) = f(x₂) → x₁ = x₂. Horizontal line test: no horizontal line cuts the graph more than once.</li>\n<li><b>Onto (surjective) ⭐:</b> EVERY codomain element is some input's image — range = codomain. For every b ∈ B, f(a) = b has a solution.</li>\n<li><b>Bijective ⭐⭐:</b> one-one AND onto — a perfect matching!</li>\n<li>Many-one: several inputs share an output (on f(x) = x², both 2 and −2 map to 4). Into: some codomain elements stay unused.</li>\n</ul>\n<p class=\"small-note\">🎯 f(x) = x², R → R: NOT one-one (±2 give the same image), NOT onto (negatives have no preimage). Change the domain/codomain and the answer changes — always read both!</p>"
   },
   {
    "h": "5️⃣ Counting Functions and Smart Checks",
    "body": "<ul>\n<li>n(A) = m, n(B) = n → total functions A → B: <b>n^m</b> (each element gets n choices).</li>\n<li>One-one functions (m ≤ n): <b>ⁿPₘ = n!/(n−m)!</b>. If m &gt; n, there are ZERO one-one functions!</li>\n<li>Bijections when n(A) = n(B) = n: <b>n!</b> — and then every onto function is automatically one-one. ⭐</li>\n<li>A strictly increasing/decreasing function is always <b>one-one</b> (used heavily in calculus).</li>\n<li>Odd/even functions: f(−x) = −f(x) (odd), f(−x) = f(x) (even) — handy in one-one checks.</li>\n</ul>\n<p class=\"small-note\">💡 On finite sets: one-one ⟺ onto ⟺ bijective. On infinite sets this fails (f(n) = 2n on N → even numbers is one-one but not onto!)</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Relation basics",
    "items": [
     "Relation = A × B ka subset",
     "Domain = first elements, Range = second",
     "n elements pe 2^(n²) relations"
    ]
   },
   {
    "h": "Types ⭐",
    "items": [
     "Reflexive: (a,a) sabke liye",
     "Symmetric: (a,b) → (b,a)",
     "Transitive: (a,b),(b,c) → (a,c)"
    ]
   },
   {
    "h": "Equivalence ⭐",
    "items": [
     "R + S + T teeno chahiye",
     "Equivalence class [a] = a se related sab",
     "Classes: barabar ya disjoint"
    ]
   },
   {
    "h": "Functions ⭐",
    "items": [
     "One-one: alag input → alag output",
     "Onto: range = codomain",
     "Bijective = one-one + onto"
    ]
   },
   {
    "h": "Counting ⭐",
    "items": [
     "Total functions: n^m",
     "One-one: ⁿPₘ",
     "Bijections (equal sets): n!"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल",
    "items": [
     "संबंध = A × B का उपसमुच्चय",
     "प्रांत = प्रथम अवयव, परिसर = द्वितीय",
     "n अवयवों पर 2^(n²) संबंध"
    ]
   },
   {
    "h": "प्रकार ⭐",
    "items": [
     "स्वतुल्य: (a,a) सभी के लिए",
     "सममित: (a,b) → (b,a)",
     "संक्रामक: (a,b),(b,c) → (a,c)"
    ]
   },
   {
    "h": "तुल्यता ⭐",
    "items": [
     "स्वतुल्य + सममित + संक्रामक",
     "वर्ग [a] = a से संबंधित सभी",
     "वर्ग: समान या असंयुक्त"
    ]
   },
   {
    "h": "फलन ⭐",
    "items": [
     "एकैकी: भिन्न इनपुट → भिन्न आउटपुट",
     "आच्छादक: परिसर = सहप्रांत",
     "एकैकी आच्छादक = दोनों"
    ]
   },
   {
    "h": "गिनती ⭐",
    "items": [
     "कुल फलन: n^m",
     "एकैकी: ⁿPₘ",
     "एकैकी आच्छादक (समान समुच्चय): n!"
    ]
   }
  ],
  "en": [
   {
    "h": "Relation basics",
    "items": [
     "Relation = subset of A × B",
     "Domain = first elements, Range = second",
     "n elements → 2^(n²) relations"
    ]
   },
   {
    "h": "Types ⭐",
    "items": [
     "Reflexive: (a,a) for all",
     "Symmetric: (a,b) → (b,a)",
     "Transitive: (a,b),(b,c) → (a,c)"
    ]
   },
   {
    "h": "Equivalence ⭐",
    "items": [
     "Needs R + S + T",
     "Class [a] = everything related to a",
     "Classes: equal or disjoint"
    ]
   },
   {
    "h": "Functions ⭐",
    "items": [
     "One-one: distinct inputs → distinct outputs",
     "Onto: range = codomain",
     "Bijective = one-one + onto"
    ]
   },
   {
    "h": "Counting ⭐",
    "items": [
     "Total functions: n^m",
     "One-one: ⁿPₘ",
     "Bijections (equal sets): n!"
    ]
   }
  ]
 },
 "practice": [
  [
   "A = {1, 2, 3} pe kitne relations possible hain?",
   "n(A) = 3 → A × A me 9 pairs → <b>2⁹ = 512</b> relations."
  ],
  [
   "R = {(a, b) : a = b} on Z — reflexive hai?",
   "<b>Haan</b> — har a ke liye (a, a) ∈ R kyunki a = a. (Symmetric aur transitive bhi hai — equivalence relation!)"
  ],
  [
   "R = {(a, b) : a < b} on R — symmetric hai?",
   "<b>Nahi</b> — 1 < 2 matlab (1, 2) ∈ R, par 2 < 1 false hai, to (2, 1) ∉ R."
  ],
  [
   "'Is friend of' relation symmetric hai par transitive kyun nahi?",
   "A friend of B aur B friend of C ka matlab ye nahi ki A friend of C — <b>transitive fail</b>. Dosti chain guarantee nahi deti!"
  ],
  [
   "Equivalence class kya hota hai?",
   "[a] = {x : (x, a) ∈ R} — <b>a se related saare elements ka set</b>. Do classes ya to same hoti hain ya disjoint."
  ],
  [
   "f(x) = x², f : R → R. One-one hai?",
   "<b>Nahi</b> — f(2) = f(−2) = 4, alag inputs ka same output."
  ],
  [
   "f(x) = 2x + 3, f : R → R. Onto hai?",
   "<b>Haan</b> — koi bhi y ∈ R ke liye x = (y − 3)/2 ∈ R deta hai f(x) = y. Range = codomain. (One-one bhi hai → bijective!)"
  ],
  [
   "n(A) = 3, n(B) = 5. A → B kitne one-one functions?",
   "⁵P₃ = 5×4×3 = <b>60</b>."
  ],
  [
   "n(A) = n(B) = 4. Kitne bijective functions?",
   "4! = <b>24</b> — equal finite sets pe bijection = permutation."
  ],
  [
   "Ek relation symmetric aur transitive hai. Kya reflexive zaroor hoga?",
   "<b>Zaroori nahi</b> — empty relation (ya {(a,b),(b,a),(a,a),(b,b)} jaisa partial) counterexample hai. Sab elements ka self-pair hona alag se check karna padta hai."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-2/",
  "title": "Inverse Trigonometric Functions"
 }
}

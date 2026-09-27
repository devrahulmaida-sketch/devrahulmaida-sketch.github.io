# Class 11 Maths, Chapter 2 - Relations and Functions
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 2,
 "title_en": "Relations and Functions",
 "title_hi": "संबंध एवं फलन",
 "tagline": "Ordered pairs se functions tak — domain, range aur graphs",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 2: Relations and Functions — long + short notes in Hindi, English, Hinglish. Cartesian product, relations, functions, domain, range, modulus, greatest integer function.",
 "video": None,
 "card_tag": "Ordered pairs se functions tak — domain, range aur graphs",
 "card_topics": [
  "🔗 Cartesian product",
  "📊 Relations + domain/range",
  "⚙️ Functions + vertical line test",
  "📈 |x|, [x], 1/x graphs"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Cartesian Product — Ordered Pairs Ki Duniya",
    "body": "<ul>\n<li><b>Ordered pair (a, b):</b> order MATTER karta hai — (a, b) ≠ (b, a) jab tak a = b na ho. (Sets se yahi farak — {a,b} = {b,a} par (a,b) ≠ (b,a)!)</li>\n<li><b>Cartesian product ⭐:</b> A × B = {(a, b) : a ∈ A, b ∈ B} — A ke har element ko B ke har element se jodo. Coordinates ka origin yahi hai!</li>\n<li><b>Counting:</b> n(A × B) = n(A) × n(B). A me 3, B me 4 → 12 ordered pairs.</li>\n<li><b>Non-commutative:</b> A × B ≠ B × A (jab A ≠ B). A × φ = φ.</li>\n<li><b>Real plane:</b> R × R = R² — poora coordinate plane! Har point (x, y) ek ordered pair hai.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: A = {shirts}, B = {pants} — A × B = saare possible outfits! Order matter karta hai: (shirt, pant) outfit hai, (pant, shirt) ulta likhna.</p>"
   },
   {
    "h": "2️⃣ Relations — Connections Ka Set ⭐",
    "body": "<ul>\n<li><b>Relation ⭐:</b> A × B ka koi bhi SUBSET — yani A se B ke beech connections ka collection. R ⊆ A × B.</li>\n<li><b>Domain:</b> relation me involved A ke saare elements (first components). <b>Range:</b> involved B ke elements (second components). <b>Codomain:</b> poora B (range ⊆ codomain!). ⭐</li>\n<li><b>Total relations possible:</b> A × B ke subsets = 2^(n(A)×n(B)).</li>\n<li><b>Example:</b> A = {students}, B = {subjects}, R = {(student, subject) : student passes subject} — real life relation!</li>\n<li><b>Arrow diagrams aur roster form</b> se relation likhte hain; set-builder bhi: R = {(x, y) : y = x + 1, x ∈ A}.</li>\n</ul>\n<p class=\"small-note\">🎯 Range vs codomain confusion pakka aata hai: codomain = pura target set B; range = jo actually hit hua (chhota ya barabar).</p>"
   },
   {
    "h": "3️⃣ Functions — Har Input Ka Ek Hi Output ⭐",
    "body": "<ul>\n<li><b>Function ⭐:</b> aisa relation jisme A ka HAR element ka B me EXACTLY EK image ho. Do conditions: (1) koi element chhoota nahi, (2) kisi ke do images nahi.</li>\n<li><b>Notation:</b> f : A → B, f(x) = image. A = domain, B = codomain.</li>\n<li><b>Check karna:</b> arrow diagram me har input se EXACTLY ek arrow — do arrows ya zero arrow = function NAHI!</li>\n<li><b>Examples:</b> f(x) = x² (har x ka ek square ✓); x² + y² = 25 se y alone function nahi (ek x ke do y — ±!). ⭐</li>\n<li><b>Vertical line test (graphs pe):</b> koi bhi vertical line graph ko ek se zyada jagah kaate to function nahi.</li>\n<li><b>Identity function:</b> f(x) = x. <b>Constant function:</b> f(x) = c (sabka same image).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: function = vending machine — har button (input) pe exactly ek item (output). Ek button pe do items ya koi button dead → machine kharab (function nahi)!</p>"
   },
   {
    "h": "4️⃣ Important Functions Aur Unke Graphs ⭐",
    "body": "<table class=\"tbl\">\n<tr><th>Function</th><th>Formula</th><th>Domain</th><th>Range</th></tr>\n<tr><td>Identity</td><td>f(x) = x</td><td>R</td><td>R</td></tr>\n<tr><td>Constant</td><td>f(x) = c</td><td>R</td><td>{c}</td></tr>\n<tr><td>Polynomial</td><td>f(x) = x², x³...</td><td>R</td><td>x²: [0, ∞)</td></tr>\n<tr><td>Rational</td><td>f(x) = 1/x</td><td>R − {0}</td><td>R − {0}</td></tr>\n<tr><td>Modulus ⭐</td><td>f(x) = |x|</td><td>R</td><td>[0, ∞)</td></tr>\n<tr><td>Signum</td><td>f(x) = x/|x|</td><td>R − {0}</td><td>{−1, 0, 1}</td></tr>\n<tr><td>Greatest integer ⭐</td><td>f(x) = [x]</td><td>R</td><td>Z</td></tr>\n</table>\n<ul>\n<li><b>|x|:</b> V-shape graph — x ≥ 0 pe y = x, x &lt; 0 pe y = −x. Hamesha non-negative output!</li>\n<li><b>[x] (floor):</b> sabse bada integer ≤ x — [3.7] = 3, [−2.3] = <b>−3</b> (neeche jaate hain, zero ki taraf nahi!). ⭐</li>\n<li><b>Signum:</b> positive pe 1, negative pe −1, zero pe 0.</li>\n<li><b>1/x graph:</b> hyperbola — x = 0 pe undefined (asymptote!), do branches.</li>\n</ul>\n<p class=\"small-note\">🎯 [−2.3] = −3 sabse common trap! Floor hamesha LEFT jaata hai number line pe, zero ki taraf nahi.</p>"
   },
   {
    "h": "5️⃣ Algebra of Functions — Jod, Ghata, Guna, Bhag",
    "body": "<ul>\n<li><b>Addition:</b> (f + g)(x) = f(x) + g(x) — same domain pe pointwise jodo.</li>\n<li><b>Subtraction:</b> (f − g)(x) = f(x) − g(x).</li>\n<li><b>Multiplication:</b> (fg)(x) = f(x)·g(x).</li>\n<li><b>Division ⭐:</b> (f/g)(x) = f(x)/g(x) — jahan g(x) ≠ 0 (domain se woh points nikal do!).</li>\n<li><b>Scalar multiple:</b> (αf)(x) = α·f(x).</li>\n<li><b>Domains:</b> sum/difference/product ka domain = dono domains ka INTERSECTION; quotient ka = intersection minus g ke zeros. ⭐</li>\n<li>Example: f(x) = √x (domain x ≥ 0), g(x) = 1/x (domain x ≠ 0) → (f+g) ka domain = (0, ∞).</li>\n</ul>\n<p class=\"small-note\">💡 Functions ka algebra easy hai — bas yaad rakho domain intersection hota hai, aur divide karte time denominator ke zeros hatao!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ कार्तीय गुणन — क्रमित युग्मों की दुनिया",
    "body": "<ul>\n<li><b>क्रमित युग्म (a, b):</b> क्रम महत्वपूर्ण — (a, b) ≠ (b, a) जब तक a = b न हो।</li>\n<li><b>कार्तीय गुणन ⭐:</b> A × B = {(a, b) : a ∈ A, b ∈ B} — A के प्रत्येक अवयव को B के प्रत्येक से जोड़ो।</li>\n<li><b>गिनती:</b> n(A × B) = n(A) × n(B)।</li>\n<li><b>अक्रमविनिमेय:</b> A × B ≠ B × A (जब A ≠ B)। A × φ = φ।</li>\n<li><b>वास्तविक तल:</b> R × R = R² — पूरा निर्देशांक तल!</li>\n</ul>\n<p class=\"small-note\">💡 A = {शर्ट}, B = {पैंट} — A × B = सभी संभव पोशाकें!</p>"
   },
   {
    "h": "2️⃣ संबंध — संपर्कों का समुच्चय ⭐",
    "body": "<ul>\n<li><b>संबंध ⭐:</b> A × B का कोई भी उपसमुच्चय। R ⊆ A × B।</li>\n<li><b>प्रांत (domain):</b> संबंध में प्रयुक्त A के अवयव। <b>परिसर (range):</b> प्रयुक्त B के अवयव। <b>सहप्रांत (codomain):</b> पूरा B (परिसर ⊆ सहप्रांत!)। ⭐</li>\n<li><b>कुल संबंध:</b> 2^(n(A)×n(B))।</li>\n<li><b>उदाहरण:</b> R = {(x, y) : y = x + 1, x ∈ A}।</li>\n</ul>\n<p class=\"small-note\">🎯 परिसर बनाम सहप्रांत: सहप्रांत = पूरा लक्ष्य समुच्चय; परिसर = जो वास्तव में प्राप्त हुआ।</p>"
   },
   {
    "h": "3️⃣ फलन — हर इनपुट का एक ही आउटपुट ⭐",
    "body": "<ul>\n<li><b>फलन ⭐:</b> ऐसा संबंध जिसमें A का प्रत्येक अवयव का B में <b>ठीक एक</b> प्रतिबिंब हो।</li>\n<li><b>संकेत:</b> f : A → B, f(x) = प्रतिबिंब।</li>\n<li><b>जांच:</b> हर इनपुट से ठीक एक तीर — दो तीर या शून्य = फलन नहीं!</li>\n<li><b>उदाहरण:</b> f(x) = x² ✓; x² + y² = 25 से y फलन नहीं (एक x के दो y — ±!)। ⭐</li>\n<li><b>ऊर्ध्व रेखा परीक्षण:</b> कोई ऊर्ध्व रेखा आलेख को एक से अधिक बार काटे तो फलन नहीं।</li>\n<li><b>तत्समक फलन:</b> f(x) = x। <b>अचर फलन:</b> f(x) = c।</li>\n</ul>\n<p class=\"small-note\">💡 फलन = वेंडिंग मशीन — हर बटन पर ठीक एक आइटम!</p>"
   },
   {
    "h": "4️⃣ महत्वपूर्ण फलन और उनके आलेख ⭐",
    "body": "<table class=\"tbl\">\n<tr><th>फलन</th><th>सूत्र</th><th>प्रांत</th><th>परिसर</th></tr>\n<tr><td>तत्समक</td><td>f(x) = x</td><td>R</td><td>R</td></tr>\n<tr><td>अचर</td><td>f(x) = c</td><td>R</td><td>{c}</td></tr>\n<tr><td>परिमेय</td><td>f(x) = 1/x</td><td>R − {0}</td><td>R − {0}</td></tr>\n<tr><td>मापांक ⭐</td><td>f(x) = |x|</td><td>R</td><td>[0, ∞)</td></tr>\n<tr><td>चिह्न (signum)</td><td>f(x) = x/|x|</td><td>R − {0}</td><td>{−1, 0, 1}</td></tr>\n<tr><td>महत्तम पूर्णांक ⭐</td><td>f(x) = [x]</td><td>R</td><td>Z</td></tr>\n</table>\n<ul>\n<li><b>|x|:</b> V-आकार आलेख — सदैव ऋणेतर आउटपुट!</li>\n<li><b>[x] (floor):</b> x से छोटा या बराबर सबसे बड़ा पूर्णांक — [3.7] = 3, [−2.3] = <b>−3</b>! ⭐</li>\n<li><b>1/x आलेख:</b> अतिपरवलय — x = 0 पर अपरिभाषित (अनंतस्पर्शी!), दो शाखाएं।</li>\n</ul>\n<p class=\"small-note\">🎯 [−2.3] = −3 सबसे बड़ा जाल! Floor संख्या रेखा पर सदैव बाएं जाता है।</p>"
   },
   {
    "h": "5️⃣ फलनों की बीजगणित — जोड़, घटाव, गुणा, भाग",
    "body": "<ul>\n<li><b>योग:</b> (f + g)(x) = f(x) + g(x)।</li>\n<li><b>अंतर:</b> (f − g)(x) = f(x) − g(x)।</li>\n<li><b>गुणन:</b> (fg)(x) = f(x)·g(x)।</li>\n<li><b>भाग ⭐:</b> (f/g)(x) = f(x)/g(x) — जहां g(x) ≠ 0!</li>\n<li><b>प्रांत:</b> योग/अंतर/गुणन का प्रांत = दोनों प्रांतों का सर्वनिष्ठ; भाग का = सर्वनिष्ठ ऋण g के शून्य। ⭐</li>\n<li>उदाहरण: f(x) = √x (x ≥ 0), g(x) = 1/x (x ≠ 0) → (f+g) का प्रांत = (0, ∞)।</li>\n</ul>\n<p class=\"small-note\">💡 प्रांत सर्वनिष्ठ होता है, और भाग में हर के शून्य हटाओ!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Cartesian Product — The World of Ordered Pairs",
    "body": "<ul>\n<li><b>Ordered pair (a, b):</b> order MATTERS — (a, b) ≠ (b, a) unless a = b. (This is exactly how pairs differ from sets — {a,b} = {b,a} but (a,b) ≠ (b,a)!)</li>\n<li><b>Cartesian product ⭐:</b> A × B = {(a, b) : a ∈ A, b ∈ B} — pair every element of A with every element of B. This is the origin of coordinates!</li>\n<li><b>Counting:</b> n(A × B) = n(A) × n(B). 3 in A, 4 in B → 12 ordered pairs.</li>\n<li><b>Non-commutative:</b> A × B ≠ B × A (when A ≠ B). A × φ = φ.</li>\n<li><b>The real plane:</b> R × R = R² — the whole coordinate plane! Every point (x, y) is an ordered pair.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: A = {shirts}, B = {pants} — A × B = every possible outfit! Order matters: (shirt, pant) is an outfit; (pant, shirt) is writing it backwards.</p>"
   },
   {
    "h": "2️⃣ Relations — A Set of Connections ⭐",
    "body": "<ul>\n<li><b>Relation ⭐:</b> ANY subset of A × B — a collection of connections from A to B. R ⊆ A × B.</li>\n<li><b>Domain:</b> all elements of A involved in the relation (first components). <b>Range:</b> the involved elements of B (second components). <b>Codomain:</b> the whole of B (range ⊆ codomain!). ⭐</li>\n<li><b>Total possible relations:</b> subsets of A × B = 2^(n(A)×n(B)).</li>\n<li><b>Example:</b> A = {students}, B = {subjects}, R = {(student, subject) : student passed the subject} — a real-life relation!</li>\n<li>Write relations with arrow diagrams, rosters, or set-builder form: R = {(x, y) : y = x + 1, x ∈ A}.</li>\n</ul>\n<p class=\"small-note\">🎯 The range-vs-codomain confusion is guaranteed in exams: codomain = the full target set B; range = what actually gets hit (smaller or equal).</p>"
   },
   {
    "h": "3️⃣ Functions — Exactly One Output per Input ⭐",
    "body": "<ul>\n<li><b>Function ⭐:</b> a relation where EVERY element of A has EXACTLY ONE image in B. Two conditions: (1) no element left out, (2) no element has two images.</li>\n<li><b>Notation:</b> f : A → B, f(x) = the image. A = domain, B = codomain.</li>\n<li><b>Checking:</b> in an arrow diagram every input must have EXACTLY one arrow — two arrows or none means NOT a function!</li>\n<li><b>Examples:</b> f(x) = x² (every x has one square ✓); from x² + y² = 25, y alone is not a function (one x gives two y's — ±!). ⭐</li>\n<li><b>Vertical line test:</b> if any vertical line cuts the graph more than once, it is not a function.</li>\n<li><b>Identity function:</b> f(x) = x. <b>Constant function:</b> f(x) = c (same image for all).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: a function is a vending machine — every button (input) gives exactly one item (output). Two items from one button or a dead button means the machine is broken (not a function)!</p>"
   },
   {
    "h": "4️⃣ Important Functions and Their Graphs ⭐",
    "body": "<table class=\"tbl\">\n<tr><th>Function</th><th>Formula</th><th>Domain</th><th>Range</th></tr>\n<tr><td>Identity</td><td>f(x) = x</td><td>R</td><td>R</td></tr>\n<tr><td>Constant</td><td>f(x) = c</td><td>R</td><td>{c}</td></tr>\n<tr><td>Polynomial</td><td>f(x) = x², x³...</td><td>R</td><td>x²: [0, ∞)</td></tr>\n<tr><td>Rational</td><td>f(x) = 1/x</td><td>R − {0}</td><td>R − {0}</td></tr>\n<tr><td>Modulus ⭐</td><td>f(x) = |x|</td><td>R</td><td>[0, ∞)</td></tr>\n<tr><td>Signum</td><td>f(x) = x/|x|</td><td>R − {0}</td><td>{−1, 0, 1}</td></tr>\n<tr><td>Greatest integer ⭐</td><td>f(x) = [x]</td><td>R</td><td>Z</td></tr>\n</table>\n<ul>\n<li><b>|x|:</b> V-shaped graph — y = x when x ≥ 0, y = −x when x &lt; 0. Always non-negative output!</li>\n<li><b>[x] (floor):</b> the greatest integer ≤ x — [3.7] = 3, [−2.3] = <b>−3</b> (go down, not toward zero!). ⭐</li>\n<li><b>Signum:</b> 1 for positive, −1 for negative, 0 for zero.</li>\n<li><b>1/x graph:</b> a hyperbola — undefined at x = 0 (asymptote!), two branches.</li>\n</ul>\n<p class=\"small-note\">🎯 [−2.3] = −3 is the most common trap! Floor always moves LEFT on the number line, not toward zero.</p>"
   },
   {
    "h": "5️⃣ Algebra of Functions — Add, Subtract, Multiply, Divide",
    "body": "<ul>\n<li><b>Addition:</b> (f + g)(x) = f(x) + g(x) — pointwise on the same domain.</li>\n<li><b>Subtraction:</b> (f − g)(x) = f(x) − g(x).</li>\n<li><b>Multiplication:</b> (fg)(x) = f(x)·g(x).</li>\n<li><b>Division ⭐:</b> (f/g)(x) = f(x)/g(x) — wherever g(x) ≠ 0 (remove those points from the domain!).</li>\n<li><b>Scalar multiple:</b> (αf)(x) = α·f(x).</li>\n<li><b>Domains:</b> the domain of a sum/difference/product = the INTERSECTION of the two domains; for a quotient = intersection minus the zeros of g. ⭐</li>\n<li>Example: f(x) = √x (domain x ≥ 0), g(x) = 1/x (domain x ≠ 0) → domain of (f+g) = (0, ∞).</li>\n</ul>\n<p class=\"small-note\">💡 The algebra of functions is easy — just remember the domain is an intersection, and when dividing, drop the denominator's zeros!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Cartesian ⭐",
    "items": [
     "A×B = {(a,b): a∈A, b∈B}",
     "n(A×B) = n(A)×n(B)",
     "A×B ≠ B×A"
    ]
   },
   {
    "h": "Relations",
    "items": [
     "Relation = A×B ka subset",
     "Range ⊆ codomain (B)",
     "Total relations: 2^(mn)"
    ]
   },
   {
    "h": "Function ⭐",
    "items": [
     "Har input → exactly 1 output",
     "Vertical line test",
     "x²+y²=25: y function nahi"
    ]
   },
   {
    "h": "Key Functions ⭐",
    "items": [
     "|x|: V-shape, range [0,∞)",
     "[x]: floor, [−2.3] = −3",
     "1/x: domain x≠0, hyperbola"
    ]
   },
   {
    "h": "Algebra",
    "items": [
     "(f±g)(x), (fg)(x) pointwise",
     "(f/g): g(x)≠0 wale points hatao",
     "Domain = intersection"
    ]
   }
  ],
  "hi": [
   {
    "h": "कार्तीय ⭐",
    "items": [
     "A×B = {(a,b)}",
     "n(A×B) = n(A)×n(B)",
     "A×B ≠ B×A"
    ]
   },
   {
    "h": "संबंध",
    "items": [
     "संबंध = A×B का उपसमुच्चय",
     "परिसर ⊆ सहप्रांत",
     "कुल संबंध: 2^(mn)"
    ]
   },
   {
    "h": "फलन ⭐",
    "items": [
     "हर इनपुट → ठीक 1 आउटपुट",
     "ऊर्ध्व रेखा परीक्षण",
     "x²+y²=25: y फलन नहीं"
    ]
   },
   {
    "h": "मुख्य फलन ⭐",
    "items": [
     "|x|: V-आकार, परिसर [0,∞)",
     "[x]: floor, [−2.3] = −3",
     "1/x: प्रांत x≠0"
    ]
   },
   {
    "h": "बीजगणित",
    "items": [
     "(f±g)(x), (fg)(x)",
     "(f/g): g(x)≠0",
     "प्रांत = सर्वनिष्ठ"
    ]
   }
  ],
  "en": [
   {
    "h": "Cartesian ⭐",
    "items": [
     "A×B = {(a,b): a∈A, b∈B}",
     "n(A×B) = n(A)×n(B)",
     "A×B ≠ B×A"
    ]
   },
   {
    "h": "Relations",
    "items": [
     "Relation = subset of A×B",
     "Range ⊆ codomain (B)",
     "Total relations: 2^(mn)"
    ]
   },
   {
    "h": "Function ⭐",
    "items": [
     "Every input → exactly 1 output",
     "Vertical line test",
     "x²+y²=25: y not a function"
    ]
   },
   {
    "h": "Key Functions ⭐",
    "items": [
     "|x|: V-shape, range [0,∞)",
     "[x]: floor, [−2.3] = −3",
     "1/x: domain x≠0, hyperbola"
    ]
   },
   {
    "h": "Algebra",
    "items": [
     "(f±g)(x), (fg)(x) pointwise",
     "(f/g): remove zeros of g",
     "Domain = intersection"
    ]
   }
  ]
 },
 "practice": [
  [
   "A = {1, 2}, B = {a, b, c}. n(A × B)?",
   "n(A×B) = 2×3 = <b>6</b>."
  ],
  [
   "(a, b) = (3, 5) hai to a aur b?",
   "Ordered pair me components match: a = <b>3</b>, b = <b>5</b>."
  ],
  [
   "R = {(1,2), (2,4), (3,6)} ka domain aur range?",
   "Domain = <b>{1, 2, 3}</b>, Range = <b>{2, 4, 6}</b>."
  ],
  [
   "Range aur codomain me kya farak?",
   "Codomain = <b>poora target set</b>; range = jo actually images banaye (<b>range ⊆ codomain</b>)."
  ],
  [
   "R = {(1,2), (1,3), (2,4)} function hai?",
   "<b>Nahi</b> — 1 ke do images (2 aur 3). Har input ka exactly ek output chahiye."
  ],
  [
   "f(x) = x² + 1. f(3) aur f(−3)?",
   "Dono <b>10</b> — square sign khaa jaata hai. Do inputs ka same image allowed hai!"
  ],
  [
   "[−3.7] (greatest integer) kya hoga?",
   "<b>−4</b> — floor hamesha neeche (left) jaata hai, −3 nahi!"
  ],
  [
   "f(x) = 1/(x − 2). Domain?",
   "Denominator zero nahi hona chahiye → x ≠ 2 → domain = <b>R − {2}</b>."
  ],
  [
   "f(x) = √x, g(x) = x². (f+g)(4)?",
   "f(4) = 2, g(4) = 16 → (f+g)(4) = <b>18</b>."
  ],
  [
   "Signum function ka range?",
   "<b>{−1, 0, 1}</b> — negative pe −1, zero pe 0, positive pe 1."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/maths/ch-3/",
  "title": "Trigonometric Functions"
 }
}

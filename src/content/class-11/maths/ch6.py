# Class 11 Maths, Chapter 6 - Permutations and Combinations
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 6,
 "title_en": "Permutations and Combinations",
 "title_hi": "क्रमचय और संचय",
 "tagline": "Counting ka superpower — nPr, nCr aur problem patterns",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 6: Permutations and Combinations — long + short notes in Hindi, English, Hinglish. Factorial, nPr, nCr, arrangements, selections, restriction problems.",
 "video": None,
 "card_tag": "Counting ka superpower — nPr, nCr aur problem patterns",
 "card_topics": [
  "🔢 Counting principles",
  "❗ Factorial tricks",
  "🔀 nPr (order matters)",
  "🤝 nCr (selection only)"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Counting Principles — Bina Gine Ginna ⭐",
    "body": "<ul>\n<li><b>Fundamental principle of counting (multiplication) ⭐:</b> ek kaam m ways me, doosra n ways me → DONO saath m × n ways me. (3 shirts × 4 pants = 12 outfits!)</li>\n<li><b>Extension:</b> teen cheezein? m × n × p. Passwords, number plates, phone numbers — sab isi se count hote hain.</li>\n<li><b>Addition principle ⭐:</b> ek kaam m ways me YA doosra n ways me (dono SAATH nahi) → m + n ways. OR = add, AND = multiply!</li>\n<li><b>Example:</b> 4 seater car me 4 log baithne ke ways = 4 × 3 × 2 × 1 = 24 (har seat pe ek-ek choice kam hoti gayi).</li>\n<li><b>With/without repetition distinction ⭐:</b> digits repeat allowed → har place pe same choices (10 × 10 × 10); repeat not allowed → choices ghat-ti hain (10 × 9 × 8).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: har \"stage\" pe kitne options? Multiply karte jao. Stages alag-alag cases hain (ya to ye, ya wo) to add!</p>"
   },
   {
    "h": "2️⃣ Factorial — n! Ka Power",
    "body": "<ul>\n<li><b>n! (n factorial) ⭐:</b> n! = n × (n−1) × (n−2) × ... × 3 × 2 × 1. 5! = 120, 6! = 720.</li>\n<li><b>0! = 1</b> — definition se! (Ek object ko arrange karne ka ek hi tareeka.) ⭐</li>\n<li><b>Key identity:</b> n! = n × (n−1)! — factorial ko chhota tod sakte ho: 7! = 7 × 6!.</li>\n<li><b>Simplification trick ⭐:</b> fractions me factorials cancel karo: 8!/5! = 8×7×6 = 336 (5! upar-neeche kat gaya!). Kabhi poora compute mat karo — pehle cancel!</li>\n<li><b>(n+1)! = (n+1)n!;</b> n!(n+1) = (n+1)! — rearrangements me kaam aata hai.</li>\n<li><b>1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720, 7! = 5040</b> — ye saat yaad rakho, kaafi hain!</li>\n</ul>\n<p class=\"small-note\">💡 n! = n cheezon ko LINE me lagane ke tareeke. Isliye counting ke har formula me factorial ghoomta hai!</p>"
   },
   {
    "h": "3️⃣ Permutations — Jab ORDER Matter Kare ⭐",
    "body": "<ul>\n<li><b>Permutation:</b> arrangement — order IMPORTANT hai (ABC aur BCA alag-alag!).</li>\n<li><b>nPr formula ⭐⭐:</b> n distinct objects me se r ko arrange karne ke ways = ⁿP_r = n!/(n−r)!.</li>\n<li><b>Full arrangement:</b> n ko n positions pe: ⁿP_n = n!.</li>\n<li><b>Example:</b> 5 books me se 3 ko shelf pe arrange: ⁵P₃ = 5!/2! = 60.</li>\n<li><b>With repetition ⭐:</b> n objects, r positions, repetition allowed → n^r (3-digit codes from 5 digits = 5³ = 125).</li>\n<li><b>Repeating objects wale arrangements ⭐:</b> n objects me p ek jaise, q doosre jaise → n!/(p! q!). ALLAHABAD (10 letters, 4 A, 2 L) = 10!/(4! 2!) = 75600.</li>\n<li><b>Circular permutation:</b> n ko circle me arrange: (n−1)! (ek ko fix kar do — circle ghoom sakta hai!).</li>\n</ul>\n<p class=\"small-note\">🎯 Order matter kare (arrangement, rank, position, seat) → Permutation. Code words: \"arrange\", \"order\", \"rank\", \"signals\", \"numbers banane\".</p>"
   },
   {
    "h": "4️⃣ Combinations — Jab Sirf SELECTION Matter Kare ⭐",
    "body": "<ul>\n<li><b>Combination:</b> selection — order IRRELEVANT ({A, B, C} aur {B, C, A} SAME team!).</li>\n<li><b>nCr formula ⭐⭐:</b> n distinct me se r select karne ke ways = ⁿC_r = n!/(r!(n−r)!).</li>\n<li><b>Connection:</b> ⁿP_r = ⁿC_r × r! — pehle select karo (ⁿC_r), phir arrange (r!). Isliye combination chhota hota hai!</li>\n<li><b>Key properties ⭐:</b> ⁿC_r = ⁿC_(n−r) (10 me se 3 chunna = 7 chhodna!); ⁿC_0 = ⁿC_n = 1; ⁿC_1 = n; ⁿC_r + ⁿC_(r−1) = ⁿ⁺¹C_r (Pascal rule!).</li>\n<li><b>Example:</b> 11 players me se team of 5? Sirf selection → ¹¹C₅ = 462. Captain bhi decide? ¹¹C₅ × 5 (ya pehle captain 11 ways × ¹⁰C₄).</li>\n<li><b>Total subsets connection:</b> ⁿC_0 + ⁿC_1 + ... + ⁿC_n = 2ⁿ (saare possible selections!).</li>\n</ul>\n<p class=\"small-note\">💡 Team, committee, group, selection, hand of cards → Combination. Order ka zikr nahi = order matter nahi karta!</p>"
   },
   {
    "h": "5️⃣ Problem-Solving Strategy — P&C Ke Patterns",
    "body": "<ul>\n<li><b>Pehla sawal ⭐:</b> \"Order matter karta hai?\" HAAN → permutation, NAHI → combination. Ye ek sawal 80% decide kar deta hai.</li>\n<li><b>Restriction problems (together/not together) ⭐:</b> saath rakhna ho to BUNDLE banao (ek object samjho), phir arrange; saath na ho to total − together (complementary counting!).</li>\n<li><b>Gap method ⭐:</b> \"koi do vowels saath na ho\" → pehle consonants arrange, phir gaps me vowels place karo (_C_C_C_ ke gaps!).</li>\n<li><b>Committee with conditions:</b> \"at least 2 women\" → cases banao (2W+3M, 3W+2M, 4W+1M) aur ADD karo (OR = add!).</li>\n<li><b>Complementary counting ⭐:</b> \"at least one\" → total − none. Kabhi-kabhi ulta sochna 10x easy hai!</li>\n<li><b>Distribution:</b> identical objects alag boxes me vs distinct objects — type pehchano pehle, formula baad me.</li>\n</ul>\n<p class=\"small-note\">💡 P&amp;C me formula yaad karna nahi, PATTERN pehchanna sikhna hai: together? bundle. Not together? gaps. At least? complement ya cases. Bas!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ गणना सिद्धांत — बिना गिने गिनना ⭐",
    "body": "<ul>\n<li><b>गणना का मूल सिद्धांत (गुणन) ⭐:</b> एक कार्य m तरीकों से, दूसरा n से → दोनों साथ m × n तरीकों से। (3 शर्ट × 4 पैंट = 12!)</li>\n<li><b>विस्तार:</b> तीन चीजें? m × n × p।</li>\n<li><b>योग सिद्धांत ⭐:</b> एक कार्य m से या दूसरा n से (साथ नहीं) → m + n। OR = जोड़, AND = गुणा!</li>\n<li><b>उदाहरण:</b> 4 लोगों के 4 सीटों पर बैठने के तरीके = 4 × 3 × 2 × 1 = 24।</li>\n<li><b>पुनरावृत्ति ⭐:</b> अनुमति हो → हर स्थान पर समान विकल्प (10 × 10); न हो → विकल्प घटते हैं (10 × 9)।</li>\n</ul>\n<p class=\"small-note\">💡 हर \"चरण\" पर कितने विकल्प? गुणा करते जाओ। अलग-अलग स्थितियां (या) → जोड़!</p>"
   },
   {
    "h": "2️⃣ क्रमगुणित — n! की शक्ति",
    "body": "<ul>\n<li><b>n! ⭐:</b> n! = n × (n−1) × ... × 3 × 2 × 1। 5! = 120।</li>\n<li><b>0! = 1</b> — परिभाषा से! ⭐</li>\n<li><b>मुख्य सर्वसमिका:</b> n! = n × (n−1)! — 7! = 7 × 6!।</li>\n<li><b>सरलीकरण ⭐:</b> भिन्नों में काटो: 8!/5! = 8×7×6 = 336। पहले काटो, बाद में गणना!</li>\n<li><b>याद रखो:</b> 1!=1, 2!=2, 3!=6, 4!=24, 5!=120, 6!=720, 7!=5040।</li>\n</ul>\n<p class=\"small-note\">💡 n! = n वस्तुओं को पंक्ति में लगाने के तरीके।</p>"
   },
   {
    "h": "3️⃣ क्रमचय — जब क्रम महत्वपूर्ण हो ⭐",
    "body": "<ul>\n<li><b>क्रमचय (permutation):</b> विन्यास — क्रम महत्वपूर्ण (ABC और BCA अलग!)।</li>\n<li><b>ⁿP_r सूत्र ⭐⭐:</b> n भिन्न वस्तुओं में से r को व्यवस्थित करने के तरीके = ⁿP_r = n!/(n−r)!।</li>\n<li><b>पूर्ण विन्यास:</b> ⁿP_n = n!।</li>\n<li><b>उदाहरण:</b> 5 पुस्तकों में से 3 शेल्फ पर: ⁵P₃ = 5!/2! = 60।</li>\n<li><b>पुनरावृत्ति सहित ⭐:</b> n^r।</li>\n<li><b>दोहराई वस्तुएं ⭐:</b> n!/(p! q!) — ALLAHABAD = 10!/(4! 2!) = 75600।</li>\n<li><b>वृत्तीय क्रमचय:</b> (n−1)! (एक को स्थिर करो!)।</li>\n</ul>\n<p class=\"small-note\">🎯 क्रम महत्वपूर्ण → क्रमचय। संकेत शब्द: \"व्यवस्थित\", \"क्रम\", \"रैंक\"।</p>"
   },
   {
    "h": "4️⃣ संचय — जब केवल चयन महत्वपूर्ण हो ⭐",
    "body": "<ul>\n<li><b>संचय (combination):</b> चयन — क्रम अप्रासंगिक ({A,B,C} = {B,C,A}!)।</li>\n<li><b>ⁿC_r सूत्र ⭐⭐:</b> ⁿC_r = n!/(r!(n−r)!)।</li>\n<li><b>संबंध:</b> ⁿP_r = ⁿC_r × r! — पहले चुनो, फिर व्यवस्थित करो!</li>\n<li><b>गुण ⭐:</b> ⁿC_r = ⁿC_(n−r); ⁿC_0 = ⁿC_n = 1; ⁿC_1 = n; ⁿC_r + ⁿC_(r−1) = ⁿ⁺¹C_r (पास्कल नियम!)।</li>\n<li><b>उदाहरण:</b> 11 खिलाड़ियों में से 5 की टीम? ¹¹C₅ = 462।</li>\n<li><b>कुल उपसमुच्चय:</b> ⁿC_0 + ... + ⁿC_n = 2ⁿ।</li>\n</ul>\n<p class=\"small-note\">💡 टीम, समिति, चयन → संचय। क्रम का जिक्र नहीं = क्रम अमहत्वपूर्ण!</p>"
   },
   {
    "h": "5️⃣ समस्या-समाधान रणनीति — P&C के पैटर्न",
    "body": "<ul>\n<li><b>पहला प्रश्न ⭐:</b> \"क्रम महत्वपूर्ण?\" हां → क्रमचय, नहीं → संचय।</li>\n<li><b>प्रतिबंध प्रश्न ⭐:</b> साथ रखना हो → बंडल बनाओ; साथ न हो → कुल − साथ (पूरक गणना!)।</li>\n<li><b>रिक्ति विधि ⭐:</b> \"कोई दो स्वर साथ न हों\" → पहले व्यंजन व्यवस्थित करो, फिर रिक्तियों में स्वर।</li>\n<li><b>शर्त सहित समिति:</b> \"कम से कम 2 महिलाएं\" → स्थितियां बनाओ और जोड़ो।</li>\n<li><b>पूरक गणना ⭐:</b> \"कम से कम एक\" → कुल − कोई नहीं।</li>\n</ul>\n<p class=\"small-note\">💡 P&amp;C में पैटर्न पहचानो: साथ? बंडल। साथ नहीं? रिक्तियां। कम से कम? पूरक या स्थितियां।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Counting Principles — Counting Without Counting ⭐",
    "body": "<ul>\n<li><b>Fundamental principle of counting (multiplication) ⭐:</b> if one job can be done m ways and another n ways, then BOTH together can be done m × n ways. (3 shirts × 4 pants = 12 outfits!)</li>\n<li><b>Extension:</b> three things? m × n × p. Passwords, number plates, phone numbers — all counted this way.</li>\n<li><b>Addition principle ⭐:</b> one job in m ways OR another in n ways (not both together) → m + n ways. OR = add, AND = multiply!</li>\n<li><b>Example:</b> 4 people sitting in 4 seats = 4 × 3 × 2 × 1 = 24 (each seat has one fewer choice).</li>\n<li><b>Repetition distinction ⭐:</b> repeats allowed → same choices each place (10 × 10 × 10); not allowed → shrinking choices (10 × 9 × 8).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: how many options at each \"stage\"? Keep multiplying. Separate cases (either this or that)? Add!</p>"
   },
   {
    "h": "2️⃣ Factorial — The Power of n!",
    "body": "<ul>\n<li><b>n! (n factorial) ⭐:</b> n! = n × (n−1) × (n−2) × ... × 3 × 2 × 1. 5! = 120, 6! = 720.</li>\n<li><b>0! = 1</b> — by definition! (One object can be arranged in exactly one way.) ⭐</li>\n<li><b>Key identity:</b> n! = n × (n−1)! — break factorials down: 7! = 7 × 6!.</li>\n<li><b>Simplification trick ⭐:</b> cancel factorials in fractions: 8!/5! = 8×7×6 = 336 (the 5! cancels!). Never compute fully — cancel first!</li>\n<li><b>Learn these:</b> 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720, 7! = 5040 — these seven cover most problems!</li>\n</ul>\n<p class=\"small-note\">💡 n! = the number of ways to line up n things. That is why factorials show up in every counting formula!</p>"
   },
   {
    "h": "3️⃣ Permutations — When ORDER Matters ⭐",
    "body": "<ul>\n<li><b>Permutation:</b> an arrangement — order is IMPORTANT (ABC and BCA are different!).</li>\n<li><b>nPr formula ⭐⭐:</b> arranging r out of n distinct objects = ⁿP_r = n!/(n−r)!.</li>\n<li><b>Full arrangement:</b> n objects in n positions: ⁿP_n = n!.</li>\n<li><b>Example:</b> arrange 3 of 5 books on a shelf: ⁵P₃ = 5!/2! = 60.</li>\n<li><b>With repetition ⭐:</b> n objects, r positions, repetition allowed → n^r (3-digit codes from 5 digits = 5³ = 125).</li>\n<li><b>Arrangements with repeating objects ⭐:</b> n objects with p alike and q alike → n!/(p! q!). ALLAHABAD (10 letters, 4 A's, 2 L's) = 10!/(4! 2!) = 75600.</li>\n<li><b>Circular permutation:</b> arranging n around a circle: (n−1)! (fix one — the circle can rotate!).</li>\n</ul>\n<p class=\"small-note\">🎯 Order matters (arrangement, rank, position, seat) → Permutation. Code words: \"arrange\", \"order\", \"rank\", \"signals\", \"forming numbers\".</p>"
   },
   {
    "h": "4️⃣ Combinations — When Only SELECTION Matters ⭐",
    "body": "<ul>\n<li><b>Combination:</b> a selection — order is IRRELEVANT ({A, B, C} and {B, C, A} are the SAME team!).</li>\n<li><b>nCr formula ⭐⭐:</b> selecting r out of n distinct objects = ⁿC_r = n!/(r!(n−r)!).</li>\n<li><b>The connection:</b> ⁿP_r = ⁿC_r × r! — first select (ⁿC_r), then arrange (r!). That is why combinations are smaller!</li>\n<li><b>Key properties ⭐:</b> ⁿC_r = ⁿC_(n−r) (choosing 3 of 10 = leaving out 7!); ⁿC_0 = ⁿC_n = 1; ⁿC_1 = n; ⁿC_r + ⁿC_(r−1) = ⁿ⁺¹C_r (Pascal's rule!).</li>\n<li><b>Example:</b> a team of 5 from 11 players? Selection only → ¹¹C₅ = 462. Captain too? ¹¹C₅ × 5 (or 11 ways for captain × ¹⁰C₄).</li>\n<li><b>Total subsets connection:</b> ⁿC_0 + ⁿC_1 + ... + ⁿC_n = 2ⁿ (all possible selections!).</li>\n</ul>\n<p class=\"small-note\">💡 Team, committee, group, selection, hand of cards → Combination. No mention of order = order does not matter!</p>"
   },
   {
    "h": "5️⃣ Problem-Solving Strategy — The Patterns of P&C",
    "body": "<ul>\n<li><b>The first question ⭐:</b> \"Does order matter?\" YES → permutation, NO → combination. This one question decides 80% of the problem.</li>\n<li><b>Restriction problems (together/apart) ⭐:</b> must stay together → make a BUNDLE (treat as one object), then arrange; must not be together → total − together (complementary counting!).</li>\n<li><b>Gap method ⭐:</b> \"no two vowels together\" → arrange the consonants first, then place vowels in the gaps (_C_C_C_ gaps!).</li>\n<li><b>Committee with conditions:</b> \"at least 2 women\" → make cases (2W+3M, 3W+2M, 4W+1M) and ADD them (OR = add!).</li>\n<li><b>Complementary counting ⭐:</b> \"at least one\" → total − none. Sometimes thinking backwards is 10x easier!</li>\n<li><b>Distribution:</b> identical objects into boxes vs distinct objects — identify the type first, formula second.</li>\n</ul>\n<p class=\"small-note\">💡 In P&amp;C you do not memorize formulas, you learn to recognize PATTERNS: together? bundle. Apart? gaps. At least? complement or cases. Done!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Counting ⭐",
    "items": [
     "AND (saath) = multiply",
     "OR (cases) = add",
     "Repeat allowed: n^r"
    ]
   },
   {
    "h": "Factorial",
    "items": [
     "n! = n×(n−1)×...×1",
     "0! = 1",
     "Cancel pehle, compute baad me"
    ]
   },
   {
    "h": "Permutation ⭐⭐",
    "items": [
     "ⁿP_r = n!/(n−r)!",
     "Order matter kare = P",
     "Repeats: n!/(p!q!)"
    ]
   },
   {
    "h": "Combination ⭐⭐",
    "items": [
     "ⁿC_r = n!/(r!(n−r)!)",
     "Selection only = C",
     "ⁿC_r = ⁿC_(n−r)"
    ]
   },
   {
    "h": "Patterns ⭐",
    "items": [
     "Together → bundle",
     "Not together → gaps/complement",
     "At least → cases ya total−none"
    ]
   }
  ],
  "hi": [
   {
    "h": "गणना ⭐",
    "items": [
     "AND = गुणा",
     "OR = जोड़",
     "पुनरावृत्ति: n^r"
    ]
   },
   {
    "h": "क्रमगुणित",
    "items": [
     "n! = n×...×1",
     "0! = 1",
     "पहले काटो"
    ]
   },
   {
    "h": "क्रमचय ⭐⭐",
    "items": [
     "ⁿP_r = n!/(n−r)!",
     "क्रम महत्वपूर्ण = P",
     "दोहराव: n!/(p!q!)"
    ]
   },
   {
    "h": "संचय ⭐⭐",
    "items": [
     "ⁿC_r = n!/(r!(n−r)!)",
     "केवल चयन = C",
     "ⁿC_r = ⁿC_(n−r)"
    ]
   },
   {
    "h": "पैटर्न ⭐",
    "items": [
     "साथ → बंडल",
     "साथ नहीं → रिक्तियां",
     "कम से कम → स्थितियां/पूरक"
    ]
   }
  ],
  "en": [
   {
    "h": "Counting ⭐",
    "items": [
     "AND (together) = multiply",
     "OR (cases) = add",
     "Repeats allowed: n^r"
    ]
   },
   {
    "h": "Factorial",
    "items": [
     "n! = n×(n−1)×...×1",
     "0! = 1",
     "Cancel first, compute later"
    ]
   },
   {
    "h": "Permutation ⭐⭐",
    "items": [
     "ⁿP_r = n!/(n−r)!",
     "Order matters = P",
     "Repeats: n!/(p!q!)"
    ]
   },
   {
    "h": "Combination ⭐⭐",
    "items": [
     "ⁿC_r = n!/(r!(n−r)!)",
     "Selection only = C",
     "ⁿC_r = ⁿC_(n−r)"
    ]
   },
   {
    "h": "Patterns ⭐",
    "items": [
     "Together → bundle",
     "Apart → gaps/complement",
     "At least → cases or total−none"
    ]
   }
  ]
 },
 "practice": [
  [
   "3 shirts aur 5 pants se kitne outfits?",
   "AND = multiply → 3 × 5 = <b>15</b>."
  ],
  [
   "7!/4! simplify karo.",
   "7×6×5×4!/4! = 7×6×5 = <b>210</b> (cancel pehle!)."
  ],
  [
   "5 log kitne tareeke se line me khade ho sakte hain?",
   "5! = <b>120</b> (order matter karta hai — permutation)."
  ],
  [
   "8 players me se 3 ko arrange karna hai (1st, 2nd, 3rd position).",
   "Order matter → ⁸P₃ = 8!/5! = 8×7×6 = <b>336</b>."
  ],
  [
   "10 students me se 4 ki committee?",
   "Sirf selection → ¹⁰C₄ = 10!/(4!6!) = <b>210</b>."
  ],
  [
   "ⁿC_r = ⁿC_(n−r) kyun?",
   "r chunna = n−r CHHODNA — dono ek hi kaam! (10 me se 3 chunna = 7 chhodna.)"
  ],
  [
   "BANANA ke letters kitne tareeke se arrange honge?",
   "6 letters, 3 A's, 2 N's → 6!/(3!2!) = 720/12 = <b>60</b>."
  ],
  [
   "5 friends ko round table pe arrange karna hai.",
   "Circular → (5−1)! = 4! = <b>24</b>."
  ],
  [
   "'APPLE' me kitne arrangements me dono P saath rahenge?",
   "PP ko bundle banao → 4 objects (PP, A, L, E) → 4! = <b>24</b>."
  ],
  [
   "8 me se 3 select karna hai, lekin Ramesh PAKKA ho. Kitne ways?",
   "Ramesh fixed → baaki 7 me se 2 chuno → ⁷C₂ = <b>21</b>."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/maths/ch-7/",
  "title": "Binomial Theorem"
 }
}

# Class 11 Maths, Chapter 7 - Binomial Theorem
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 7,
 "title_en": "Binomial Theorem",
 "title_hi": "द्विपद प्रमेय",
 "tagline": "(a+b)ⁿ ka superpower — general term, middle term aur coefficient tricks",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 7: Binomial Theorem — long + short notes in Hindi, English, Hinglish. Expansion, general term, middle term, greatest coefficient, remainder tricks.",
 "video": None,
 "card_tag": "(a+b)ⁿ ka superpower — general term, middle term aur coefficient tricks",
 "card_topics": [
  "🚀 Binomial expansion (a+b)ⁿ",
  "🎯 General term T(r+1)",
  "⛰️ Middle term + greatest coefficient",
  "🧮 Remainder & divisibility tricks"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Binomial Theorem Kyun — (a+b)ⁿ ka Shortcut",
    "body": "<p>(a + b)² = a² + 2ab + b² toh sabko yaad hai. Lekin exam mein (a + b)¹⁰ ya (x + 2y)¹⁵ aa jaye toh multiply karte raho ge? Kabhi nahi — time hi nahi milega. <b>Binomial Theorem</b> ek direct formula deta hai kisi bhi power ke expansion ka.</p>\n<ul>\n<li><b>Binomial expression:</b> do terms wala expression — (a + b), (x − 3y), (1 + 2x).</li>\n<li>Pattern dekho: (a+b)² = a² + 2ab + b² — powers a ki ghat rahi (2→1→0), b ki badh rahi (0→1→2). Har term me powers ka SUM = 2.</li>\n<li>Coefficients 1, 2, 1 — ye <b>combinatorics</b> se aate hain: C(2,0), C(2,1), C(2,2). Permutations &amp; Combinations chapter yahin kaam aata hai! ⭐</li>\n<li><b>Pascal's triangle:</b> har number upar ke do numbers ka sum — 1 / 1 1 / 1 2 1 / 1 3 3 1 / 1 4 6 4 1... n-th row = (a+b)ⁿ ke coefficients.</li>\n</ul>\n<p class=\"small-note\">💡 India mein isse <b>Meru Prastara</b> kehte the — 10th century ke mathematician Halayudha ne describe kiya tha, Pascal se sadiyon pehle!</p>"
   },
   {
    "h": "2️⃣ Binomial Theorem — Statement ⭐",
    "body": "<p>Kisi bhi positive integer n ke liye:</p>\n<ul>\n<li><b>(a + b)ⁿ = C(n,0)aⁿ + C(n,1)aⁿ⁻¹b + C(n,2)aⁿ⁻²b² + ... + C(n,n)bⁿ</b></li>\n<li>Compact form: (a + b)ⁿ = Σ (r = 0 to n) C(n,r) aⁿ⁻ʳ bʳ</li>\n<li><b>Terms ka count ⭐:</b> expansion me hamesha <b>n + 1 terms</b> hote hain. (a+b)⁸ → 9 terms.</li>\n<li>Har term me powers ka sum = n. a ki power n se 0 tak, b ki 0 se n tak.</li>\n<li>Coefficients symmetric hain: C(n,0) = C(n,n), C(n,1) = C(n,n−1)... pehla aur aakhri same, doosra aur second-last same.</li>\n</ul>\n<p class=\"small-note\">🎯 Example: (a+b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴ — coefficients 1,4,6,4,1 = Pascal ki 5th row!</p>"
   },
   {
    "h": "3️⃣ General Term T(r+1) — Sabse Important Formula ⭐",
    "body": "<p><b>T(r+1) = C(n,r) × aⁿ⁻ʳ × bʳ</b> — ye ek formula hi 80% exam questions solve karta hai.</p>\n<ul>\n<li><b>Dhyan rakho:</b> T(r+1) me r use hota hai — matlab pehli term T₁ ke liye r = 0, paanchvi term T₅ ke liye r = 4. Off-by-one galti sabse common hai! ⭐</li>\n<li><b>'x ki koi specific power ka coefficient' nikalna:</b> general term likho, x ki power ko required value ke equal rakho, r nikalo, phir coefficient compute karo.</li>\n<li><b>Constant term (x-independent):</b> x ki power = 0 rakhke r nikalo. Agar r integer nahi aaya to constant term exist hi nahi karta.</li>\n<li><b>Term from the end:</b> (a+b)ⁿ me end se k-th term = beginning se (n − k + 2)-th term.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: general term = Google Maps — seedha usi term pe pahunchao jo chahiye, pura expansion likhne ki zaroorat nahi!</p>"
   },
   {
    "h": "4️⃣ Middle Term(s) ⭐",
    "body": "<ul>\n<li><b>n even:</b> sirf EK middle term — <b>T(n/2 + 1)</b>. Example: (a+b)⁸ (9 terms) → middle = T₅.</li>\n<li><b>n odd:</b> DO middle terms — <b>T((n+1)/2) aur T((n+3)/2)</b>. Example: (a+b)⁷ (8 terms) → middles = T₄ aur T₅.</li>\n<li>Middle term ka coefficient hi <b>greatest coefficient</b> hota hai — C(n, n/2) jab n even.</li>\n<li>n odd ho to greatest coefficients do hain: C(n, (n−1)/2) = C(n, (n+1)/2) — dono equal.</li>\n</ul>\n<p class=\"small-note\">🎯 Coefficients pehle badhte hain, middle pe peak, phir ghat te hain — bilkul mountain shape!</p>"
   },
   {
    "h": "5️⃣ Binomial Coefficients ki Properties ⭐",
    "body": "<ul>\n<li><b>Sum of all coefficients:</b> C(n,0) + C(n,1) + ... + C(n,n) = <b>2ⁿ</b> (a = b = 1 rakhne par).</li>\n<li><b>Alternating sum:</b> C(n,0) − C(n,1) + C(n,2) − ... = <b>0</b> (a = 1, b = −1 par).</li>\n<li><b>Odd/even positions ka sum barabar:</b> C(n,0) + C(n,2) + ... = C(n,1) + C(n,3) + ... = 2ⁿ⁻¹.</li>\n<li><b>Number tricks:</b> 7¹⁰³ ka remainder? 7 = (8 − 1) likhke expand karo — (8−1)¹⁰³ me aakhri term (−1)¹⁰³ = −1 ke alawa sab 8 se divisible!</li>\n<li><b>Divisibility proofs:</b> 6ⁿ − 5n − 1 hamesha 25 se divisible (n ≥ 2) — (1+5)ⁿ expand karke dekho.</li>\n</ul>\n<p class=\"small-note\">💡 Remainder/divisibility problems ka master key: base ko (multiple ± 1) ki form me todo!</p>"
   },
   {
    "h": "6️⃣ Exam Patterns — Kaise Aata Hai Paper Me",
    "body": "<ul>\n<li><b>Direct expansion:</b> (2x + 3)⁴ type — formula lagao, 5 terms likho.</li>\n<li><b>Coefficient hunting ⭐:</b> (x + 1/x)¹⁰ me x⁴ ka coefficient — T(r+1) me x ki power 10−2r, barabar 4, r = 3.</li>\n<li><b>Constant term:</b> power zero set karo — JEE favourite.</li>\n<li><b>Middle term nikalo:</b> n even/odd check, formula lagao.</li>\n<li><b>Greatest coefficient / greatest term:</b> middle term concept use karo.</li>\n<li><b>Remainder problems:</b> 49ⁿ − 16n − 1 ÷ 64 type — (multiple ± 1) trick.</li>\n<li><b>Digits problems:</b> 2¹⁰⁰ ke last two digits — cyclicity + binomial.</li>\n</ul>\n<p class=\"small-note\">💡 90% questions sirf 3 formulas pe: (a+b)ⁿ expansion, T(r+1), middle term. Inhe ratta nahi, PATTERN samjho!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ द्विपद प्रमेय क्यों — (a+b)ⁿ का शॉर्टकट",
    "body": "<p>(a + b)² = a² + 2ab + b² सबको याद है। पर (a + b)¹⁰ या (x + 2y)¹⁵ को गुणा करते बैठोगे? परीक्षा में समय नहीं मिलेगा। <b>द्विपद प्रमेय</b> किसी भी घात के विस्तार का सीधा सूत्र देती है।</p>\n<ul>\n<li><b>द्विपद व्यंजक:</b> दो पदों वाला व्यंजक — (a + b), (x − 3y), (1 + 2x)।</li>\n<li>पैटर्न: (a+b)² = a² + 2ab + b² — a की घात घटती (2→1→0), b की बढ़ती (0→1→2)। हर पद में घातों का योग = 2।</li>\n<li>गुणांक 1, 2, 1 — ये <b>संचय (combinatorics)</b> से आते हैं: C(2,0), C(2,1), C(2,2)। ⭐</li>\n<li><b>पास्कल त्रिभुज (मेरु प्रस्तार):</b> हर संख्या ऊपर की दो संख्याओं का योग — n-वीं पंक्ति = (a+b)ⁿ के गुणांक।</li>\n</ul>\n<p class=\"small-note\">💡 भारत में इसे <b>मेरु प्रस्तार</b> कहते थे — 10वीं सदी के गणितज्ञ हलायुध ने इसका वर्णन किया था, पास्कल से सदियों पहले!</p>"
   },
   {
    "h": "2️⃣ द्विपद प्रमेय — कथन ⭐",
    "body": "<p>किसी भी धनात्मक पूर्णांक n के लिए:</p>\n<ul>\n<li><b>(a + b)ⁿ = C(n,0)aⁿ + C(n,1)aⁿ⁻¹b + C(n,2)aⁿ⁻²b² + ... + C(n,n)bⁿ</b></li>\n<li>संक्षिप्त रूप: (a + b)ⁿ = Σ (r = 0 से n) C(n,r) aⁿ⁻ʳ bʳ</li>\n<li><b>पदों की संख्या ⭐:</b> विस्तार में सदैव <b>n + 1 पद</b> होते हैं। (a+b)⁸ → 9 पद।</li>\n<li>हर पद में घातों का योग = n। a की घात n से 0 तक, b की 0 से n तक।</li>\n<li>गुणांक सममित होते हैं: C(n,0) = C(n,n), C(n,1) = C(n,n−1)... पहला और अंतिम समान।</li>\n</ul>\n<p class=\"small-note\">🎯 उदाहरण: (a+b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴ — गुणांक 1,4,6,4,1 = पास्कल त्रिभुज की 5वीं पंक्ति!</p>"
   },
   {
    "h": "3️⃣ व्यापक पद T(r+1) — सबसे महत्वपूर्ण सूत्र ⭐",
    "body": "<p><b>T(r+1) = C(n,r) × aⁿ⁻ʳ × bʳ</b> — यही एक सूत्र 80% परीक्षा प्रश्न हल करता है।</p>\n<ul>\n<li><b>ध्यान रखें:</b> T(r+1) में r प्रयोग होता है — पहले पद T₁ के लिए r = 0, पाँचवें पद T₅ के लिए r = 4। यही सबसे आम गलती है! ⭐</li>\n<li><b>'x की किसी विशिष्ट घात का गुणांक':</b> व्यापक पद लिखो, x की घात को अभीष्ट मान के बराबर रखो, r निकालो, फिर गुणांक निकालो।</li>\n<li><b>अचर पद (x-मुक्त):</b> x की घात = 0 रखकर r निकालो। r पूर्णांक न आए तो अचर पद है ही नहीं।</li>\n<li><b>अंत से पद:</b> (a+b)ⁿ में अंत से k-वाँ पद = आरंभ से (n − k + 2)-वाँ पद।</li>\n</ul>\n<p class=\"small-note\">💡 व्यापक पद = सीधा रास्ता — पूरा विस्तार लिखे बिना चाहिए वाले पद पर पहुँचो!</p>"
   },
   {
    "h": "4️⃣ मध्य पद ⭐",
    "body": "<ul>\n<li><b>n सम:</b> केवल एक मध्य पद — <b>T(n/2 + 1)</b>। उदाहरण: (a+b)⁸ (9 पद) → मध्य = T₅।</li>\n<li><b>n विषम:</b> दो मध्य पद — <b>T((n+1)/2) और T((n+3)/2)</b>। उदाहरण: (a+b)⁷ (8 पद) → मध्य = T₄ और T₅।</li>\n<li>मध्य पद का गुणांक ही <b>महत्तम गुणांक</b> होता है — C(n, n/2) जब n सम।</li>\n<li>n विषम हो तो महत्तम गुणांक दो: C(n, (n−1)/2) = C(n, (n+1)/2)।</li>\n</ul>\n<p class=\"small-note\">🎯 गुणांक पहले बढ़ते हैं, मध्य में शिखर, फिर घटते हैं — पर्वत जैसा आकार!</p>"
   },
   {
    "h": "5️⃣ द्विपद गुणांकों के गुण ⭐",
    "body": "<ul>\n<li><b>सभी गुणांकों का योग:</b> C(n,0) + C(n,1) + ... + C(n,n) = <b>2ⁿ</b> (a = b = 1 रखने पर)।</li>\n<li><b>एकांतर योग:</b> C(n,0) − C(n,1) + C(n,2) − ... = <b>0</b> (a = 1, b = −1 पर)।</li>\n<li><b>सम/विषम स्थानों का योग बराबर:</b> C(n,0) + C(n,2) + ... = C(n,1) + C(n,3) + ... = 2ⁿ⁻¹।</li>\n<li><b>शेषफल तरकीब:</b> 7¹⁰³ का शेषफल? 7 = (8 − 1) लिखकर विस्तार करो — अंतिम पद (−1)¹⁰³ = −1 के अलावा सब 8 से विभाज्य!</li>\n<li><b>विभाज्यता प्रमाण:</b> 6ⁿ − 5n − 1 सदैव 25 से विभाज्य (n ≥ 2) — (1+5)ⁿ विस्तार से।</li>\n</ul>\n<p class=\"small-note\">💡 शेषफल/विभाज्यता की मास्टर कुंजी: आधार को (गुणज ± 1) के रूप में तोड़ो!</p>"
   },
   {
    "h": "6️⃣ परीक्षा के पैटर्न",
    "body": "<ul>\n<li><b>सीधा विस्तार:</b> (2x + 3)⁴ प्रकार — सूत्र लगाओ, 5 पद लिखो।</li>\n<li><b>गुणांक खोज ⭐:</b> (x + 1/x)¹⁰ में x⁴ का गुणांक — T(r+1) में x की घात 10−2r, बराबर 4, r = 3।</li>\n<li><b>अचर पद:</b> घात शून्य रखो — JEE का पसंदीदा।</li>\n<li><b>मध्य पद:</b> n सम/विषम जाँचो, सूत्र लगाओ।</li>\n<li><b>महत्तम गुणांक/पद:</b> मध्य पद अवधारणा प्रयोग करो।</li>\n<li><b>शेषफल प्रश्न:</b> 49ⁿ − 16n − 1 ÷ 64 प्रकार — (गुणज ± 1) तरकीब।</li>\n</ul>\n<p class=\"small-note\">💡 90% प्रश्न सिर्फ 3 सूत्रों पर: विस्तार, T(r+1), मध्य पद। पैटर्न समझो, रटो मत!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Why the Binomial Theorem — a Shortcut for (a+b)ⁿ",
    "body": "<p>Everyone remembers (a + b)² = a² + 2ab + b². But if an exam throws (a + b)¹⁰ or (x + 2y)¹⁵ at you, multiplying it out will eat all your time. The <b>Binomial Theorem</b> gives a direct formula for expanding any power.</p>\n<ul>\n<li><b>Binomial expression:</b> an expression with two terms — (a + b), (x − 3y), (1 + 2x).</li>\n<li>Spot the pattern: (a+b)² = a² + 2ab + b² — powers of a fall (2→1→0), powers of b rise (0→1→2). In every term the powers SUM to 2.</li>\n<li>The coefficients 1, 2, 1 come from <b>combinatorics</b>: C(2,0), C(2,1), C(2,2). This is where Permutations &amp; Combinations pays off! ⭐</li>\n<li><b>Pascal's triangle:</b> each number is the sum of the two above it — 1 / 1 1 / 1 2 1 / 1 3 3 1... The n-th row gives the coefficients of (a+b)ⁿ.</li>\n</ul>\n<p class=\"small-note\">💡 In India this was called <b>Meru Prastara</b> — described by the 10th-century mathematician Halayudha, centuries before Pascal!</p>"
   },
   {
    "h": "2️⃣ The Binomial Theorem — Statement ⭐",
    "body": "<p>For any positive integer n:</p>\n<ul>\n<li><b>(a + b)ⁿ = C(n,0)aⁿ + C(n,1)aⁿ⁻¹b + C(n,2)aⁿ⁻²b² + ... + C(n,n)bⁿ</b></li>\n<li>Compact form: (a + b)ⁿ = Σ (r = 0 to n) C(n,r) aⁿ⁻ʳ bʳ</li>\n<li><b>Number of terms ⭐:</b> the expansion always has <b>n + 1 terms</b>. (a+b)⁸ → 9 terms.</li>\n<li>In every term the powers sum to n. The power of a runs n down to 0, and b runs 0 up to n.</li>\n<li>Coefficients are symmetric: C(n,0) = C(n,n), C(n,1) = C(n,n−1)... first equals last, second equals second-last.</li>\n</ul>\n<p class=\"small-note\">🎯 Example: (a+b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴ — coefficients 1,4,6,4,1 = the 5th row of Pascal's triangle!</p>"
   },
   {
    "h": "3️⃣ General Term T(r+1) — the Most Important Formula ⭐",
    "body": "<p><b>T(r+1) = C(n,r) × aⁿ⁻ʳ × bʳ</b> — this single formula solves 80% of exam questions.</p>\n<ul>\n<li><b>Watch out:</b> T(r+1) uses r — so T₁ needs r = 0, T₅ needs r = 4. The off-by-one slip is the most common mistake! ⭐</li>\n<li><b>'Coefficient of a specific power of x':</b> write the general term, set the power of x equal to the required value, solve for r, then compute the coefficient.</li>\n<li><b>Constant term (x-independent):</b> set the power of x = 0 and find r. If r is not an integer, no constant term exists.</li>\n<li><b>Term from the end:</b> in (a+b)ⁿ, the k-th term from the end = the (n − k + 2)-th term from the beginning.</li>\n</ul>\n<p class=\"small-note\">💡 The general term is a direct route — jump straight to the term you need without writing the whole expansion!</p>"
   },
   {
    "h": "4️⃣ Middle Term(s) ⭐",
    "body": "<ul>\n<li><b>n even:</b> exactly ONE middle term — <b>T(n/2 + 1)</b>. Example: (a+b)⁸ (9 terms) → middle = T₅.</li>\n<li><b>n odd:</b> TWO middle terms — <b>T((n+1)/2) and T((n+3)/2)</b>. Example: (a+b)⁷ (8 terms) → middles = T₄ and T₅.</li>\n<li>The middle term's coefficient is the <b>greatest coefficient</b> — C(n, n/2) when n is even.</li>\n<li>If n is odd, there are two greatest coefficients: C(n, (n−1)/2) = C(n, (n+1)/2) — equal values.</li>\n</ul>\n<p class=\"small-note\">🎯 Coefficients rise, peak in the middle, then fall — a perfect mountain shape!</p>"
   },
   {
    "h": "5️⃣ Properties of Binomial Coefficients ⭐",
    "body": "<ul>\n<li><b>Sum of all coefficients:</b> C(n,0) + C(n,1) + ... + C(n,n) = <b>2ⁿ</b> (set a = b = 1).</li>\n<li><b>Alternating sum:</b> C(n,0) − C(n,1) + C(n,2) − ... = <b>0</b> (set a = 1, b = −1).</li>\n<li><b>Odd/even position sums are equal:</b> C(n,0) + C(n,2) + ... = C(n,1) + C(n,3) + ... = 2ⁿ⁻¹.</li>\n<li><b>Remainder trick:</b> remainder of 7¹⁰³? Write 7 = (8 − 1) and expand — in (8−1)¹⁰³ everything except the last term (−1)¹⁰³ = −1 is divisible by 8!</li>\n<li><b>Divisibility proofs:</b> 6ⁿ − 5n − 1 is always divisible by 25 (n ≥ 2) — expand (1+5)ⁿ and see.</li>\n</ul>\n<p class=\"small-note\">💡 Master key for remainder/divisibility problems: break the base into (multiple ± 1) form!</p>"
   },
   {
    "h": "6️⃣ Exam Patterns — How It Appears in Papers",
    "body": "<ul>\n<li><b>Direct expansion:</b> like (2x + 3)⁴ — apply the formula, write 5 terms.</li>\n<li><b>Coefficient hunting ⭐:</b> coefficient of x⁴ in (x + 1/x)¹⁰ — in T(r+1) the power of x is 10−2r, set equal to 4, r = 3.</li>\n<li><b>Constant term:</b> set the power to zero — a JEE favourite.</li>\n<li><b>Find the middle term:</b> check n even/odd, apply the formula.</li>\n<li><b>Greatest coefficient / greatest term:</b> use the middle-term concept.</li>\n<li><b>Remainder problems:</b> like 49ⁿ − 16n − 1 ÷ 64 — the (multiple ± 1) trick.</li>\n<li><b>Digit problems:</b> last two digits of 2¹⁰⁰ — cyclicity plus binomial.</li>\n</ul>\n<p class=\"small-note\">💡 90% of questions rest on just 3 formulas: the expansion, T(r+1), and the middle term. Learn the PATTERN, not by rote!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Theorem ⭐",
    "items": [
     "(a+b)ⁿ = Σ C(n,r) aⁿ⁻ʳ bʳ",
     "Terms: n+1",
     "Powers ka sum hamesha n"
    ]
   },
   {
    "h": "General Term ⭐",
    "items": [
     "T(r+1) = C(n,r) aⁿ⁻ʳ bʳ",
     "T₅ ke liye r=4 (off-by-one trap!)",
     "Constant term: x power = 0"
    ]
   },
   {
    "h": "Middle Term ⭐",
    "items": [
     "n even → T(n/2+1)",
     "n odd → T((n+1)/2), T((n+3)/2)",
     "Middle = greatest coefficient"
    ]
   },
   {
    "h": "Properties ⭐",
    "items": [
     "Σ coefficients = 2ⁿ",
     "Alternating sum = 0",
     "Odd sum = even sum = 2ⁿ⁻¹"
    ]
   },
   {
    "h": "Tricks",
    "items": [
     "Remainder: base = multiple ± 1",
     "Pascal's triangle = coefficients",
     "End se k-th = start se (n−k+2)-th"
    ]
   }
  ],
  "hi": [
   {
    "h": "प्रमेय ⭐",
    "items": [
     "(a+b)ⁿ = Σ C(n,r) aⁿ⁻ʳ bʳ",
     "पद: n+1",
     "घातों का योग सदैव n"
    ]
   },
   {
    "h": "व्यापक पद ⭐",
    "items": [
     "T(r+1) = C(n,r) aⁿ⁻ʳ bʳ",
     "T₅ के लिए r=4",
     "अचर पद: x घात = 0"
    ]
   },
   {
    "h": "मध्य पद ⭐",
    "items": [
     "n सम → T(n/2+1)",
     "n विषम → T((n+1)/2), T((n+3)/2)",
     "मध्य = महत्तम गुणांक"
    ]
   },
   {
    "h": "गुण ⭐",
    "items": [
     "Σ गुणांक = 2ⁿ",
     "एकांतर योग = 0",
     "सम योग = विषम योग = 2ⁿ⁻¹"
    ]
   },
   {
    "h": "तरकीबें",
    "items": [
     "शेषफल: आधार = गुणज ± 1",
     "पास्कल त्रिभुज = गुणांक",
     "अंत से k-वाँ = आरंभ से (n−k+2)-वाँ"
    ]
   }
  ],
  "en": [
   {
    "h": "Theorem ⭐",
    "items": [
     "(a+b)ⁿ = Σ C(n,r) aⁿ⁻ʳ bʳ",
     "Terms: n+1",
     "Powers always sum to n"
    ]
   },
   {
    "h": "General Term ⭐",
    "items": [
     "T(r+1) = C(n,r) aⁿ⁻ʳ bʳ",
     "T₅ needs r=4 (off-by-one trap!)",
     "Constant term: x power = 0"
    ]
   },
   {
    "h": "Middle Term ⭐",
    "items": [
     "n even → T(n/2+1)",
     "n odd → T((n+1)/2), T((n+3)/2)",
     "Middle = greatest coefficient"
    ]
   },
   {
    "h": "Properties ⭐",
    "items": [
     "Σ coefficients = 2ⁿ",
     "Alternating sum = 0",
     "Odd sum = even sum = 2ⁿ⁻¹"
    ]
   },
   {
    "h": "Tricks",
    "items": [
     "Remainder: base = multiple ± 1",
     "Pascal's triangle = coefficients",
     "k-th from end = (n−k+2)-th from start"
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
  "href": "/class-11/maths/ch-8/",
  "title": "Sequences and Series"
 }
}

# Class 11 Maths, Chapter 4 - Complex Numbers and Quadratic Equations
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 4,
 "title_en": "Complex Numbers and Quadratic Equations",
 "title_hi": "सम्मिश्र संख्याएं और द्विघातीय समीकरण",
 "tagline": "i = √−1 ki duniya — Argand plane, conjugates aur complex roots",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 4: Complex Numbers and Quadratic Equations — long + short notes in Hindi, English, Hinglish. Imaginary unit i, complex algebra, modulus, Argand plane, quadratic equations with complex roots.",
  "video": {
  "youtube": "c_0OsLZtyAQ",
  "dur": "1 min 20 sec"
 },
 "card_tag": "i = √−1 ki duniya — Argand plane, conjugates aur complex roots",
 "card_topics": [
  "🧮 i powers + algebra",
  "📊 Conjugate + modulus",
  "🗺️ Argand plane + polar form",
  "🔍 D &lt; 0 complex roots"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ i Ki Duniya — Imaginary Unit ⭐",
    "body": "<ul>\n<li><b>Problem:</b> x² + 1 = 0 ka koi real solution nahi (x² = −1!). Solution? Ek naya number invent karo: <b>i = √−1</b> jiska <b>i² = −1</b>.</li>\n<li><b>Powers of i ⭐ (cycle of 4):</b> i¹ = i, i² = −1, i³ = −i, i⁴ = 1 — phir repeat! i^n nikalne ke liye n ko 4 se divide, remainder dekho (i^2023 = i^3 = −i!).</li>\n<li><b>Complex number:</b> z = a + ib form — a = <b>real part</b> Re(z), b = <b>imaginary part</b> Im(z). (b real number hai, \"imaginary\" sirf naam hai!)</li>\n<li><b>Purely real:</b> b = 0 (z = 5). <b>Purely imaginary:</b> a = 0 (z = 3i).</li>\n<li><b>Equality:</b> a + ib = c + id tabhi jab a = c AUR b = d — dono parts alag-alag match karne chahiye! ⭐</li>\n<li>Complex numbers ka set C — R ⊂ C (har real number ek complex number hai with b = 0).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: i ek \"upgrade\" hai number system ka — jaise negative numbers ne subtraction ko hamesha possible kiya, i ne square roots ko hamesha possible kiya!</p>"
   },
   {
    "h": "2️⃣ Complex Algebra — Jod, Ghata, Guna ⭐",
    "body": "<ul>\n<li><b>Add/Subtract:</b> real parts apas me, imaginary parts apas me — (a + ib) + (c + id) = (a + c) + i(b + d). Bas itna hi!</li>\n<li><b>Multiply:</b> normal expansion, bas <b>i² = −1 substitute</b> kar do: (a + ib)(c + id) = (ac − bd) + i(ad + bc). ⭐</li>\n<li><b>Conjugate ⭐:</b> z = a + ib ka conjugate z̄ = a − ib — sirf imaginary part ka sign flip. (z + z̄ = 2a real; z − z̄ = 2ib purely imaginary!)</li>\n<li><b>zz̄ = a² + b²</b> — hamesha REAL aur non-negative! Division ka master key yahi hai.</li>\n<li><b>Division ⭐:</b> numerator-denominator dono ko denominator ke CONJUGATE se multiply karo: (a+ib)/(c+id) = (a+ib)(c−id)/(c²+d²) — denominator real ban jaata hai!</li>\n<li><b>Properties:</b> z̄₁ + z̄₂ = conjugate of sum; conjugate of product = product of conjugates; z = z̄ ⟺ z real.</li>\n</ul>\n<p class=\"small-note\">🎯 Division trick yaad rakho: \"conjugate se multiply\" — surds me rationalize karte the na (√2+1 ke saath √2−1), wahi game, bas i ke saath!</p>"
   },
   {
    "h": "3️⃣ Modulus aur Argand Plane ⭐",
    "body": "<ul>\n<li><b>Argand plane:</b> complex number z = a + ib ko point (a, b) se dikhate hain — x-axis = real, y-axis = imaginary. Har complex number ek POINT (ya vector)!</li>\n<li><b>Modulus ⭐:</b> |z| = √(a² + b²) — origin se point ki DISTANCE. Hamesha non-negative real.</li>\n<li><b>|z|² = zz̄</b> — modulus aur conjugate ka connection (proof: zz̄ = a² + b² hi to hai!).</li>\n<li><b>Argument (arg z):</b> positive real axis se angle θ — tan θ = b/a (QUADRANT dekh ke θ lo — sirf formula se galat ho jaata hai!). ⭐</li>\n<li><b>Polar form:</b> z = r(cos θ + i sin θ) jahan r = |z| — modulus-argument style me likhna.</li>\n<li><b>Properties:</b> |z₁z₂| = |z₁||z₂|; |z₁/z₂| = |z₁|/|z₂|; triangle inequality |z₁ + z₂| ≤ |z₁| + |z₂|. ⭐</li>\n</ul>\n<p class=\"small-note\">💡 Feel: complex number = plane ka point. Modulus = origin se doori (Pythagoras!), argument = direction (angle). Real geometry, sirf \"imaginary\" naam!</p>"
   },
   {
    "h": "4️⃣ Quadratic Equations — Ab Complex Roots Bhi ⭐",
    "body": "<ul>\n<li><b>Standard form:</b> ax² + bx + c = 0 (a ≠ 0). <b>Quadratic formula ⭐:</b> x = (−b ± √(b² − 4ac))/2a.</li>\n<li><b>Discriminant D = b² − 4ac ⭐:</b> D &gt; 0 → do ALG real roots; D = 0 → do EQUAL real roots (x = −b/2a); D &lt; 0 → do COMPLEX conjugate roots!</li>\n<li><b>Complex roots hamesha conjugate pairs me aate hain ⭐:</b> agar 2 + 3i ek root hai (real coefficients me), to 2 − 3i bhi root hai PAKKA.</li>\n<li><b>Sum and product ⭐:</b> roots ka sum = −b/a, product = c/a — Vieta's relations (bahut kaam ke!).</li>\n<li><b>Equation banana:</b> roots p, q hon → x² − (sum)x + product = 0 → x² − (p+q)x + pq = 0.</li>\n<li><b>Example:</b> x² + 2x + 5 = 0 → D = 4 − 20 = −16 → x = (−2 ± 4i)/2 = −1 ± 2i.</li>\n</ul>\n<p class=\"small-note\">🎯 D &lt; 0 ka matlab ab \"no solution\" NAHI — \"complex solutions\" hai! Complex numbers ke baad HAR quadratic solvable hai.</p>"
   },
   {
    "h": "5️⃣ Square Roots of Complex Numbers aur Tricks",
    "body": "<ul>\n<li><b>√(a + ib) nikalna ⭐:</b> maano √(a+ib) = x + iy → square karke compare: x² − y² = a, 2xy = b. Do equations, solve for x, y (dono signs possible — do roots!).</li>\n<li><b>Formula shortcut:</b> x = √((|z| + a)/2), y = ±√((|z| − a)/2) — y ka sign b ke sign pe (b &gt; 0 to same signs, b &lt; 0 to opposite). ⭐</li>\n<li><b>Cube roots of unity ⭐:</b> x³ = 1 ke roots: 1, ω, ω² jahan ω = (−1 + i√3)/2. Properties: 1 + ω + ω² = 0, ω³ = 1. (JEE favourite!)</li>\n<li><b>i ke powers simplify:</b> (1 + i)² = 2i, (1 − i)² = −2i, (1 + i)(1 − i) = 2. ⭐</li>\n<li><b>1/i = −i</b> (kyunki i × (−i) = −i² = 1) — division simplify karne me kaam aata hai.</li>\n</ul>\n<p class=\"small-note\">💡 ω ka 1 + ω + ω² = 0 wala property questions ko 2 line me khatam kar deta hai — ratna nahi, SAMAJHNA: teen roots ek triangle banate hain Argand plane pe, sum zero!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ i की दुनिया — काल्पनिक इकाई ⭐",
    "body": "<ul>\n<li><b>समस्या:</b> x² + 1 = 0 का कोई वास्तविक हल नहीं। समाधान? नई संख्या: <b>i = √−1</b> जिसका <b>i² = −1</b>।</li>\n<li><b>i की घातें ⭐ (4 का चक्र):</b> i¹ = i, i² = −1, i³ = −i, i⁴ = 1 — फिर दोहराव! i^n के लिए n को 4 से भाग दो।</li>\n<li><b>सम्मिश्र संख्या:</b> z = a + ib — a = वास्तविक भाग, b = काल्पनिक भाग।</li>\n<li><b>शुद्ध वास्तविक:</b> b = 0। <b>शुद्ध काल्पनिक:</b> a = 0।</li>\n<li><b>समानता:</b> a + ib = c + id ⟺ a = c और b = d। ⭐</li>\n</ul>\n<p class=\"small-note\">💡 i संख्या प्रणाली का \"अपग्रेड\" — जैसे ऋण संख्याओं ने घटाव संभव किया, i ने वर्गमूल संभव किया!</p>"
   },
   {
    "h": "2️⃣ सम्मिश्र बीजगणित — जोड़, घटाव, गुणा ⭐",
    "body": "<ul>\n<li><b>जोड़/घटाव:</b> वास्तविक भाग आपस में, काल्पनिक आपस में — (a + c) + i(b + d)।</li>\n<li><b>गुणा:</b> सामान्य प्रसार, <b>i² = −1 प्रतिस्थापित</b>: (a + ib)(c + id) = (ac − bd) + i(ad + bc)। ⭐</li>\n<li><b>संयुग्मी ⭐:</b> z = a + ib का संयुग्मी z̄ = a − ib। (z + z̄ = 2a वास्तविक!)</li>\n<li><b>zz̄ = a² + b²</b> — सदैव वास्तविक और ऋणेतर!</li>\n<li><b>भाग ⭐:</b> अंश-हर दोनों को हर के संयुग्मी से गुणा करो — हर वास्तविक बन जाता है!</li>\n</ul>\n<p class=\"small-note\">🎯 भाग की युक्ति: \"संयुग्मी से गुणा\" — परिमेयकरण जैसा खेल!</p>"
   },
   {
    "h": "3️⃣ मापांक और आर्गंड तल ⭐",
    "body": "<ul>\n<li><b>आर्गंड तल:</b> z = a + ib को बिंदु (a, b) से — x-अक्ष वास्तविक, y-अक्ष काल्पनिक।</li>\n<li><b>मापांक ⭐:</b> |z| = √(a² + b²) — मूलबिंदु से दूरी।</li>\n<li><b>|z|² = zz̄</b> — मापांक-संयुग्मी संबंध।</li>\n<li><b>कोणांक (arg z):</b> धन वास्तविक अक्ष से कोण — tan θ = b/a (<b>चतुर्थांश</b> देखकर!)। ⭐</li>\n<li><b>ध्रुवीय रूप:</b> z = r(cos θ + i sin θ)।</li>\n<li><b>गुण:</b> |z₁z₂| = |z₁||z₂|; |z₁ + z₂| ≤ |z₁| + |z₂| (त्रिभुज असमिका)। ⭐</li>\n</ul>\n<p class=\"small-note\">💡 सम्मिश्र संख्या = तल का बिंदु। मापांक = दूरी, कोणांक = दिशा।</p>"
   },
   {
    "h": "4️⃣ द्विघात समीकरण — अब सम्मिश्र मूल भी ⭐",
    "body": "<ul>\n<li><b>मानक रूप:</b> ax² + bx + c = 0। <b>द्विघात सूत्र ⭐:</b> x = (−b ± √(b² − 4ac))/2a।</li>\n<li><b>विविक्तकर D = b² − 4ac ⭐:</b> D &gt; 0 → दो भिन्न वास्तविक मूल; D = 0 → दो समान मूल; D &lt; 0 → दो सम्मिश्र संयुग्मी मूल!</li>\n<li><b>सम्मिश्र मूल सदैव संयुग्मी युग्म में ⭐:</b> यदि 2 + 3i एक मूल है (वास्तविक गुणांकों में), तो 2 − 3i भी मूल है।</li>\n<li><b>योग और गुणनफल ⭐:</b> मूलों का योग = −b/a, गुणनफल = c/a।</li>\n<li><b>समीकरण बनाना:</b> मूल p, q → x² − (p+q)x + pq = 0।</li>\n<li><b>उदाहरण:</b> x² + 2x + 5 = 0 → D = −16 → x = −1 ± 2i।</li>\n</ul>\n<p class=\"small-note\">🎯 D &lt; 0 का अर्थ \"कोई हल नहीं\" नहीं — \"सम्मिश्र हल\" है!</p>"
   },
   {
    "h": "5️⃣ सम्मिश्र वर्गमूल और युक्तियां",
    "body": "<ul>\n<li><b>√(a + ib) ⭐:</b> माना √(a+ib) = x + iy → वर्ग करके तुलना: x² − y² = a, 2xy = b।</li>\n<li><b>शॉर्टकट:</b> x = √((|z| + a)/2), y = ±√((|z| − a)/2)। ⭐</li>\n<li><b>इकाई के घनमूल ⭐:</b> x³ = 1 के मूल: 1, ω, ω² जहां ω = (−1 + i√3)/2। 1 + ω + ω² = 0, ω³ = 1।</li>\n<li><b>सरलीकरण:</b> (1 + i)² = 2i, (1 + i)(1 − i) = 2, 1/i = −i। ⭐</li>\n</ul>\n<p class=\"small-note\">💡 1 + ω + ω² = 0 — तीनों मूल आर्गंड तल पर त्रिभुज बनाते हैं, योग शून्य!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ The World of i — The Imaginary Unit ⭐",
    "body": "<ul>\n<li><b>The problem:</b> x² + 1 = 0 has no real solution (x² = −1!). The fix? Invent a new number: <b>i = √−1</b> with <b>i² = −1</b>.</li>\n<li><b>Powers of i ⭐ (cycle of 4):</b> i¹ = i, i² = −1, i³ = −i, i⁴ = 1 — then it repeats! To find i^n, divide n by 4 and check the remainder (i^2023 = i³ = −i!).</li>\n<li><b>Complex number:</b> the form z = a + ib — a = the <b>real part</b> Re(z), b = the <b>imaginary part</b> Im(z). (b is a real number; \"imaginary\" is just a name!)</li>\n<li><b>Purely real:</b> b = 0 (z = 5). <b>Purely imaginary:</b> a = 0 (z = 3i).</li>\n<li><b>Equality:</b> a + ib = c + id only when a = c AND b = d — both parts must match separately! ⭐</li>\n<li>The set of complex numbers is C — R ⊂ C (every real number is a complex number with b = 0).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: i is an upgrade to the number system — just as negatives made subtraction always possible, i makes square roots always possible!</p>"
   },
   {
    "h": "2️⃣ Complex Algebra — Add, Subtract, Multiply ⭐",
    "body": "<ul>\n<li><b>Add/Subtract:</b> combine the real parts and the imaginary parts separately — (a + ib) + (c + id) = (a + c) + i(b + d). That is all!</li>\n<li><b>Multiply:</b> expand normally, then <b>substitute i² = −1</b>: (a + ib)(c + id) = (ac − bd) + i(ad + bc). ⭐</li>\n<li><b>Conjugate ⭐:</b> the conjugate of z = a + ib is z̄ = a − ib — flip only the imaginary part's sign. (z + z̄ = 2a is real; z − z̄ = 2ib is purely imaginary!)</li>\n<li><b>zz̄ = a² + b²</b> — always REAL and non-negative! This is the master key for division.</li>\n<li><b>Division ⭐:</b> multiply numerator and denominator by the denominator's CONJUGATE: (a+ib)/(c+id) = (a+ib)(c−id)/(c²+d²) — the denominator turns real!</li>\n<li><b>Properties:</b> the conjugate of a sum = the sum of conjugates; the conjugate of a product = the product of conjugates; z = z̄ ⟺ z is real.</li>\n</ul>\n<p class=\"small-note\">🎯 Remember the division trick: \"multiply by the conjugate\" — the same game as rationalizing surds (√2+1 with √2−1), just with i!</p>"
   },
   {
    "h": "3️⃣ The Modulus and the Argand Plane ⭐",
    "body": "<ul>\n<li><b>Argand plane:</b> the complex number z = a + ib is shown as the point (a, b) — x-axis = real, y-axis = imaginary. Every complex number is a POINT (or vector)!</li>\n<li><b>Modulus ⭐:</b> |z| = √(a² + b²) — the DISTANCE from the origin. Always a non-negative real.</li>\n<li><b>|z|² = zz̄</b> — the modulus-conjugate connection (zz̄ = a² + b² exactly!).</li>\n<li><b>Argument (arg z):</b> the angle θ from the positive real axis — tan θ = b/a (check the QUADRANT; the formula alone misleads!). ⭐</li>\n<li><b>Polar form:</b> z = r(cos θ + i sin θ) where r = |z| — writing in modulus-argument style.</li>\n<li><b>Properties:</b> |z₁z₂| = |z₁||z₂|; |z₁/z₂| = |z₁|/|z₂|; the triangle inequality |z₁ + z₂| ≤ |z₁| + |z₂|. ⭐</li>\n</ul>\n<p class=\"small-note\">💡 Feel: a complex number is a point on the plane. Modulus = distance from the origin (Pythagoras!), argument = direction (angle). Real geometry, just an \"imaginary\" name!</p>"
   },
   {
    "h": "4️⃣ Quadratic Equations — Now with Complex Roots ⭐",
    "body": "<ul>\n<li><b>Standard form:</b> ax² + bx + c = 0 (a ≠ 0). <b>The quadratic formula ⭐:</b> x = (−b ± √(b² − 4ac))/2a.</li>\n<li><b>Discriminant D = b² − 4ac ⭐:</b> D &gt; 0 → two DIFFERENT real roots; D = 0 → two EQUAL real roots (x = −b/2a); D &lt; 0 → two COMPLEX conjugate roots!</li>\n<li><b>Complex roots always come in conjugate pairs ⭐:</b> if 2 + 3i is a root (with real coefficients), then 2 − 3i is a root for sure.</li>\n<li><b>Sum and product ⭐:</b> sum of roots = −b/a, product = c/a — Vieta's relations (hugely useful!).</li>\n<li><b>Building an equation:</b> if the roots are p, q → x² − (sum)x + product = 0 → x² − (p+q)x + pq = 0.</li>\n<li><b>Example:</b> x² + 2x + 5 = 0 → D = 4 − 20 = −16 → x = (−2 ± 4i)/2 = −1 ± 2i.</li>\n</ul>\n<p class=\"small-note\">🎯 D &lt; 0 no longer means \"no solution\" — it means \"complex solutions\"! With complex numbers, EVERY quadratic is solvable.</p>"
   },
   {
    "h": "5️⃣ Square Roots of Complex Numbers and Tricks",
    "body": "<ul>\n<li><b>Finding √(a + ib) ⭐:</b> let √(a+ib) = x + iy → square and compare: x² − y² = a, 2xy = b. Two equations, solve for x, y (both signs possible — two roots!).</li>\n<li><b>Formula shortcut:</b> x = √((|z| + a)/2), y = ±√((|z| − a)/2) — the sign of y depends on b (b &gt; 0 → same signs, b &lt; 0 → opposite). ⭐</li>\n<li><b>Cube roots of unity ⭐:</b> the roots of x³ = 1 are 1, ω, ω² where ω = (−1 + i√3)/2. Properties: 1 + ω + ω² = 0, ω³ = 1. (A JEE favourite!)</li>\n<li><b>Handy simplifications:</b> (1 + i)² = 2i, (1 − i)² = −2i, (1 + i)(1 − i) = 2. ⭐</li>\n<li><b>1/i = −i</b> (since i × (−i) = −i² = 1) — useful for simplifying division.</li>\n</ul>\n<p class=\"small-note\">💡 The property 1 + ω + ω² = 0 kills questions in two lines — do not just memorize it, SEE it: the three roots form a triangle on the Argand plane, so their sum is zero!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "i Basics ⭐",
    "items": [
     "i² = −1; cycle: i, −1, −i, 1",
     "z = a + ib (a real, b imag)",
     "i^n: n mod 4 dekho"
    ]
   },
   {
    "h": "Algebra ⭐",
    "items": [
     "Multiply: i² → −1 substitute",
     "Conjugate z̄ = a − ib",
     "zz̄ = a² + b² (real!)"
    ]
   },
   {
    "h": "Argand ⭐",
    "items": [
     "|z| = √(a²+b²) = distance",
     "arg z: tan θ = b/a (quadrant!)",
     "|z₁z₂| = |z₁||z₂|"
    ]
   },
   {
    "h": "Quadratic ⭐",
    "items": [
     "D &lt; 0 → complex conjugate pair",
     "Sum = −b/a, product = c/a",
     "x² − (sum)x + product = 0"
    ]
   },
   {
    "h": "Tricks",
    "items": [
     "1/i = −i; (1+i)² = 2i",
     "ω³ = 1, 1+ω+ω² = 0",
     "√z: x²−y²=a, 2xy=b"
    ]
   }
  ],
  "hi": [
   {
    "h": "i मूल ⭐",
    "items": [
     "i² = −1; चक्र: i, −1, −i, 1",
     "z = a + ib",
     "i^n: n mod 4"
    ]
   },
   {
    "h": "बीजगणित ⭐",
    "items": [
     "गुणा: i² → −1",
     "संयुग्मी z̄ = a − ib",
     "zz̄ = a² + b²"
    ]
   },
   {
    "h": "आर्गंड ⭐",
    "items": [
     "|z| = √(a²+b²)",
     "arg z: चतुर्थांश देखो",
     "|z₁z₂| = |z₁||z₂|"
    ]
   },
   {
    "h": "द्विघात ⭐",
    "items": [
     "D &lt; 0 → संयुग्मी युग्म",
     "योग = −b/a, गुणनफल = c/a",
     "x² − (योग)x + गुणनफल = 0"
    ]
   },
   {
    "h": "युक्तियां",
    "items": [
     "1/i = −i; (1+i)² = 2i",
     "ω³ = 1, 1+ω+ω² = 0",
     "√z: x²−y²=a, 2xy=b"
    ]
   }
  ],
  "en": [
   {
    "h": "i Basics ⭐",
    "items": [
     "i² = −1; cycle: i, −1, −i, 1",
     "z = a + ib (a real, b imag)",
     "i^n: check n mod 4"
    ]
   },
   {
    "h": "Algebra ⭐",
    "items": [
     "Multiply: substitute i² → −1",
     "Conjugate z̄ = a − ib",
     "zz̄ = a² + b² (real!)"
    ]
   },
   {
    "h": "Argand ⭐",
    "items": [
     "|z| = √(a²+b²) = distance",
     "arg z: tan θ = b/a (quadrant!)",
     "|z₁z₂| = |z₁||z₂|"
    ]
   },
   {
    "h": "Quadratic ⭐",
    "items": [
     "D &lt; 0 → complex conjugate pair",
     "Sum = −b/a, product = c/a",
     "x² − (sum)x + product = 0"
    ]
   },
   {
    "h": "Tricks",
    "items": [
     "1/i = −i; (1+i)² = 2i",
     "ω³ = 1, 1+ω+ω² = 0",
     "√z: x²−y²=a, 2xy=b"
    ]
   }
  ]
 },
 "practice": [
  [
   "i^47 ka value?",
   "47 = 4×11 + 3 → i^47 = i³ = <b>−i</b>."
  ],
  [
   "(2 + 3i)(1 − i) multiply karo.",
   "= 2 − 2i + 3i − 3i² = 2 + i + 3 = <b>5 + i</b> (i² = −1 substitute kiya!)."
  ],
  [
   "z = 3 + 4i. |z| aur z̄?",
   "|z| = √(9 + 16) = <b>5</b>; z̄ = <b>3 − 4i</b>."
  ],
  [
   "(1 + i)/(1 − i) simplify karo.",
   "Conjugate se multiply: (1+i)²/((1)²+(1)²) = 2i/2 = <b>i</b>."
  ],
  [
   "x² − 4x + 13 = 0 ke roots?",
   "D = 16 − 52 = −36 → x = (4 ± 6i)/2 = <b>2 ± 3i</b> (conjugate pair!)."
  ],
  [
   "Ek quadratic ke roots 3 + 2i aur 3 − 2i hain. Equation?",
   "Sum = 6, product = 9 + 4 = 13 → <b>x² − 6x + 13 = 0</b>."
  ],
  [
   "Real coefficients wali quadratic ka ek root 1 + i hai. Dusra?",
   "<b>1 − i</b> — complex roots hamesha conjugate pairs me aate hain."
  ],
  [
   "1 + ω + ω² ka value? (ω = cube root of unity)",
   "<b>0</b> — aur ω³ = 1. Dono properties JEE favourites hain."
  ],
  [
   "z = 1 + i√3 ko polar form me likho.",
   "r = √(1+3) = 2, tan θ = √3 → θ = π/3 (Q1) → z = <b>2(cos π/3 + i sin π/3)</b>."
  ],
  [
   "1/i ko a + ib form me?",
   "1/i = 1/i × (−i)/(−i) = −i/1 = <b>−i</b> (ya 0 − 1i)."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/maths/ch-5/",
  "title": "Linear Inequalities"
 }
}

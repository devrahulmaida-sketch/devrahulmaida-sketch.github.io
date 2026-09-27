# Class 12 Maths, Chapter 3 - Matrices
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 3,
 "title_en": "Matrices",
 "title_hi": "आव्यूह",
 "tagline": "Grids ka ganit — operations, transpose, symmetric matrices aur inverse",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 3: Matrices — long + short notes in Hindi, English, Hinglish. Matrix operations, multiplication, transpose, symmetric and skew-symmetric matrices, invertible matrices.",
 "video": None,
 "card_tag": "Grids ka ganit — operations, transpose, symmetric matrices aur inverse",
 "card_topics": [
  "🔢 Matrix basics + order",
  "✖️ Multiplication (AB ≠ BA!)",
  "🔁 Transpose + symmetric/skew",
  "↩️ Inverse concept"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Matrix Kya Hai — Numbers Ka Grid",
    "body": "<ul>\n<li><b>Matrix:</b> numbers/symbols ka rectangular arrangement rows aur columns me — data ko organize karne ka super-tool (marks tables, images, networks sab matrices hain!).</li>\n<li><b>Order ⭐:</b> m × n matlab m rows, n columns. 3 × 2 matrix = 3 rows, 2 columns, total <b>6 elements</b>.</li>\n<li><b>Element aᵢⱼ:</b> i-th row, j-th column wala number. Pehle ROW, phir COLUMN — \"row pehle, column baad me\".</li>\n<li>Do matrices <b>equal</b> tab: same order AUR har corresponding element same.</li>\n<li>Example: A = [2 3; 1 −4] (2×2), a₁₂ = 3, a₂₁ = 1.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: matrix = Excel sheet of numbers. Address system bilkul spreadsheet jaisa — (row, column).</p>"
   },
   {
    "h": "2️⃣ Matrices Ke Types ⭐",
    "body": "<ul>\n<li><b>Row matrix:</b> 1 × n. <b>Column matrix:</b> m × 1. <b>Square matrix:</b> m = n (order n).</li>\n<li><b>Zero matrix (O):</b> saare elements 0. <b>Diagonal matrix:</b> square matrix jisme non-diagonal elements 0 — sirf a₁₁, a₂₂, ... non-zero ho sakte hain.</li>\n<li><b>Scalar matrix:</b> diagonal + saare diagonal elements EQUAL (k, k, k...). <b>Identity matrix (I) ⭐:</b> diagonal pe 1, baaki 0 — multiplication ka \"1\" (AI = IA = A).</li>\n<li><b>Upper triangular:</b> diagonal ke NEECHE sab 0. <b>Lower triangular:</b> diagonal ke UPAR sab 0.</li>\n<li><b>Equal matrices:</b> same order + same elements, element-by-element.</li>\n</ul>\n<p class=\"small-note\">🎯 Identity matrix = matrix duniya ka 1. Har square matrix A ke liye AI = IA = A. Isse inverse ka concept banta hai!</p>"
   },
   {
    "h": "3️⃣ Operations — Add, Subtract, Multiply ⭐⭐",
    "body": "<ul>\n<li><b>Addition/Subtraction:</b> SIRF same-order matrices — corresponding elements add/subtract karo. A + B = B + A (commutative hai!).</li>\n<li><b>Scalar multiplication:</b> kA = har element ko k se multiply — har element pe kaam karta hai, sirf ek pe nahi!</li>\n<li><b>Matrix multiplication ⭐⭐:</b> A(m×n) × B(n×p) possible SIRF jab A ke columns = B ki rows → result m×p. Element (i,j) = <b>row i of A · column j of B</b> (dot product).</li>\n<li><b>AB ≠ BA generally! ⭐⭐</b> Matrix multiplication commutative NAHI hota — order matter karta hai. Kabhi-kabhi AB possible ho aur BA possible hi na ho!</li>\n<li>AB = O ka matlab A = O ya B = O <b>NAHI</b> hai — non-zero matrices ka product bhi zero aa sakta hai!</li>\n<li>Associative: (AB)C = A(BC). Distributive: A(B + C) = AB + AC.</li>\n</ul>\n<p class=\"small-note\">💡 Multiplication = \"row ko column se milao\". Pehla element: pehli row × pehli column, phir slide karte jao.</p>"
   },
   {
    "h": "4️⃣ Transpose aur Symmetric/Skew-Symmetric ⭐",
    "body": "<ul>\n<li><b>Transpose (A′ ya Aᵀ):</b> rows ko columns bana do — (A′)ᵢⱼ = aⱼᵢ. m×n → n×m ho jaati hai.</li>\n<li><b>Transpose ke rules ⭐:</b> (A′)′ = A; (A + B)′ = A′ + B′; (kA)′ = kA′; <b>(AB)′ = B′A′</b> — ORDER ULAT JAATA HAI!</li>\n<li><b>Symmetric matrix ⭐:</b> A′ = A — diagonal ke across mirror image. (aᵢⱼ = aⱼᵢ)</li>\n<li><b>Skew-symmetric matrix ⭐:</b> A′ = −A — diagonal elements ZAROOR 0 hote hain (aᵢᵢ = −aᵢᵢ → 0)!</li>\n<li><b>Power move ⭐⭐:</b> HAR square matrix = symmetric + skew-symmetric ka sum: <b>A = ½(A + A′) + ½(A − A′)</b> — pehla part symmetric, doosra skew-symmetric. Direct 3-marker!</li>\n</ul>\n<p class=\"small-note\">🎯 (AB)′ = B′A′ — \"ulti taraf se transpose karo\". Sabse zyada test hone wala rule!</p>"
   },
   {
    "h": "5️⃣ Invertible Matrices aur Syllabus Note",
    "body": "<ul>\n<li><b>Invertible matrix:</b> square matrix A invertible hai agar koi B mile jisse AB = BA = I — wo B hai <b>A⁻¹</b> (inverse). Inverse UNIQUE hota hai.</li>\n<li><b>(AB)⁻¹ = B⁻¹A⁻¹ ⭐</b> — transpose jaisa hi order-flip rule!</li>\n<li>Inverse nikalne ka tareeqa (adjoint method) <b>Chapter 4 (Determinants)</b> me aata hai — pehle determinant seekhna zaroori hai.</li>\n<li><b>Rationalized syllabus ⭐:</b> <b>elementary row/column operations</b> (aur unse inverse nikalna) NCERT se <b>DELETE</b> ho gaye — ab inverse sirf adjoint method se.</li>\n<li>Word problems: matrices se data organize + multiply karna (price × quantity type) — boards me aata rehta hai.</li>\n</ul>\n<p class=\"small-note\">💡 Inverse = \"undo\" matrix. Number me jaise ×3 ka undo ÷3, waise matrix me A ka undo A⁻¹.</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ आव्यूह क्या है — संख्याओं का ग्रिड",
    "body": "<ul>\n<li><b>आव्यूह (matrix):</b> संख्याओं/प्रतीकों का आयताकार विन्यास पंक्तियों और स्तंभों में।</li>\n<li><b>कोटि (order) ⭐:</b> m × n यानी m पंक्तियां, n स्तंभ — कुल <b>mn अवयव</b>।</li>\n<li><b>अवयव aᵢⱼ:</b> i-वीं पंक्ति, j-वां स्तंभ। पहले पंक्ति, फिर स्तंभ!</li>\n<li>दो आव्यूह <b>समान</b> तब: समान कोटि और प्रत्येक संगत अवयव समान।</li>\n</ul>\n<p class=\"small-note\">💡 आव्यूह = संख्याओं की स्प्रेडशीट। पता: (पंक्ति, स्तंभ)।</p>"
   },
   {
    "h": "2️⃣ आव्यूहों के प्रकार ⭐",
    "body": "<ul>\n<li><b>पंक्ति आव्यूह:</b> 1 × n। <b>स्तंभ आव्यूह:</b> m × 1। <b>वर्ग आव्यूह:</b> m = n।</li>\n<li><b>शून्य आव्यूह:</b> सभी अवयव 0। <b>विकर्ण आव्यूह:</b> अविकर्ण अवयव 0।</li>\n<li><b>अदिश आव्यूह:</b> विकर्ण पर सभी समान। <b>तत्समक आव्यूह (I) ⭐:</b> विकर्ण पर 1, शेष 0 — AI = IA = A।</li>\n<li><b>उपरि-त्रिभुजीय:</b> विकर्ण के नीचे सब 0। <b>अधो-त्रिभुजीय:</b> ऊपर सब 0।</li>\n</ul>\n<p class=\"small-note\">🎯 तत्समक आव्यूह = आव्यूह संसार का 1।</p>"
   },
   {
    "h": "3️⃣ संक्रियाएं — जोड़, घटाव, गुणन ⭐⭐",
    "body": "<ul>\n<li><b>योग/व्यवकलन:</b> केवल समान-कोटि आव्यूह — संगत अवयव जोड़ो/घटाओ। A + B = B + A।</li>\n<li><b>अदिश गुणन:</b> kA = प्रत्येक अवयव × k।</li>\n<li><b>आव्यूह गुणन ⭐⭐:</b> A(m×n) × B(n×p) केवल तब जब A के स्तंभ = B की पंक्तियां → परिणाम m×p। अवयव (i,j) = <b>A की पंक्ति i · B का स्तंभ j</b>।</li>\n<li><b>सामान्यतः AB ≠ BA! ⭐⭐</b> गुणन क्रमविनिमेय <b>नहीं</b>।</li>\n<li>AB = O का अर्थ A = O या B = O <b>नहीं</b>!</li>\n<li>साहचर्य: (AB)C = A(BC)। वितरण: A(B + C) = AB + AC।</li>\n</ul>\n<p class=\"small-note\">💡 गुणन = \"पंक्ति को स्तंभ से मिलाओ\"।</p>"
   },
   {
    "h": "4️⃣ परिवर्त और सममित/विषम-सममित ⭐",
    "body": "<ul>\n<li><b>परिवर्त (A′):</b> पंक्तियों को स्तंभ बना दो — (A′)ᵢⱼ = aⱼᵢ।</li>\n<li><b>नियम ⭐:</b> (A′)′ = A; (A + B)′ = A′ + B′; <b>(AB)′ = B′A′</b> — क्रम उलट जाता है!</li>\n<li><b>सममित ⭐:</b> A′ = A। <b>विषम-सममित ⭐:</b> A′ = −A — विकर्ण अवयव अनिवार्य रूप से <b>0</b>!</li>\n<li><b>महत्वपूर्ण ⭐⭐:</b> प्रत्येक वर्ग आव्यूह = सममित + विषम-सममित: <b>A = ½(A + A′) + ½(A − A′)</b>।</li>\n</ul>\n<p class=\"small-note\">🎯 (AB)′ = B′A′ — सबसे अधिक परीक्षित नियम!</p>"
   },
   {
    "h": "5️⃣ व्युत्क्रमणीय आव्यूह और पाठ्यक्रम टिप्पणी",
    "body": "<ul>\n<li><b>व्युत्क्रमणीय आव्यूह:</b> यदि AB = BA = I हो तो B = <b>A⁻¹</b>। व्युत्क्रम अद्वितीय होता है।</li>\n<li><b>(AB)⁻¹ = B⁻¹A⁻¹ ⭐</b> — क्रम उलटने का नियम!</li>\n<li>व्युत्क्रम की विधि (सहखंडज) <b>अध्याय 4 (सारणिक)</b> में आती है।</li>\n<li><b>युक्तिसंगत पाठ्यक्रम ⭐:</b> <b>प्रारंभिक पंक्ति/स्तंभ संक्रियाएं</b> NCERT से <b>हटाई गईं</b> — व्युत्क्रम अब केवल सहखंडज विधि से।</li>\n</ul>\n<p class=\"small-note\">💡 व्युत्क्रम = \"पूर्ववत\" आव्यूह।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ What Is a Matrix — A Grid of Numbers",
    "body": "<ul>\n<li><b>Matrix:</b> a rectangular arrangement of numbers/symbols in rows and columns — a super-tool for organizing data (marks tables, images, networks are all matrices!).</li>\n<li><b>Order ⭐:</b> m × n means m rows, n columns. A 3 × 2 matrix has 3 rows, 2 columns, <b>6 elements</b> total.</li>\n<li><b>Element aᵢⱼ:</b> the number in the i-th row, j-th column. ROW first, COLUMN second.</li>\n<li>Two matrices are <b>equal</b> only when: same order AND every corresponding element matches.</li>\n<li>Example: A = [2 3; 1 −4] (2×2), a₁₂ = 3, a₂₁ = 1.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: a matrix is an Excel sheet of numbers. The address system works exactly like a spreadsheet — (row, column).</p>"
   },
   {
    "h": "2️⃣ Types of Matrices ⭐",
    "body": "<ul>\n<li><b>Row matrix:</b> 1 × n. <b>Column matrix:</b> m × 1. <b>Square matrix:</b> m = n (order n).</li>\n<li><b>Zero matrix (O):</b> every element is 0. <b>Diagonal matrix:</b> a square matrix whose non-diagonal elements are 0.</li>\n<li><b>Scalar matrix:</b> diagonal + all diagonal entries EQUAL (k, k, k...). <b>Identity matrix (I) ⭐:</b> 1s on the diagonal, 0 elsewhere — the \"1\" of multiplication (AI = IA = A).</li>\n<li><b>Upper triangular:</b> everything BELOW the diagonal is 0. <b>Lower triangular:</b> everything ABOVE the diagonal is 0.</li>\n<li><b>Equal matrices:</b> same order + same elements, element by element.</li>\n</ul>\n<p class=\"small-note\">🎯 The identity matrix is the matrix world's 1. For every square matrix A, AI = IA = A. This is where the idea of an inverse comes from!</p>"
   },
   {
    "h": "3️⃣ Operations — Add, Subtract, Multiply ⭐⭐",
    "body": "<ul>\n<li><b>Addition/Subtraction:</b> ONLY same-order matrices — add/subtract corresponding elements. A + B = B + A (commutative!).</li>\n<li><b>Scalar multiplication:</b> kA = multiply EVERY element by k — it hits all elements, not just one!</li>\n<li><b>Matrix multiplication ⭐⭐:</b> A(m×n) × B(n×p) works ONLY when A's columns = B's rows → result is m×p. Element (i,j) = <b>row i of A · column j of B</b> (a dot product).</li>\n<li><b>AB ≠ BA in general! ⭐⭐</b> Matrix multiplication is NOT commutative — order matters. Sometimes AB exists and BA does not!</li>\n<li>AB = O does NOT mean A = O or B = O — non-zero matrices can multiply to zero!</li>\n<li>Associative: (AB)C = A(BC). Distributive: A(B + C) = AB + AC.</li>\n</ul>\n<p class=\"small-note\">💡 Multiplication = \"marry a row with a column\". First element: first row × first column, then keep sliding.</p>"
   },
   {
    "h": "4️⃣ Transpose and Symmetric/Skew-Symmetric ⭐",
    "body": "<ul>\n<li><b>Transpose (A′ or Aᵀ):</b> turn rows into columns — (A′)ᵢⱼ = aⱼᵢ. An m×n matrix becomes n×m.</li>\n<li><b>Transpose rules ⭐:</b> (A′)′ = A; (A + B)′ = A′ + B′; (kA)′ = kA′; <b>(AB)′ = B′A′</b> — the ORDER FLIPS!</li>\n<li><b>Symmetric matrix ⭐:</b> A′ = A — a mirror image across the diagonal (aᵢⱼ = aⱼᵢ).</li>\n<li><b>Skew-symmetric matrix ⭐:</b> A′ = −A — diagonal entries MUST be 0 (aᵢᵢ = −aᵢᵢ → 0)!</li>\n<li><b>Power move ⭐⭐:</b> EVERY square matrix = symmetric + skew-symmetric: <b>A = ½(A + A′) + ½(A − A′)</b> — the first part is symmetric, the second skew-symmetric. A direct 3-marker!</li>\n</ul>\n<p class=\"small-note\">🎯 (AB)′ = B′A′ — \"transpose from the back\". The most-tested rule of the chapter!</p>"
   },
   {
    "h": "5️⃣ Invertible Matrices and Syllabus Note",
    "body": "<ul>\n<li><b>Invertible matrix:</b> a square matrix A is invertible if some B exists with AB = BA = I — that B is <b>A⁻¹</b> (the inverse). The inverse is UNIQUE.</li>\n<li><b>(AB)⁻¹ = B⁻¹A⁻¹ ⭐</b> — the same order-flip rule as transpose!</li>\n<li>The method to find an inverse (adjoint method) comes in <b>Chapter 4 (Determinants)</b> — you need determinants first.</li>\n<li><b>Rationalized syllabus ⭐:</b> <b>elementary row/column operations</b> (and finding inverses with them) are <b>DELETED</b> from NCERT — inverse now comes only through the adjoint method.</li>\n<li>Word problems: organizing data with matrices and multiplying (price × quantity type) — keeps appearing in boards.</li>\n</ul>\n<p class=\"small-note\">💡 Inverse = the \"undo\" matrix. Like ×3 is undone by ÷3 in numbers, A is undone by A⁻¹ in matrices.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics",
    "items": [
     "Matrix = rows × columns grid",
     "Order m×n: m rows, n columns",
     "aᵢⱼ = row i, column j"
    ]
   },
   {
    "h": "Types ⭐",
    "items": [
     "Square: m=n; Diagonal: sirf diagonal",
     "Identity I: diagonal 1, baaki 0",
     "Scalar: diagonal sab equal"
    ]
   },
   {
    "h": "Operations ⭐⭐",
    "items": [
     "Add: same order only",
     "AB: A.cols = B.rows, result m×p",
     "AB ≠ BA generally!"
    ]
   },
   {
    "h": "Transpose ⭐",
    "items": [
     "A′: rows ↔ columns",
     "(AB)′ = B′A′ (order flip!)",
     "Symmetric A′=A; skew A′=−A"
    ]
   },
   {
    "h": "Inverse ⭐",
    "items": [
     "AB = BA = I → B = A⁻¹",
     "(AB)⁻¹ = B⁻¹A⁻¹",
     "Elementary operations DELETED"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल",
    "items": [
     "आव्यूह = पंक्ति × स्तंभ ग्रिड",
     "कोटि m×n",
     "aᵢⱼ = पंक्ति i, स्तंभ j"
    ]
   },
   {
    "h": "प्रकार ⭐",
    "items": [
     "वर्ग: m=n; विकर्ण",
     "तत्समक I: विकर्ण 1",
     "अदिश: विकर्ण सभी समान"
    ]
   },
   {
    "h": "संक्रियाएं ⭐⭐",
    "items": [
     "योग: समान कोटि",
     "AB: A.स्तंभ = B.पंक्तियां",
     "AB ≠ BA सामान्यतः!"
    ]
   },
   {
    "h": "परिवर्त ⭐",
    "items": [
     "A′: पंक्ति ↔ स्तंभ",
     "(AB)′ = B′A′",
     "सममित A′=A; विषम A′=−A"
    ]
   },
   {
    "h": "व्युत्क्रम ⭐",
    "items": [
     "AB = BA = I → B = A⁻¹",
     "(AB)⁻¹ = B⁻¹A⁻¹",
     "प्रारंभिक संक्रियाएं हटाई गईं"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics",
    "items": [
     "Matrix = rows × columns grid",
     "Order m×n: m rows, n columns",
     "aᵢⱼ = row i, column j"
    ]
   },
   {
    "h": "Types ⭐",
    "items": [
     "Square: m=n; Diagonal: only diagonal",
     "Identity I: 1s on diagonal",
     "Scalar: diagonal entries equal"
    ]
   },
   {
    "h": "Operations ⭐⭐",
    "items": [
     "Add: same order only",
     "AB: A.cols = B.rows, result m×p",
     "AB ≠ BA in general!"
    ]
   },
   {
    "h": "Transpose ⭐",
    "items": [
     "A′: rows ↔ columns",
     "(AB)′ = B′A′ (order flips!)",
     "Symmetric A′=A; skew A′=−A"
    ]
   },
   {
    "h": "Inverse ⭐",
    "items": [
     "AB = BA = I → B = A⁻¹",
     "(AB)⁻¹ = B⁻¹A⁻¹",
     "Elementary operations DELETED"
    ]
   }
  ]
 },
 "practice": [
  [
   "A = [2 −1; 3 4] hai. a₂₁ kitna hai?",
   "Row 2, column 1 → <b>3</b>."
  ],
  [
   "A 2×3 hai, B 3×4 hai. AB ka order?",
   "A ke columns (3) = B ki rows (3) → possible hai, result <b>2×4</b>."
  ],
  [
   "kya matrix multiplication commutative hai?",
   "<b>Nahi</b> — generally AB ≠ BA. Kabhi-kabhi barabar ho jaaye (jaise I ke saath), par rule nahi hai."
  ],
  [
   "A = [1 2; 3 4], B = [0 1; 1 0]. (AB)′ kya hoga?",
   "AB = [2 1; 4 3] → (AB)′ = <b>[2 4; 1 3]</b>. Check: B′A′ bhi wahi aata hai — order flip rule!"
  ],
  [
   "Skew-symmetric matrix ke diagonal elements kya hote hain?",
   "<b>0</b> — kyunki aᵢᵢ = −aᵢᵢ ⇒ 2aᵢᵢ = 0."
  ],
  [
   "A′ = A ho to matrix kaisi hai?",
   "<b>Symmetric</b> — diagonal ke across mirror image."
  ],
  [
   "Har square matrix ko symmetric + skew-symmetric me kaise todo?",
   "A = <b>½(A + A′) + ½(A − A′)</b> — pehla symmetric, doosra skew-symmetric."
  ],
  [
   "A = [2 0; 0 2] kaunsi matrix hai?",
   "<b>Scalar matrix</b> — diagonal hai aur diagonal elements equal (2, 2)."
  ],
  [
   "AB = O ho to kya A = O ya B = O zaroor hai?",
   "<b>Nahi</b> — non-zero matrices ka product bhi zero matrix aa sakta hai. Numbers jaisa rule yahan nahi chalta!"
  ],
  [
   "(AB)⁻¹ kiske barabar hota hai?",
   "<b>B⁻¹A⁻¹</b> — inverse me bhi order flip hota hai, transpose ki tarah."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-4/",
  "title": "Determinants"
 }
}

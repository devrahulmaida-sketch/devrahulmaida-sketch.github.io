# Class 12 Maths, Chapter 4 - Determinants
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 4,
 "title_en": "Determinants",
 "title_hi": "सारणिक",
 "tagline": "det nikalna, adjoint, inverse aur equations ka matrix method",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 4: Determinants — long + short notes in Hindi, English, Hinglish. Determinant expansion, minors, cofactors, adjoint, inverse, solving linear equations.",
 "video": None,
 "card_tag": "det nikalna, adjoint, inverse aur equations ka matrix method",
 "card_topics": [
  "🔢 2×2 & 3×3 expansion",
  "🧮 Minors, cofactors, adjoint",
  "↩️ A⁻¹ = adjA/|A|",
  "📐 Solving AX = B"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Determinant Kya Hai — Matrix Ka Number",
    "body": "<ul>\n<li><b>Determinant:</b> har SQUARE matrix se juda ek number — det(A) ya |A|. Ye batata hai matrix invertible hai ya nahi, aur equations solve karne me kaam aata hai.</li>\n<li><b>2×2 ka formula ⭐:</b> |a b; c d| = <b>ad − bc</b> — main diagonal ka product MINUS other diagonal ka product.</li>\n<li>Example: |2 3; 1 4| = 2·4 − 3·1 = <b>5</b>.</li>\n<li>Sirf SQUARE matrix ka determinant hota hai — 2×3 matrix ka det nahi hota!</li>\n<li>|A| ek NUMBER hai (positive, negative ya zero) — matrix nahi. |kA| = kⁿ|A| for n×n matrix (har row se k nikalta hai!).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: determinant = matrix ka \"strength meter\". Zero aaya to matrix \"weak\" (singular) — inverse nahi banega.</p>"
   },
   {
    "h": "2️⃣ 3×3 Determinant — Expansion Method ⭐⭐",
    "body": "<ul>\n<li><b>Expansion along first row:</b> |A| = a₁₁·C₁₁ + a₁₂·C₁₂ + a₁₃·C₁₃ — element × uska cofactor, phir add.</li>\n<li><b>Sign pattern ⭐:</b> + − + / − + − / + − + (chessboard jaisa!). Position (i,j) ka sign = (−1)^(i+j).</li>\n<li><b>Minor Mᵢⱼ:</b> i-th row aur j-th column hata ke bache determinant ka value. <b>Cofactor Cᵢⱼ = (−1)^(i+j)·Mᵢⱼ</b>.</li>\n<li><b>KISI bhi row ya column se expand kar sakte ho</b> — answer same aata hai! Smart move: jis row/column me SABSE ZYADA ZERO ho, wahi choose karo — calculation aasaan.</li>\n<li>Example: |1 2 3; 0 4 5; 0 0 6| = 1·(4·6 − 5·0) = <b>24</b> (first column se expand kiya, do zeros mile free!).</li>\n</ul>\n<p class=\"small-note\">🎯 Triangular matrix (diagonal ke ek taraf sab 0) ka determinant = diagonal elements ka product! Shortcut yaad rakho.</p>"
   },
   {
    "h": "3️⃣ Adjoint — Inverse Ka Pehla Step ⭐",
    "body": "<ul>\n<li><b>Adjoint (adj A):</b> cofactor matrix ka TRANSPOSE. Pehle har element ki jagah uska cofactor likho, phir rows ↔ columns kar do.</li>\n<li><b>2×2 shortcut ⭐:</b> A = [a b; c d] → adj A = [d −b; −c a] — diagonal swap, off-diagonal ke signs flip!</li>\n<li><b>Golden identity ⭐⭐:</b> A·(adj A) = (adj A)·A = <b>|A|·I</b> — yahi se inverse ka formula banta hai.</li>\n<li>3×3 me 9 cofactors nikalne padte hain — dheere aur carefully, sign pattern double-check karo (yahi galti hoti hai!).</li>\n</ul>\n<p class=\"small-note\">💡 adj = \"cofactor transpose\". Yaad rakho: C likhte ho rows me, par adj me wo columns ban jaate hain.</p>"
   },
   {
    "h": "4️⃣ Inverse Nikalna — A⁻¹ = adj A / |A| ⭐⭐",
    "body": "<ul>\n<li><b>Formula ⭐⭐:</b> <b>A⁻¹ = (1/|A|)·adj A</b> — golden identity ko |A| se divide karke milta hai.</li>\n<li><b>Condition:</b> inverse TABHI exists jab <b>|A| ≠ 0</b>. |A| = 0 → matrix <b>singular</b>, koi inverse nahi!</li>\n<li><b>Non-singular matrix:</b> |A| ≠ 0 — invertible. Dono words same cheez ke hain.</li>\n<li><b>Useful results ⭐:</b> |A⁻¹| = 1/|A|; |adj A| = |A|^(n−1) (n order); (A⁻¹)⁻¹ = A; |AB| = |A|·|B|.</li>\n<li>Steps: (1) |A| nikalo — zero to stop! (2) cofactors → adj (3) divide by |A|.</li>\n</ul>\n<p class=\"small-note\">🎯 Pehle |A| check karo — zero hai to aage ki mehnat bekar! Exam me pehla step hamesha ye.</p>"
   },
   {
    "h": "5️⃣ Linear Equations Solve Karna — Matrix Method ⭐⭐",
    "body": "<ul>\n<li><b>Setup:</b> equations system ko AX = B form me likho — A = coefficients matrix, X = variables column, B = constants column.</li>\n<li><b>Solution ⭐:</b> X = A⁻¹B — bas inverse nikaal ke B se multiply karo!</li>\n<li><b>Teen cases ⭐⭐:</b> (1) |A| ≠ 0 → <b>unique solution</b> (X = A⁻¹B). (2) |A| = 0 aur (adj A)B ≠ O → <b>NO solution</b> (inconsistent). (3) |A| = 0 aur (adj A)B = O → <b>infinitely many</b> ya no solution (further check).</li>\n<li><b>Homogeneous system</b> (B = O): |A| ≠ 0 → sirf trivial solution (x = y = z = 0). |A| = 0 → infinitely many (non-trivial) solutions.</li>\n<li><b>Syllabus note ⭐:</b> determinants ki <b>properties</b> (row operations se simplify karna) rationalized NCERT se <b>DELETE</b> ho gayi — direct expansion + adjoint/inverse + equations pe focus karo.</li>\n</ul>\n<p class=\"small-note\">💡 Consistency check ka flow: |A| dekho → non-zero to done; zero to (adj A)B dekho. Ye 5-marker ka fixed pattern hai!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ सारणिक क्या है — आव्यूह की संख्या",
    "body": "<ul>\n<li><b>सारणिक (determinant):</b> प्रत्येक <b>वर्ग</b> आव्यूह से जुड़ी एक संख्या — det(A) या |A|।</li>\n<li><b>2×2 सूत्र ⭐:</b> |a b; c d| = <b>ad − bc</b> — मुख्य विकर्ण का गुणनफल ऋण अन्य विकर्ण का।</li>\n<li>उदाहरण: |2 3; 1 4| = 2·4 − 3·1 = <b>5</b>।</li>\n<li>केवल वर्ग आव्यूह का सारणिक होता है!</li>\n<li>|A| एक संख्या है। n×n आव्यूह के लिए <b>|kA| = kⁿ|A|</b>।</li>\n</ul>\n<p class=\"small-note\">💡 सारणिक = आव्यूह का \"सामर्थ्य मापक\"। शून्य आया तो आव्यूह अव्युत्क्रमणीय (singular)।</p>"
   },
   {
    "h": "2️⃣ 3×3 सारणिक — प्रसार विधि ⭐⭐",
    "body": "<ul>\n<li><b>प्रथम पंक्ति से प्रसार:</b> |A| = a₁₁·C₁₁ + a₁₂·C₁₂ + a₁₃·C₁₃ — अवयव × सहखंड, फिर योग।</li>\n<li><b>चिह्न पैटर्न ⭐:</b> + − + / − + − / + − +। स्थिति (i,j) का चिह्न = (−1)^(i+j)।</li>\n<li><b>उपसारणिक Mᵢⱼ:</b> i-वीं पंक्ति और j-वां स्तंभ हटाकर शेष सारणिक। <b>सहखंड Cᵢⱼ = (−1)^(i+j)·Mᵢⱼ</b>।</li>\n<li><b>किसी भी पंक्ति/स्तंभ से प्रसार कर सकते हैं</b> — उत्तर समान! जहां सबसे अधिक शून्य, वही चुनो।</li>\n<li>उदाहरण: |1 2 3; 0 4 5; 0 0 6| = 1·(4·6 − 5·0) = <b>24</b>।</li>\n</ul>\n<p class=\"small-note\">🎯 त्रिभुजीय आव्यूह का सारणिक = विकर्ण अवयवों का गुणनफल!</p>"
   },
   {
    "h": "3️⃣ सहखंडज — व्युत्क्रम का पहला चरण ⭐",
    "body": "<ul>\n<li><b>सहखंडज (adj A):</b> सहखंड आव्यूह का <b>परिवर्त</b>। पहले प्रत्येक अवयव का सहखंड लिखो, फिर पंक्तियां ↔ स्तंभ।</li>\n<li><b>2×2 शॉर्टकट ⭐:</b> A = [a b; c d] → adj A = [d −b; −c a] — विकर्ण अदला-बदली, अविकर्ण चिह्न उलट!</li>\n<li><b>स्वर्ण सर्वसमिका ⭐⭐:</b> A·(adj A) = (adj A)·A = <b>|A|·I</b>।</li>\n<li>3×3 में 9 सहखंड निकालने पड़ते हैं — चिह्न पैटर्न दोबारा जांचो!</li>\n</ul>\n<p class=\"small-note\">💡 adj = \"सहखंड परिवर्त\"।</p>"
   },
   {
    "h": "4️⃣ व्युत्क्रम निकालना — A⁻¹ = adj A / |A| ⭐⭐",
    "body": "<ul>\n<li><b>सूत्र ⭐⭐:</b> <b>A⁻¹ = (1/|A|)·adj A</b>।</li>\n<li><b>शर्त:</b> व्युत्क्रम <b>तभी</b> है जब <b>|A| ≠ 0</b>। |A| = 0 → आव्यूह <b>अव्युत्क्रमणीय (singular)</b>!</li>\n<li><b>उपयोगी परिणाम ⭐:</b> |A⁻¹| = 1/|A|; |adj A| = |A|^(n−1); (A⁻¹)⁻¹ = A; |AB| = |A|·|B|।</li>\n<li>चरण: (1) |A| निकालो — शून्य तो रुक जाओ! (2) सहखंड → adj (3) |A| से भाग।</li>\n</ul>\n<p class=\"small-note\">🎯 पहले |A| जांचो — शून्य है तो आगे की मेहनत व्यर्थ!</p>"
   },
   {
    "h": "5️⃣ रैखिक समीकरण हल करना — आव्यूह विधि ⭐⭐",
    "body": "<ul>\n<li><b>व्यवस्था:</b> समीकरणों को AX = B रूप में लिखो।</li>\n<li><b>हल ⭐:</b> X = A⁻¹B।</li>\n<li><b>तीन स्थितियां ⭐⭐:</b> (1) |A| ≠ 0 → <b>अद्वितीय हल</b>। (2) |A| = 0 और (adj A)B ≠ O → <b>कोई हल नहीं</b>। (3) |A| = 0 और (adj A)B = O → <b>अनंत हल</b> संभव (आगे जांच)।</li>\n<li><b>समघातीय निकाय</b> (B = O): |A| ≠ 0 → केवल तुच्छ हल। |A| = 0 → अनंत हल।</li>\n<li><b>पाठ्यक्रम टिप्पणी ⭐:</b> सारणिकों के <b>गुणधर्म</b> NCERT से <b>हटाए गए</b> — प्रसार + सहखंडज + समीकरणों पर ध्यान दो।</li>\n</ul>\n<p class=\"small-note\">💡 प्रवाह: |A| देखो → अशून्य तो हल; शून्य तो (adj A)B देखो।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ What Is a Determinant — A Matrix's Number",
    "body": "<ul>\n<li><b>Determinant:</b> a number attached to every SQUARE matrix — det(A) or |A|. It tells you whether the matrix is invertible and helps solve equations.</li>\n<li><b>2×2 formula ⭐:</b> |a b; c d| = <b>ad − bc</b> — main diagonal product MINUS the other diagonal product.</li>\n<li>Example: |2 3; 1 4| = 2·4 − 3·1 = <b>5</b>.</li>\n<li>Only SQUARE matrices have determinants — a 2×3 matrix has none!</li>\n<li>|A| is a NUMBER (positive, negative or zero) — not a matrix. |kA| = kⁿ|A| for an n×n matrix (k pulls out of every row!).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: the determinant is a matrix's \"strength meter\". Zero means the matrix is \"weak\" (singular) — no inverse will exist.</p>"
   },
   {
    "h": "2️⃣ 3×3 Determinants — Expansion Method ⭐⭐",
    "body": "<ul>\n<li><b>Expansion along the first row:</b> |A| = a₁₁·C₁₁ + a₁₂·C₁₂ + a₁₃·C₁₃ — element × its cofactor, then add.</li>\n<li><b>Sign pattern ⭐:</b> + − + / − + − / + − + (like a chessboard!). The sign at position (i,j) is (−1)^(i+j).</li>\n<li><b>Minor Mᵢⱼ:</b> the determinant left after deleting row i and column j. <b>Cofactor Cᵢⱼ = (−1)^(i+j)·Mᵢⱼ</b>.</li>\n<li><b>You can expand along ANY row or column</b> — same answer! Smart move: pick the one with the MOST ZEROS — easier calculation.</li>\n<li>Example: |1 2 3; 0 4 5; 0 0 6| = 1·(4·6 − 5·0) = <b>24</b> (expanded along the first column — two free zeros!).</li>\n</ul>\n<p class=\"small-note\">🎯 A triangular matrix (all zeros on one side of the diagonal) has determinant = product of diagonal entries! Remember the shortcut.</p>"
   },
   {
    "h": "3️⃣ Adjoint — The First Step to Inverse ⭐",
    "body": "<ul>\n<li><b>Adjoint (adj A):</b> the TRANSPOSE of the cofactor matrix. First replace every element with its cofactor, then swap rows ↔ columns.</li>\n<li><b>2×2 shortcut ⭐:</b> A = [a b; c d] → adj A = [d −b; −c a] — swap the diagonal, flip the off-diagonal signs!</li>\n<li><b>Golden identity ⭐⭐:</b> A·(adj A) = (adj A)·A = <b>|A|·I</b> — the inverse formula comes straight from this.</li>\n<li>For 3×3 you must compute 9 cofactors — go slow and double-check the sign pattern (that is where mistakes happen!).</li>\n</ul>\n<p class=\"small-note\">💡 adj = \"cofactor transpose\". You write cofactors in rows, but in adj they become columns.</p>"
   },
   {
    "h": "4️⃣ Finding the Inverse — A⁻¹ = adj A / |A| ⭐⭐",
    "body": "<ul>\n<li><b>Formula ⭐⭐:</b> <b>A⁻¹ = (1/|A|)·adj A</b> — divide the golden identity by |A|.</li>\n<li><b>Condition:</b> the inverse exists ONLY when <b>|A| ≠ 0</b>. |A| = 0 → the matrix is <b>singular</b>, no inverse!</li>\n<li><b>Non-singular matrix:</b> |A| ≠ 0 — invertible. Both words mean the same thing.</li>\n<li><b>Useful results ⭐:</b> |A⁻¹| = 1/|A|; |adj A| = |A|^(n−1) (for order n); (A⁻¹)⁻¹ = A; |AB| = |A|·|B|.</li>\n<li>Steps: (1) find |A| — if zero, stop! (2) cofactors → adj (3) divide by |A|.</li>\n</ul>\n<p class=\"small-note\">🎯 Check |A| first — if it is zero, all further effort is wasted! Always the first step in exams.</p>"
   },
   {
    "h": "5️⃣ Solving Linear Equations — The Matrix Method ⭐⭐",
    "body": "<ul>\n<li><b>Setup:</b> write the system as AX = B — A = coefficient matrix, X = variable column, B = constant column.</li>\n<li><b>Solution ⭐:</b> X = A⁻¹B — just find the inverse and multiply by B!</li>\n<li><b>Three cases ⭐⭐:</b> (1) |A| ≠ 0 → <b>unique solution</b> (X = A⁻¹B). (2) |A| = 0 and (adj A)B ≠ O → <b>NO solution</b> (inconsistent). (3) |A| = 0 and (adj A)B = O → <b>infinitely many</b> or none (needs further checking).</li>\n<li><b>Homogeneous system</b> (B = O): |A| ≠ 0 → only the trivial solution (x = y = z = 0). |A| = 0 → infinitely many (non-trivial) solutions.</li>\n<li><b>Syllabus note ⭐:</b> the <b>properties of determinants</b> (simplifying via row operations) are <b>DELETED</b> from rationalized NCERT — focus on direct expansion + adjoint/inverse + equations.</li>\n</ul>\n<p class=\"small-note\">💡 Consistency-check flow: look at |A| → non-zero means done; zero means check (adj A)B. This is the fixed 5-marker pattern!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics ⭐",
    "items": [
     "det sirf square matrix ka",
     "2×2: ad − bc",
     "|kA| = kⁿ|A|"
    ]
   },
   {
    "h": "3×3 ⭐⭐",
    "items": [
     "Expand: element × cofactor",
     "Signs: +−+/−+−/+-+",
     "Zeros wali row/column choose karo"
    ]
   },
   {
    "h": "Adjoint ⭐",
    "items": [
     "adj A = cofactor matrix ka transpose",
     "2×2: [d −b; −c a]",
     "A·adjA = |A|·I"
    ]
   },
   {
    "h": "Inverse ⭐⭐",
    "items": [
     "A⁻¹ = adjA/|A|, |A|≠0 chahiye",
     "|A|=0 → singular, no inverse",
     "|adjA| = |A|ⁿ⁻¹"
    ]
   },
   {
    "h": "Equations ⭐⭐",
    "items": [
     "AX=B → X=A⁻¹B",
     "|A|≠0: unique; =0: check (adjA)B",
     "Properties of det DELETED"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल ⭐",
    "items": [
     "सारणिक केवल वर्ग आव्यूह का",
     "2×2: ad − bc",
     "|kA| = kⁿ|A|"
    ]
   },
   {
    "h": "3×3 ⭐⭐",
    "items": [
     "प्रसार: अवयव × सहखंड",
     "चिह्न: +−+/−+−/+-+",
     "शून्य वाली पंक्ति/स्तंभ चुनो"
    ]
   },
   {
    "h": "सहखंडज ⭐",
    "items": [
     "adj A = सहखंड आव्यूह का परिवर्त",
     "2×2: [d −b; −c a]",
     "A·adjA = |A|·I"
    ]
   },
   {
    "h": "व्युत्क्रम ⭐⭐",
    "items": [
     "A⁻¹ = adjA/|A|, |A|≠0",
     "|A|=0 → अव्युत्क्रमणीय",
     "|adjA| = |A|ⁿ⁻¹"
    ]
   },
   {
    "h": "समीकरण ⭐⭐",
    "items": [
     "AX=B → X=A⁻¹B",
     "|A|≠0: अद्वितीय; =0: (adjA)B जांचो",
     "सारणिक गुणधर्म हटाए गए"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics ⭐",
    "items": [
     "det only for square matrices",
     "2×2: ad − bc",
     "|kA| = kⁿ|A|"
    ]
   },
   {
    "h": "3×3 ⭐⭐",
    "items": [
     "Expand: element × cofactor",
     "Signs: +−+/−+−/+-+",
     "Pick the row/column with zeros"
    ]
   },
   {
    "h": "Adjoint ⭐",
    "items": [
     "adj A = transpose of cofactor matrix",
     "2×2: [d −b; −c a]",
     "A·adjA = |A|·I"
    ]
   },
   {
    "h": "Inverse ⭐⭐",
    "items": [
     "A⁻¹ = adjA/|A|, needs |A|≠0",
     "|A|=0 → singular, no inverse",
     "|adjA| = |A|ⁿ⁻¹"
    ]
   },
   {
    "h": "Equations ⭐⭐",
    "items": [
     "AX=B → X=A⁻¹B",
     "|A|≠0: unique; =0: check (adjA)B",
     "Properties of det DELETED"
    ]
   }
  ]
 },
 "practice": [
  [
   "|3 5; 2 4| ka value nikalo.",
   "ad − bc = 3·4 − 5·2 = 12 − 10 = <b>2</b>."
  ],
  [
   "A 3×3 matrix hai, |A| = 2. |2A| kitna hoga?",
   "|kA| = kⁿ|A| = 2³ × 2 = <b>16</b>."
  ],
  [
   "Position (2,3) ka cofactor sign kya hai?",
   "(−1)^(2+3) = (−1)⁵ = <b>−1</b> — negative sign."
  ],
  [
   "A = [1 2; 3 4] ka adjoint likho.",
   "Diagonal swap, off-diagonal sign flip: adj A = <b>[4 −2; −3 1]</b>."
  ],
  [
   "|A| = 0 ho to A ka inverse exist karta hai?",
   "<b>Nahi</b> — |A| = 0 ka matlab matrix singular hai, A⁻¹ exist nahi karta."
  ],
  [
   "A = [2 0; 0 3] ka inverse nikalo.",
   "|A| = 6, adj A = [3 0; 0 2] → A⁻¹ = <b>[1/2 0; 0 1/3]</b>."
  ],
  [
   "AX = B system me |A| ≠ 0 hai. Solution?",
   "X = <b>A⁻¹B</b> — unique solution guaranteed."
  ],
  [
   "|AB| aur |A||B| me kya relation hai?",
   "|AB| = <b>|A|·|B|</b> — product ka det = det ka product."
  ],
  [
   "|adj A| ka formula kya hai (order n)?",
   "<b>|A|^(n−1)</b> — 3×3 ke liye |adj A| = |A|²."
  ],
  [
   "Homogeneous system (B = O) me |A| = 0 ho to?",
   "<b>Infinitely many solutions</b> — non-trivial solutions exist karte hain (sirf x=y=z=0 nahi)."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-5/",
  "title": "Continuity and Differentiability"
 }
}

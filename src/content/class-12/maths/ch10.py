# Class 12 Maths, Chapter 10 - Vector Algebra
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 10,
 "title_en": "Vector Algebra",
 "title_hi": "सदिश बीजगणित",
 "tagline": "Arrows ka ganit — dot product, cross product aur unke tests",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 10: Vector Algebra — long + short notes in Hindi, English, Hinglish. Vectors, types, addition, section formula, dot product, cross product, applications.",
 "video": None,
 "card_tag": "Arrows ka ganit — dot product, cross product aur unke tests",
 "card_topics": [
  "➡️ Vector basics + types",
  "➕ Addition + section formula",
  "· Dot product (perpendicular test)",
  "✖️ Cross product (area + parallel test)"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Vector Kya Hai — Direction Wala Quantity ⭐",
    "body": "<ul>\n<li><b>Scalar vs Vector:</b> scalar = sirf MAGNITUDE (mass, speed, temperature). Vector = magnitude + DIRECTION dono (velocity, force, displacement).</li>\n<li><b>Notation:</b> a⃗ ya AB⃗ (A = tail/initial point, B = head/terminal). Magnitude: |a⃗| — hamesha non-negative number.</li>\n<li><b>Types ⭐:</b> <b>Zero vector</b> (0⃗, magnitude 0, direction undefined); <b>unit vector</b> (magnitude 1: â = a⃗/|a⃗|); <b>equal vectors</b> (same magnitude + same direction); <b>negative</b> −a⃗ (same magnitude, opposite direction); <b>collinear</b> (same/parallel line); <b>coplanar</b> (same plane me).</li>\n<li><b>Position vector:</b> origin se point tak ka vector — P(x, y, z) ka p.v. = <b>xî + yĵ + zk̂</b>.</li>\n<li><b>î, ĵ, k̂:</b> x, y, z axes ke unit vectors — 3D ka foundation trio!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: scalar batata hai \"kitna\", vector batata hai \"kitna + kidhar\". Arrow hi vector hai — lambai = magnitude, nok = direction.</p>"
   },
   {
    "h": "2️⃣ Addition, Components aur Section Formula ⭐",
    "body": "<ul>\n<li><b>Triangle law ⭐:</b> a⃗ + b⃗ = pehle vector ka head doosre ki tail se jodo → tail-to-head resultant. <b>Parallelogram law:</b> same tail se start → diagonal = a⃗ + b⃗.</li>\n<li><b>Component form me add ⭐:</b> (a₁î + a₂ĵ + a₃k̂) + (b₁î + b₂ĵ + b₃k̂) = (a₁+b₁)î + (a₂+b₂)ĵ + (a₃+b₃)k̂ — components alag-alag add!</li>\n<li><b>Scalar multiplication:</b> λa⃗ = magnitude |λ| guna; direction same (λ &gt; 0) ya opposite (λ &lt; 0). Components sab λ se multiply.</li>\n<li><b>Magnitude ⭐:</b> |a⃗| = <b>√(a₁² + a₂² + a₃²)</b>. Unit vector: â = a⃗/|a⃗|.</li>\n<li><b>AB⃗ = B ke p.v. − A ke p.v. ⭐</b> (head − tail). Section formula: P, AB ko m:n me divide kare → p⃗ = <b>(mb⃗ + na⃗)/(m + n)</b> (internal).</li>\n</ul>\n<p class=\"small-note\">🎯 Section formula yaad rakho: \"cross-multiply and add\" — m wale ko b se, n wale ko a se (ulti taraf ke weight!).</p>"
   },
   {
    "h": "3️⃣ Dot Product — Scalar Wala Product ⭐⭐",
    "body": "<ul>\n<li><b>Definition ⭐⭐:</b> a⃗·b⃗ = <b>|a⃗||b⃗|cos θ</b> — answer ek SCALAR (number) aata hai, vector nahi!</li>\n<li><b>Component form ⭐⭐:</b> a⃗·b⃗ = <b>a₁b₁ + a₂b₂ + a₃b₃</b> — corresponding components multiply karke add. Super easy!</li>\n<li><b>Perpendicular test ⭐⭐:</b> a⃗·b⃗ = 0 ⟺ vectors <b>PERPENDICULAR</b> (non-zero vectors ke liye). Sabse zyada use hone wala test!</li>\n<li><b>Angle nikalna ⭐:</b> cos θ = (a⃗·b⃗)/(|a⃗||b⃗|) — dot product aur magnitudes se angle!</li>\n<li>Properties: a⃗·b⃗ = b⃗·a⃗ (commutative ✓); a⃗·a⃗ = |a⃗|²; î·î = 1, î·ĵ = 0 (axes perpendicular!).</li>\n<li><b>Projection:</b> a⃗ ka b⃗ pe projection = (a⃗·b⃗)/|b⃗| — shadow ki length.</li>\n</ul>\n<p class=\"small-note\">💡 Dot product = \"kitna saath chal rahe hain\". Same direction → max positive; perpendicular → 0; opposite → max negative.</p>"
   },
   {
    "h": "4️⃣ Cross Product — Vector Wala Product ⭐⭐",
    "body": "<ul>\n<li><b>Definition ⭐⭐:</b> a⃗×b⃗ = <b>|a⃗||b⃗|sin θ · n̂</b> — answer ek VECTOR jo dono ke PERPENDICULAR hota hai (right-hand rule se direction!).</li>\n<li><b>Determinant form ⭐⭐:</b> a⃗×b⃗ = |î ĵ k̂; a₁ a₂ a₃; b₁ b₂ b₃| — pehli row me î ĵ k̂, phir a⃗, phir b⃗ ke components. Determinant expand karo!</li>\n<li><b>ANTI-commutative ⭐⭐:</b> a⃗×b⃗ = <b>−(b⃗×a⃗)</b> — order ulta kiya to sign ulta! (Dot product me aisa nahi tha!)</li>\n<li><b>Parallel test ⭐:</b> a⃗×b⃗ = 0⃗ ⟺ vectors <b>PARALLEL/collinear</b> (ya components proportional: a₁/b₁ = a₂/b₂ = a₃/b₃).</li>\n<li><b>Area ⭐⭐:</b> |a⃗×b⃗| = <b>parallelogram ka area</b> (sides a⃗, b⃗). Triangle ka area = <b>½|a⃗×b⃗|</b>.</li>\n<li>î×ĵ = k̂, ĵ×k̂ = î, k̂×î = ĵ (cyclic!); par ĵ×î = −k̂ (ulta = minus).</li>\n</ul>\n<p class=\"small-note\">💡 Cross product = \"perpendicular nikalo + area do\". Right hand: fingers a⃗ se b⃗ curl karo, thumb = a⃗×b⃗ ki direction.</p>"
   },
   {
    "h": "5️⃣ Applications aur Syllabus Note",
    "body": "<ul>\n<li><b>Collinearity of 3 points ⭐:</b> AB⃗ aur AC⃗ parallel (ya AB⃗ = λAC⃗) → A, B, C collinear.</li>\n<li><b>Work done (physics link):</b> W = F⃗·d⃗ — dot product. Torque: τ⃗ = r⃗×F⃗ — cross product.</li>\n<li><b>Perpendicular vector banana ⭐:</b> do vectors ke common perpendicular chahiye? a⃗×b⃗ hi wo vector hai — normalize karke unit: ±(a⃗×b⃗)/|a⃗×b⃗|.</li>\n<li><b>Syllabus note ⭐:</b> <b>scalar triple product</b> (a⃗·(b⃗×c⃗)) rationalized NCERT se <b>DELETE</b> ho chuka hai — sirf dot aur cross products pe focus.</li>\n<li>Chapter 11 (3D Geometry) me vectors hi use hote hain — lines ki equations, angles sab inhi operations se bante hain.</li>\n</ul>\n<p class=\"small-note\">🎯 Dot = perpendicular test + angle + work. Cross = parallel test + area + perpendicular vector. Ye mapping clear hai to chapter sorted!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ सदिश क्या है — दिशा वाली राशि ⭐",
    "body": "<ul>\n<li><b>अदिश बनाम सदिश:</b> अदिश = केवल <b>परिमाण</b> (द्रव्यमान, चाल)। सदिश = परिमाण + <b>दिशा</b> दोनों (वेग, बल, विस्थापन)।</li>\n<li><b>संकेत:</b> a⃗ या AB⃗ (A = पूंछ, B = शीर्ष)। परिमाण: |a⃗| — सदैव अऋणात्मक।</li>\n<li><b>प्रकार ⭐:</b> <b>शून्य सदिश</b> (परिमाण 0); <b>मात्रक सदिश</b> (परिमाण 1: â = a⃗/|a⃗|); <b>समान सदिश</b> (समान परिमाण + दिशा); <b>ऋणात्मक</b> −a⃗; <b>संरेख</b> (समांतर); <b>समतलीय</b>।</li>\n<li><b>स्थिति सदिश:</b> मूल बिंदु से बिंदु तक — P(x, y, z) का = <b>xî + yĵ + zk̂</b>।</li>\n<li><b>î, ĵ, k̂:</b> x, y, z अक्षों के मात्रक सदिश।</li>\n</ul>\n<p class=\"small-note\">💡 अदिश बताता है \"कितना\", सदिश \"कितना + किधर\"। तीर ही सदिश है!</p>"
   },
   {
    "h": "2️⃣ योग, घटक और अनुभाग सूत्र ⭐",
    "body": "<ul>\n<li><b>त्रिभुज नियम ⭐:</b> a⃗ + b⃗ = पहले का शीर्ष दूसरे की पूंछ से → पूंछ-से-शीर्ष परिणामी। <b>समांतर चतुर्भुज नियम:</b> विकर्ण = योग।</li>\n<li><b>घटक रूप में योग ⭐:</b> संगत घटक अलग-अलग जोड़ो: (a₁+b₁)î + (a₂+b₂)ĵ + (a₃+b₃)k̂।</li>\n<li><b>अदिश गुणन:</b> λa⃗ = परिमाण |λ| गुना; दिशा समान (λ &gt; 0) या विपरीत (λ &lt; 0)।</li>\n<li><b>परिमाण ⭐:</b> |a⃗| = <b>√(a₁² + a₂² + a₃²)</b>। मात्रक: â = a⃗/|a⃗|।</li>\n<li><b>AB⃗ = B का स्थिति सदिश − A का ⭐</b>। अनुभाग सूत्र: p⃗ = <b>(mb⃗ + na⃗)/(m + n)</b> (आंतरिक)।</li>\n</ul>\n<p class=\"small-note\">🎯 अनुभाग सूत्र: \"उल्टी ओर के भार\" — m वाले को b से!</p>"
   },
   {
    "h": "3️⃣ अदिश गुणनफल — डॉट प्रोडक्ट ⭐⭐",
    "body": "<ul>\n<li><b>परिभाषा ⭐⭐:</b> a⃗·b⃗ = <b>|a⃗||b⃗|cos θ</b> — उत्तर एक <b>अदिश</b> (संख्या)!</li>\n<li><b>घटक रूप ⭐⭐:</b> a⃗·b⃗ = <b>a₁b₁ + a₂b₂ + a₃b₃</b>।</li>\n<li><b>लंबवत परीक्षण ⭐⭐:</b> a⃗·b⃗ = 0 ⟺ सदिश <b>लंबवत</b> (अशून्य सदिशों के लिए)।</li>\n<li><b>कोण ⭐:</b> cos θ = (a⃗·b⃗)/(|a⃗||b⃗|)।</li>\n<li>गुण: a⃗·b⃗ = b⃗·a⃗ (क्रमविनिमेय); a⃗·a⃗ = |a⃗|²; î·ĵ = 0।</li>\n<li><b>प्रक्षेप:</b> a⃗ का b⃗ पर = (a⃗·b⃗)/|b⃗|।</li>\n</ul>\n<p class=\"small-note\">💡 डॉट = \"कितना साथ चल रहे हैं\"। लंबवत → 0!</p>"
   },
   {
    "h": "4️⃣ सदिश गुणनफल — क्रॉस प्रोडक्ट ⭐⭐",
    "body": "<ul>\n<li><b>परिभाषा ⭐⭐:</b> a⃗×b⃗ = <b>|a⃗||b⃗|sin θ · n̂</b> — उत्तर एक <b>सदिश</b>, दोनों के लंबवत (दाएं-हाथ का नियम!)।</li>\n<li><b>सारणिक रूप ⭐⭐:</b> a⃗×b⃗ = |î ĵ k̂; a₁ a₂ a₃; b₁ b₂ b₃| — सारणिक प्रसार करो!</li>\n<li><b>प्रति-क्रमविनिमेय ⭐⭐:</b> a⃗×b⃗ = <b>−(b⃗×a⃗)</b> — क्रम उलटा तो चिह्न उलटा!</li>\n<li><b>समांतर परीक्षण ⭐:</b> a⃗×b⃗ = 0⃗ ⟺ सदिश <b>समांतर</b> (या घटक समानुपाती)।</li>\n<li><b>क्षेत्रफल ⭐⭐:</b> |a⃗×b⃗| = <b>समांतर चतुर्भुज का क्षेत्रफल</b>; त्रिभुज = <b>½|a⃗×b⃗|</b>।</li>\n<li>î×ĵ = k̂, ĵ×k̂ = î, k̂×î = ĵ (चक्रीय!); उल्टा = ऋण।</li>\n</ul>\n<p class=\"small-note\">💡 क्रॉस = \"लंबवत निकालो + क्षेत्रफल दो\"।</p>"
   },
   {
    "h": "5️⃣ अनुप्रयोग और पाठ्यक्रम टिप्पणी",
    "body": "<ul>\n<li><b>3 बिंदुओं की संरेखता ⭐:</b> AB⃗ = λAC⃗ → A, B, C संरेख।</li>\n<li><b>भौतिकी लिंक:</b> कार्य W = F⃗·d⃗ (डॉट); बलाघूर्ण τ⃗ = r⃗×F⃗ (क्रॉस)।</li>\n<li><b>लंबवत सदिश बनाना ⭐:</b> दोनों के उभयनिष्ठ लंबवत = a⃗×b⃗; मात्रक: ±(a⃗×b⃗)/|a⃗×b⃗|।</li>\n<li><b>पाठ्यक्रम टिप्पणी ⭐:</b> <b>अदिश त्रिगुणनफल</b> (a⃗·(b⃗×c⃗)) NCERT से <b>हटाया गया</b> — केवल डॉट और क्रॉस पर ध्यान दो।</li>\n<li>अध्याय 11 (त्रिविम ज्यामिति) में यही संक्रियाएं चलती हैं।</li>\n</ul>\n<p class=\"small-note\">🎯 डॉट = लंबवत परीक्षण + कोण। क्रॉस = समांतर परीक्षण + क्षेत्रफल। यह मैपिंग स्पष्ट तो अध्याय सॉर्टेड!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ What Is a Vector — A Quantity with Direction ⭐",
    "body": "<ul>\n<li><b>Scalar vs Vector:</b> a scalar has only MAGNITUDE (mass, speed, temperature). A vector has magnitude AND DIRECTION both (velocity, force, displacement).</li>\n<li><b>Notation:</b> a⃗ or AB⃗ (A = tail/initial point, B = head/terminal). Magnitude: |a⃗| — always a non-negative number.</li>\n<li><b>Types ⭐:</b> <b>zero vector</b> (0⃗, magnitude 0, direction undefined); <b>unit vector</b> (magnitude 1: â = a⃗/|a⃗|); <b>equal vectors</b> (same magnitude + same direction); <b>negative</b> −a⃗ (same magnitude, opposite direction); <b>collinear</b> (on the same/parallel line); <b>coplanar</b> (in one plane).</li>\n<li><b>Position vector:</b> the vector from the origin to a point — P(x, y, z) has p.v. <b>xî + yĵ + zk̂</b>.</li>\n<li><b>î, ĵ, k̂:</b> the unit vectors along the x, y, z axes — the foundation trio of 3D!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: a scalar says \"how much\", a vector says \"how much + which way\". An arrow IS a vector — length = magnitude, tip = direction.</p>"
   },
   {
    "h": "2️⃣ Addition, Components and the Section Formula ⭐",
    "body": "<ul>\n<li><b>Triangle law ⭐:</b> a⃗ + b⃗ = join the head of the first vector to the tail of the second → the tail-to-head resultant. <b>Parallelogram law:</b> starting from the same tail → the diagonal = a⃗ + b⃗.</li>\n<li><b>Adding in components ⭐:</b> (a₁î + a₂ĵ + a₃k̂) + (b₁î + b₂ĵ + b₃k̂) = (a₁+b₁)î + (a₂+b₂)ĵ + (a₃+b₃)k̂ — add components separately!</li>\n<li><b>Scalar multiplication:</b> λa⃗ = magnitude × |λ|; direction same (λ &gt; 0) or opposite (λ &lt; 0). Every component gets multiplied.</li>\n<li><b>Magnitude ⭐:</b> |a⃗| = <b>√(a₁² + a₂² + a₃²)</b>. Unit vector: â = a⃗/|a⃗|.</li>\n<li><b>AB⃗ = p.v. of B − p.v. of A ⭐</b> (head − tail). Section formula: if P divides AB in m:n, p⃗ = <b>(mb⃗ + na⃗)/(m + n)</b> (internal).</li>\n</ul>\n<p class=\"small-note\">🎯 Section formula memory: \"cross the weights\" — the m-part pairs with b (the opposite end)!</p>"
   },
   {
    "h": "3️⃣ Dot Product — The Scalar Product ⭐⭐",
    "body": "<ul>\n<li><b>Definition ⭐⭐:</b> a⃗·b⃗ = <b>|a⃗||b⃗|cos θ</b> — the answer is a SCALAR (a number), not a vector!</li>\n<li><b>Component form ⭐⭐:</b> a⃗·b⃗ = <b>a₁b₁ + a₂b₂ + a₃b₃</b> — multiply corresponding components and add. Super easy!</li>\n<li><b>Perpendicularity test ⭐⭐:</b> a⃗·b⃗ = 0 ⟺ the vectors are <b>PERPENDICULAR</b> (for non-zero vectors). The most-used test in the chapter!</li>\n<li><b>Finding the angle ⭐:</b> cos θ = (a⃗·b⃗)/(|a⃗||b⃗|) — angle from the dot product and the magnitudes!</li>\n<li>Properties: a⃗·b⃗ = b⃗·a⃗ (commutative ✓); a⃗·a⃗ = |a⃗|²; î·î = 1, î·ĵ = 0 (the axes are perpendicular!).</li>\n<li><b>Projection:</b> the projection of a⃗ on b⃗ = (a⃗·b⃗)/|b⃗| — the shadow's length.</li>\n</ul>\n<p class=\"small-note\">💡 Dot product = \"how much are they moving together\". Same direction → max positive; perpendicular → 0; opposite → max negative.</p>"
   },
   {
    "h": "4️⃣ Cross Product — The Vector Product ⭐⭐",
    "body": "<ul>\n<li><b>Definition ⭐⭐:</b> a⃗×b⃗ = <b>|a⃗||b⃗|sin θ · n̂</b> — the answer is a VECTOR PERPENDICULAR to both (direction by the right-hand rule!).</li>\n<li><b>Determinant form ⭐⭐:</b> a⃗×b⃗ = |î ĵ k̂; a₁ a₂ a₃; b₁ b₂ b₃| — first row î ĵ k̂, then the components of a⃗, then b⃗. Expand the determinant!</li>\n<li><b>ANTI-commutative ⭐⭐:</b> a⃗×b⃗ = <b>−(b⃗×a⃗)</b> — flip the order and the sign flips! (The dot product had no such rule!)</li>\n<li><b>Parallel test ⭐:</b> a⃗×b⃗ = 0⃗ ⟺ the vectors are <b>PARALLEL/collinear</b> (or components are proportional: a₁/b₁ = a₂/b₂ = a₃/b₃).</li>\n<li><b>Area ⭐⭐:</b> |a⃗×b⃗| = <b>area of the parallelogram</b> (with sides a⃗, b⃗). Triangle's area = <b>½|a⃗×b⃗|</b>.</li>\n<li>î×ĵ = k̂, ĵ×k̂ = î, k̂×î = ĵ (cyclic!); but ĵ×î = −k̂ (reversed = minus).</li>\n</ul>\n<p class=\"small-note\">💡 Cross product = \"find the perpendicular + get the area\". Right hand: curl fingers from a⃗ to b⃗; the thumb points along a⃗×b⃗.</p>"
   },
   {
    "h": "5️⃣ Applications and Syllabus Note",
    "body": "<ul>\n<li><b>Collinearity of 3 points ⭐:</b> AB⃗ and AC⃗ parallel (or AB⃗ = λAC⃗) → A, B, C are collinear.</li>\n<li><b>Physics link:</b> work done W = F⃗·d⃗ — the dot product. Torque: τ⃗ = r⃗×F⃗ — the cross product.</li>\n<li><b>Building a perpendicular vector ⭐:</b> need a common perpendicular to two vectors? a⃗×b⃗ is exactly that — normalize it for the unit vector: ±(a⃗×b⃗)/|a⃗×b⃗|.</li>\n<li><b>Syllabus note ⭐:</b> the <b>scalar triple product</b> (a⃗·(b⃗×c⃗)) is <b>DELETED</b> from rationalized NCERT — focus only on dot and cross products.</li>\n<li>Chapter 11 (3D Geometry) runs on vectors — line equations and angles all come from these operations.</li>\n</ul>\n<p class=\"small-note\">🎯 Dot = perpendicular test + angle + work. Cross = parallel test + area + perpendicular vector. Clear this mapping and the chapter is sorted!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics ⭐",
    "items": [
     "Vector = magnitude + direction",
     "â = a⃗/|a⃗| (unit vector)",
     "|a⃗| = √(a₁²+a₂²+a₃²)"
    ]
   },
   {
    "h": "Operations ⭐",
    "items": [
     "Add: components alag-alag",
     "AB⃗ = b⃗ − a⃗ (head − tail)",
     "Section: (mb⃗+na⃗)/(m+n)"
    ]
   },
   {
    "h": "Dot product ⭐⭐",
    "items": [
     "a⃗·b⃗ = |a||b|cosθ = a₁b₁+a₂b₂+a₃b₃",
     "Perpendicular ⟺ dot = 0",
     "cosθ = (a⃗·b⃗)/(|a||b|)"
    ]
   },
   {
    "h": "Cross product ⭐⭐",
    "items": [
     "|a×b| = |a||b|sinθ, direction ⊥",
     "Determinant form (î ĵ k̂ row)",
     "a⃗×b⃗ = −(b⃗×a⃗)!"
    ]
   },
   {
    "h": "Uses ⭐",
    "items": [
     "½|a⃗×b⃗| = triangle area",
     "Parallel ⟺ cross = 0⃗",
     "Scalar triple product DELETED"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल ⭐",
    "items": [
     "सदिश = परिमाण + दिशा",
     "â = a⃗/|a⃗|",
     "|a⃗| = √(a₁²+a₂²+a₃²)"
    ]
   },
   {
    "h": "संक्रियाएं ⭐",
    "items": [
     "योग: घटक अलग-अलग",
     "AB⃗ = b⃗ − a⃗",
     "अनुभाग: (mb⃗+na⃗)/(m+n)"
    ]
   },
   {
    "h": "डॉट ⭐⭐",
    "items": [
     "a⃗·b⃗ = |a||b|cosθ = a₁b₁+a₂b₂+a₃b₃",
     "लंबवत ⟺ डॉट = 0",
     "cosθ = (a⃗·b⃗)/(|a||b|)"
    ]
   },
   {
    "h": "क्रॉस ⭐⭐",
    "items": [
     "|a×b| = |a||b|sinθ, दिशा ⊥",
     "सारणिक रूप",
     "a⃗×b⃗ = −(b⃗×a⃗)!"
    ]
   },
   {
    "h": "उपयोग ⭐",
    "items": [
     "½|a⃗×b⃗| = त्रिभुज क्षेत्रफल",
     "समांतर ⟺ क्रॉस = 0⃗",
     "अदिश त्रिगुणनफल हटाया गया"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics ⭐",
    "items": [
     "Vector = magnitude + direction",
     "â = a⃗/|a⃗| (unit vector)",
     "|a⃗| = √(a₁²+a₂²+a₃²)"
    ]
   },
   {
    "h": "Operations ⭐",
    "items": [
     "Add: components separately",
     "AB⃗ = b⃗ − a⃗ (head − tail)",
     "Section: (mb⃗+na⃗)/(m+n)"
    ]
   },
   {
    "h": "Dot product ⭐⭐",
    "items": [
     "a⃗·b⃗ = |a||b|cosθ = a₁b₁+a₂b₂+a₃b₃",
     "Perpendicular ⟺ dot = 0",
     "cosθ = (a⃗·b⃗)/(|a||b|)"
    ]
   },
   {
    "h": "Cross product ⭐⭐",
    "items": [
     "|a×b| = |a||b|sinθ, direction ⊥",
     "Determinant form (î ĵ k̂ row)",
     "a⃗×b⃗ = −(b⃗×a⃗)!"
    ]
   },
   {
    "h": "Uses ⭐",
    "items": [
     "½|a⃗×b⃗| = triangle area",
     "Parallel ⟺ cross = 0⃗",
     "Scalar triple product DELETED"
    ]
   }
  ]
 },
 "practice": [
  [
   "a⃗ = 2î + 3ĵ − k̂ ka magnitude?",
   "|a⃗| = √(4 + 9 + 1) = <b>√14</b>."
  ],
  [
   "a⃗ = 3î + 4ĵ ka unit vector?",
   "|a⃗| = 5 → â = <b>(3/5)î + (4/5)ĵ</b> — vector ko uske magnitude se divide karo."
  ],
  [
   "A(1, 2, 3), B(4, 5, 6). AB⃗ kya hai?",
   "AB⃗ = b⃗ − a⃗ = <b>3î + 3ĵ + 3k̂</b> (head − tail)."
  ],
  [
   "a⃗·b⃗ = 0 ka kya matlab (non-zero vectors)?",
   "Vectors <b>perpendicular</b> hain — cos θ = 0, θ = 90°."
  ],
  [
   "a⃗ = î + ĵ, b⃗ = î − ĵ. a⃗·b⃗ nikalo.",
   "1·1 + 1·(−1) + 0 = <b>0</b> — perpendicular hain!"
  ],
  [
   "a⃗×b⃗ = −(b⃗×a⃗) kyun important hai?",
   "Cross product <b>anti-commutative</b> hai — <b>order badla to sign badla</b>. Dot product commutative tha, cross nahi!"
  ],
  [
   "Do vectors ke sides wale parallelogram ka area?",
   "<b>|a⃗×b⃗|</b> — cross product ka magnitude. (Triangle ka: ½|a⃗×b⃗|.)"
  ],
  [
   "î × ĵ kya hai? Aur ĵ × î?",
   "î × ĵ = <b>k̂</b>; ĵ × î = <b>−k̂</b> — cyclic order positive, reverse negative."
  ],
  [
   "A, B, C collinear hain kaise check karein (vectors se)?",
   "AB⃗ aur AC⃗ <b>parallel</b> hone chahiye — AB⃗ = λAC⃗ ya AB⃗ × AC⃗ = 0⃗."
  ],
  [
   "Scalar triple product a⃗·(b⃗×c⃗) syllabus me hai?",
   "<b>Nahi</b> — rationalized NCERT se <b>delete</b> ho chuka hai. Sirf dot aur cross products padhne hain."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-11/",
  "title": "Three Dimensional Geometry"
 }
}

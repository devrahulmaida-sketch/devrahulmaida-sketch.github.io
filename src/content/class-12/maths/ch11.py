# Class 12 Maths, Chapter 11 - Three Dimensional Geometry
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 11,
 "title_en": "Three Dimensional Geometry",
 "title_hi": "त्रिविम ज्यामिति",
 "tagline": "3D space me lines — direction cosines, equations, angles aur shortest distance",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 11: Three Dimensional Geometry — long + short notes in Hindi, English, Hinglish. Direction cosines and ratios, equation of a line, angle between lines, shortest distance between skew lines.",
 "video": None,
 "card_tag": "3D space me lines — direction cosines, equations, angles aur shortest distance",
 "card_topics": [
  "🧭 Direction cosines & ratios",
  "📏 Line equations (2 forms)",
  "📐 Angle between lines",
  "📉 Shortest distance (skew)"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Direction Cosines aur Direction Ratios — Line Ki Disha ⭐⭐",
    "body": "<ul>\n<li><b>Direction cosines (DCs) ⭐⭐:</b> line jo angles α, β, γ axes ke saath banati hai, unke <b>cosines</b> — <b>l = cos α, m = cos β, n = cos γ</b>. Har line ki direction = 3 numbers!</li>\n<li><b>Golden identity ⭐⭐:</b> <b>l² + m² + n² = 1</b> — DCs hamesha ye satisfy karte hain (unit vector ke components hain!).</li>\n<li><b>Direction ratios (DRs) ⭐:</b> DCs ke <b>PROPORTIONAL</b> koi bhi 3 numbers (a, b, c) — a/l = b/m = c/n. DRs infinite hain, DCs unique (sign ke saath)!</li>\n<li><b>DRs → DCs ⭐⭐:</b> l = a/√(a²+b²+c²), m = b/√(a²+b²+c²), n = c/√(a²+b²+c²) — <b>normalize</b> karo!</li>\n<li>Do points P(x₁,y₁,z₁), Q(x₂,y₂,z₂) se guzarne wali line ke DRs: <b>(x₂−x₁, y₂−y₁, z₂−z₁)</b> — coordinates ghatao, bas!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: DRs = recipe ka ratio (2:3:1), DCs = exact measurement (unit vector). Ratio se exact nikalne ke liye √(sum of squares) se divide karo.</p>"
   },
   {
    "h": "2️⃣ Line Ki Equations — Vector aur Cartesian Form ⭐⭐",
    "body": "<ul>\n<li><b>Line ke liye 2 cheezein chahiye:</b> ek POINT jis se guzre + ek DIRECTION jis taraf jaaye. Dono mile to line fix!</li>\n<li><b>Vector form ⭐⭐:</b> r⃗ = <b>a⃗ + λb⃗</b> — a⃗ = point ka position vector, b⃗ = direction vector, λ = parameter (har λ pe line ka ek point!).</li>\n<li><b>Cartesian form ⭐⭐:</b> <b>(x − x₁)/a = (y − y₁)/b = (z − z₁)/c</b> — (x₁, y₁, z₁) point, (a, b, c) DRs. Dono forms ek hi line hain!</li>\n<li><b>Conversion:</b> vector se cartesian: a⃗ ke components numerator ke saath, b⃗ ke components denominators me. Cartesian se vector: point + λ×DRs.</li>\n<li><b>Do points se line ⭐:</b> r⃗ = a⃗ + λ(b⃗ − a⃗) — direction = doosra point − pehla point. Cartesian: (x−x₁)/(x₂−x₁) = (y−y₁)/(y₂−y₁) = (z−z₁)/(z₂−z₁).</li>\n<li>Denominator me 0 aaye to matlab wo coordinate CONSTANT hai (line us axis ke perpendicular plane me) — panic nahi, special case hai.</li>\n</ul>\n<p class=\"small-note\">🎯 λ = \"line pe ghoomne ka dial\". λ = 0 pe point a⃗, λ badhao to direction b⃗ me chalte jao!</p>"
   },
   {
    "h": "3️⃣ Do Lines Ke Beech Ka Angle ⭐",
    "body": "<ul>\n<li><b>Formula (DRs se) ⭐⭐:</b> cos θ = <b>(a₁a₂ + b₁b₂ + c₁c₂)/[√(a₁²+b₁²+c₁²)·√(a₂²+b₂²+c₂²)]</b> — direction vectors ka DOT product formula hi hai!</li>\n<li><b>Vector form me:</b> cos θ = |b⃗₁·b⃗₂|/(|b⃗₁||b⃗₂|) — lines ke direction vectors use karo.</li>\n<li><b>Perpendicular ⭐:</b> a₁a₂ + b₁b₂ + c₁c₂ = <b>0</b> — DRs ka \"dot\" zero! (Lines me ye sabse zyada pucha jaata hai.)</li>\n<li><b>Parallel ⭐:</b> DRs <b>PROPORTIONAL</b> — a₁/a₂ = b₁/b₂ = c₁/c₂. (Vector me: b⃗₁ = λb⃗₂.)</li>\n<li>DCs se bhi chalega: cos θ = l₁l₂ + m₁m₂ + n₁n₂ — kyunki DCs normalized hain, denominator 1!</li>\n<li>Angle hamesha ACUTE lena hai (modulus lagake) — lines ke beech \"the\" angle wo hota hai.</li>\n</ul>\n<p class=\"small-note\">💡 Lines ka angle = unke direction vectors ka angle. Chapter 10 ka dot product yahan wapas aaya — vectors aur 3D ek hi duniya hai!</p>"
   },
   {
    "h": "4️⃣ Shortest Distance — Skew aur Parallel Lines ⭐⭐",
    "body": "<ul>\n<li><b>Skew lines:</b> do lines jo na parallel hon, na intersect karein (alag-alag planes me) — unke beech ka sabse chhota gap = <b>shortest distance</b> (SD).</li>\n<li><b>SD formula (skew) ⭐⭐:</b> lines r⃗ = a⃗₁ + λb⃗₁ aur r⃗ = a⃗₂ + μb⃗₂ → SD = <b>|(a⃗₂ − a⃗₁)·(b⃗₁×b⃗₂)| / |b⃗₁×b⃗₂|</b> — \"points ka difference, cross pe project karo, cross se divide\".</li>\n<li><b>Intersect check ⭐:</b> agar SD = 0 → lines <b>INTERSECT</b> karti hain (ya coplanar hain)! Yehi condition hai.</li>\n<li><b>Parallel lines ka SD ⭐:</b> d = <b>|b⃗×(a⃗₂ − a⃗₁)|/|b⃗|</b> — ek line ka direction aur dono ke points ka difference use karo.</li>\n<li><b>Cartesian me:</b> pehle vector form me convert karo (point + DRs nikaal ke) — direct cartesian formula yaad karne ki zaroorat nahi!</li>\n</ul>\n<p class=\"small-note\">🎯 SD ka flow: a⃗₂ − a⃗₁ nikalo → b⃗₁×b⃗₂ nikalo → dot → divide. 5-marker ka fixed recipe — 3-4 baar practice karo to set ho jaayega.</p>"
   },
   {
    "h": "5️⃣ Syllabus Note — Planes Deleted! ⭐",
    "body": "<ul>\n<li><b>Badi khabar ⭐⭐:</b> rationalized NCERT/CBSE me <b>PLANE ke saare topics DELETE</b> — plane ki equations, coplanar lines, angle between planes, line-plane angle, point se plane ki distance — <b>kuch nahi padhna!</b></li>\n<li><b>Chapter ab sirf LINES ka hai:</b> DCs/DRs → line ki equations → do lines ka angle → shortest distance. Bas!</li>\n<li>Pehle ye chapter 3D me sabse lamba tha — ab chapter almost HALF ho gaya hai. Marks wahi (unit ~14 with vectors), kaam aadha!</li>\n<li><b>Vectors (Ch 10) strong rakho:</b> dot, cross, magnitude — har formula unhi pe chalta hai.</li>\n<li>JEE aspirants note: JEE syllabus me planes abhi bhi hain — boards ke liye skip, JEE ke liye separately cover karna hoga.</li>\n</ul>\n<p class=\"small-note\">💡 Boards: sirf lines. JEE: planes bhi. Apne target ke hisaab se padho — dono lists alag hain!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ दिक्-कोज्या और दिक्-अनुपात — रेखा की दिशा ⭐⭐",
    "body": "<ul>\n<li><b>दिक्-कोज्या (DCs) ⭐⭐:</b> रेखा अक्षों से α, β, γ कोण बनाए तो <b>l = cos α, m = cos β, n = cos γ</b>।</li>\n<li><b>स्वर्ण सर्वसमिका ⭐⭐:</b> <b>l² + m² + n² = 1</b> — DCs मात्रक सदिश के घटक हैं!</li>\n<li><b>दिक्-अनुपात (DRs) ⭐:</b> DCs के <b>समानुपाती</b> कोई तीन संख्याएं (a, b, c)। DRs अनंत, DCs अद्वितीय!</li>\n<li><b>DRs → DCs ⭐⭐:</b> l = a/√(a²+b²+c²) आदि — <b>सामान्यीकरण</b> करो!</li>\n<li>बिंदु P(x₁,y₁,z₁), Q(x₂,y₂,z₂) से रेखा के DRs: <b>(x₂−x₁, y₂−y₁, z₂−z₁)</b>।</li>\n</ul>\n<p class=\"small-note\">💡 DRs = अनुपात, DCs = मात्रक रूप। √(वर्गों का योग) से भाग दो।</p>"
   },
   {
    "h": "2️⃣ रेखा के समीकरण — सदिश और कार्तीय रूप ⭐⭐",
    "body": "<ul>\n<li><b>रेखा के लिए 2 चीजें:</b> एक <b>बिंदु</b> + एक <b>दिशा</b> — दोनों मिलें तो रेखा निश्चित!</li>\n<li><b>सदिश रूप ⭐⭐:</b> r⃗ = <b>a⃗ + λb⃗</b> — a⃗ बिंदु का स्थिति सदिश, b⃗ दिशा सदिश, λ प्राचल।</li>\n<li><b>कार्तीय रूप ⭐⭐:</b> <b>(x − x₁)/a = (y − y₁)/b = (z − z₁)/c</b>।</li>\n<li><b>दो बिंदुओं से रेखा ⭐:</b> r⃗ = a⃗ + λ(b⃗ − a⃗); कार्तीय: (x−x₁)/(x₂−x₁) = ...</li>\n<li>हर में 0 आए तो वह निर्देशांक <b>अचर</b> है — विशिष्ट स्थिति, घबराओ नहीं!</li>\n</ul>\n<p class=\"small-note\">🎯 λ = \"रेखा पर घूमने का डायल\" — λ = 0 पर बिंदु a⃗!</p>"
   },
   {
    "h": "3️⃣ दो रेखाओं के बीच का कोण ⭐",
    "body": "<ul>\n<li><b>सूत्र (DRs से) ⭐⭐:</b> cos θ = <b>(a₁a₂ + b₁b₂ + c₁c₂)/[√(a₁²+b₁²+c₁²)·√(a₂²+b₂²+c₂²)]</b> — दिशा सदिशों का डॉट!</li>\n<li><b>सदिश रूप में:</b> cos θ = |b⃗₁·b⃗₂|/(|b⃗₁||b⃗₂|)।</li>\n<li><b>लंबवत ⭐:</b> a₁a₂ + b₁b₂ + c₁c₂ = <b>0</b>।</li>\n<li><b>समांतर ⭐:</b> DRs <b>समानुपाती</b> — a₁/a₂ = b₁/b₂ = c₁/c₂।</li>\n<li>DCs से: cos θ = l₁l₂ + m₁m₂ + n₁n₂।</li>\n<li>कोण सदैव <b>न्यून</b> (acute) लो — मापांक लगाकर!</li>\n</ul>\n<p class=\"small-note\">💡 रेखाओं का कोण = दिशा सदिशों का कोण।</p>"
   },
   {
    "h": "4️⃣ न्यूनतम दूरी — विषमतलीय और समांतर रेखाएं ⭐⭐",
    "body": "<ul>\n<li><b>विषमतलीय रेखाएं (skew):</b> न समांतर, न प्रतिच्छेदी — भिन्न समतलों में। सबसे छोटा अंतर = <b>न्यूनतम दूरी (SD)</b>।</li>\n<li><b>SD सूत्र (skew) ⭐⭐:</b> SD = <b>|(a⃗₂ − a⃗₁)·(b⃗₁×b⃗₂)| / |b⃗₁×b⃗₂|</b>।</li>\n<li><b>प्रतिच्छेद जांच ⭐:</b> SD = 0 → रेखाएं <b>प्रतिच्छेद</b> करती हैं!</li>\n<li><b>समांतर रेखाओं का SD ⭐:</b> d = <b>|b⃗×(a⃗₂ − a⃗₁)|/|b⃗|</b>।</li>\n<li><b>कार्तीय में:</b> पहले सदिश रूप में बदलो — सीधा कार्तीय सूत्र रटने की जरूरत नहीं!</li>\n</ul>\n<p class=\"small-note\">🎯 SD प्रवाह: a⃗₂ − a⃗₁ → b⃗₁×b⃗₂ → डॉट → भाग। निश्चित 5-अंकीय विधि!</p>"
   },
   {
    "h": "5️⃣ पाठ्यक्रम टिप्पणी — समतल हटाए गए! ⭐",
    "body": "<ul>\n<li><b>बड़ी खबर ⭐⭐:</b> युक्तिसंगत NCERT/CBSE में <b>समतल (plane) के सभी विषय हटाए गए</b> — समतल का समीकरण, समतलीय रेखाएं, समतलों का कोण, रेखा-समतल कोण, बिंदु-समतल दूरी!</li>\n<li><b>अध्याय अब केवल रेखाओं का:</b> DCs/DRs → समीकरण → कोण → न्यूनतम दूरी। बस!</li>\n<li>पहले यह सबसे लंबा अध्याय था — अब लगभग <b>आधा</b> हो गया। अंक वही, काम आधा!</li>\n<li><b>सदिश (अध्याय 10) मजबूत रखो:</b> डॉट, क्रॉस, परिमाण — हर सूत्र इन्हीं पर चलता है।</li>\n<li>JEE विद्यार्थी ध्यान दें: JEE में समतल <b>अभी भी</b> हैं — बोर्ड के लिए छोड़ो, JEE के लिए अलग से पढ़ो।</li>\n</ul>\n<p class=\"small-note\">💡 बोर्ड: केवल रेखाएं। JEE: समतल भी। लक्ष्य के अनुसार पढ़ो!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Direction Cosines and Ratios — A Line's Direction ⭐⭐",
    "body": "<ul>\n<li><b>Direction cosines (DCs) ⭐⭐:</b> if a line makes angles α, β, γ with the axes, its DCs are <b>l = cos α, m = cos β, n = cos γ</b>. A line's direction = 3 numbers!</li>\n<li><b>Golden identity ⭐⭐:</b> <b>l² + m² + n² = 1</b> — DCs always satisfy this (they are the components of a unit vector!).</li>\n<li><b>Direction ratios (DRs) ⭐:</b> any 3 numbers <b>PROPORTIONAL</b> to the DCs — a/l = b/m = c/n. DRs are infinite; DCs are unique (with sign)!</li>\n<li><b>DRs → DCs ⭐⭐:</b> l = a/√(a²+b²+c²), m = b/√(a²+b²+c²), n = c/√(a²+b²+c²) — just <b>normalize</b>!</li>\n<li>DRs of the line through P(x₁,y₁,z₁) and Q(x₂,y₂,z₂): <b>(x₂−x₁, y₂−y₁, z₂−z₁)</b> — subtract the coordinates, done!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: DRs = the recipe's ratio (2:3:1), DCs = the exact measurement (a unit vector). Divide by √(sum of squares) to go from ratio to exact.</p>"
   },
   {
    "h": "2️⃣ Equations of a Line — Vector and Cartesian Forms ⭐⭐",
    "body": "<ul>\n<li><b>A line needs 2 things:</b> a POINT it passes through + a DIRECTION it runs along. Both fixed → the line is fixed!</li>\n<li><b>Vector form ⭐⭐:</b> r⃗ = <b>a⃗ + λb⃗</b> — a⃗ = position vector of the point, b⃗ = direction vector, λ = parameter (each λ gives one point on the line!).</li>\n<li><b>Cartesian form ⭐⭐:</b> <b>(x − x₁)/a = (y − y₁)/b = (z − z₁)/c</b> — (x₁, y₁, z₁) is the point, (a, b, c) are the DRs. Both forms describe the same line!</li>\n<li><b>Conversion:</b> vector → cartesian: a⃗'s components go with the numerators, b⃗'s into the denominators. Cartesian → vector: point + λ×DRs.</li>\n<li><b>Line through two points ⭐:</b> r⃗ = a⃗ + λ(b⃗ − a⃗) — direction = second point − first point. Cartesian: (x−x₁)/(x₂−x₁) = (y−y₁)/(y₂−y₁) = (z−z₁)/(z₂−z₁).</li>\n<li>A 0 in a denominator just means that coordinate is CONSTANT — a special case, no panic!</li>\n</ul>\n<p class=\"small-note\">🎯 λ = \"the dial for moving along the line\". At λ = 0 you stand at a⃗; turn the dial and you walk along b⃗!</p>"
   },
   {
    "h": "3️⃣ The Angle Between Two Lines ⭐",
    "body": "<ul>\n<li><b>Formula (via DRs) ⭐⭐:</b> cos θ = <b>(a₁a₂ + b₁b₂ + c₁c₂)/[√(a₁²+b₁²+c₁²)·√(a₂²+b₂²+c₂²)]</b> — it is just the DOT product formula of the direction vectors!</li>\n<li><b>In vector form:</b> cos θ = |b⃗₁·b⃗₂|/(|b⃗₁||b⃗₂|) — use the direction vectors of the lines.</li>\n<li><b>Perpendicular ⭐:</b> a₁a₂ + b₁b₂ + c₁c₂ = <b>0</b> — the \"dot\" of the DRs is zero! (The most-asked check for lines.)</li>\n<li><b>Parallel ⭐:</b> DRs are <b>PROPORTIONAL</b> — a₁/a₂ = b₁/b₂ = c₁/c₂. (In vectors: b⃗₁ = λb⃗₂.)</li>\n<li>DCs work too: cos θ = l₁l₂ + m₁m₂ + n₁n₂ — since DCs are normalized, the denominator is 1!</li>\n<li>Always take the ACUTE angle (apply modulus) — \"the\" angle between lines is that one.</li>\n</ul>\n<p class=\"small-note\">💡 The angle between lines = the angle between their direction vectors. Chapter 10's dot product returns — vectors and 3D are one world!</p>"
   },
   {
    "h": "4️⃣ Shortest Distance — Skew and Parallel Lines ⭐⭐",
    "body": "<ul>\n<li><b>Skew lines:</b> two lines that are neither parallel nor intersecting (they lie in different planes) — the smallest gap between them is the <b>shortest distance</b> (SD).</li>\n<li><b>SD formula (skew) ⭐⭐:</b> for lines r⃗ = a⃗₁ + λb⃗₁ and r⃗ = a⃗₂ + μb⃗₂ → SD = <b>|(a⃗₂ − a⃗₁)·(b⃗₁×b⃗₂)| / |b⃗₁×b⃗₂|</b> — \"difference of points, projected on the cross, divided by the cross\".</li>\n<li><b>Intersection check ⭐:</b> if SD = 0 → the lines <b>INTERSECT</b> (they are coplanar)! That is the condition.</li>\n<li><b>SD of parallel lines ⭐:</b> d = <b>|b⃗×(a⃗₂ − a⃗₁)|/|b⃗|</b> — use one line's direction and the difference of the two points.</li>\n<li><b>In cartesian form:</b> first convert to vector form (extract the point + DRs) — no need to memorize a direct cartesian formula!</li>\n</ul>\n<p class=\"small-note\">🎯 SD flow: find a⃗₂ − a⃗₁ → find b⃗₁×b⃗₂ → dot → divide. A fixed 5-marker recipe — practise it 3-4 times and it sets.</p>"
   },
   {
    "h": "5️⃣ Syllabus Note — Planes Deleted! ⭐",
    "body": "<ul>\n<li><b>Big news ⭐⭐:</b> in rationalized NCERT/CBSE, ALL <b>PLANE topics are DELETED</b> — the equation of a plane, coplanar lines, angle between planes, line-plane angle, point-to-plane distance — <b>none of it!</b></li>\n<li><b>The chapter is now only about LINES:</b> DCs/DRs → equations of a line → angle between lines → shortest distance. That is all!</li>\n<li>This used to be the longest 3D chapter — now it is almost HALF. Same marks (~14 for the unit with vectors), half the work!</li>\n<li><b>Keep vectors (Ch 10) strong:</b> dot, cross, magnitude — every formula here runs on them.</li>\n<li>JEE aspirants, note: planes are STILL in the JEE syllabus — skip for boards, cover separately for JEE.</li>\n</ul>\n<p class=\"small-note\">💡 Boards: only lines. JEE: planes too. Study by your target — the two lists are different!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "DCs/DRs ⭐⭐",
    "items": [
     "l=cosα, m=cosβ, n=cosγ",
     "l²+m²+n²=1",
     "DRs→DCs: √(a²+b²+c²) se divide"
    ]
   },
   {
    "h": "Line equations ⭐⭐",
    "items": [
     "r⃗ = a⃗ + λb⃗",
     "(x−x₁)/a = (y−y₁)/b = (z−z₁)/c",
     "2 points: direction = b⃗−a⃗"
    ]
   },
   {
    "h": "Angle ⭐",
    "items": [
     "cosθ = (b⃗₁·b⃗₂)/(|b⃗₁||b⃗₂|)",
     "Perpendicular: a₁a₂+b₁b₂+c₁c₂=0",
     "Parallel: DRs proportional"
    ]
   },
   {
    "h": "Shortest distance ⭐⭐",
    "items": [
     "Skew: |(a₂−a₁)·(b₁×b₂)|/|b₁×b₂|",
     "SD=0 → intersecting",
     "Parallel: |b×(a₂−a₁)|/|b|"
    ]
   },
   {
    "h": "Syllabus ⭐⭐",
    "items": [
     "PLANES completely DELETED",
     "Sirf lines padhni hain",
     "JEE me planes alag se"
    ]
   }
  ],
  "hi": [
   {
    "h": "DCs/DRs ⭐⭐",
    "items": [
     "l=cosα, m=cosβ, n=cosγ",
     "l²+m²+n²=1",
     "DRs→DCs: √(a²+b²+c²) से भाग"
    ]
   },
   {
    "h": "रेखा समीकरण ⭐⭐",
    "items": [
     "r⃗ = a⃗ + λb⃗",
     "(x−x₁)/a = (y−y₁)/b = (z−z₁)/c",
     "2 बिंदु: दिशा = b⃗−a⃗"
    ]
   },
   {
    "h": "कोण ⭐",
    "items": [
     "cosθ = (b⃗₁·b⃗₂)/(|b⃗₁||b⃗₂|)",
     "लंबवत: a₁a₂+b₁b₂+c₁c₂=0",
     "समांतर: DRs समानुपाती"
    ]
   },
   {
    "h": "न्यूनतम दूरी ⭐⭐",
    "items": [
     "Skew: |(a₂−a₁)·(b₁×b₂)|/|b₁×b₂|",
     "SD=0 → प्रतिच्छेदी",
     "समांतर: |b×(a₂−a₁)|/|b|"
    ]
   },
   {
    "h": "पाठ्यक्रम ⭐⭐",
    "items": [
     "समतल पूर्णतः हटाए गए",
     "केवल रेखाएं पढ़नी हैं",
     "JEE में समतल अलग से"
    ]
   }
  ],
  "en": [
   {
    "h": "DCs/DRs ⭐⭐",
    "items": [
     "l=cosα, m=cosβ, n=cosγ",
     "l²+m²+n²=1",
     "DRs→DCs: divide by √(a²+b²+c²)"
    ]
   },
   {
    "h": "Line equations ⭐⭐",
    "items": [
     "r⃗ = a⃗ + λb⃗",
     "(x−x₁)/a = (y−y₁)/b = (z−z₁)/c",
     "2 points: direction = b⃗−a⃗"
    ]
   },
   {
    "h": "Angle ⭐",
    "items": [
     "cosθ = (b⃗₁·b⃗₂)/(|b⃗₁||b⃗₂|)",
     "Perpendicular: a₁a₂+b₁b₂+c₁c₂=0",
     "Parallel: DRs proportional"
    ]
   },
   {
    "h": "Shortest distance ⭐⭐",
    "items": [
     "Skew: |(a₂−a₁)·(b₁×b₂)|/|b₁×b₂|",
     "SD=0 → intersecting",
     "Parallel: |b×(a₂−a₁)|/|b|"
    ]
   },
   {
    "h": "Syllabus ⭐⭐",
    "items": [
     "PLANES completely DELETED",
     "Only lines to study",
     "Planes separately for JEE"
    ]
   }
  ]
 },
 "practice": [
  [
   "DRs (2, −3, 6) ke corresponding DCs?",
   "√(4+9+36) = 7 → <b>(2/7, −3/7, 6/7)</b>."
  ],
  [
   "l² + m² + n² ka value hamesha?",
   "<b>1</b> — DCs unit vector ke components hain."
  ],
  [
   "P(1, 2, 3), Q(4, 0, 5) se line ke DRs?",
   "<b>(3, −2, 2)</b> — Q − P."
  ],
  [
   "Point (1, 2, 3) se guzarti, direction (2, 1, −1) wali line ka vector equation?",
   "r⃗ = <b>(î + 2ĵ + 3k̂) + λ(2î + ĵ − k̂)</b>."
  ],
  [
   "(x−1)/2 = (y−2)/3 = (z+1)/4 me point aur DRs kya hain?",
   "Point <b>(1, 2, −1)</b>, DRs <b>(2, 3, 4)</b> — (z−(−1)) dhyan se!"
  ],
  [
   "Do lines perpendicular kab hoti hain (DRs se)?",
   "Jab <b>a₁a₂ + b₁b₂ + c₁c₂ = 0</b> — direction vectors ka dot zero."
  ],
  [
   "DRs (1, 2, 3) aur (2, 4, 6) wali lines ka relation?",
   "<b>Parallel</b> — DRs proportional hain (1:2 ratio sab me)."
  ],
  [
   "Skew lines ki shortest distance ka formula?",
   "SD = <b>|(a⃗₂ − a⃗₁)·(b⃗₁×b⃗₂)| / |b⃗₁×b⃗₂|</b>."
  ],
  [
   "SD = 0 aane pe lines kaisi hain?",
   "<b>Intersecting (coplanar)</b> — na skew na strictly parallel."
  ],
  [
   "Plane ka equation ab bhi Class 12 boards me aata hai?",
   "<b>Nahi</b> — plane ke saare topics rationalized syllabus se <b>delete</b> ho chuke hain. Sirf lines! (JEE ke liye planes alag se padho.)"
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-12/",
  "title": "Linear Programming"
 }
}

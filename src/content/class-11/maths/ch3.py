# Class 11 Maths, Chapter 3 - Trigonometric Functions
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 3,
 "title_en": "Trigonometric Functions",
 "title_hi": "त्रिकोणमितीय फलन",
 "tagline": "Radians, unit circle aur identities — trig ka complete toolkit",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 3: Trigonometric Functions — long + short notes in Hindi, English, Hinglish. Radians, unit circle, ASTC signs, sum-difference formulas, double angle, graphs.",
 "video": None,
 "card_tag": "Radians, unit circle aur identities — trig ka complete toolkit",
 "card_topics": [
  "📐 Radians + conversion",
  "🔄 Unit circle + ASTC",
  "➕ Sum-difference formulas",
  "✖️ Double/triple angles"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Angles aur Radians — Measurement Ka New Unit ⭐",
    "body": "<ul>\n<li><b>Degree measure:</b> pura circle = 360°. 1° = 60′ (minutes), 1′ = 60″ (seconds).</li>\n<li><b>Radian ⭐:</b> jab arc ki length = radius ho, tab bana angle = 1 radian. Pura circle = 2π radian (kyunki circumference = 2πr!).</li>\n<li><b>Conversion ⭐:</b> π radian = 180° → 1 radian ≈ 57.3°, 1° = π/180 radian. Radian me likhna JEE/CBSE me default hai!</li>\n<li><b>Common angles yaad karo:</b> 30° = π/6, 45° = π/4, 60° = π/3, 90° = π/2, 180° = π, 270° = 3π/2, 360° = 2π.</li>\n<li><b>Arc length formula ⭐:</b> l = rθ (θ radian me hi!) — degree me use karne pe answer galat.</li>\n<li>Negative angle = clockwise, positive = anticlockwise. Angles kisi bhi size ke ho sakte hain (2π se zyada bhi!).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: radian = arc ko radius se measure karna. Kitne radius lambi arc? — utne radians! Pura circle me exactly 2π radius lambi arc fit hoti hai.</p>"
   },
   {
    "h": "2️⃣ Trig Ratios Unit Circle Pe ⭐",
    "body": "<ul>\n<li><b>Unit circle (radius 1):</b> angle θ ke point P(x, y) ke liye <b>cos θ = x, sin θ = y</b>, tan θ = y/x. Yehi definition hai sab angles ke liye (90°+ bhi)!</li>\n<li><b>Other ratios:</b> tan = sin/cos, cot = 1/tan, sec = 1/cos, cosec = 1/sin.</li>\n<li><b>Signs by quadrant ⭐ (ASTC — \"All Students Take Chemistry\"):</b> Q1 (0-90°): SAB positive; Q2 (90-180°): sirf Sin (+cosec); Q3 (180-270°): sirf Tan (+cot); Q4 (270-360°): sirf Cos (+sec).</li>\n<li><b>Fundamental values table:</b> sin/cos/tan for 0, π/6, π/4, π/3, π/2 — ye table RATT lo (0, 1/2, 1/√2, √3/2, 1 pattern sin me!).</li>\n<li><b>Pythagorean identity ⭐:</b> sin²θ + cos²θ = 1 → 1 + tan²θ = sec²θ, 1 + cot²θ = cosec²θ (divide karke banti hain!).</li>\n<li><b>Domain check:</b> tan, sec undefined jahan cos = 0 (π/2, 3π/2...); cot, cosec undefined jahan sin = 0 (0, π...).</li>\n</ul>\n<p class=\"small-note\">🎯 ASTC me order yaad rakho: quadrant badhta hai (1→2→3→4) to positive ratio: All → Sin → Tan → Cos.</p>"
   },
   {
    "h": "3️⃣ Negative aur Related Angles Ke Formulas",
    "body": "<ul>\n<li><b>Even-odd ⭐:</b> cos(−x) = cos x (EVEN), sin(−x) = −sin x (ODD), tan(−x) = −tan x (ODD).</li>\n<li><b>Periodicity:</b> sin, cos ka period 2π (sin(x + 2π) = sin x); tan, cot ka period π. ⭐</li>\n<li><b>Complementary (90° minus):</b> sin(π/2 − x) = cos x, cos(π/2 − x) = sin x, tan(π/2 − x) = cot x — cofunctions swap!</li>\n<li><b>Supplementary (180° minus/plus):</b> sin(π − x) = sin x, cos(π − x) = −cos x; sin(π + x) = −sin x, cos(π + x) = −cos x.</li>\n<li><b>Trick ⭐:</b> koi bhi bada angle → π/2 ke multiples me todo. π/2 ke EVEN multiple pe function SAME rehta hai, ODD multiple pe cofunction ban jaata hai; sign ASTC se.</li>\n<li>Example: sin(7π/6) = sin(π + π/6) = −sin(π/6) = −1/2 (Q3 me sin negative!).</li>\n</ul>\n<p class=\"small-note\">💡 Har bade angle ka answer do steps me: (1) reference angle nikalo, (2) quadrant dekh ke sign lagao (ASTC).</p>"
   },
   {
    "h": "4️⃣ Sum aur Difference Formulas ⭐⭐",
    "body": "<ul>\n<li><b>cos(x + y) = cos x cos y − sin x sin y</b> (minus andar, minus bahar!) <b>cos(x − y) = cos x cos y + sin x sin y</b></li>\n<li><b>sin(x + y) = sin x cos y + cos x sin y</b> <b>sin(x − y) = sin x cos y − cos x sin y</b></li>\n<li><b>tan(x + y) = (tan x + tan y)/(1 − tan x tan y)</b>; minus wala: numerator minus, denominator plus.</li>\n<li><b>Derived gems ⭐:</b> cos(π/2 + x) = −sin x, sin(π/2 + x) = cos x, cos(π + x) = −cos x — sab sum formulas se nikalte hain!</li>\n<li><b>Product-to-sum:</b> 2 sin x cos y = sin(x+y) + sin(x−y); 2 cos x cos y = cos(x+y) + cos(x−y); 2 sin x sin y = cos(x−y) − cos(x+y). ⭐</li>\n<li><b>Sum-to-product:</b> sin x + sin y = 2 sin((x+y)/2)cos((x−y)/2); cos x + cos y = 2 cos((x+y)/2)cos((x−y)/2); cos x − cos y = −2 sin((x+y)/2)sin((x−y)/2); sin x − sin y = 2 cos((x+y)/2)sin((x−y)/2).</li>\n</ul>\n<p class=\"small-note\">💡 Memory trick: cos expansion me sign FLIP hota hai (plus andar, minus bahar), sin me SAME rehta hai. Tan wala fraction — niche hamesha ulta sign!</p>"
   },
   {
    "h": "5️⃣ Multiple Angles aur Graphs",
    "body": "<ul>\n<li><b>Double angle ⭐⭐:</b> sin 2x = 2 sin x cos x; cos 2x = cos²x − sin²x = 2cos²x − 1 = 1 − 2sin²x; tan 2x = 2tan x/(1 − tan²x).</li>\n<li><b>Triple angle:</b> sin 3x = 3sin x − 4sin³x; cos 3x = 4cos³x − 3cos x; tan 3x = (3tan x − tan³x)/(1 − 3tan²x).</li>\n<li><b>Half-angle (power reduction) ⭐:</b> sin²x = (1 − cos 2x)/2, cos²x = (1 + cos 2x)/2 — integration me lifeline (12th me kaam aayega)!</li>\n<li><b>sin x graph:</b> wave 0 se start, max 1 at π/2, period 2π. <b>cos x:</b> max 1 se start (sin ko π/2 left shift = cos!).</li>\n<li><b>tan x graph:</b> period π, x = π/2 pe undefined (asymptotes), −∞ se +∞ tak.</li>\n<li><b>Range:</b> −1 ≤ sin x, cos x ≤ 1 hamesha; tan x kuch bhi ho sakta hai (−∞, ∞). ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 cos 2x ke teeno forms sabse zyada puche jaate hain — especially 1 − 2sin²x (sin²x isolate karne ke liye)!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ कोण और रेडियन — मापन की नई इकाई ⭐",
    "body": "<ul>\n<li><b>डिग्री माप:</b> पूरा वृत्त = 360°। 1° = 60′, 1′ = 60″।</li>\n<li><b>रेडियन ⭐:</b> जब चाप की लंबाई = त्रिज्या, तब बना कोण = 1 रेडियन। पूरा वृत्त = 2π रेडियन।</li>\n<li><b>रूपांतरण ⭐:</b> π रेडियन = 180° → 1° = π/180 रेडियन।</li>\n<li><b>मानक कोण:</b> 30° = π/6, 45° = π/4, 60° = π/3, 90° = π/2।</li>\n<li><b>चाप लंबाई ⭐:</b> l = rθ (θ रेडियन में ही!)।</li>\n</ul>\n<p class=\"small-note\">💡 रेडियन = चाप को त्रिज्या से मापना। पूरे वृत्त में ठीक 2π त्रिज्या लंबी चाप समाती है!</p>"
   },
   {
    "h": "2️⃣ इकाई वृत्त पर त्रिकोणमितीय अनुपात ⭐",
    "body": "<ul>\n<li><b>इकाई वृत्त:</b> कोण θ के बिंदु P(x, y) के लिए <b>cos θ = x, sin θ = y</b>, tan θ = y/x।</li>\n<li><b>अन्य अनुपात:</b> tan = sin/cos, cot = 1/tan, sec = 1/cos, cosec = 1/sin।</li>\n<li><b>चतुर्थांश चिह्न ⭐ (ASTC):</b> Q1: सभी धनात्मक; Q2: केवल Sin; Q3: केवल Tan; Q4: केवल Cos।</li>\n<li><b>पाइथागोरस सर्वसमिका ⭐:</b> sin²θ + cos²θ = 1 → 1 + tan²θ = sec²θ, 1 + cot²θ = cosec²θ।</li>\n<li><b>अपरिभाषित:</b> tan, sec जहां cos = 0; cot, cosec जहां sin = 0।</li>\n</ul>\n<p class=\"small-note\">🎯 ASTC: चतुर्थांश बढ़ने पर धनात्मक अनुपात: सभी → Sin → Tan → Cos।</p>"
   },
   {
    "h": "3️⃣ ऋणात्मक और संबंधित कोणों के सूत्र",
    "body": "<ul>\n<li><b>सम-विषम ⭐:</b> cos(−x) = cos x (सम), sin(−x) = −sin x (विषम)।</li>\n<li><b>आवर्तता:</b> sin, cos का आवर्तकाल 2π; tan, cot का π। ⭐</li>\n<li><b>पूरक (90°):</b> sin(π/2 − x) = cos x, cos(π/2 − x) = sin x — सह-फलन बदल जाते हैं!</li>\n<li><b>संपूरक (180°):</b> sin(π − x) = sin x, cos(π − x) = −cos x।</li>\n<li><b>युक्ति ⭐:</b> बड़ा कोण → π/2 के गुणक में तोड़ो। सम गुणक पर फलन समान, विषम पर सह-फलन; चिह्न ASTC से।</li>\n</ul>\n<p class=\"small-note\">💡 दो चरण: (1) संदर्भ कोण, (2) चतुर्थांश से चिह्न।</p>"
   },
   {
    "h": "4️⃣ योग और अंतर सूत्र ⭐⭐",
    "body": "<ul>\n<li><b>cos(x + y) = cos x cos y − sin x sin y</b>; <b>cos(x − y) = cos x cos y + sin x sin y</b></li>\n<li><b>sin(x ± y) = sin x cos y ± cos x sin y</b></li>\n<li><b>tan(x + y) = (tan x + tan y)/(1 − tan x tan y)</b></li>\n<li><b>गुणन-से-योग:</b> 2 sin x cos y = sin(x+y) + sin(x−y); 2 cos x cos y = cos(x+y) + cos(x−y); 2 sin x sin y = cos(x−y) − cos(x+y)। ⭐</li>\n<li><b>योग-से-गुणन:</b> sin x + sin y = 2 sin((x+y)/2)cos((x−y)/2); cos x − cos y = −2 sin((x+y)/2)sin((x−y)/2)।</li>\n</ul>\n<p class=\"small-note\">💡 cos में चिह्न पलटता है, sin में समान रहता है। tan में हर में उल्टा चिह्न!</p>"
   },
   {
    "h": "5️⃣ बहु-कोण सूत्र और आलेख",
    "body": "<ul>\n<li><b>द्वि-कोण ⭐⭐:</b> sin 2x = 2 sin x cos x; cos 2x = cos²x − sin²x = 2cos²x − 1 = 1 − 2sin²x; tan 2x = 2tan x/(1 − tan²x)।</li>\n<li><b>त्रि-कोण:</b> sin 3x = 3sin x − 4sin³x; cos 3x = 4cos³x − 3cos x।</li>\n<li><b>अर्ध-कोण ⭐:</b> sin²x = (1 − cos 2x)/2, cos²x = (1 + cos 2x)/2।</li>\n<li><b>आलेख:</b> sin तरंग 0 से, cos 1 से; tan का आवर्तकाल π, π/2 पर अनंतस्पर्शी।</li>\n<li><b>परिसर:</b> −1 ≤ sin x, cos x ≤ 1; tan x कुछ भी (−∞, ∞)। ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 cos 2x के तीनों रूप सर्वाधिक पूछे जाते हैं!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Angles and Radians — A New Unit of Measurement ⭐",
    "body": "<ul>\n<li><b>Degree measure:</b> a full circle = 360°. 1° = 60′ (minutes), 1′ = 60″ (seconds).</li>\n<li><b>Radian ⭐:</b> the angle made when the arc length equals the radius = 1 radian. A full circle = 2π radians (the circumference is 2πr!).</li>\n<li><b>Conversion ⭐:</b> π radians = 180° → 1 radian ≈ 57.3°, 1° = π/180 radians. Radians are the default in JEE/CBSE!</li>\n<li><b>Memorize the common angles:</b> 30° = π/6, 45° = π/4, 60° = π/3, 90° = π/2, 180° = π, 270° = 3π/2, 360° = 2π.</li>\n<li><b>Arc length ⭐:</b> l = rθ (θ MUST be in radians!) — using degrees here gives wrong answers.</li>\n<li>Negative angle = clockwise, positive = anticlockwise. Angles can be any size (more than 2π too!).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: a radian measures the arc in units of the radius. How many radii long is the arc? That many radians! Exactly 2π radius-lengths fit around a circle.</p>"
   },
   {
    "h": "2️⃣ Trig Ratios on the Unit Circle ⭐",
    "body": "<ul>\n<li><b>Unit circle (radius 1):</b> for the point P(x, y) at angle θ, <b>cos θ = x, sin θ = y</b>, tan θ = y/x. This is THE definition for all angles (even beyond 90°)!</li>\n<li><b>Other ratios:</b> tan = sin/cos, cot = 1/tan, sec = 1/cos, cosec = 1/sin.</li>\n<li><b>Signs by quadrant ⭐ (ASTC):</b> Q1 (0-90°): ALL positive; Q2 (90-180°): only Sin (+cosec); Q3 (180-270°): only Tan (+cot); Q4 (270-360°): only Cos (+sec).</li>\n<li><b>The standard values table:</b> sin/cos/tan for 0, π/6, π/4, π/3, π/2 — learn it cold (sin goes 0, 1/2, 1/√2, √3/2, 1!).</li>\n<li><b>Pythagorean identity ⭐:</b> sin²θ + cos²θ = 1 → 1 + tan²θ = sec²θ, 1 + cot²θ = cosec²θ (made by dividing!).</li>\n<li><b>Domain check:</b> tan and sec are undefined where cos = 0 (π/2, 3π/2...); cot and cosec where sin = 0 (0, π...).</li>\n</ul>\n<p class=\"small-note\">🎯 Remember the ASTC order: as the quadrant rises (1→2→3→4), the positive ratio goes All → Sin → Tan → Cos.</p>"
   },
   {
    "h": "3️⃣ Formulas for Negative and Related Angles",
    "body": "<ul>\n<li><b>Even-odd ⭐:</b> cos(−x) = cos x (EVEN), sin(−x) = −sin x (ODD), tan(−x) = −tan x (ODD).</li>\n<li><b>Periodicity:</b> sin and cos have period 2π (sin(x + 2π) = sin x); tan and cot have period π. ⭐</li>\n<li><b>Complementary (90° minus):</b> sin(π/2 − x) = cos x, cos(π/2 − x) = sin x, tan(π/2 − x) = cot x — cofunctions swap!</li>\n<li><b>Supplementary (180° minus/plus):</b> sin(π − x) = sin x, cos(π − x) = −cos x; sin(π + x) = −sin x, cos(π + x) = −cos x.</li>\n<li><b>The trick ⭐:</b> break any big angle into multiples of π/2. An EVEN multiple keeps the function the same; an ODD multiple switches to the cofunction; take the sign from ASTC.</li>\n<li>Example: sin(7π/6) = sin(π + π/6) = −sin(π/6) = −1/2 (sin is negative in Q3!).</li>\n</ul>\n<p class=\"small-note\">💡 Every big angle resolves in two steps: (1) find the reference angle, (2) fix the sign from the quadrant (ASTC).</p>"
   },
   {
    "h": "4️⃣ Sum and Difference Formulas ⭐⭐",
    "body": "<ul>\n<li><b>cos(x + y) = cos x cos y − sin x sin y</b> (minus inside, minus outside!) <b>cos(x − y) = cos x cos y + sin x sin y</b></li>\n<li><b>sin(x + y) = sin x cos y + cos x sin y</b> <b>sin(x − y) = sin x cos y − cos x sin y</b></li>\n<li><b>tan(x + y) = (tan x + tan y)/(1 − tan x tan y)</b>; for minus: minus on top, plus below.</li>\n<li><b>Derived gems ⭐:</b> cos(π/2 + x) = −sin x, sin(π/2 + x) = cos x, cos(π + x) = −cos x — all come from the sum formulas!</li>\n<li><b>Product-to-sum:</b> 2 sin x cos y = sin(x+y) + sin(x−y); 2 cos x cos y = cos(x+y) + cos(x−y); 2 sin x sin y = cos(x−y) − cos(x+y). ⭐</li>\n<li><b>Sum-to-product:</b> sin x + sin y = 2 sin((x+y)/2)cos((x−y)/2); cos x + cos y = 2 cos((x+y)/2)cos((x−y)/2); cos x − cos y = −2 sin((x+y)/2)sin((x−y)/2); sin x − sin y = 2 cos((x+y)/2)sin((x−y)/2).</li>\n</ul>\n<p class=\"small-note\">💡 Memory trick: the cos expansion FLIPS the sign (plus inside, minus outside); sin keeps the SAME sign. In tan, the denominator always takes the opposite sign!</p>"
   },
   {
    "h": "5️⃣ Multiple Angles and Graphs",
    "body": "<ul>\n<li><b>Double angle ⭐⭐:</b> sin 2x = 2 sin x cos x; cos 2x = cos²x − sin²x = 2cos²x − 1 = 1 − 2sin²x; tan 2x = 2tan x/(1 − tan²x).</li>\n<li><b>Triple angle:</b> sin 3x = 3sin x − 4sin³x; cos 3x = 4cos³x − 3cos x; tan 3x = (3tan x − tan³x)/(1 − 3tan²x).</li>\n<li><b>Half-angle (power reduction) ⭐:</b> sin²x = (1 − cos 2x)/2, cos²x = (1 + cos 2x)/2 — a lifeline in integration (Class 12)!</li>\n<li><b>sin x graph:</b> a wave starting at 0, peaking at 1 at π/2, period 2π. <b>cos x:</b> starts at 1 (shift sin left by π/2 and you get cos!).</li>\n<li><b>tan x graph:</b> period π, undefined at x = π/2 (asymptotes), runs from −∞ to +∞.</li>\n<li><b>Range:</b> −1 ≤ sin x, cos x ≤ 1 always; tan x can be anything (−∞, ∞). ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 All three forms of cos 2x are heavily asked — especially 1 − 2sin²x (for isolating sin²x)!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Radians ⭐",
    "items": [
     "π rad = 180°",
     "30°=π/6, 45°=π/4, 60°=π/3",
     "Arc: l = rθ (radian only!)"
    ]
   },
   {
    "h": "Unit Circle ⭐",
    "items": [
     "cos θ = x, sin θ = y",
     "ASTC signs by quadrant",
     "sin²θ + cos²θ = 1"
    ]
   },
   {
    "h": "Identities",
    "items": [
     "sin(−x)=−sin x; cos(−x)=cos x",
     "sin/cos period 2π; tan π",
     "sin(π/2−x) = cos x"
    ]
   },
   {
    "h": "Sum/Diff ⭐⭐",
    "items": [
     "cos(x+y): minus andar minus bahar",
     "sin(x±y) = sin x cos y ± cos x sin y",
     "tan: (t₁+t₂)/(1−t₁t₂)"
    ]
   },
   {
    "h": "Multi-angles ⭐",
    "items": [
     "sin 2x = 2sin x cos x",
     "cos 2x = 1−2sin²x (3 forms)",
     "sin²x = (1−cos2x)/2"
    ]
   }
  ],
  "hi": [
   {
    "h": "रेडियन ⭐",
    "items": [
     "π rad = 180°",
     "30°=π/6, 45°=π/4, 60°=π/3",
     "चाप: l = rθ"
    ]
   },
   {
    "h": "इकाई वृत्त ⭐",
    "items": [
     "cos θ = x, sin θ = y",
     "ASTC चिह्न",
     "sin²θ + cos²θ = 1"
    ]
   },
   {
    "h": "सर्वसमिकाएं",
    "items": [
     "sin(−x)=−sin x; cos(−x)=cos x",
     "sin/cos आवर्त 2π; tan π",
     "sin(π/2−x) = cos x"
    ]
   },
   {
    "h": "योग/अंतर ⭐⭐",
    "items": [
     "cos(x+y): अंदर ऋण बाहर ऋण",
     "sin(x±y) = sin x cos y ± cos x sin y",
     "tan: (t₁+t₂)/(1−t₁t₂)"
    ]
   },
   {
    "h": "बहु-कोण ⭐",
    "items": [
     "sin 2x = 2sin x cos x",
     "cos 2x = 1−2sin²x",
     "sin²x = (1−cos2x)/2"
    ]
   }
  ],
  "en": [
   {
    "h": "Radians ⭐",
    "items": [
     "π rad = 180°",
     "30°=π/6, 45°=π/4, 60°=π/3",
     "Arc: l = rθ (radians only!)"
    ]
   },
   {
    "h": "Unit Circle ⭐",
    "items": [
     "cos θ = x, sin θ = y",
     "ASTC signs by quadrant",
     "sin²θ + cos²θ = 1"
    ]
   },
   {
    "h": "Identities",
    "items": [
     "sin(−x)=−sin x; cos(−x)=cos x",
     "sin/cos period 2π; tan π",
     "sin(π/2−x) = cos x"
    ]
   },
   {
    "h": "Sum/Diff ⭐⭐",
    "items": [
     "cos(x+y): minus in, minus out",
     "sin(x±y) = sin x cos y ± cos x sin y",
     "tan: (t₁+t₂)/(1−t₁t₂)"
    ]
   },
   {
    "h": "Multi-angles ⭐",
    "items": [
     "sin 2x = 2sin x cos x",
     "cos 2x = 1−2sin²x (3 forms)",
     "sin²x = (1−cos2x)/2"
    ]
   }
  ]
 },
 "practice": [
  [
   "45° ko radians me convert karo.",
   "45° × π/180 = <b>π/4</b> radian."
  ],
  [
   "7π/6 radians ko degrees me.",
   "7π/6 × 180/π = <b>210°</b>."
  ],
  [
   "sin(210°) ka value?",
   "210° = 180° + 30° → Q3 me sin negative → sin(210°) = −sin(30°) = <b>−1/2</b>."
  ],
  [
   "Kaunse quadrant me sin positive par cos negative?",
   "sin + aur cos − sirf <b>Q2</b> me (ASTC: Q2 = sirf Sin positive)."
  ],
  [
   "sin²θ + cos²θ = 1 se 1 + tan²θ kaise banta hai?",
   "Poori identity ko cos²θ se divide karo: sin²θ/cos²θ + 1 = 1/cos²θ → tan²θ + 1 = <b>sec²θ</b>."
  ],
  [
   "sin(x + y) ka expansion?",
   "sin(x + y) = <b>sin x cos y + cos x sin y</b> (sign same rehta hai)."
  ],
  [
   "cos 2x ke teen forms likho.",
   "cos 2x = <b>cos²x − sin²x = 2cos²x − 1 = 1 − 2sin²x</b>."
  ],
  [
   "sin 75° ka exact value? (Hint: 75 = 45 + 30)",
   "sin(45+30) = sin45cos30 + cos45sin30 = (1/√2)(√3/2) + (1/√2)(1/2) = <b>(√6 + √2)/4</b>."
  ],
  [
   "tan x ka period aur domain?",
   "Period = <b>π</b>; domain = R minus jahan cos x = 0, yani <b>x ≠ (2n+1)π/2</b>."
  ],
  [
   "5 cm radius wale circle me 2 radian angle ka arc length?",
   "l = rθ = 5×2 = <b>10 cm</b> (θ radian me diya hai, direct!)."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/maths/ch-4/",
  "title": "Complex Numbers and Quadratic Equations"
 }
}

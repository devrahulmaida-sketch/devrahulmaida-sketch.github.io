# Class 12 Maths, Chapter 8 - Application of Integrals
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 8,
 "title_en": "Application of Integrals",
 "title_hi": "समाकलनों के अनुप्रयोग",
 "tagline": "Curves ke neeche aur beech ka area — integral ko geometry me badalna",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 8: Application of Integrals — long + short notes in Hindi, English, Hinglish. Area under curves, area between curve and line, circle, ellipse, parabola areas by integration.",
 "video": None,
 "card_tag": "Curves ke neeche aur beech ka area — integral ko geometry me badalna",
 "card_topics": [
  "📐 Area = definite integral",
  "📊 Curve + line ke beech",
  "⭕ Circle/ellipse areas",
  "✏️ 5-marker strategy"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Area = Integral — Core Concept ⭐",
    "body": "<ul>\n<li><b>Basic idea:</b> curve y = f(x) ke NEECHE, x-axis ke saath, x = a se x = b tak ka area = <b>∫ₐᵇ f(x) dx</b> — definite integral hi area hai!</li>\n<li><b>Kyun kaam karta hai:</b> area ko patli-patli vertical strips (width dx, height f(x)) me todo — har strip ka area f(x)dx, sabka sum = integral.</li>\n<li><b>Axis ke NEECHE wala area ⭐:</b> integral NEGATIVE aata hai — area hamesha POSITIVE chahiye, to <b>|integral|</b> lo. Sign ka dhyan!</li>\n<li><b>y-axis ke saath area:</b> x = g(y) type curve ho to <b>∫cᵈ g(y) dy</b> — horizontal strips, y ke respect me integrate.</li>\n<li>Curve axis ko kaate to intervals todo — har piece ka area alag nikal ke POSITIVE values add karo.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: integral = lakhs of thin strips ka sum. Slice karo, add karo — yahi calculus ka area mantra hai.</p>"
   },
   {
    "h": "2️⃣ Simple Areas — Curve + Axis ⭐⭐",
    "body": "<ul>\n<li><b>Steps ⭐:</b> (1) Curve ka rough sketch banao (intersections dhundo!). (2) Limits fix karo (a, b). (3) ∫ₐᵇ f(x) dx evaluate karo. (4) Negative aaya to absolute value.</li>\n<li>Example: y = x², 0 se 2: area = ∫₀² x² dx = [x³/3]₀² = <b>8/3 sq units</b>.</li>\n<li><b>Line ke neeche ka area:</b> y = x, 0 se 1 → ∫₀¹ x dx = 1/2 — triangle (½·1·1 = 0.5 ✓) — geometry se verify ho jaata hai!</li>\n<li><b>Symmetric curves ⭐:</b> even function (y = x², y = cos x) ho to <b>2 × ∫₀ᵃ</b> — half area ka double. Kaam aadha!</li>\n<li>sin x ka 0 se π tak area = ∫₀^π sin x dx = [−cos x]₀^π = <b>2</b> (ek arch ka area 2 square units — classic result!).</li>\n</ul>\n<p class=\"small-note\">🎯 Sketch ZAROOR banao — bina figure ke limits galat padte hain. 1 minute ka sketch = full marks ka insurance.</p>"
   },
   {
    "h": "3️⃣ Do Curves / Curve aur Line Ke Beech Ka Area ⭐⭐",
    "body": "<ul>\n<li><b>Rule ⭐⭐:</b> area between = <b>∫ₐᵇ [UPPER curve − LOWER curve] dx</b> — upar wali minus neeche wali, integrate karo.</li>\n<li><b>Limits kahan se?</b> Dono curves ke <b>INTERSECTION POINTS</b> — equations barabar karke solve karo, wahi a aur b bante hain.</li>\n<li>Example: y = x² aur y = x: intersection x² = x → x = 0, 1. 0 se 1 me line upar: area = ∫₀¹ (x − x²) dx = [x²/2 − x³/3]₀¹ = <b>1/6</b>.</li>\n<li><b>Kaun upar? ⭐</b> Interval ka koi test point (jaise x = 0.5) dono me daal ke compare karo — sketch se bhi clear hota hai.</li>\n<li><b>Syllabus note ⭐:</b> rationalized NCERT me \"area between any two curves\" ka general case delete hua; boards me <b>curve + line</b> ya simple pairs (parabola-line, circle-line) aate hain — method same hai.</li>\n</ul>\n<p class=\"small-note\">💡 Upper minus lower = height of each strip. Intersection = strips ki shuruaat aur khatam hone ki jagah.</p>"
   },
   {
    "h": "4️⃣ Standard Curves Ke Areas — Circle, Parabola, Ellipse ⭐",
    "body": "<ul>\n<li><b>Circle x² + y² = a² ka area ⭐:</b> quadrant ka area × 4: 4∫₀ᵃ √(a² − x²) dx = 4·(πa²/4) = <b>πa²</b> — integration se πa² PROOF hota hai (favourite 5-marker!).</li>\n<li><b>Ellipse x²/a² + y²/b² = 1:</b> same method → area = <b>πab</b>. Circle hi special case (a = b)!</li>\n<li><b>Parabola y² = 4ax aur line x = b:</b> area = 2∫₀ᵇ √(4ax) dx (upar-neeche symmetric!) = (8/3)b√(ab) type.</li>\n<li><b>Parabola vs chord:</b> y² = 4ax aur y = mx ka bounded region — intersection points se limits, upper − lower.</li>\n<li>Symmetry ka FULL use karo: circle/ellipse me 4×, parabola me 2× — integration half ya quarter me khatam!</li>\n</ul>\n<p class=\"small-note\">🎯 Circle ka area integration se nikalna NCERT ka flagship example hai — steps ratt lo, exam me same aata hai.</p>"
   },
   {
    "h": "5️⃣ Exam Strategy aur Common Mistakes",
    "body": "<ul>\n<li><b>Fixed pattern:</b> boards me 5-marker — \"find the area bounded by...\" — sketch + intersection + integral + answer with sq units.</li>\n<li><b>Mistake 1:</b> intersection points solve kiye bina limits guess karna. <b>Mistake 2:</b> upper-lower ulta lena (negative area aa jaata hai!).</li>\n<li><b>Mistake 3:</b> symmetric region me multiply karna bhool jaana (2× ya 4×). <b>Mistake 4:</b> units na likhna.</li>\n<li><b>Check karna:</b> answer ka rough estimate geometry se karo (triangle/rectangle se compare) — negative ya absurd bada answer = kahin galti hai.</li>\n<li>Chapter chhota hai — integrals (Ch 7) strong hain to ye FREE marks hain. √(a² − x²) ka formula yaad rakho, circle problems usi pe chalte hain.</li>\n</ul>\n<p class=\"small-note\">💡 AOI = \"integral ko geometry me translate karna\". Ch 7 mehnat yahan double returns deti hai.</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ क्षेत्रफल = समाकलन — मूल अवधारणा ⭐",
    "body": "<ul>\n<li><b>मूल विचार:</b> वक्र y = f(x) के नीचे, x-अक्ष के साथ, x = a से b तक का क्षेत्रफल = <b>∫ₐᵇ f(x) dx</b>।</li>\n<li><b>क्यों:</b> क्षेत्रफल को पतली ऊर्ध्व पट्टियों (चौड़ाई dx, ऊंचाई f(x)) में बांटो — सबका योग = समाकलन।</li>\n<li><b>अक्ष के नीचे ⭐:</b> समाकलन ऋणात्मक आता है — क्षेत्रफल सदैव धनात्मक, तो <b>|समाकलन|</b> लो।</li>\n<li><b>y-अक्ष के साथ:</b> x = g(y) हो तो <b>∫cᵈ g(y) dy</b> — क्षैतिज पट्टियां।</li>\n<li>वक्र अक्ष काटे तो अंतराल बांटो — प्रत्येक भाग का धनात्मक क्षेत्रफल जोड़ो।</li>\n</ul>\n<p class=\"small-note\">💡 समाकलन = लाखों पतली पट्टियों का योग।</p>"
   },
   {
    "h": "2️⃣ सरल क्षेत्रफल — वक्र + अक्ष ⭐⭐",
    "body": "<ul>\n<li><b>चरण ⭐:</b> (1) रफ आरेख बनाओ। (2) सीमाएं तय करो। (3) ∫ₐᵇ f(x) dx निकालो। (4) ऋणात्मक आए तो निरपेक्ष मान।</li>\n<li>उदाहरण: y = x², 0 से 2: क्षेत्रफल = ∫₀² x² dx = [x³/3]₀² = <b>8/3 वर्ग इकाई</b>।</li>\n<li><b>सममित वक्र ⭐:</b> सम फलन हो तो <b>2 × ∫₀ᵃ</b> — आधा काम!</li>\n<li>sin x का 0 से π क्षेत्रफल = [−cos x]₀^π = <b>2</b> (क्लासिक परिणाम!)।</li>\n</ul>\n<p class=\"small-note\">🎯 आरेख अवश्य बनाओ — बिना आकृति के सीमाएं गलत पड़ती हैं।</p>"
   },
   {
    "h": "3️⃣ वक्र और रेखा के बीच का क्षेत्रफल ⭐⭐",
    "body": "<ul>\n<li><b>नियम ⭐⭐:</b> क्षेत्रफल = <b>∫ₐᵇ [ऊपरी वक्र − निचला वक्र] dx</b>।</li>\n<li><b>सीमाएं कहां से?</b> दोनों के <b>प्रतिच्छेदन बिंदुओं</b> से — समीकरण बराबर करके हल करो।</li>\n<li>उदाहरण: y = x² और y = x: प्रतिच्छेदन x = 0, 1। क्षेत्रफल = ∫₀¹ (x − x²) dx = <b>1/6</b>।</li>\n<li><b>कौन ऊपर? ⭐</b> अंतराल का परीक्षण बिंदु दोनों में रखकर तुलना करो।</li>\n<li><b>पाठ्यक्रम टिप्पणी ⭐:</b> \"किन्हीं दो वक्रों के बीच क्षेत्रफल\" का सामान्य रूप हटाया गया; बोर्ड में वक्र + रेखा आता है — विधि वही है।</li>\n</ul>\n<p class=\"small-note\">💡 ऊपर − नीचे = प्रत्येक पट्टी की ऊंचाई।</p>"
   },
   {
    "h": "4️⃣ मानक वक्रों के क्षेत्रफल — वृत्त, परवलय, दीर्घवृत्त ⭐",
    "body": "<ul>\n<li><b>वृत्त x² + y² = a² ⭐:</b> चतुर्थांश × 4: 4∫₀ᵃ √(a² − x²) dx = <b>πa²</b> — समाकलन से प्रमाण (प्रिय 5-अंकीय!)।</li>\n<li><b>दीर्घवृत्त x²/a² + y²/b² = 1:</b> क्षेत्रफल = <b>πab</b>।</li>\n<li><b>परवलय y² = 4ax और रेखा x = b:</b> क्षेत्रफल = 2∫₀ᵇ √(4ax) dx (सममिति!)।</li>\n<li>सममिति का पूरा उपयोग करो: वृत्त/दीर्घवृत्त में 4×, परवलय में 2×।</li>\n</ul>\n<p class=\"small-note\">🎯 समाकलन से वृत्त का क्षेत्रफल = NCERT का प्रमुख उदाहरण — चरण कंठस्थ करो।</p>"
   },
   {
    "h": "5️⃣ परीक्षा रणनीति और सामान्य गलतियां",
    "body": "<ul>\n<li><b>निश्चित पैटर्न:</b> बोर्ड में 5-अंकीय — आरेख + प्रतिच्छेदन + समाकलन + वर्ग इकाइयों में उत्तर।</li>\n<li><b>गलती 1:</b> प्रतिच्छेदन हल किए बिना सीमाएं अनुमान करना। <b>गलती 2:</b> ऊपर-नीचे उल्टा लेना।</li>\n<li><b>गलती 3:</b> सममिति का गुणक (2×/4×) भूलना। <b>गलती 4:</b> इकाइयां न लिखना।</li>\n<li><b>जांच:</b> ज्यामिति से मोटा अनुमान करो — ऋणात्मक उत्तर = कहीं गलती।</li>\n<li>अध्याय छोटा है — समाकलन (अध्याय 7) मजबूत हो तो ये मुफ्त अंक हैं।</li>\n</ul>\n<p class=\"small-note\">💡 AOI = \"समाकलन को ज्यामिति में बदलना\"।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Area = Integral — The Core Concept ⭐",
    "body": "<ul>\n<li><b>Basic idea:</b> the area UNDER the curve y = f(x), with the x-axis, from x = a to x = b is <b>∫ₐᵇ f(x) dx</b> — the definite integral IS the area!</li>\n<li><b>Why it works:</b> slice the area into thin vertical strips (width dx, height f(x)) — each strip has area f(x)dx, and their sum is the integral.</li>\n<li><b>Area BELOW the axis ⭐:</b> the integral comes out NEGATIVE — area must always be POSITIVE, so take <b>|integral|</b>. Watch the sign!</li>\n<li><b>Area with the y-axis:</b> for a curve of the form x = g(y), use <b>∫cᵈ g(y) dy</b> — horizontal strips, integrate in y.</li>\n<li>If the curve crosses the axis, split into intervals — compute each piece and add POSITIVE values.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: an integral is the sum of lakhs of thin strips. Slice it, add it — that is the calculus mantra for area.</p>"
   },
   {
    "h": "2️⃣ Simple Areas — Curve + Axis ⭐⭐",
    "body": "<ul>\n<li><b>Steps ⭐:</b> (1) Draw a rough sketch (find intersections!). (2) Fix the limits (a, b). (3) Evaluate ∫ₐᵇ f(x) dx. (4) Negative? Take the absolute value.</li>\n<li>Example: y = x² from 0 to 2: area = ∫₀² x² dx = [x³/3]₀² = <b>8/3 sq units</b>.</li>\n<li><b>Area under a line:</b> y = x from 0 to 1 → ∫₀¹ x dx = 1/2 — a triangle (½·1·1 = 0.5 ✓) — verifiable by geometry!</li>\n<li><b>Symmetric curves ⭐:</b> for an even function (y = x², y = cos x) use <b>2 × ∫₀ᵃ</b> — double the half. Half the work!</li>\n<li>Area under sin x from 0 to π = ∫₀^π sin x dx = [−cos x]₀^π = <b>2</b> (one arch = 2 square units — a classic!).</li>\n</ul>\n<p class=\"small-note\">🎯 ALWAYS sketch — without a figure, limits read wrong. A 1-minute sketch is insurance for full marks.</p>"
   },
   {
    "h": "3️⃣ Area Between a Curve and a Line ⭐⭐",
    "body": "<ul>\n<li><b>Rule ⭐⭐:</b> area between = <b>∫ₐᵇ [UPPER curve − LOWER curve] dx</b> — top minus bottom, then integrate.</li>\n<li><b>Where do limits come from?</b> The <b>INTERSECTION POINTS</b> of the two curves — set the equations equal and solve; those are a and b.</li>\n<li>Example: y = x² and y = x: intersection x² = x → x = 0, 1. From 0 to 1 the line is above: area = ∫₀¹ (x − x²) dx = [x²/2 − x³/3]₀¹ = <b>1/6</b>.</li>\n<li><b>Which is upper? ⭐</b> Plug any test point of the interval (like x = 0.5) into both and compare — the sketch also makes it clear.</li>\n<li><b>Syllabus note ⭐:</b> the general \"area between any two curves\" case is deleted in rationalized NCERT; boards ask <b>curve + line</b> or simple pairs (parabola-line, circle-line) — the method stays the same.</li>\n</ul>\n<p class=\"small-note\">💡 Upper minus lower = the height of each strip. Intersections = where the strips start and end.</p>"
   },
   {
    "h": "4️⃣ Areas of Standard Curves — Circle, Parabola, Ellipse ⭐",
    "body": "<ul>\n<li><b>Area of the circle x² + y² = a² ⭐:</b> quadrant area × 4: 4∫₀ᵃ √(a² − x²) dx = 4·(πa²/4) = <b>πa²</b> — integration PROVES πa² (a favourite 5-marker!).</li>\n<li><b>Ellipse x²/a² + y²/b² = 1:</b> same method → area = <b>πab</b>. The circle is the special case (a = b)!</li>\n<li><b>Parabola y² = 4ax with the line x = b:</b> area = 2∫₀ᵇ √(4ax) dx (symmetric above-below!) = (8/3)b√(ab) type.</li>\n<li><b>Parabola vs chord:</b> the region bounded by y² = 4ax and y = mx — limits from intersection points, upper − lower.</li>\n<li>Use symmetry FULLY: 4× for circles/ellipses, 2× for parabolas — the integration finishes in a half or a quarter!</li>\n</ul>\n<p class=\"small-note\">🎯 Finding the circle's area by integration is NCERT's flagship example — memorize the steps; the exam repeats it.</p>"
   },
   {
    "h": "5️⃣ Exam Strategy and Common Mistakes",
    "body": "<ul>\n<li><b>Fixed pattern:</b> a 5-marker in boards — \"find the area bounded by...\" — sketch + intersections + integral + answer in sq units.</li>\n<li><b>Mistake 1:</b> guessing limits without solving intersections. <b>Mistake 2:</b> swapping upper-lower (you get a negative area!).</li>\n<li><b>Mistake 3:</b> forgetting the symmetry multiplier (2× or 4×). <b>Mistake 4:</b> skipping units.</li>\n<li><b>How to check:</b> estimate the answer roughly from geometry (compare with a triangle/rectangle) — a negative or absurdly large answer means an error somewhere.</li>\n<li>A small chapter — if integrals (Ch 7) are strong, these are FREE marks. Keep the √(a² − x²) formula ready; circle problems run on it.</li>\n</ul>\n<p class=\"small-note\">💡 AOI = \"translating integrals into geometry\". The effort of Ch 7 pays double here.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Concept ⭐",
    "items": [
     "Area = ∫ₐᵇ f(x) dx",
     "Strips ka sum = integral",
     "Negative integral → |value|"
    ]
   },
   {
    "h": "Simple areas ⭐",
    "items": [
     "Sketch → limits → integrate",
     "Even function: 2 × half",
     "sin x, 0-π ka area = 2"
    ]
   },
   {
    "h": "Between curves ⭐⭐",
    "items": [
     "∫(upper − lower) dx",
     "Limits = intersection points",
     "Test point se upar/neeche check"
    ]
   },
   {
    "h": "Standard ⭐",
    "items": [
     "Circle: πa² (4× quadrant)",
     "Ellipse: πab",
     "Parabola: symmetry 2× use karo"
    ]
   },
   {
    "h": "Exam tips",
    "items": [
     "5-marker fixed pattern",
     "Units likho (sq units)",
     "Area between 2 curves ka general case DELETED"
    ]
   }
  ],
  "hi": [
   {
    "h": "अवधारणा ⭐",
    "items": [
     "क्षेत्रफल = ∫ₐᵇ f(x) dx",
     "पट्टियों का योग = समाकलन",
     "ऋणात्मक → |मान|"
    ]
   },
   {
    "h": "सरल क्षेत्रफल ⭐",
    "items": [
     "आरेख → सीमाएं → समाकलन",
     "सम फलन: 2 × आधा",
     "sin x, 0-π = 2"
    ]
   },
   {
    "h": "वक्रों के बीच ⭐⭐",
    "items": [
     "∫(ऊपरी − निचला) dx",
     "सीमाएं = प्रतिच्छेदन बिंदु",
     "परीक्षण बिंदु से जांच"
    ]
   },
   {
    "h": "मानक ⭐",
    "items": [
     "वृत्त: πa² (4× चतुर्थांश)",
     "दीर्घवृत्त: πab",
     "परवलय: सममिति 2×"
    ]
   },
   {
    "h": "परीक्षा",
    "items": [
     "5-अंकीय निश्चित पैटर्न",
     "वर्ग इकाइयां लिखो",
     "दो वक्रों का सामान्य रूप हटाया गया"
    ]
   }
  ],
  "en": [
   {
    "h": "Concept ⭐",
    "items": [
     "Area = ∫ₐᵇ f(x) dx",
     "Sum of strips = integral",
     "Negative integral → |value|"
    ]
   },
   {
    "h": "Simple areas ⭐",
    "items": [
     "Sketch → limits → integrate",
     "Even function: 2 × half",
     "Area under sin x, 0-π = 2"
    ]
   },
   {
    "h": "Between curves ⭐⭐",
    "items": [
     "∫(upper − lower) dx",
     "Limits = intersection points",
     "Use a test point for up/down"
    ]
   },
   {
    "h": "Standard ⭐",
    "items": [
     "Circle: πa² (4× quadrant)",
     "Ellipse: πab",
     "Parabola: use 2× symmetry"
    ]
   },
   {
    "h": "Exam tips",
    "items": [
     "Fixed 5-marker pattern",
     "Write units (sq units)",
     "General two-curve case DELETED"
    ]
   }
  ]
 },
 "practice": [
  [
   "y = x² ke neeche 0 se 3 tak ka area?",
   "∫₀³ x² dx = [x³/3]₀³ = 27/3 = <b>9 sq units</b>."
  ],
  [
   "Curve x-axis ke neeche ho to area kaise nikalein?",
   "Integral negative aayega — <b>|∫ f(x) dx|</b> lo, area hamesha positive hota hai."
  ],
  [
   "y = x² aur y = x ke beech ka area (0 se 1)?",
   "∫₀¹ (x − x²) dx = 1/2 − 1/3 = <b>1/6</b>."
  ],
  [
   "Do curves ke beech area ke liye limits kahan se aati hain?",
   "<b>Intersection points</b> se — dono equations barabar karke solve karo."
  ],
  [
   "x² + y² = a² wale circle ka area integration se?",
   "4∫₀ᵃ √(a² − x²) dx = 4 × (πa²/4) = <b>πa²</b>."
  ],
  [
   "Ellipse x²/a² + y²/b² = 1 ka area?",
   "<b>πab</b> — circle ka general version."
  ],
  [
   "∫₀^π sin x dx ka value?",
   "[−cos x]₀^π = −(−1) − (−1) = <b>2</b> — ek arch ka area."
  ],
  [
   "Even function ka −a se a area ka shortcut?",
   "<b>2∫₀ᵃ f(x) dx</b> — aadha nikalo, double karo."
  ],
  [
   "y² = 4x aur x = 1 se bana area?",
   "2∫₀¹ 2√x dx = 4·[x^(3/2)/(3/2)]₀¹ = <b>8/3</b> sq units (symmetry use ki!)."
  ],
  [
   "Area ka answer negative aa jaaye to kya matlab?",
   "<b>Upper-lower ulta liya hai</b> ya curve axis ke neeche hai — absolute value lo, limits/curve order dobara check karo."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-9/",
  "title": "Differential Equations"
 }
}

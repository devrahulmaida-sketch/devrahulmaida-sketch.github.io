# Class 12 Maths, Chapter 6 - Application of Derivatives
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 6,
 "title_en": "Application of Derivatives",
 "title_hi": "अवकलजों के अनुप्रयोग",
 "tagline": "Rate of change, increasing-decreasing aur maxima-minima ke word problems",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 6: Application of Derivatives — long + short notes in Hindi, English, Hinglish. Rate of change, increasing and decreasing functions, maxima and minima, word problems.",
 "video": None,
 "card_tag": "Rate of change, increasing-decreasing aur maxima-minima ke word problems",
 "card_topics": [
  "⏱️ Rate of change problems",
  "📈 Increasing/decreasing",
  "⛰️ Maxima & minima tests",
  "📝 Word problems (5-markers)"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Rate of Change — Derivative Ka Asli Matlab ⭐",
    "body": "<ul>\n<li><b>Core idea:</b> dy/dx = <b>y ki change rate x ke respect me</b>. Physics me: velocity = dx/dt, acceleration = dv/dt.</li>\n<li><b>Rate of change problems ⭐:</b> (1) Jo quantity change ho rahi hai uska relation likho (jaise circle ka area A = πr²). (2) Dono taraf TIME ke respect me differentiate karo: dA/dt = 2πr·dr/dt. (3) Given values daal ke unknown rate nikalo.</li>\n<li>Example: balloon ka radius 2 cm/s se badh raha hai, r = 10 pe dA/dt = 2π(10)(2) = <b>40π cm²/s</b>.</li>\n<li><b>Dhyaan:</b> rate NEGATIVE bhi ho sakti hai — matlab quantity GHAT rahi hai (leak, cooling, shrinking).</li>\n<li>Units hamesha likho — cm/s, m²/s — examiner marks deta hai units pe bhi!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: derivative = speedometer. Position batata hai function, SPEED batata hai derivative!</p>"
   },
   {
    "h": "2️⃣ Increasing aur Decreasing Functions ⭐⭐",
    "body": "<ul>\n<li><b>Test ⭐⭐:</b> interval me <b>f′(x) &gt; 0 → strictly increasing</b>; <b>f′(x) &lt; 0 → strictly decreasing</b>. Slope positive = graph upar ja raha; negative = neeche.</li>\n<li><b>Method:</b> (1) f′(x) nikalo. (2) f′(x) = 0 ke points (critical points) se number line todo. (3) Har interval me f′(x) ka SIGN check karo.</li>\n<li>Example: f(x) = x² − 4x + 3 → f′(x) = 2x − 4. x &lt; 2: f′ &lt; 0 (decreasing); x &gt; 2: f′ &gt; 0 (increasing).</li>\n<li><b>Quadratic yaad rakhne ka trick:</b> upward parabola vertex ke PEHLE decreasing, BAAD me increasing.</li>\n<li>Log/trig wale functions me bhi same sign-analysis chalta hai — bas f′ sahi nikalna aana chahiye!</li>\n</ul>\n<p class=\"small-note\">🎯 Sign chart banao: critical points pe vertical lines, har zone me + ya −. Yehi 4-marker ka framework hai.</p>"
   },
   {
    "h": "3️⃣ Maxima aur Minima — Peaks aur Valleys ⭐⭐",
    "body": "<ul>\n<li><b>Critical points:</b> jahan f′(x) = 0 ya f′(x) exist NAHI karta — yahi maxima/minima ke candidates hain.</li>\n<li><b>First derivative test:</b> f′ ka sign + se − ho jaaye → <b>local MAXIMUM</b>; − se + ho jaaye → <b>local MINIMUM</b>. Sign change nahi hua (point of inflection type) → na max na min.</li>\n<li><b>Second derivative test ⭐⭐:</b> critical point c pe: f″(c) &lt; 0 → <b>local max</b>; f″(c) &gt; 0 → <b>local min</b>; f″(c) = 0 → test FAIL, first derivative test lagao.</li>\n<li><b>Local vs Absolute:</b> local = apne neighbourhood ka best; absolute (global) = POORE domain/interval ka best. Closed interval [a, b] me absolute max/min ke liye critical points AUR endpoints (a, b) dono check karo! ⭐</li>\n<li>Turning point = wo point jahan graph direction badalta hai (max ya min).</li>\n</ul>\n<p class=\"small-note\">💡 Pahad socho: top pe slope 0 (max), ghati ke bottom pe slope 0 (min). Second derivative batata hai upar-muh (min) ya neeche-muh (max) katora hai.</p>"
   },
   {
    "h": "4️⃣ Maxima/Minima Ke Word Problems ⭐⭐",
    "body": "<ul>\n<li><b>Strategy:</b> (1) Jo maximize/minimize karna hai usko ek variable ke function me likho (constraint use karke). (2) f′ = 0 solve karo. (3) Second derivative se confirm karo max ya min. (4) Answer units ke saath!</li>\n<li><b>Classic 1 ⭐:</b> Fixed perimeter me MAXIMUM area ka rectangle = <b>SQUARE</b> hamesha!</li>\n<li><b>Classic 2:</b> Fixed sum (x + y = k) me product xy maximum jab <b>x = y = k/2</b>.</li>\n<li><b>Classic 3:</b> Minimum surface area / maximum volume wale box-cylinder problems — constraint se h eliminate karo, phir differentiate.</li>\n<li><b>Classic 4:</b> Number ka square minimum / two parts ka product maximum type NCERT exercises — same pattern.</li>\n<li>Ye problems 5-markers hain — steps likhne pe marks milte hain, sirf answer pe nahi!</li>\n</ul>\n<p class=\"small-note\">🎯 80% word problems me ek hi move kaam aata hai: constraint se ek variable hatao → single-variable calculus.</p>"
   },
   {
    "h": "5️⃣ Syllabus Note aur Exam Weightage",
    "body": "<ul>\n<li><b>Rationalized syllabus ⭐:</b> <b>tangents &amp; normals</b> (equations nikalna) aur <b>approximations (differentials se)</b> NCERT/CBSE se <b>DELETE</b> ho chuke hain — ab chapter ke 3 pillars: rate of change, increasing/decreasing, maxima/minima.</li>\n<li><b>Weightage:</b> Calculus unit (Ch 5-9) boards me ~35 marks — AOD se pakka 5-marker word problem aata hai.</li>\n<li><b>Common mistakes:</b> second derivative test bhool jaana; closed interval me endpoints check na karna; constraint eliminate kiye bina differentiate kar dena.</li>\n<li>JEE me isi chapter se tangent-normal, monotonicity, maxima-minima sab aate hain — concepts yahan strong karo to aage kaam aayenge.</li>\n<li>Graph sochna sikh lo: f′ ka sign chart dimag me ban jaaye to 90% questions visual ho jaate hain.</li>\n</ul>\n<p class=\"small-note\">💡 AOD = derivative ki \"job interview\" — theory chhoti, applications badi. Word problems ki practice hi asli tayari hai.</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ परिवर्तन दर — अवकलज का असली अर्थ ⭐",
    "body": "<ul>\n<li><b>मूल विचार:</b> dy/dx = <b>x के सापेक्ष y की परिवर्तन दर</b>। भौतिकी में: वेग = dx/dt, त्वरण = dv/dt।</li>\n<li><b>दर वाले प्रश्न ⭐:</b> (1) राशियों का संबंध लिखो (A = πr²)। (2) दोनों ओर <b>समय</b> के सापेक्ष अवकलन: dA/dt = 2πr·dr/dt। (3) मान रखकर अज्ञात दर निकालो।</li>\n<li>उदाहरण: त्रिज्या 2 cm/s से बढ़ रही है, r = 10 पर dA/dt = 2π(10)(2) = <b>40π cm²/s</b>।</li>\n<li><b>ध्यान दो:</b> दर ऋणात्मक भी हो सकती है — राशि <b>घट</b> रही है।</li>\n<li>इकाइयां अवश्य लिखो — cm/s, m²/s!</li>\n</ul>\n<p class=\"small-note\">💡 अवकलज = स्पीडोमीटर। स्थिति फलन बताता है, गति अवकलज!</p>"
   },
   {
    "h": "2️⃣ वर्धमान और ह्रासमान फलन ⭐⭐",
    "body": "<ul>\n<li><b>परीक्षण ⭐⭐:</b> अंतराल में <b>f′(x) &gt; 0 → वर्धमान</b>; <b>f′(x) &lt; 0 → ह्रासमान</b>।</li>\n<li><b>विधि:</b> (1) f′(x) निकालो। (2) f′(x) = 0 के बिंदुओं से संख्या रेखा बांटो। (3) प्रत्येक अंतराल में f′ का <b>चिह्न</b> जांचो।</li>\n<li>उदाहरण: f(x) = x² − 4x + 3 → f′(x) = 2x − 4। x &lt; 2: ह्रासमान; x &gt; 2: वर्धमान।</li>\n<li><b>द्विघात ट्रिक:</b> ऊपर-मुंह परवलय शीर्ष से पहले ह्रासमान, बाद में वर्धमान।</li>\n</ul>\n<p class=\"small-note\">🎯 चिह्न चार्ट बनाओ — यही 4-अंकीय प्रश्न का ढांचा है।</p>"
   },
   {
    "h": "3️⃣ उच्चिष्ठ और निम्निष्ठ — चोटियां और घाटियां ⭐⭐",
    "body": "<ul>\n<li><b>क्रांतिक बिंदु:</b> जहां f′(x) = 0 या f′(x) मौजूद नहीं — यही उच्चिष्ठ/निम्निष्ठ के उम्मीदवार।</li>\n<li><b>प्रथम अवकलज परीक्षण:</b> f′ का चिह्न + से − → <b>स्थानीय उच्चिष्ठ</b>; − से + → <b>स्थानीय निम्निष्ठ</b>।</li>\n<li><b>द्वितीय अवकलज परीक्षण ⭐⭐:</b> क्रांतिक बिंदु c पर: f″(c) &lt; 0 → <b>उच्चिष्ठ</b>; f″(c) &gt; 0 → <b>निम्निष्ठ</b>; f″(c) = 0 → परीक्षण विफल!</li>\n<li><b>स्थानीय बनाम निरपेक्ष:</b> बंद अंतराल [a, b] में निरपेक्ष उच्च/निम्न के लिए क्रांतिक बिंदु <b>और</b> सीमा बिंदु (a, b) दोनों जांचो! ⭐</li>\n</ul>\n<p class=\"small-note\">💡 पहाड़ सोचो: चोटी पर ढलान 0 (उच्चिष्ठ), घाटी में 0 (निम्निष्ठ)।</p>"
   },
   {
    "h": "4️⃣ उच्चिष्ठ/निम्निष्ठ के शाब्दिक प्रश्न ⭐⭐",
    "body": "<ul>\n<li><b>रणनीति:</b> (1) अधिकतम/न्यूनतम राशि को एक चर के फलन में लिखो (बंधन से)। (2) f′ = 0 हल करो। (3) द्वितीय अवकलज से पुष्टि। (4) इकाइयों सहित उत्तर!</li>\n<li><b>क्लासिक 1 ⭐:</b> निश्चित परिमाप में अधिकतम क्षेत्रफल वाला आयत = <b>वर्ग</b>!</li>\n<li><b>क्लासिक 2:</b> निश्चित योग (x + y = k) में गुणनफल xy अधिकतम जब <b>x = y = k/2</b>।</li>\n<li><b>क्लासिक 3:</b> न्यूनतम पृष्ठ-क्षेत्रफल / अधिकतम आयतन वाले बक्से-बेलन प्रश्न — बंधन से h हटाओ, फिर अवकलन।</li>\n<li>ये 5-अंकीय हैं — चरणों पर अंक मिलते हैं!</li>\n</ul>\n<p class=\"small-note\">🎯 80% प्रश्नों में एक ही चाल: बंधन से एक चर हटाओ → एक-चर कलन।</p>"
   },
   {
    "h": "5️⃣ पाठ्यक्रम टिप्पणी और परीक्षा महत्व",
    "body": "<ul>\n<li><b>युक्तिसंगत पाठ्यक्रम ⭐:</b> <b>स्पर्शरेखाएं और अभिलंब</b> तथा <b>सन्निकटन (differentials)</b> NCERT/CBSE से <b>हटाए गए</b> — अब 3 स्तंभ: परिवर्तन दर, वर्धमान/ह्रासमान, उच्चिष्ठ/निम्निष्ठ।</li>\n<li><b>महत्व:</b> कलन इकाई (अध्याय 5-9) बोर्ड में ~35 अंक — AOD से 5-अंकीय शाब्दिक प्रश्न पक्का।</li>\n<li><b>सामान्य गलतियां:</b> द्वितीय अवकलज परीक्षण भूलना; सीमा बिंदु न जांचना; बंधन हटाए बिना अवकलन।</li>\n<li>JEE में स्पर्शरेखा-अभिलंब, एकदिष्टता, उच्च-निम्न सब आते हैं — अवधारणाएं यहां मजबूत करो।</li>\n</ul>\n<p class=\"small-note\">💡 AOD = अवकलज की \"नौकरी की इंटरव्यू\" — शाब्दिक प्रश्नों का अभ्यास ही असली तैयारी।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Rate of Change — What a Derivative Really Means ⭐",
    "body": "<ul>\n<li><b>Core idea:</b> dy/dx = <b>the rate of change of y with respect to x</b>. In physics: velocity = dx/dt, acceleration = dv/dt.</li>\n<li><b>Rate problems ⭐:</b> (1) Write the relation between the changing quantities (like a circle's area A = πr²). (2) Differentiate both sides with respect to TIME: dA/dt = 2πr·dr/dt. (3) Plug in the given values and solve for the unknown rate.</li>\n<li>Example: a balloon's radius grows at 2 cm/s; at r = 10, dA/dt = 2π(10)(2) = <b>40π cm²/s</b>.</li>\n<li><b>Note:</b> a rate can be NEGATIVE — it means the quantity is DECREASING (leak, cooling, shrinking).</li>\n<li>Always write units — cm/s, m²/s — examiners award marks for units too!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: the derivative is a speedometer. The function tells position, the derivative tells SPEED!</p>"
   },
   {
    "h": "2️⃣ Increasing and Decreasing Functions ⭐⭐",
    "body": "<ul>\n<li><b>Test ⭐⭐:</b> on an interval, <b>f′(x) &gt; 0 → strictly increasing</b>; <b>f′(x) &lt; 0 → strictly decreasing</b>. Positive slope = graph climbing; negative = falling.</li>\n<li><b>Method:</b> (1) Find f′(x). (2) Split the number line at the critical points (where f′(x) = 0). (3) Check the SIGN of f′(x) in each interval.</li>\n<li>Example: f(x) = x² − 4x + 3 → f′(x) = 2x − 4. x &lt; 2: f′ &lt; 0 (decreasing); x &gt; 2: f′ &gt; 0 (increasing).</li>\n<li><b>Quadratic trick:</b> an upward parabola is decreasing BEFORE the vertex, increasing AFTER it.</li>\n<li>Log/trig functions follow the same sign analysis — you just need f′ computed correctly!</li>\n</ul>\n<p class=\"small-note\">🎯 Build a sign chart: vertical lines at critical points, + or − in each zone. This is the 4-marker framework.</p>"
   },
   {
    "h": "3️⃣ Maxima and Minima — Peaks and Valleys ⭐⭐",
    "body": "<ul>\n<li><b>Critical points:</b> where f′(x) = 0 or f′(x) does NOT exist — these are the candidates for maxima/minima.</li>\n<li><b>First derivative test:</b> f′ changes sign + to − → <b>local MAXIMUM</b>; − to + → <b>local MINIMUM</b>. No sign change → neither (inflection-type point).</li>\n<li><b>Second derivative test ⭐⭐:</b> at a critical point c: f″(c) &lt; 0 → <b>local max</b>; f″(c) &gt; 0 → <b>local min</b>; f″(c) = 0 → test FAILS, use the first derivative test.</li>\n<li><b>Local vs Absolute:</b> local = best in its neighbourhood; absolute (global) = best over the WHOLE domain/interval. On a closed interval [a, b] check critical points AND the endpoints (a, b) for absolute max/min! ⭐</li>\n<li>Turning point = where the graph changes direction (a max or a min).</li>\n</ul>\n<p class=\"small-note\">💡 Picture a mountain: at the top the slope is 0 (max), at the valley bottom it is 0 (min). The second derivative tells whether the bowl faces up (min) or down (max).</p>"
   },
   {
    "h": "4️⃣ Maxima/Minima Word Problems ⭐⭐",
    "body": "<ul>\n<li><b>Strategy:</b> (1) Write the quantity to maximize/minimize as a function of ONE variable (use the constraint). (2) Solve f′ = 0. (3) Confirm max or min with the second derivative. (4) Answer with units!</li>\n<li><b>Classic 1 ⭐:</b> the rectangle of MAXIMUM area for a fixed perimeter is always a <b>SQUARE</b>!</li>\n<li><b>Classic 2:</b> for a fixed sum (x + y = k), the product xy is maximum when <b>x = y = k/2</b>.</li>\n<li><b>Classic 3:</b> minimum surface area / maximum volume box-and-cylinder problems — eliminate h using the constraint, then differentiate.</li>\n<li><b>Classic 4:</b> NCERT exercises on minimum squares / maximum products of two parts — same pattern.</li>\n<li>These are 5-markers — marks come for the STEPS, not just the final answer!</li>\n</ul>\n<p class=\"small-note\">🎯 One move solves 80% of word problems: eliminate a variable using the constraint → single-variable calculus.</p>"
   },
   {
    "h": "5️⃣ Syllabus Note and Exam Weightage",
    "body": "<ul>\n<li><b>Rationalized syllabus ⭐:</b> <b>tangents &amp; normals</b> (finding their equations) and <b>approximations (via differentials)</b> are <b>DELETED</b> from NCERT/CBSE — the chapter now has 3 pillars: rate of change, increasing/decreasing, maxima/minima.</li>\n<li><b>Weightage:</b> the Calculus unit (Ch 5-9) carries ~35 marks in boards — a 5-marker AOD word problem is guaranteed.</li>\n<li><b>Common mistakes:</b> forgetting the second derivative test; not checking endpoints on a closed interval; differentiating without eliminating the constraint.</li>\n<li>For JEE this chapter feeds tangent-normal, monotonicity, and maxima-minima questions — strong concepts here pay off later.</li>\n<li>Learn to picture the graph: once the sign chart of f′ forms in your head, 90% of questions turn visual.</li>\n</ul>\n<p class=\"small-note\">💡 AOD is the derivative's \"job interview\" — small theory, big applications. Practising word problems is the real preparation.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Rate of change ⭐",
    "items": [
     "dy/dx = y ki rate x me",
     "Relation likho → t me differentiate",
     "Negative rate = quantity ghat rahi"
    ]
   },
   {
    "h": "Inc/Dec ⭐⭐",
    "items": [
     "f′ > 0 → increasing",
     "f′ &lt; 0 → decreasing",
     "Critical points se sign chart"
    ]
   },
   {
    "h": "Max/Min ⭐⭐",
    "items": [
     "f′ = 0 → candidates",
     "f″ &lt; 0 → max; f″ > 0 → min",
     "+ se − sign change → max"
    ]
   },
   {
    "h": "Absolute ⭐",
    "items": [
     "Closed interval: critical + endpoints",
     "Local ≠ global",
     "f″ = 0 → first derivative test"
    ]
   },
   {
    "h": "Syllabus ⭐",
    "items": [
     "Tangents/normals DELETED",
     "Approximations DELETED",
     "3 pillars: rate, inc/dec, max-min"
    ]
   }
  ],
  "hi": [
   {
    "h": "परिवर्तन दर ⭐",
    "items": [
     "dy/dx = y की दर x में",
     "संबंध → t में अवकलन",
     "ऋणात्मक दर = राशि घट रही"
    ]
   },
   {
    "h": "वर्धमान/ह्रासमान ⭐⭐",
    "items": [
     "f′ > 0 → वर्धमान",
     "f′ &lt; 0 → ह्रासमान",
     "क्रांतिक बिंदुओं से चिह्न चार्ट"
    ]
   },
   {
    "h": "उच्च/निम्न ⭐⭐",
    "items": [
     "f′ = 0 → उम्मीदवार",
     "f″ &lt; 0 → उच्चिष्ठ; f″ > 0 → निम्निष्ठ",
     "+ से − चिह्न बदलाव → उच्चिष्ठ"
    ]
   },
   {
    "h": "निरपेक्ष ⭐",
    "items": [
     "बंद अंतराल: क्रांतिक + सीमा बिंदु",
     "स्थानीय ≠ निरपेक्ष",
     "f″ = 0 → प्रथम अवकलज परीक्षण"
    ]
   },
   {
    "h": "पाठ्यक्रम ⭐",
    "items": [
     "स्पर्शरेखा/अभिलंब हटाए गए",
     "सन्निकटन हटाया गया",
     "3 स्तंभ: दर, वर्ध/ह्रास, उच्च-निम्न"
    ]
   }
  ],
  "en": [
   {
    "h": "Rate of change ⭐",
    "items": [
     "dy/dx = rate of y w.r.t. x",
     "Write relation → differentiate in t",
     "Negative rate = quantity decreasing"
    ]
   },
   {
    "h": "Inc/Dec ⭐⭐",
    "items": [
     "f′ > 0 → increasing",
     "f′ &lt; 0 → decreasing",
     "Sign chart from critical points"
    ]
   },
   {
    "h": "Max/Min ⭐⭐",
    "items": [
     "f′ = 0 → candidates",
     "f″ &lt; 0 → max; f″ > 0 → min",
     "+ to − sign change → max"
    ]
   },
   {
    "h": "Absolute ⭐",
    "items": [
     "Closed interval: critical + endpoints",
     "Local ≠ global",
     "f″ = 0 → first derivative test"
    ]
   },
   {
    "h": "Syllabus ⭐",
    "items": [
     "Tangents/normals DELETED",
     "Approximations DELETED",
     "3 pillars: rate, inc/dec, max-min"
    ]
   }
  ]
 },
 "practice": [
  [
   "dy/dx ka physical matlab kya hai?",
   "<b>y ki parivartan dar x ke sapeksh</b> — jaise velocity position ki rate hai time me."
  ],
  [
   "Circle ka radius 3 cm/s se badh raha hai. r = 5 pe area ki rate?",
   "A = πr² → dA/dt = 2πr·dr/dt = 2π(5)(3) = <b>30π cm²/s</b>."
  ],
  [
   "f′(x) &lt; 0 poore interval me ho to function kaisa hai?",
   "<b>Strictly decreasing</b> — slope negative, graph neeche utar raha hai."
  ],
  [
   "f(x) = x² − 6x + 5 kab decreasing hai?",
   "f′(x) = 2x − 6 &lt; 0 jab x &lt; 3 → <b>(−∞, 3) me decreasing</b>."
  ],
  [
   "Critical point pe f″(c) > 0 ho to kya hai?",
   "<b>Local minimum</b> — upar-muh katora shape."
  ],
  [
   "f″(c) = 0 aa jaaye to kya karein?",
   "Second derivative test <b>fail</b> — <b>first derivative test</b> (sign change) lagao."
  ],
  [
   "x + y = 20 ho to xy kab maximum?",
   "Jab <b>x = y = 10</b> — product 100. Fixed sum me barabar parts ka product max!"
  ],
  [
   "Closed interval [a, b] pe absolute maximum kaise dhundein?",
   "Critical points + <b>endpoints a, b</b> — sab pe f ka value compare karo, sabse bada = absolute max."
  ],
  [
   "Fixed perimeter me maximum area wala rectangle kaunsa?",
   "<b>Square</b> — hamesha! Length = breadth."
  ],
  [
   "Tangents aur normals ke questions ab bhi boards me aate hain?",
   "<b>Nahi</b> — tangents/normals aur approximations rationalized syllabus se <b>delete</b> ho chuke hain."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-7/",
  "title": "Integrals"
 }
}

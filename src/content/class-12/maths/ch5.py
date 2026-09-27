# Class 12 Maths, Chapter 5 - Continuity and Differentiability
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 5,
 "title_en": "Continuity and Differentiability",
 "title_hi": "संतत्य तथा अवकलनीयता",
 "tagline": "LHL-RHL se lekar chain rule aur second derivatives tak — calculus ka engine",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 5: Continuity and Differentiability — long + short notes in Hindi, English, Hinglish. Continuity, differentiability, chain rule, implicit, logarithmic, parametric differentiation, second order derivatives.",
 "video": None,
 "card_tag": "LHL-RHL se lekar chain rule aur second derivatives tak — calculus ka engine",
 "card_topics": [
  "📈 Continuity (LHL = RHL)",
  "📐 Differentiability rules",
  "⛓️ Chain + implicit + log diff",
  "📊 Second order derivatives"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Continuity — Bina Break Ka Function ⭐⭐",
    "body": "<ul>\n<li><b>Intuition:</b> graph bina pen uthaye ban jaaye to function continuous hai — koi jump, hole ya break nahi.</li>\n<li><b>Definition ⭐⭐:</b> f, x = a pe <b>continuous</b> hai agar <b>lim(x→a) f(x) = f(a)</b> — limit ka value = function ka value. Teen cheezein chahiye: limit EXISTS, f(a) DEFINED, dono EQUAL.</li>\n<li><b>LHL = RHL check ⭐:</b> limit exist karne ke liye Left Hand Limit = Right Hand Limit hona chahiye. Dono nikalo, compare karo!</li>\n<li>Example: f(x) = |x| at x = 0: LHL = RHL = 0 = f(0) → <b>continuous</b>. (Par differentiable nahi — aage dekho!)</li>\n<li>Polynomials, sin x, cos x, eˣ HAR JAGAH continuous hain — ye standard results free me use karo.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: continuous = road bina speed-breaker. Pen uthaana pada to wahan discontinuity hai!</p>"
   },
   {
    "h": "2️⃣ Discontinuity Ke Types aur Continuous Functions Ka Algebra",
    "body": "<ul>\n<li><b>Jump discontinuity:</b> LHL ≠ RHL — graph ek level se doosre pe \"kood\" jaata hai (greatest integer function [x] har integer pe!).</li>\n<li><b>Missing point:</b> limit exists par f(a) defined nahi ya alag — graph me ek chhota hole.</li>\n<li><b>Infinite discontinuity:</b> function point ke paas ±∞ ko udd jaata hai (1/x at x = 0).</li>\n<li><b>Algebra ⭐:</b> continuous functions ka sum, difference, product, scalar multiple sab continuous. Quotient bhi — jahan denominator ≠ 0.</li>\n<li><b>Composite:</b> g continuous at a + f continuous at g(a) → fog continuous at a.</li>\n<li>Interval pe continuous = us interval ke HAR point pe continuous.</li>\n</ul>\n<p class=\"small-note\">🎯 [x] (greatest integer) har integer pe discontinuous; {x} (fractional part) bhi. Boards ka favourite example!</p>"
   },
   {
    "h": "3️⃣ Differentiability — Slope Har Jagah ⭐⭐",
    "body": "<ul>\n<li><b>Definition ⭐:</b> f′(a) = lim(h→0) [f(a+h) − f(a)]/h — ye limit EXIST kare to f, a pe differentiable hai. Matlab us point pe unique tangent/slope hai.</li>\n<li><b>Differentiable ⟹ Continuous ⭐⭐:</b> differentiable hai to continuous ZAROOR hai. Par ULTA TRUE NAHI — continuous hai to differentiable ho, ye guarantee nahi!</li>\n<li><b>|x| at x = 0 ⭐:</b> continuous HAI (LHL = RHL = 0), par differentiable NAHI — left slope −1, right slope +1, dono alag → sharp corner!</li>\n<li>Corner, cusp, vertical tangent ya break — in sab points pe differentiability fail hoti hai.</li>\n<li>Standard: polynomials, sin x, cos x, eˣ har jagah differentiable. |x|, [x] apne break/corner points pe nahi.</li>\n</ul>\n<p class=\"small-note\">🎯 Yaad rakhne ka flow: Differentiable → Continuous → (ulta galat!). |x| at 0 = classic counterexample, exam me pakka aata hai.</p>"
   },
   {
    "h": "4️⃣ Differentiation Ke Rules — Chain, Implicit, Log ⭐⭐",
    "body": "<ul>\n<li><b>Chain rule ⭐⭐:</b> d/dx[f(g(x))] = f′(g(x))·g′(x) — bahar wale ka derivative × andar wale ka derivative. Example: d/dx sin(x²) = cos(x²)·2x.</li>\n<li><b>Implicit differentiation ⭐:</b> jab y alag na ho sake (x² + y² = 25), dono taraf x ke respect me differentiate karo, y ke terms me dy/dx lagao, phir solve karo.</li>\n<li><b>Exponential/Log ⭐:</b> d/dx eˣ = eˣ; d/dx aˣ = aˣ·ln a; d/dx ln x = 1/x; d/dx logₐx = 1/(x ln a).</li>\n<li><b>Logarithmic differentiation ⭐⭐:</b> jab power me bhi x ho (xˣ, (sin x)^(cos x)) — dono taraf ln lo, power neeche utaro, phir differentiate karo. y = xˣ → dy/dx = xˣ(1 + ln x).</li>\n<li><b>Parametric ⭐:</b> x = f(t), y = g(t) → dy/dx = (dy/dt)/(dx/dt).</li>\n</ul>\n<p class=\"small-note\">💡 Chain rule = \"peel the onion\" — sabse bahar wala layer pehle, andar tak ek-ek layer.</p>"
   },
   {
    "h": "5️⃣ Second Order Derivatives aur Syllabus Note",
    "body": "<ul>\n<li><b>Second derivative ⭐:</b> derivative ka derivative — d²y/dx² = d/dx(dy/dx). Pehla slope batata hai, doosra slope ki CHANGE RATE (concavity!).</li>\n<li>Parametric me d²y/dx² = d/dx(dy/dx) — dy/dx ko phir se x ke respect me differentiate karo (dy/dt, dx/dt use karke), common mistake: sirf t ke respect me kar dena!</li>\n<li><b>Syllabus note ⭐:</b> <b>Rolle's Theorem aur Lagrange's Mean Value Theorem</b> rationalized NCERT se <b>DELETE</b> ho chuke hain — unke statements/proofs ab nahi padhne.</li>\n<li>Inverse trig functions ke derivatives (d/dx sin⁻¹x = 1/√(1−x²) etc.) chapter me hain — integration me bhi yahi reuse hote hain.</li>\n<li>Board pattern: ek chain-rule 2-marker, ek implicit/log-differentiation 3-marker, ek second-order/parametric 5-marker — ye trio fixed hai.</li>\n</ul>\n<p class=\"small-note\">🎯 d²y/dx² me galati 90% students karte hain parametric case me — formula: d/dt(dy/dx) ÷ dx/dt. Practice se pakka karo!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ संतत्य — बिना ब्रेक का फलन ⭐⭐",
    "body": "<ul>\n<li><b>अंतर्ज्ञान:</b> आलेख बिना कलम उठाए बन जाए तो फलन <b>संतत (continuous)</b> है — कोई छलांग या छिद्र नहीं।</li>\n<li><b>परिभाषा ⭐⭐:</b> f, x = a पर संतत है यदि <b>lim(x→a) f(x) = f(a)</b> — तीन शर्तें: सीमा का अस्तित्व, f(a) परिभाषित, दोनों बराबर।</li>\n<li><b>LHL = RHL जांच ⭐:</b> सीमा के लिए बायीं और दायीं सीमा बराबर होनी चाहिए।</li>\n<li>उदाहरण: f(x) = |x|, x = 0 पर: LHL = RHL = 0 = f(0) → <b>संतत</b>।</li>\n<li>बहुपद, sin x, cos x, eˣ <b>सर्वत्र</b> संतत हैं।</li>\n</ul>\n<p class=\"small-note\">💡 संतत = बिना उभार की सड़क। कलम उठानी पड़ी तो असंतत्य!</p>"
   },
   {
    "h": "2️⃣ असंतत्य के प्रकार और संतत फलनों का बीजगणित",
    "body": "<ul>\n<li><b>छलांग असंतत्य:</b> LHL ≠ RHL — आलेख \"कूद\" जाता है (महत्तम पूर्णांक फलन [x] प्रत्येक पूर्णांक पर!)।</li>\n<li><b>छिद्र:</b> सीमा है पर f(a) परिभाषित नहीं या भिन्न।</li>\n<li><b>अनंत असंतत्य:</b> बिंदु के पास फलन ±∞ की ओर (1/x, x = 0 पर)।</li>\n<li><b>बीजगणित ⭐:</b> संतत फलनों का योग, अंतर, गुणनफल, अदिश गुणक सब संतत। भागफल भी — जहां हर ≠ 0।</li>\n<li><b>संयुक्त फलन:</b> g, a पर संतत + f, g(a) पर संतत → fog, a पर संतत।</li>\n</ul>\n<p class=\"small-note\">🎯 [x] और {x} प्रत्येक पूर्णांक पर असंतत — बोर्ड का प्रिय उदाहरण!</p>"
   },
   {
    "h": "3️⃣ अवकलनीयता — हर जगह ढलान ⭐⭐",
    "body": "<ul>\n<li><b>परिभाषा ⭐:</b> f′(a) = lim(h→0) [f(a+h) − f(a)]/h — यह सीमा <b>मौजूद</b> हो तो f, a पर अवकलनीय।</li>\n<li><b>अवकलनीय ⟹ संतत ⭐⭐:</b> अवकलनीय है तो संतत <b>अवश्य</b>। पर उल्टा सत्य <b>नहीं</b>!</li>\n<li><b>|x|, x = 0 पर ⭐:</b> संतत <b>है</b>, पर अवकलनीय <b>नहीं</b> — बायां ढलान −1, दायां +1 → तीखा कोना!</li>\n<li>कोना, शिखर (cusp), ऊर्ध्व स्पर्शरेखा या ब्रेक — सभी पर अवकलनीयता विफल।</li>\n<li>बहुपद, sin x, cos x, eˣ सर्वत्र अवकलनीय।</li>\n</ul>\n<p class=\"small-note\">🎯 प्रवाह: अवकलनीय → संतत → (उल्टा गलत!)। |x|, 0 पर = क्लासिक प्रत्युदाहरण।</p>"
   },
   {
    "h": "4️⃣ अवकलन के नियम — श्रृंखला, अप्रत्यक्ष, लघुगणक ⭐⭐",
    "body": "<ul>\n<li><b>श्रृंखला नियम ⭐⭐:</b> d/dx[f(g(x))] = f′(g(x))·g′(x)। उदाहरण: d/dx sin(x²) = cos(x²)·2x।</li>\n<li><b>अप्रत्यक्ष अवकलन ⭐:</b> y अलग न हो सके (x² + y² = 25) तो दोनों ओर x के सापेक्ष अवकलन करो, फिर dy/dx निकालो।</li>\n<li><b>चरघातांकी/लघुगणक ⭐:</b> d/dx eˣ = eˣ; d/dx aˣ = aˣ·ln a; d/dx ln x = 1/x।</li>\n<li><b>लघुगणकीय अवकलन ⭐⭐:</b> घात में x हो (xˣ) तो दोनों ओर ln लो। y = xˣ → dy/dx = <b>xˣ(1 + ln x)</b>।</li>\n<li><b>प्राचलिक ⭐:</b> x = f(t), y = g(t) → dy/dx = (dy/dt)/(dx/dt)।</li>\n</ul>\n<p class=\"small-note\">💡 श्रृंखला नियम = \"प्याज छीलो\" — बाहरी परत पहले, फिर अंदर एक-एक परत।</p>"
   },
   {
    "h": "5️⃣ द्वितीय-कोटि अवकलज और पाठ्यक्रम टिप्पणी",
    "body": "<ul>\n<li><b>द्वितीय अवकलज ⭐:</b> अवकलज का अवकलज — d²y/dx² = d/dx(dy/dx)। ढलान की <b>परिवर्तन दर</b> बताता है।</li>\n<li>प्राचलिक में d²y/dx² = d/dt(dy/dx) ÷ dx/dt — सामान्य गलती: केवल t के सापेक्ष कर देना!</li>\n<li><b>पाठ्यक्रम टिप्पणी ⭐:</b> <b>रोले का प्रमेय और लाग्रांज का मध्यमान प्रमेय</b> NCERT से <b>हटाए गए</b> हैं।</li>\n<li>प्रतिलोम त्रिकोणमितीय फलनों के अवकलज (d/dx sin⁻¹x = 1/√(1−x²)) समाकलन में भी काम आते हैं।</li>\n</ul>\n<p class=\"small-note\">🎯 प्राचलिक द्वितीय अवकलज में 90% गलती — सूत्र अभ्यास से पक्का करो!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Continuity — A Function Without Breaks ⭐⭐",
    "body": "<ul>\n<li><b>Intuition:</b> if you can draw the graph without lifting your pen, the function is continuous — no jumps, holes or breaks.</li>\n<li><b>Definition ⭐⭐:</b> f is <b>continuous</b> at x = a if <b>lim(x→a) f(x) = f(a)</b> — three things must hold: the limit EXISTS, f(a) is DEFINED, and the two are EQUAL.</li>\n<li><b>LHL = RHL check ⭐:</b> for the limit to exist, the Left Hand Limit must equal the Right Hand Limit. Compute both, compare!</li>\n<li>Example: f(x) = |x| at x = 0: LHL = RHL = 0 = f(0) → <b>continuous</b>. (But not differentiable — see ahead!)</li>\n<li>Polynomials, sin x, cos x, eˣ are continuous EVERYWHERE — use these standard results freely.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: continuous = a road without speed-breakers. If you had to lift the pen, there is a discontinuity there!</p>"
   },
   {
    "h": "2️⃣ Types of Discontinuity and the Algebra of Continuous Functions",
    "body": "<ul>\n<li><b>Jump discontinuity:</b> LHL ≠ RHL — the graph \"jumps\" from one level to another (the greatest integer function [x] at every integer!).</li>\n<li><b>Missing point:</b> the limit exists but f(a) is undefined or different — a small hole in the graph.</li>\n<li><b>Infinite discontinuity:</b> the function shoots to ±∞ near the point (1/x at x = 0).</li>\n<li><b>Algebra ⭐:</b> sums, differences, products and scalar multiples of continuous functions are continuous. Quotients too — wherever the denominator ≠ 0.</li>\n<li><b>Composite:</b> g continuous at a + f continuous at g(a) → fog continuous at a.</li>\n<li>Continuous on an interval = continuous at EVERY point of that interval.</li>\n</ul>\n<p class=\"small-note\">🎯 [x] (greatest integer) is discontinuous at every integer; {x} (fractional part) too. A board favourite!</p>"
   },
   {
    "h": "3️⃣ Differentiability — A Slope Everywhere ⭐⭐",
    "body": "<ul>\n<li><b>Definition ⭐:</b> f′(a) = lim(h→0) [f(a+h) − f(a)]/h — if this limit EXISTS, f is differentiable at a. It means a unique tangent/slope exists there.</li>\n<li><b>Differentiable ⟹ Continuous ⭐⭐:</b> differentiability forces continuity. The CONVERSE is NOT true — continuity alone guarantees nothing!</li>\n<li><b>|x| at x = 0 ⭐:</b> continuous YES (LHL = RHL = 0), differentiable NO — left slope −1, right slope +1, a sharp corner!</li>\n<li>Corner, cusp, vertical tangent or break — differentiability fails at all such points.</li>\n<li>Standard: polynomials, sin x, cos x, eˣ are differentiable everywhere. |x|, [x] fail at their break/corner points.</li>\n</ul>\n<p class=\"small-note\">🎯 Flow to remember: Differentiable → Continuous → (reverse is false!). |x| at 0 is the classic counterexample, guaranteed in exams.</p>"
   },
   {
    "h": "4️⃣ Differentiation Rules — Chain, Implicit, Log ⭐⭐",
    "body": "<ul>\n<li><b>Chain rule ⭐⭐:</b> d/dx[f(g(x))] = f′(g(x))·g′(x) — derivative of the outer × derivative of the inner. Example: d/dx sin(x²) = cos(x²)·2x.</li>\n<li><b>Implicit differentiation ⭐:</b> when y cannot be isolated (x² + y² = 25), differentiate both sides with respect to x, attach dy/dx to y-terms, then solve.</li>\n<li><b>Exponential/Log ⭐:</b> d/dx eˣ = eˣ; d/dx aˣ = aˣ·ln a; d/dx ln x = 1/x; d/dx logₐx = 1/(x ln a).</li>\n<li><b>Logarithmic differentiation ⭐⭐:</b> when x sits in the power (xˣ, (sin x)^(cos x)) — take ln on both sides, bring the power down, then differentiate. y = xˣ → dy/dx = xˣ(1 + ln x).</li>\n<li><b>Parametric ⭐:</b> x = f(t), y = g(t) → dy/dx = (dy/dt)/(dx/dt).</li>\n</ul>\n<p class=\"small-note\">💡 Chain rule = \"peel the onion\" — outermost layer first, then one layer at a time inward.</p>"
   },
   {
    "h": "5️⃣ Second Order Derivatives and Syllabus Note",
    "body": "<ul>\n<li><b>Second derivative ⭐:</b> the derivative of the derivative — d²y/dx² = d/dx(dy/dx). The first gives the slope; the second gives the slope's RATE OF CHANGE (concavity!).</li>\n<li>In parametric form d²y/dx² = d/dx(dy/dx) — differentiate dy/dx with respect to x again (using dy/dt, dx/dt); common mistake: differentiating only with respect to t!</li>\n<li><b>Syllabus note ⭐:</b> <b>Rolle's Theorem and Lagrange's Mean Value Theorem</b> are <b>DELETED</b> from rationalized NCERT — skip their statements and proofs.</li>\n<li>Derivatives of inverse trig functions (d/dx sin⁻¹x = 1/√(1−x²) etc.) are in the chapter — the same results get reused in integration.</li>\n<li>Board pattern: one chain-rule 2-marker, one implicit/log-differentiation 3-marker, one second-order/parametric 5-marker — this trio is fixed.</li>\n</ul>\n<p class=\"small-note\">🎯 90% of mistakes in d²y/dx² happen in the parametric case — the formula is d/dt(dy/dx) ÷ dx/dt. Drill it!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Continuity ⭐⭐",
    "items": [
     "lim f(x) = f(a) at a",
     "LHL = RHL = f(a)",
     "Polynomial, sin, cos, eˣ sab continuous"
    ]
   },
   {
    "h": "Discontinuity",
    "items": [
     "Jump: LHL ≠ RHL",
     "Hole: limit hai, value nahi",
     "[x] har integer pe discontinuous"
    ]
   },
   {
    "h": "Differentiability ⭐⭐",
    "items": [
     "f′(a) ka limit exist kare",
     "Differentiable ⟹ Continuous",
     "|x| at 0: cont. HAI, diff NAHI"
    ]
   },
   {
    "h": "Rules ⭐⭐",
    "items": [
     "Chain: f′(g)·g′",
     "Log diff: xˣ type pe ln lo",
     "Parametric: dy/dx = (dy/dt)/(dx/dt)"
    ]
   },
   {
    "h": "Second order ⭐",
    "items": [
     "d²y/dx² = slope ki change rate",
     "Parametric: d/dt(dy/dx) ÷ dx/dt",
     "Rolle's & MVT DELETED"
    ]
   }
  ],
  "hi": [
   {
    "h": "संतत्य ⭐⭐",
    "items": [
     "lim f(x) = f(a)",
     "LHL = RHL = f(a)",
     "बहुपद, sin, cos, eˣ सर्वत्र संतत"
    ]
   },
   {
    "h": "असंतत्य",
    "items": [
     "छलांग: LHL ≠ RHL",
     "छिद्र: सीमा है, मान नहीं",
     "[x] प्रत्येक पूर्णांक पर असंतत"
    ]
   },
   {
    "h": "अवकलनीयता ⭐⭐",
    "items": [
     "f′(a) की सीमा मौजूद हो",
     "अवकलनीय ⟹ संतत",
     "|x|, 0 पर: संतत हां, अवकलनीय नहीं"
    ]
   },
   {
    "h": "नियम ⭐⭐",
    "items": [
     "श्रृंखला: f′(g)·g′",
     "लघुगणकीय: xˣ पर ln लो",
     "प्राचलिक: dy/dx = (dy/dt)/(dx/dt)"
    ]
   },
   {
    "h": "द्वितीय ⭐",
    "items": [
     "d²y/dx² = ढलान की परिवर्तन दर",
     "प्राचलिक: d/dt(dy/dx) ÷ dx/dt",
     "रोले व मध्यमान प्रमेय हटाए गए"
    ]
   }
  ],
  "en": [
   {
    "h": "Continuity ⭐⭐",
    "items": [
     "lim f(x) = f(a) at a",
     "LHL = RHL = f(a)",
     "Polynomials, sin, cos, eˣ all continuous"
    ]
   },
   {
    "h": "Discontinuity",
    "items": [
     "Jump: LHL ≠ RHL",
     "Hole: limit exists, value missing",
     "[x] discontinuous at every integer"
    ]
   },
   {
    "h": "Differentiability ⭐⭐",
    "items": [
     "The limit for f′(a) must exist",
     "Differentiable ⟹ Continuous",
     "|x| at 0: continuous YES, differentiable NO"
    ]
   },
   {
    "h": "Rules ⭐⭐",
    "items": [
     "Chain: f′(g)·g′",
     "Log diff: take ln for xˣ type",
     "Parametric: dy/dx = (dy/dt)/(dx/dt)"
    ]
   },
   {
    "h": "Second order ⭐",
    "items": [
     "d²y/dx² = rate of change of slope",
     "Parametric: d/dt(dy/dx) ÷ dx/dt",
     "Rolle's & MVT DELETED"
    ]
   }
  ]
 },
 "practice": [
  [
   "f(x) = |x|, x = 0 pe continuous hai?",
   "<b>Haan</b> — LHL = RHL = 0 = f(0). Limit = function value, to continuous."
  ],
  [
   "f(x) = |x|, x = 0 pe differentiable hai?",
   "<b>Nahi</b> — left slope −1, right slope +1. Corner point pe unique tangent nahi banti."
  ],
  [
   "'Continuous ⟹ differentiable' — sahi hai?",
   "<b>Galat</b> — ulta sahi hai: differentiable ⟹ continuous. |x| at 0 iska counterexample hai."
  ],
  [
   "f(x) = [x] (greatest integer), x = 2 pe continuous?",
   "<b>Nahi</b> — LHL = 1, RHL = 2, dono alag → jump discontinuity."
  ],
  [
   "d/dx [sin(x²)] nikalo.",
   "Chain rule: <b>cos(x²)·2x</b> — bahar sin ka derivative, andar x² ka."
  ],
  [
   "y = xˣ ka dy/dx?",
   "ln y = x ln x → (1/y)y′ = 1 + ln x → dy/dx = <b>xˣ(1 + ln x)</b>."
  ],
  [
   "x = 2t, y = t² ho to dy/dx?",
   "dy/dt = 2t, dx/dt = 2 → dy/dx = 2t/2 = <b>t</b>."
  ],
  [
   "d/dx (eˣ) aur d/dx (ln x)?",
   "d/dx eˣ = <b>eˣ</b>; d/dx ln x = <b>1/x</b>."
  ],
  [
   "x² + y² = 25 pe dy/dx nikalo.",
   "2x + 2y(dy/dx) = 0 → dy/dx = <b>−x/y</b>."
  ],
  [
   "Rolle's Theorem ab bhi Class 12 syllabus me hai?",
   "<b>Nahi</b> — Rolle's aur Lagrange's MVT dono rationalized NCERT se <b>delete</b> ho chuke hain."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-6/",
  "title": "Application of Derivatives"
 }
}

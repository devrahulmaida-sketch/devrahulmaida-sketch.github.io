# Class 12 Maths, Chapter 7 - Integrals
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 7,
 "title_en": "Integrals",
 "title_hi": "समाकलन",
 "tagline": "Substitution, by parts, partial fractions aur definite integral properties — calculus ka sabse bada chapter",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 7: Integrals — long + short notes in Hindi, English, Hinglish. Indefinite integrals, substitution, integration by parts, partial fractions, definite integrals and properties.",
 "video": None,
 "card_tag": "Substitution, by parts, partial fractions aur definite integral properties — calculus ka sabse bada chapter",
 "card_topics": [
  "∫ Basic formulas + C",
  "🔀 Substitution method",
  "🧩 By parts (ILATE)",
  "👑 Definite integral properties"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Integration Ka Concept — Differentiation Ka Ulta ⭐",
    "body": "<ul>\n<li><b>Antiderivative:</b> integration = differentiation ka REVERSE. d/dx(x²) = 2x, to ∫2x dx = x². ∫ f(x) dx ka matlab: wo function jiska derivative f(x) hai.</li>\n<li><b>+C kyun? ⭐</b> x², x² + 5, x² − 100 — sabka derivative 2x hai! Constant ka derivative 0 hota hai, isliye answer me hamesha <b>arbitrary constant C</b> jodo.</li>\n<li><b>Power rule ⭐⭐:</b> ∫ xⁿ dx = <b>xⁿ⁺¹/(n+1) + C</b> (n ≠ −1). Power ek badhao, naye power se divide!</li>\n<li><b>Exception:</b> ∫ (1/x) dx = <b>ln|x| + C</b> — power rule n = −1 pe fail hota hai, yahan log aata hai.</li>\n<li><b>Must-know formulas:</b> ∫ eˣ dx = eˣ; ∫ aˣ dx = aˣ/ln a; ∫ sin x dx = −cos x; ∫ cos x dx = sin x; ∫ sec²x dx = tan x; ∫ cosec²x dx = −cot x; ∫ sec x tan x dx = sec x; ∫ cosec x cot x dx = −cosec x. (Sab + C!)</li>\n<li>Sum/difference rule: ∫(f ± g) = ∫f ± ∫g; constant bahar: ∫kf = k∫f.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: differentiation neeche ki taraf (break karna), integration upar ki taraf (jodna). Answer ka check: derivative karke wapas f(x) aa jaana chahiye!</p>"
   },
   {
    "h": "2️⃣ Substitution Method — Change Kardo, Easy Banado ⭐⭐",
    "body": "<ul>\n<li><b>Idea:</b> andar wali complicated cheez ko <b>t</b> maan lo — uska derivative dx ke saath adjust karke integral simple form me aa jaata hai.</li>\n<li><b>Signal ⭐:</b> integrand me ek function AUR uska derivative dono dikhe (derivative × dx wala pair) → substitution lagao!</li>\n<li>Example: ∫ 2x·cos(x²) dx → t = x², dt = 2x dx → ∫ cos t dt = sin t = <b>sin(x²) + C</b>.</li>\n<li><b>Common patterns ⭐:</b> ∫ f′(x)/f(x) dx = <b>ln|f(x)| + C</b> (numerator = denominator ka derivative!); ∫ f′(x)·√f(x) dx = (2/3)f(x)^(3/2); ∫ f′(x)·e^(f(x)) dx = e^(f(x)) + C.</li>\n<li>Trig identities bhi substitution ke saath milke kaam karti hain — sin 2x = 2 sin x cos x type pehle simplify karo.</li>\n<li>Definite integral me substitution: <b>limits bhi badlo</b> t ke hisaab se (ya wapas x me aao) — dono tarike sahi, par limits mat bhoolo!</li>\n</ul>\n<p class=\"small-note\">🎯 Golden eye: \"kya numerator/second factor pehle wale ka derivative hai?\" Haan → substitution = 2 line me answer.</p>"
   },
   {
    "h": "3️⃣ Integration by Parts — Product Ka Ilaj ⭐⭐",
    "body": "<ul>\n<li><b>Formula ⭐⭐:</b> ∫ u·v dx = <b>u∫v dx − ∫(u′·∫v dx) dx</b> — \"pehla function × doosre ka integral − derivative × integral ka integral\".</li>\n<li><b>ILATE ⭐:</b> pehla function (u) kaun? priority order: <b>I</b>nverse trig → <b>L</b>og → <b>A</b>lgebraic → <b>T</b>rig → <b>E</b>xponential. Jo pehle aaye, wo u!</li>\n<li>Example: ∫ x·eˣ dx → u = x (algebraic), v = eˣ → x·eˣ − ∫1·eˣ dx = <b>eˣ(x − 1) + C</b>.</li>\n<li><b>ln x akela ho to ⭐:</b> ∫ ln x dx = ∫ ln x · 1 dx → u = ln x, v = 1 → x ln x − x + C. (1 ko second function maano!)</li>\n<li><b>Loop trick:</b> ∫ eˣ sin x dx jaise me do baar parts lagao — original integral wapas aata hai, phir usse solve karo (algebra!): answer = eˣ(sin x − cos x)/2 + C.</li>\n</ul>\n<p class=\"small-note\">💡 ILATE yaad rakho — u galat choose kiya to integral aur complicated ho jaata hai. Sahi u = half battle won.</p>"
   },
   {
    "h": "4️⃣ Partial Fractions — Rational Functions Todna ⭐",
    "body": "<ul>\n<li><b>Kab:</b> integrand P(x)/Q(x) ho (polynomial ÷ polynomial) aur degree of P &lt; degree of Q. Pehle factors todo, phir fractions me baanto.</li>\n<li><b>Linear factors ⭐:</b> 1/[(x−a)(x−b)] = A/(x−a) + B/(x−b) — A, B nikalo (values daal ke ya compare karke), phir har part ka integral ln ban jaata hai!</li>\n<li><b>Repeated factor:</b> 1/[(x−a)²(x−b)] = A/(x−a) + B/(x−a)² + C/(x−b) — har power ke liye ek term.</li>\n<li><b>Quadratic factor (irreducible):</b> (px + q)/(ax² + bx + c) wala numerator rakho.</li>\n<li>Degree of P ≥ Q ho to pehle <b>long division</b> karo — quotient + remainder/Q, phir partial fractions.</li>\n<li>Example: ∫ dx/[(x−1)(x−2)] = ∫[−1/(x−1) + 1/(x−2)] dx = <b>ln|x−2| − ln|x−1| + C</b>.</li>\n</ul>\n<p class=\"small-note\">🎯 Partial fractions = \"badi fraction ko chhoti fractions me todo\" — har tukda standard ln/1/x² form ban jaata hai.</p>"
   },
   {
    "h": "5️⃣ Special Integrals — Standard Forms ⭐⭐",
    "body": "<ul>\n<li><b>∫ dx/(x² + a²) = (1/a) tan⁻¹(x/a) + C</b>; <b>∫ dx/(x² − a²) = (1/2a) ln|(x−a)/(x+a)| + C</b>; <b>∫ dx/(a² − x²) = (1/2a) ln|(a+x)/(a−x)| + C</b>.</li>\n<li><b>∫ dx/√(a² − x²) = sin⁻¹(x/a) + C</b>; <b>∫ dx/√(x² + a²) = ln|x + √(x² + a²)| + C</b>; <b>∫ dx/√(x² − a²) = ln|x + √(x² − a²)| + C</b>.</li>\n<li><b>√ ke upar wale ⭐:</b> ∫ √(a² − x²) dx = (x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C; ∫ √(x² ± a²) dx = (x/2)√(x² ± a²) ± (a²/2) ln|x + √(x² ± a²)| + C.</li>\n<li><b>Quadratic denominator me ⭐:</b> complete the square! x² + 4x + 5 = (x+2)² + 1 → tan⁻¹ form. Ye move 80% questions me chahiye.</li>\n<li>Numerator = derivative of denominator ka linear combo banake split karo (px + q = A·d(denominator)/dx + B) — quadratic wale integrals ka master key.</li>\n</ul>\n<p class=\"small-note\">💡 Ye 8-9 formulas rattne padte hain — par pattern ek: tan⁻¹/sin⁻¹/ln. Square complete karna aaya to sab apply hoga.</p>"
   },
   {
    "h": "6️⃣ Definite Integrals aur Properties ⭐⭐",
    "body": "<ul>\n<li><b>Definite integral:</b> ∫ₐᵇ f(x) dx = F(b) − F(a) — antiderivative F nikalo, upper limit daalo, lower limit ka minus. <b>No +C needed!</b> (C cancel ho jaata hai.)</li>\n<li><b>Meaning ⭐:</b> curve ke NEECHE ka area (x-axis ke saath), a se b tak. Negative area bhi possible (axis ke neeche wala part).</li>\n<li><b>Basic properties:</b> ∫ₐᵇ f = −∫ᵦₐ f (limits swap → sign flip); ∫ₐᵇ f = ∫ₐᶜ f + ∫cᵦ f (tod sakte ho); ∫ₐᵇ kf = k∫ₐᵇ f.</li>\n<li><b>King property ⭐⭐:</b> ∫₀ᵃ f(x) dx = <b>∫₀ᵃ f(a − x) dx</b> — x ko (a − x) se replace kar sakte ho! Trig integrals me magic karta hai. General: ∫ₐᵇ f(x) dx = ∫ₐᵇ f(a + b − x) dx.</li>\n<li><b>Even/odd ⭐:</b> ∫₋ₐᵃ f(x) dx = <b>2∫₀ᵃ f(x) dx agar f EVEN</b>; <b>0 agar f ODD</b>. Symmetric limits pe pehle even/odd check karo!</li>\n<li><b>Syllabus note:</b> definite integral as <b>limit of a sum</b> NCERT se DELETE — properties + evaluation pe focus.</li>\n</ul>\n<p class=\"small-note\">🎯 King property use karke ∫₀^(π/2) sinⁿx/(sinⁿx + cosⁿx) dx = π/4 jaisa \"impossible-looking\" integral 30 seconds me solve hota hai — seekh ke jao!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ समाकलन की अवधारणा — अवकलन का उल्टा ⭐",
    "body": "<ul>\n<li><b>प्रतिअवकलज:</b> समाकलन = अवकलन का <b>विपरीत</b>। d/dx(x²) = 2x, तो ∫2x dx = x²।</li>\n<li><b>+C क्यों? ⭐</b> x², x² + 5 — सबका अवकलज 2x है! इसलिए उत्तर में सदैव <b>अचर C</b> जोड़ो।</li>\n<li><b>घात नियम ⭐⭐:</b> ∫ xⁿ dx = <b>xⁿ⁺¹/(n+1) + C</b> (n ≠ −1)।</li>\n<li><b>अपवाद:</b> ∫ (1/x) dx = <b>ln|x| + C</b>।</li>\n<li><b>आवश्यक सूत्र:</b> ∫ eˣ dx = eˣ; ∫ sin x dx = −cos x; ∫ cos x dx = sin x; ∫ sec²x dx = tan x (सब + C!)।</li>\n</ul>\n<p class=\"small-note\">💡 जांच: उत्तर का अवकलन करके f(x) वापस आना चाहिए!</p>"
   },
   {
    "h": "2️⃣ प्रतिस्थापन विधि — बदलो, सरल बनाओ ⭐⭐",
    "body": "<ul>\n<li><b>विचार:</b> जटिल भाग को <b>t</b> मानो — उसका अवकलज dx के साथ मिलाकर समाकलन सरल हो जाता है।</li>\n<li><b>संकेत ⭐:</b> एक फलन <b>और</b> उसका अवकलज दोनों दिखें → प्रतिस्थापन!</li>\n<li>उदाहरण: ∫ 2x·cos(x²) dx → t = x² → ∫ cos t dt = <b>sin(x²) + C</b>।</li>\n<li><b>सामान्य पैटर्न ⭐:</b> ∫ f′(x)/f(x) dx = <b>ln|f(x)| + C</b>; ∫ f′(x)·e^(f(x)) dx = e^(f(x)) + C।</li>\n<li>निश्चित समाकलन में प्रतिस्थापन: <b>सीमाएं भी बदलो</b>!</li>\n</ul>\n<p class=\"small-note\">🎯 \"क्या अंश हर का अवकलज है?\" हां → ln|f(x)| सीधे!</p>"
   },
   {
    "h": "3️⃣ खंडश: समाकलन — गुणनफल का इलाज ⭐⭐",
    "body": "<ul>\n<li><b>सूत्र ⭐⭐:</b> ∫ u·v dx = <b>u∫v dx − ∫(u′·∫v dx) dx</b>।</li>\n<li><b>ILATE ⭐:</b> u की प्राथमिकता: प्रतिलोम त्रिकोणमितीय → लघुगणक → बीजीय → त्रिकोणमितीय → चरघातांकी।</li>\n<li>उदाहरण: ∫ x·eˣ dx = x·eˣ − ∫eˣ dx = <b>eˣ(x − 1) + C</b>।</li>\n<li><b>ln x अकेला हो तो ⭐:</b> ∫ ln x dx = <b>x ln x − x + C</b> (1 को दूसरा फलन मानो)।</li>\n<li><b>चक्र तरकीब:</b> ∫ eˣ sin x dx में दो बार खंडश: — मूल समाकलन लौटता है, बीजगणित से हल: eˣ(sin x − cos x)/2 + C।</li>\n</ul>\n<p class=\"small-note\">💡 ILATE याद रखो — सही u = आधी जीत।</p>"
   },
   {
    "h": "4️⃣ आंशिक भिन्नें — परिमेय फलन तोड़ना ⭐",
    "body": "<ul>\n<li><b>कब:</b> P(x)/Q(x) हो और P की घात &lt; Q की घात। पहले गुणनखंड, फिर भिन्नों में बांटो।</li>\n<li><b>रैखिक गुणनखंड ⭐:</b> 1/[(x−a)(x−b)] = A/(x−a) + B/(x−b) — प्रत्येक भाग का समाकलन ln बनता है!</li>\n<li><b>दोहराया गुणनखंड:</b> प्रत्येक घात के लिए एक पद: A/(x−a) + B/(x−a)² + ...</li>\n<li>घात P ≥ Q हो तो पहले <b>भाग</b> दो।</li>\n<li>उदाहरण: ∫ dx/[(x−1)(x−2)] = <b>ln|x−2| − ln|x−1| + C</b>।</li>\n</ul>\n<p class=\"small-note\">🎯 बड़ी भिन्न → छोटी भिन्नें → प्रत्येक मानक रूप।</p>"
   },
   {
    "h": "5️⃣ विशिष्ट समाकलन — मानक रूप ⭐⭐",
    "body": "<ul>\n<li><b>∫ dx/(x² + a²) = (1/a) tan⁻¹(x/a)</b>; <b>∫ dx/(x² − a²) = (1/2a) ln|(x−a)/(x+a)|</b>।</li>\n<li><b>∫ dx/√(a² − x²) = sin⁻¹(x/a)</b>; <b>∫ dx/√(x² ± a²) = ln|x + √(x² ± a²)|</b>।</li>\n<li><b>∫ √(a² − x²) dx = (x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C</b>।</li>\n<li><b>द्विघात हर में ⭐:</b> वर्ग पूर्ण करो! x² + 4x + 5 = (x+2)² + 1 → tan⁻¹ रूप।</li>\n<li>अंश को हर के अवकलज के रैखिक संयोजन में तोड़ो — द्विघात समाकलनों की कुंजी।</li>\n</ul>\n<p class=\"small-note\">💡 8-9 सूत्र कंठस्थ करने ही पड़ते हैं — पैटर्न एक: tan⁻¹/sin⁻¹/ln।</p>"
   },
   {
    "h": "6️⃣ निश्चित समाकलन और गुणधर्म ⭐⭐",
    "body": "<ul>\n<li><b>निश्चित समाकलन:</b> ∫ₐᵇ f(x) dx = F(b) − F(a) — <b>+C नहीं!</b></li>\n<li><b>अर्थ ⭐:</b> a से b तक वक्र के <b>नीचे का क्षेत्रफल</b>।</li>\n<li><b>मूल गुणधर्म:</b> ∫ₐᵇ f = −∫ᵦₐ f; ∫ₐᵇ f = ∫ₐᶜ f + ∫cᵦ f।</li>\n<li><b>राजा गुणधर्म ⭐⭐:</b> ∫₀ᵃ f(x) dx = <b>∫₀ᵃ f(a − x) dx</b>; सामान्यतः ∫ₐᵇ f(x) dx = ∫ₐᵇ f(a + b − x) dx।</li>\n<li><b>सम/विषम ⭐:</b> ∫₋ₐᵃ f = <b>2∫₀ᵃ f (सम फलन)</b>; <b>0 (विषम फलन)</b>।</li>\n<li><b>पाठ्यक्रम टिप्पणी:</b> योग की सीमा के रूप में निश्चित समाकलन NCERT से <b>हटाया गया</b>।</li>\n</ul>\n<p class=\"small-note\">🎯 राजा गुणधर्म से \"असंभव-लगने वाले\" त्रिकोणमितीय समाकलन सेकंडों में हल!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ The Concept of Integration — Differentiation in Reverse ⭐",
    "body": "<ul>\n<li><b>Antiderivative:</b> integration is the REVERSE of differentiation. d/dx(x²) = 2x, so ∫2x dx = x². ∫ f(x) dx means: the function whose derivative is f(x).</li>\n<li><b>Why +C? ⭐</b> x², x² + 5, x² − 100 — all have derivative 2x! The derivative of a constant is 0, so always attach an <b>arbitrary constant C</b>.</li>\n<li><b>Power rule ⭐⭐:</b> ∫ xⁿ dx = <b>xⁿ⁺¹/(n+1) + C</b> (n ≠ −1). Raise the power by one, divide by the new power!</li>\n<li><b>Exception:</b> ∫ (1/x) dx = <b>ln|x| + C</b> — the power rule fails at n = −1; log steps in.</li>\n<li><b>Must-know formulas:</b> ∫ eˣ dx = eˣ; ∫ aˣ dx = aˣ/ln a; ∫ sin x dx = −cos x; ∫ cos x dx = sin x; ∫ sec²x dx = tan x; ∫ cosec²x dx = −cot x; ∫ sec x tan x dx = sec x; ∫ cosec x cot x dx = −cosec x. (All + C!)</li>\n<li>Sum/difference rule: ∫(f ± g) = ∫f ± ∫g; constants pull out: ∫kf = k∫f.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: differentiation breaks down, integration builds up. Check your answer: its derivative must give back f(x)!</p>"
   },
   {
    "h": "2️⃣ Substitution — Change It, Simplify It ⭐⭐",
    "body": "<ul>\n<li><b>Idea:</b> call the complicated inner piece <b>t</b> — once its derivative pairs with dx, the integral collapses into a simple form.</li>\n<li><b>Signal ⭐:</b> you see a function AND its derivative together (derivative × dx pair) → substitute!</li>\n<li>Example: ∫ 2x·cos(x²) dx → t = x², dt = 2x dx → ∫ cos t dt = sin t = <b>sin(x²) + C</b>.</li>\n<li><b>Common patterns ⭐:</b> ∫ f′(x)/f(x) dx = <b>ln|f(x)| + C</b> (numerator = derivative of the denominator!); ∫ f′(x)·√f(x) dx = (2/3)f(x)^(3/2); ∫ f′(x)·e^(f(x)) dx = e^(f(x)) + C.</li>\n<li>Trig identities team up with substitution — simplify first with things like sin 2x = 2 sin x cos x.</li>\n<li>Substitution in a definite integral: <b>change the limits too</b> into t (or convert back to x) — both fine, but never forget the limits!</li>\n</ul>\n<p class=\"small-note\">🎯 Golden eye: \"is the numerator/second factor the derivative of the first?\" Yes → substitution solves it in 2 lines.</p>"
   },
   {
    "h": "3️⃣ Integration by Parts — Handling Products ⭐⭐",
    "body": "<ul>\n<li><b>Formula ⭐⭐:</b> ∫ u·v dx = <b>u∫v dx − ∫(u′·∫v dx) dx</b> — \"first function × integral of the second − integral of (derivative × integral)\".</li>\n<li><b>ILATE ⭐:</b> which function is u? Priority order: <b>I</b>nverse trig → <b>L</b>og → <b>A</b>lgebraic → <b>T</b>rig → <b>E</b>xponential. Whichever comes first is u!</li>\n<li>Example: ∫ x·eˣ dx → u = x (algebraic), v = eˣ → x·eˣ − ∫1·eˣ dx = <b>eˣ(x − 1) + C</b>.</li>\n<li><b>When ln x stands alone ⭐:</b> ∫ ln x dx = ∫ ln x · 1 dx → u = ln x, v = 1 → x ln x − x + C. (Treat 1 as the second function!)</li>\n<li><b>Loop trick:</b> for ∫ eˣ sin x dx apply parts twice — the original integral returns, then solve it algebraically: eˣ(sin x − cos x)/2 + C.</li>\n</ul>\n<p class=\"small-note\">💡 Remember ILATE — a wrong choice of u makes the integral worse. The right u wins half the battle.</p>"
   },
   {
    "h": "4️⃣ Partial Fractions — Breaking Rational Functions ⭐",
    "body": "<ul>\n<li><b>When:</b> the integrand is P(x)/Q(x) (polynomial ÷ polynomial) with degree of P &lt; degree of Q. Factor first, then split into fractions.</li>\n<li><b>Linear factors ⭐:</b> 1/[(x−a)(x−b)] = A/(x−a) + B/(x−b) — find A, B (plug values or compare), and each part integrates into ln!</li>\n<li><b>Repeated factor:</b> 1/[(x−a)²(x−b)] = A/(x−a) + B/(x−a)² + C/(x−b) — one term per power.</li>\n<li><b>Irreducible quadratic factor:</b> use a numerator of the form (px + q).</li>\n<li>If degree of P ≥ Q, do <b>long division</b> first — quotient + remainder/Q, then partial fractions.</li>\n<li>Example: ∫ dx/[(x−1)(x−2)] = ∫[−1/(x−1) + 1/(x−2)] dx = <b>ln|x−2| − ln|x−1| + C</b>.</li>\n</ul>\n<p class=\"small-note\">🎯 Partial fractions = \"break a big fraction into small ones\" — each piece becomes a standard ln/1/x² form.</p>"
   },
   {
    "h": "5️⃣ Special Integrals — Standard Forms ⭐⭐",
    "body": "<ul>\n<li><b>∫ dx/(x² + a²) = (1/a) tan⁻¹(x/a) + C</b>; <b>∫ dx/(x² − a²) = (1/2a) ln|(x−a)/(x+a)| + C</b>; <b>∫ dx/(a² − x²) = (1/2a) ln|(a+x)/(a−x)| + C</b>.</li>\n<li><b>∫ dx/√(a² − x²) = sin⁻¹(x/a) + C</b>; <b>∫ dx/√(x² + a²) = ln|x + √(x² + a²)| + C</b>; <b>∫ dx/√(x² − a²) = ln|x + √(x² − a²)| + C</b>.</li>\n<li><b>Root-on-top forms ⭐:</b> ∫ √(a² − x²) dx = (x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C; ∫ √(x² ± a²) dx = (x/2)√(x² ± a²) ± (a²/2) ln|x + √(x² ± a²)| + C.</li>\n<li><b>Quadratic denominators ⭐:</b> complete the square! x² + 4x + 5 = (x+2)² + 1 → tan⁻¹ form. This move is needed in 80% of questions.</li>\n<li>Split the numerator as a linear combo of the denominator's derivative (px + q = A·d(denominator)/dx + B) — the master key for quadratic integrals.</li>\n</ul>\n<p class=\"small-note\">💡 These 8-9 formulas must be memorized — but the pattern is one: tan⁻¹/sin⁻¹/ln. Learn to complete the square and everything applies.</p>"
   },
   {
    "h": "6️⃣ Definite Integrals and Their Properties ⭐⭐",
    "body": "<ul>\n<li><b>Definite integral:</b> ∫ₐᵇ f(x) dx = F(b) − F(a) — find the antiderivative F, plug the upper limit, subtract the lower. <b>No +C needed!</b> (C cancels out.)</li>\n<li><b>Meaning ⭐:</b> the AREA under the curve (with the x-axis) from a to b. Negative areas exist too (parts below the axis).</li>\n<li><b>Basic properties:</b> ∫ₐᵇ f = −∫ᵦₐ f (swapping limits flips the sign); ∫ₐᵇ f = ∫ₐᶜ f + ∫cᵦ f (you can split); ∫ₐᵇ kf = k∫ₐᵇ f.</li>\n<li><b>King property ⭐⭐:</b> ∫₀ᵃ f(x) dx = <b>∫₀ᵃ f(a − x) dx</b> — replace x by (a − x)! Works magic on trig integrals. General: ∫ₐᵇ f(x) dx = ∫ₐᵇ f(a + b − x) dx.</li>\n<li><b>Even/odd ⭐:</b> ∫₋ₐᵃ f(x) dx = <b>2∫₀ᵃ f(x) dx if f is EVEN</b>; <b>0 if f is ODD</b>. With symmetric limits, check even/odd first!</li>\n<li><b>Syllabus note:</b> the definite integral as a <b>limit of a sum</b> is DELETED from NCERT — focus on properties + evaluation.</li>\n</ul>\n<p class=\"small-note\">🎯 With the king property, scary integrals like ∫₀^(π/2) sinⁿx/(sinⁿx + cosⁿx) dx = π/4 solve in 30 seconds — learn it!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics ⭐",
    "items": [
     "∫ = differentiation ka ulta",
     "+C hamesha (indefinite)",
     "∫xⁿdx = xⁿ⁺¹/(n+1); ∫1/x = ln|x|"
    ]
   },
   {
    "h": "Substitution ⭐⭐",
    "items": [
     "Andar wale ko t maano",
     "Signal: function + uska derivative",
     "f′/f → ln|f|"
    ]
   },
   {
    "h": "By parts ⭐⭐",
    "items": [
     "∫uv = u∫v − ∫(u′∫v)",
     "u choose: ILATE order",
     "∫ln x = x ln x − x"
    ]
   },
   {
    "h": "Special forms ⭐",
    "items": [
     "1/(x²+a²) → (1/a)tan⁻¹",
     "1/√(a²−x²) → sin⁻¹",
     "Quadratic: complete the square"
    ]
   },
   {
    "h": "Definite ⭐⭐",
    "items": [
     "F(b) − F(a), no +C",
     "King: ∫₀ᵃf(x) = ∫₀ᵃf(a−x)",
     "Even: 2×half; Odd: 0"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल ⭐",
    "items": [
     "∫ = अवकलन का उल्टा",
     "+C सदैव (अनिश्चित)",
     "∫xⁿdx = xⁿ⁺¹/(n+1); ∫1/x = ln|x|"
    ]
   },
   {
    "h": "प्रतिस्थापन ⭐⭐",
    "items": [
     "भीतरी भाग को t",
     "संकेत: फलन + उसका अवकलज",
     "f′/f → ln|f|"
    ]
   },
   {
    "h": "खंडश: ⭐⭐",
    "items": [
     "∫uv = u∫v − ∫(u′∫v)",
     "u: ILATE क्रम",
     "∫ln x = x ln x − x"
    ]
   },
   {
    "h": "मानक रूप ⭐",
    "items": [
     "1/(x²+a²) → (1/a)tan⁻¹",
     "1/√(a²−x²) → sin⁻¹",
     "द्विघात: वर्ग पूर्ण करो"
    ]
   },
   {
    "h": "निश्चित ⭐⭐",
    "items": [
     "F(b) − F(a), +C नहीं",
     "राजा: ∫₀ᵃf(x) = ∫₀ᵃf(a−x)",
     "सम: 2×आधा; विषम: 0"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics ⭐",
    "items": [
     "∫ = reverse of differentiation",
     "Always +C (indefinite)",
     "∫xⁿdx = xⁿ⁺¹/(n+1); ∫1/x = ln|x|"
    ]
   },
   {
    "h": "Substitution ⭐⭐",
    "items": [
     "Set the inner piece = t",
     "Signal: function + its derivative",
     "f′/f → ln|f|"
    ]
   },
   {
    "h": "By parts ⭐⭐",
    "items": [
     "∫uv = u∫v − ∫(u′∫v)",
     "Choose u by ILATE",
     "∫ln x = x ln x − x"
    ]
   },
   {
    "h": "Special forms ⭐",
    "items": [
     "1/(x²+a²) → (1/a)tan⁻¹",
     "1/√(a²−x²) → sin⁻¹",
     "Quadratic: complete the square"
    ]
   },
   {
    "h": "Definite ⭐⭐",
    "items": [
     "F(b) − F(a), no +C",
     "King: ∫₀ᵃf(x) = ∫₀ᵃf(a−x)",
     "Even: 2×half; Odd: 0"
    ]
   }
  ]
 },
 "practice": [
  [
   "∫ x⁵ dx nikalo.",
   "x⁶/6 <b>+ C</b> — power ek badhao, naye power se divide."
  ],
  [
   "∫ (1/x) dx kya hai?",
   "<b>ln|x| + C</b> — power rule n = −1 pe kaam nahi karta."
  ],
  [
   "∫ 2x·sin(x²) dx kaise karein?",
   "t = x² → dt = 2x dx → ∫ sin t dt = −cos t = <b>−cos(x²) + C</b>."
  ],
  [
   "∫ f′(x)/f(x) dx ka direct formula?",
   "<b>ln|f(x)| + C</b> — numerator denominator ka derivative hai."
  ],
  [
   "∫ x·eˣ dx nikalo (by parts).",
   "u = x, v = eˣ → x·eˣ − ∫eˣ dx = <b>eˣ(x − 1) + C</b> (ILATE: algebraic pehle)."
  ],
  [
   "∫ ln x dx ka answer?",
   "<b>x ln x − x + C</b> — 1 ko second function maan ke by parts."
  ],
  [
   "∫ dx/(x² + 9) kya hoga?",
   "a = 3 → (1/3) <b>tan⁻¹(x/3) + C</b>."
  ],
  [
   "∫₀¹ x² dx ka value?",
   "F(x) = x³/3 → F(1) − F(0) = 1/3 − 0 = <b>1/3</b>."
  ],
  [
   "∫₋₂² x³ dx kya hai?",
   "x³ <b>odd</b> function hai, symmetric limits → <b>0</b>."
  ],
  [
   "King property bolo.",
   "∫₀ᵃ f(x) dx = <b>∫₀ᵃ f(a − x) dx</b> — x ki jagah (a − x) rakh sakte ho, value same."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-8/",
  "title": "Application of Integrals"
 }
}

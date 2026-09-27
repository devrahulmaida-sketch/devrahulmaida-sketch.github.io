# Class 11 Maths, Chapter 12 - Limits and Derivatives
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 12,
 "title_en": "Limits and Derivatives",
 "title_hi": "सीमा और अवकलज",
 "tagline": "Calculus ki entry — limits se derivatives tak",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 12: Limits and Derivatives — long + short notes in Hindi, English, Hinglish. Limits, standard limits, first principle, derivative rules.",
 "video": None,
 "card_tag": "Calculus ki entry — limits se derivatives tak",
 "card_topics": [
  "🚪 Limits + LHL/RHL",
  "📐 Standard limits",
  "⚡ Derivative = rate of change",
  "🛠️ Power/product/quotient rules"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Limits — Calculus ka Darwaza",
    "body": "<p><b>Calculus</b> maths ka wo superpower hai jo CHANGE ko measure karta hai — gari ki speed, curve ki slope, population ki growth. Aur calculus ki entry hoti hai <b>limit</b> se. Limit ka matlab: x jab kisi value ke bahut KAREEB jata hai (touch nahi karta!), to function kis value ke kareeb jata hai?</p>\n<ul>\n<li><b>Limit ka idea:</b> lim(x→a) f(x) = L — x, a ke paas aane pe f(x), L ke paas jaata hai.</li>\n<li><b>Feel wala example ⭐:</b> f(x) = (x² − 1)/(x − 1). x = 1 pe 0/0 — undefined! Lekin x = 1.001 daalo to 2.001, x = 0.999 daalo to 1.999 — dono taraf se 2 ke paas. Limit = 2!</li>\n<li><b>Left-hand limit (LHL):</b> chhoti values se approach. <b>Right-hand limit (RHL):</b> badi values se. Limit exist kare ⟺ LHL = RHL ⭐</li>\n<li><b>Limit ≠ value:</b> f(a) defined na bhi ho, limit ho sakti hai (jaise upar wale example me).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: limit = \"kis taraf ja raha hai\", value = \"kahan khada hai\" — dono alag cheezein!</p>"
   },
   {
    "h": "2️⃣ Limits ke Rules aur Standard Limits ⭐",
    "body": "<ul>\n<li><b>Algebra of limits:</b> limits add/subtract/multiply/divide ho jaati hain (denominator ki limit 0 na ho divide me).</li>\n<li><b>Polynomial/direct substitution:</b> x = a direct daal do — kaam kar gaya to wahi limit!</li>\n<li><b>0/0 form ⭐:</b> direct daalne pe 0/0 aaye to FACTOR karo aur cancel karo — (x²−1)/(x−1) = (x+1)(x−1)/(x−1) = x+1 → 2.</li>\n<li><b>Standard limit 1 ⭐:</b> lim(x→0) (sin x)/x = 1 (x radians me!).</li>\n<li><b>Standard limit 2 ⭐:</b> lim(x→0) (tan x)/x = 1.</li>\n<li><b>Standard limit 3 ⭐:</b> lim(x→a) (xⁿ − aⁿ)/(x − a) = n·aⁿ⁻¹.</li>\n<li><b>Standard limit 4:</b> lim(x→0) (1 + x)^(1/x) = e; lim(x→0) (eˣ − 1)/x = 1; lim(x→0) log(1+x)/x = 1.</li>\n</ul>\n<p class=\"small-note\">🎯 90% limit problems: direct substitution → 0/0? → factor/cancel ya standard limit pe lao!</p>"
   },
   {
    "h": "3️⃣ Derivatives — Rate of Change ⭐",
    "body": "<p><b>Derivative</b> = instantaneous rate of change = curve ki slope ek exact point pe. Speedometer socho — average speed nahi, ISS PAL ki speed!</p>\n<ul>\n<li><b>First principle (definition) ⭐:</b> f'(x) = lim(h→0) [f(x + h) − f(x)]/h.</li>\n<li><b>Notation:</b> f'(x), dy/dx, D[f(x)] — sab same matlab.</li>\n<li><b>Geometric meaning ⭐:</b> curve pe (x, f(x)) point pe TANGENT ki slope.</li>\n<li><b>Example (first principle):</b> f(x) = x² → f'(x) = lim(h→0) [(x+h)² − x²]/h = lim(h→0) (2x + h) = 2x.</li>\n<li><b>Physical meaning:</b> s(t) position → s'(t) velocity → s''(t) acceleration.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: average speed = puri trip ka slope; derivative = speedometer ka exact reading — ek instant ka slope!</p>"
   },
   {
    "h": "4️⃣ Derivatives ke Rules ⭐",
    "body": "<ul>\n<li><b>Power rule ⭐:</b> d/dx (xⁿ) = n·xⁿ⁻¹. (x³ → 3x², x → 1, constant → 0)</li>\n<li><b>Constant multiple:</b> d/dx [c·f(x)] = c·f'(x).</li>\n<li><b>Sum/difference rule:</b> d/dx [f ± g] = f' ± g' — term by term karo!</li>\n<li><b>Product rule ⭐:</b> d/dx [u·v] = u'v + uv' — \"first ka derivative × second + first × second ka derivative\".</li>\n<li><b>Quotient rule ⭐:</b> d/dx [u/v] = (u'v − uv')/v² — \"neeche wala square, upar: neech-der minus der-neech\".</li>\n<li><b>Standard derivatives ⭐:</b> d/dx (sin x) = cos x; d/dx (cos x) = −sin x; d/dx (tan x) = sec²x; d/dx (eˣ) = eˣ; d/dx (log x) = 1/x.</li>\n</ul>\n<p class=\"small-note\">🎯 Quotient rule ka order yaad rakho: (u'v − uv') — MINUS hai, order ulta kar diya to sign galt!</p>"
   },
   {
    "h": "5️⃣ Exam Patterns — Limits & Derivatives ka Paper",
    "body": "<ul>\n<li><b>Direct limits:</b> substitution se — free marks.</li>\n<li><b>0/0 limits ⭐:</b> factorize + cancel, ya rationalization (surds me conjugate multiply).</li>\n<li><b>Trig limits ⭐:</b> (sin ax)/(bx) = a/b type — standard limit pe convert karo.</li>\n<li><b>(xⁿ − aⁿ)/(x − a) limits:</b> formula n·aⁿ⁻¹ — super fast.</li>\n<li><b>First principle se derivative ⭐:</b> board exam me compulsory — definition likhna, limit evaluate karna.</li>\n<li><b>Rules se derivative:</b> power/product/quotient — polynomial + trig mix.</li>\n<li><b>LHL/RHL check:</b> \"limit exist karti hai?\" — dono sides nikalo.</li>\n</ul>\n<p class=\"small-note\">💡 Derivative ke questions Class 12 calculus ka 70% base hain — abhi pakka kar lo to aage aasaan!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ सीमा (Limit) — कलन का द्वार",
    "body": "<p><b>कलन (Calculus)</b> गणित की वह शक्ति है जो परिवर्तन को मापती है — गति, ढलान, वृद्धि। और कलन की शुरुआत <b>सीमा</b> से होती है। सीमा का अर्थ: x जब किसी मान के बहुत निकट जाता है (छूता नहीं!), तो फलन किस मान के निकट जाता है?</p>\n<ul>\n<li><b>सीमा की अवधारणा:</b> lim(x→a) f(x) = L — x, a के निकट आने पर f(x), L के निकट जाता है।</li>\n<li><b>उदाहरण ⭐:</b> f(x) = (x² − 1)/(x − 1)। x = 1 पर 0/0 — अपरिभाषित! पर x = 1.001 रखो तो 2.001, x = 0.999 रखो तो 1.999 — दोनों ओर से 2 के निकट। सीमा = 2!</li>\n<li><b>वाम सीमा (LHL):</b> छोटे मानों से। <b>दक्षिण सीमा (RHL):</b> बड़े मानों से। सीमा का अस्तित्व ⟺ LHL = RHL ⭐</li>\n<li><b>सीमा ≠ मान:</b> f(a) परिभाषित न भी हो, सीमा हो सकती है।</li>\n</ul>\n<p class=\"small-note\">💡 सीमा = \"किस ओर जा रहा है\", मान = \"कहाँ खड़ा है\" — दोनों अलग!</p>"
   },
   {
    "h": "2️⃣ सीमा के नियम और मानक सीमाएँ ⭐",
    "body": "<ul>\n<li><b>सीमा का बीजगणित:</b> सीमाएँ जुड़/घटा/गुणा/भाग हो सकती हैं (भाग में हर की सीमा 0 न हो)।</li>\n<li><b>बहुपद:</b> x = a सीधे रखो — बन गया तो वही सीमा!</li>\n<li><b>0/0 रूप ⭐:</b> गुणनखंड करके काटो — (x²−1)/(x−1) = x+1 → 2।</li>\n<li><b>मानक सीमा 1 ⭐:</b> lim(x→0) (sin x)/x = 1 (x रेडियन में!)।</li>\n<li><b>मानक सीमा 2 ⭐:</b> lim(x→0) (tan x)/x = 1।</li>\n<li><b>मानक सीमा 3 ⭐:</b> lim(x→a) (xⁿ − aⁿ)/(x − a) = n·aⁿ⁻¹।</li>\n<li><b>मानक सीमा 4:</b> lim(x→0) (eˣ − 1)/x = 1; lim(x→0) log(1+x)/x = 1।</li>\n</ul>\n<p class=\"small-note\">🎯 90% प्रश्न: प्रतिस्थापन → 0/0? → गुणनखंड या मानक सीमा पर लाओ!</p>"
   },
   {
    "h": "3️⃣ अवकलज (Derivative) — परिवर्तन की दर ⭐",
    "body": "<p><b>अवकलज</b> = तात्क्षणिक परिवर्तन दर = वक्र की ढलान एक निश्चित बिंदु पर। स्पीडोमीटर सोचो — औसत चाल नहीं, इस क्षण की चाल!</p>\n<ul>\n<li><b>प्रथम सिद्धांत (परिभाषा) ⭐:</b> f'(x) = lim(h→0) [f(x + h) − f(x)]/h।</li>\n<li><b>संकेत:</b> f'(x), dy/dx, D[f(x)]।</li>\n<li><b>ज्यामितीय अर्थ ⭐:</b> वक्र पर बिंदु (x, f(x)) पर स्पर्शरेखा की ढलान।</li>\n<li><b>उदाहरण:</b> f(x) = x² → f'(x) = lim(h→0) [(x+h)² − x²]/h = 2x।</li>\n<li><b>भौतिक अर्थ:</b> s(t) स्थिति → s'(t) वेग → s''(t) त्वरण।</li>\n</ul>\n<p class=\"small-note\">💡 औसत चाल = पूरी यात्रा की ढलान; अवकलज = स्पीडोमीटर की क्षणिक रीडिंग!</p>"
   },
   {
    "h": "4️⃣ अवकलज के नियम ⭐",
    "body": "<ul>\n<li><b>घात नियम ⭐:</b> d/dx (xⁿ) = n·xⁿ⁻¹।</li>\n<li><b>अचर गुणक:</b> d/dx [c·f(x)] = c·f'(x)।</li>\n<li><b>योग/अंतर नियम:</b> d/dx [f ± g] = f' ± g'।</li>\n<li><b>गुणन नियम ⭐:</b> d/dx [u·v] = u'v + uv'।</li>\n<li><b>भाग नियम ⭐:</b> d/dx [u/v] = (u'v − uv')/v²।</li>\n<li><b>मानक अवकलज ⭐:</b> (sin x)' = cos x; (cos x)' = −sin x; (tan x)' = sec²x; (eˣ)' = eˣ; (log x)' = 1/x।</li>\n</ul>\n<p class=\"small-note\">🎯 भाग नियम का क्रम याद रखो: (u'v − uv') — MINUS है, क्रम उल्टा तो चिह्न गलत!</p>"
   },
   {
    "h": "5️⃣ परीक्षा के पैटर्न",
    "body": "<ul>\n<li><b>सीधी सीमाएँ:</b> प्रतिस्थापन से।</li>\n<li><b>0/0 सीमाएँ ⭐:</b> गुणनखंड + कटौती, या परिमेयकरण।</li>\n<li><b>त्रिकोणमितीय सीमाएँ ⭐:</b> (sin ax)/(bx) = a/b प्रकार।</li>\n<li><b>(xⁿ − aⁿ)/(x − a) सीमाएँ:</b> सूत्र n·aⁿ⁻¹।</li>\n<li><b>प्रथम सिद्धांत से अवकलज ⭐:</b> बोर्ड में अनिवार्य — परिभाषा + सीमा।</li>\n<li><b>नियमों से अवकलज:</b> घात/गुणन/भाग।</li>\n</ul>\n<p class=\"small-note\">💡 ये प्रश्न कक्षा 12 कलन का 70% आधार हैं — अभी पक्का कर लो!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Limits — the Gateway to Calculus",
    "body": "<p><b>Calculus</b> is the mathematical superpower that measures CHANGE — a car's speed, a curve's slope, a population's growth. And calculus begins with the <b>limit</b>. A limit asks: as x gets very CLOSE to some value (without touching it!), what value does the function approach?</p>\n<ul>\n<li><b>The idea:</b> lim(x→a) f(x) = L — as x nears a, f(x) nears L.</li>\n<li><b>Feel-it example ⭐:</b> f(x) = (x² − 1)/(x − 1). At x = 1 it's 0/0 — undefined! But x = 1.001 gives 2.001, x = 0.999 gives 1.999 — both sides approach 2. The limit is 2!</li>\n<li><b>Left-hand limit (LHL):</b> approach from smaller values. <b>Right-hand limit (RHL):</b> from larger values. The limit exists ⟺ LHL = RHL ⭐</li>\n<li><b>Limit ≠ value:</b> f(a) may not even be defined, yet the limit can exist (like the example above).</li>\n</ul>\n<p class=\"small-note\">💡 Feel it: a limit is \"where it's heading\"; a value is \"where it stands\" — two different things!</p>"
   },
   {
    "h": "2️⃣ Limit Rules and Standard Limits ⭐",
    "body": "<ul>\n<li><b>Algebra of limits:</b> limits add, subtract, multiply, and divide (as long as the denominator's limit isn't 0).</li>\n<li><b>Polynomials/direct substitution:</b> just plug in x = a — if it works, that's the limit!</li>\n<li><b>0/0 form ⭐:</b> if substitution gives 0/0, FACTOR and cancel — (x²−1)/(x−1) = (x+1)(x−1)/(x−1) = x+1 → 2.</li>\n<li><b>Standard limit 1 ⭐:</b> lim(x→0) (sin x)/x = 1 (x in radians!).</li>\n<li><b>Standard limit 2 ⭐:</b> lim(x→0) (tan x)/x = 1.</li>\n<li><b>Standard limit 3 ⭐:</b> lim(x→a) (xⁿ − aⁿ)/(x − a) = n·aⁿ⁻¹.</li>\n<li><b>Standard limit 4:</b> lim(x→0) (eˣ − 1)/x = 1; lim(x→0) log(1+x)/x = 1.</li>\n</ul>\n<p class=\"small-note\">🎯 90% of limit problems: try substitution → 0/0? → factor/cancel or convert to a standard limit!</p>"
   },
   {
    "h": "3️⃣ Derivatives — the Rate of Change ⭐",
    "body": "<p>A <b>derivative</b> is the instantaneous rate of change — the slope of a curve at one exact point. Think of a speedometer — not average speed, but the speed at THIS instant!</p>\n<ul>\n<li><b>First principle (definition) ⭐:</b> f'(x) = lim(h→0) [f(x + h) − f(x)]/h.</li>\n<li><b>Notation:</b> f'(x), dy/dx, D[f(x)] — all mean the same thing.</li>\n<li><b>Geometric meaning ⭐:</b> the slope of the TANGENT to the curve at (x, f(x)).</li>\n<li><b>Example (first principle):</b> f(x) = x² → f'(x) = lim(h→0) [(x+h)² − x²]/h = lim(h→0) (2x + h) = 2x.</li>\n<li><b>Physical meaning:</b> position s(t) → velocity s'(t) → acceleration s''(t).</li>\n</ul>\n<p class=\"small-note\">💡 Feel it: average speed is the slope of the whole trip; the derivative is the speedometer's exact reading — one instant's slope!</p>"
   },
   {
    "h": "4️⃣ Derivative Rules ⭐",
    "body": "<ul>\n<li><b>Power rule ⭐:</b> d/dx (xⁿ) = n·xⁿ⁻¹. (x³ → 3x², x → 1, constant → 0)</li>\n<li><b>Constant multiple:</b> d/dx [c·f(x)] = c·f'(x).</li>\n<li><b>Sum/difference rule:</b> d/dx [f ± g] = f' ± g' — differentiate term by term!</li>\n<li><b>Product rule ⭐:</b> d/dx [u·v] = u'v + uv' — \"derivative of first × second + first × derivative of second\".</li>\n<li><b>Quotient rule ⭐:</b> d/dx [u/v] = (u'v − uv')/v² — \"square the bottom; on top: bottom-der minus der-bottom\".</li>\n<li><b>Standard derivatives ⭐:</b> (sin x)' = cos x; (cos x)' = −sin x; (tan x)' = sec²x; (eˣ)' = eˣ; (log x)' = 1/x.</li>\n</ul>\n<p class=\"small-note\">🎯 Remember the quotient rule's order: (u'v − uv') — it's a MINUS, so swapping the order flips the sign!</p>"
   },
   {
    "h": "5️⃣ Exam Patterns — Limits & Derivatives in Papers",
    "body": "<ul>\n<li><b>Direct limits:</b> by substitution — free marks.</li>\n<li><b>0/0 limits ⭐:</b> factorize + cancel, or rationalize (multiply by the conjugate for surds).</li>\n<li><b>Trig limits ⭐:</b> (sin ax)/(bx) = a/b type — convert to the standard limit.</li>\n<li><b>(xⁿ − aⁿ)/(x − a) limits:</b> use n·aⁿ⁻¹ — super fast.</li>\n<li><b>First-principle derivatives ⭐:</b> compulsory in boards — write the definition, evaluate the limit.</li>\n<li><b>Rule-based derivatives:</b> power/product/quotient — polynomials mixed with trig.</li>\n<li><b>LHL/RHL checks:</b> \"does the limit exist?\" — compute both sides.</li>\n</ul>\n<p class=\"small-note\">💡 These questions form 70% of the base for Class 12 calculus — lock them in now and cruise later!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Limits ⭐",
    "items": [
     "Limit exist ⟺ LHL = RHL",
     "Direct substitution pehle",
     "0/0 → factor + cancel"
    ]
   },
   {
    "h": "Standard Limits ⭐",
    "items": [
     "(sin x)/x → 1",
     "(xⁿ − aⁿ)/(x − a) → n·aⁿ⁻¹",
     "(eˣ − 1)/x → 1"
    ]
   },
   {
    "h": "Derivative ⭐",
    "items": [
     "f'(x) = lim(h→0) [f(x+h) − f(x)]/h",
     "= tangent ki slope",
     "= instantaneous rate of change"
    ]
   },
   {
    "h": "Rules ⭐",
    "items": [
     "(xⁿ)' = n·xⁿ⁻¹",
     "(uv)' = u'v + uv'",
     "(u/v)' = (u'v − uv')/v²"
    ]
   },
   {
    "h": "Standard Derivs",
    "items": [
     "(sin x)' = cos x, (cos x)' = −sin x",
     "(eˣ)' = eˣ, (log x)' = 1/x",
     "(tan x)' = sec²x"
    ]
   }
  ],
  "hi": [
   {
    "h": "सीमा ⭐",
    "items": [
     "अस्तित्व ⟺ LHL = RHL",
     "पहले प्रतिस्थापन",
     "0/0 → गुणनखंड + कटौती"
    ]
   },
   {
    "h": "मानक सीमाएँ ⭐",
    "items": [
     "(sin x)/x → 1",
     "(xⁿ − aⁿ)/(x − a) → n·aⁿ⁻¹",
     "(eˣ − 1)/x → 1"
    ]
   },
   {
    "h": "अवकलज ⭐",
    "items": [
     "f'(x) = lim(h→0) [f(x+h) − f(x)]/h",
     "= स्पर्शरेखा की ढलान",
     "= तात्क्षणिक परिवर्तन दर"
    ]
   },
   {
    "h": "नियम ⭐",
    "items": [
     "(xⁿ)' = n·xⁿ⁻¹",
     "(uv)' = u'v + uv'",
     "(u/v)' = (u'v − uv')/v²"
    ]
   },
   {
    "h": "मानक अवकलज",
    "items": [
     "(sin x)' = cos x, (cos x)' = −sin x",
     "(eˣ)' = eˣ, (log x)' = 1/x",
     "(tan x)' = sec²x"
    ]
   }
  ],
  "en": [
   {
    "h": "Limits ⭐",
    "items": [
     "Limit exists ⟺ LHL = RHL",
     "Try direct substitution first",
     "0/0 → factor + cancel"
    ]
   },
   {
    "h": "Standard Limits ⭐",
    "items": [
     "(sin x)/x → 1",
     "(xⁿ − aⁿ)/(x − a) → n·aⁿ⁻¹",
     "(eˣ − 1)/x → 1"
    ]
   },
   {
    "h": "Derivative ⭐",
    "items": [
     "f'(x) = lim(h→0) [f(x+h) − f(x)]/h",
     "= slope of tangent",
     "= instantaneous rate of change"
    ]
   },
   {
    "h": "Rules ⭐",
    "items": [
     "(xⁿ)' = n·xⁿ⁻¹",
     "(uv)' = u'v + uv'",
     "(u/v)' = (u'v − uv')/v²"
    ]
   },
   {
    "h": "Standard Derivs",
    "items": [
     "(sin x)' = cos x, (cos x)' = −sin x",
     "(eˣ)' = eˣ, (log x)' = 1/x",
     "(tan x)' = sec²x"
    ]
   }
  ]
 },
 "practice": [
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ],
  [
   "q",
   "a"
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/maths/ch-13/",
  "title": "Statistics"
 }
}

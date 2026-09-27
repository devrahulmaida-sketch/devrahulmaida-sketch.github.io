# Class 12 Maths, Chapter 2 - Inverse Trigonometric Functions
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 2,
 "title_en": "Inverse Trigonometric Functions",
 "title_hi": "प्रतिलोम त्रिकोणमितीय फलन",
 "tagline": "Principal values, branch table aur sin⁻¹/cos⁻¹/tan⁻¹ ka pura khel",
 "jee": "MEDIUM",
 "meta_desc": "Class 12 Maths Chapter 2: Inverse Trigonometric Functions — long + short notes in Hindi, English, Hinglish. Principal value branches, domain and range, evaluation of sin⁻¹, cos⁻¹, tan⁻¹.",
 "video": None,
 "card_tag": "Principal values, branch table aur sin⁻¹/cos⁻¹/tan⁻¹ ka pura khel",
 "card_topics": [
  "🔄 Inverse ka concept",
  "📋 Principal value branches",
  "🎯 Value nikalna step-by-step",
  "📉 Graphs + syllabus update"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Inverse Trig Ka Funda — Function Ulta Karna",
    "body": "<ul>\n<li><b>Idea:</b> sin(x) = y ka matlab hai x = sin⁻¹(y) — inverse function angle WAPAS deta hai. \"Kis angle ka sine 1/2 hai?\" → sin⁻¹(1/2) = π/6.</li>\n<li><b>Problem:</b> trig functions periodic hain → infinitely many angles same value dete hain. Inverse banane ke liye domain RESTRICT karte hain taaki function one-one ho jaaye.</li>\n<li><b>Principal value branch ⭐:</b> wo restricted domain jisme function one-one + onto ban jaata hai. Us branch se aane wala answer = <b>principal value</b>.</li>\n<li>sin⁻¹x, cos⁻¹x... likhne ka matlab: \"wo (principal) angle jiska sine/cosine x hai\". sin⁻¹(1) = π/2, sirf π/2 — baaki saare angles (5π/2, 9π/2...) ignore!</li>\n<li>Notation alert: sin⁻¹x ka matlab 1/sin x NAHI hai (wo to cosec x hai) — inverse FUNCTION hai, reciprocal nahi!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: normal function angle se value deta hai; inverse function value se angle deta hai — bas angle ek fixed \"preferred zone\" se aata hai.</p>"
   },
   {
    "h": "2️⃣ Principal Value Branches — Sabse Important Table ⭐⭐",
    "body": "<ul>\n<li><b>sin⁻¹x:</b> domain [−1, 1], range (principal branch) <b>[−π/2, π/2]</b>.</li>\n<li><b>cos⁻¹x:</b> domain [−1, 1], range <b>[0, π]</b>.</li>\n<li><b>tan⁻¹x:</b> domain R (sab reals!), range <b>(−π/2, π/2)</b>.</li>\n<li><b>cot⁻¹x:</b> domain R, range <b>(0, π)</b>.</li>\n<li><b>sec⁻¹x:</b> domain (−∞, −1] ∪ [1, ∞), range <b>[0, π] − {π/2}</b>.</li>\n<li><b>cosec⁻¹x:</b> domain (−∞, −1] ∪ [1, ∞), range <b>[−π/2, π/2] − {0}</b>.</li>\n<li>Trick yaad rakhne ka: <b>sin, tan, cosec ki branch −π/2 se π/2</b> (right half of circle); <b>cos, cot, sec ki 0 se π</b> (upper half). sec/cosec me beech ka point (π/2 ya 0) excluded!</li>\n</ul>\n<p class=\"small-note\">🎯 Ye table = chapter ka 80% marks! Ratta nahi — samajh: jis half-circle me function one-one hai, wahi branch.</p>"
   },
   {
    "h": "3️⃣ Values Nikalna — Step-by-Step Method",
    "body": "<ul>\n<li><b>Step 1:</b> wo angle socho jiska trig value diya ho — sin⁻¹(√3/2) → sin(π/3) = √3/2.</li>\n<li><b>Step 2 ⭐:</b> check karo angle PRINCIPAL BRANCH me hai ya nahi. π/3 ∈ [−π/2, π/2] ✓ → answer π/3.</li>\n<li><b>Negative input:</b> sin⁻¹(−1/2): sin(−π/6) = −1/2 aur −π/6 branch me hai → <b>−π/6</b>. cos⁻¹(−1/2): cos(2π/3) = −1/2, 2π/3 ∈ [0, π] ✓ → <b>2π/3</b>.</li>\n<li><b>Standard values yaad karo:</b> 0, 1/2, 1/√2, √3/2, 1 ke liye π/6, π/4, π/3, π/2 family — bina table ke instant aana chahiye.</li>\n<li><b>tan⁻¹(−√3):</b> tan(−π/3) = −√3 → <b>−π/3</b> (branch (−π/2, π/2) me hai).</li>\n</ul>\n<p class=\"small-note\">💡 Hamesha 2 sawaal: (1) kis angle ka value ye hai? (2) kya wo angle branch ke andar hai? Nahi hai to equivalent angle lo jo andar ho.</p>"
   },
   {
    "h": "4️⃣ Graphs aur Behaviour",
    "body": "<ul>\n<li><b>sin⁻¹x ka graph:</b> −1 se 1 tak rising curve, (−1, −π/2) se (1, π/2) — origin se pass, odd function jaisa symmetric.</li>\n<li><b>cos⁻¹x ka graph:</b> falling curve — (−1, π) se (1, 0). x badhane pe value GHATTI hai (sin⁻¹ se ulta!).</li>\n<li><b>tan⁻¹x ka graph:</b> poori real line pe rising S-curve, dono taraf ±π/2 ko approach karta hai (asymptotes) — kabhi touch nahi karta.</li>\n<li>Inverse trig functions <b>increasing ya decreasing strictly</b> hote hain apni branch pe — isliye one-one hain.</li>\n<li>Domain ke bahar function undefined: sin⁻¹(2) likhna hi galat hai — 2 domain [−1, 1] me nahi!</li>\n</ul>\n<p class=\"small-note\">💡 Graph se yaad rakho: sin⁻¹ ↑, cos⁻¹ ↓, tan⁻¹ S-shape with walls at ±π/2.</p>"
   },
   {
    "h": "5️⃣ Syllabus Note aur Typical Exam Pattern",
    "body": "<ul>\n<li><b>Rationalized syllabus ⭐:</b> inverse trig ki <b>elementary properties</b> (addition formulas, sin⁻¹x + cos⁻¹x = π/2 type identities, 2tan⁻¹x conversions) NCERT/CBSE se <b>DELETE</b> ho chuki hain — unke proof/simplify questions ab nahi aate.</li>\n<li><b>Ab kya aata hai:</b> principal values nikalna, domain/range poochna, simple evaluation (sin⁻¹(1/2), cos⁻¹(−√3/2) type), aur branch pe based one-liners.</li>\n<li><b>Board tip:</b> answer hamesha PRINCIPAL VALUE me do — radians me (π/6 likho, 30° nahi, jab tak degree na maanga ho).</li>\n<li><b>Common mistake:</b> cos⁻¹(−1/2) ko −π/3 likh dena — −π/3 branch [0, π] me NAHI hai! Sahi: 2π/3.</li>\n<li>JEE me ye chapter chhota hai par integration/differentiation me inverse trig aata rehta hai — branch concept wahan kaam aayega.</li>\n</ul>\n<p class=\"small-note\">🎯 Formula-heavy identities gayab, concept-focused chapter bacha — branch table + principal value practice = full marks.</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ प्रतिलोम त्रिकोणमिति का मूल — फलन उल्टा करना",
    "body": "<ul>\n<li><b>मूल विचार:</b> sin(x) = y का अर्थ x = sin⁻¹(y) — प्रतिलोम फलन कोण <b>वापस</b> देता है।</li>\n<li><b>समस्या:</b> त्रिकोणमितीय फलन आवर्ती हैं → अनंत कोण एक ही मान देते हैं। प्रतिलोम के लिए प्रांत <b>प्रतिबंधित</b> करना पड़ता है ताकि फलन एकैकी हो।</li>\n<li><b>मुख्य मान शाखा ⭐:</b> वह प्रतिबंधित प्रांत जिसमें फलन एकैकी + आच्छादक हो। उस शाखा का उत्तर = <b>मुख्य मान</b>।</li>\n<li>sin⁻¹(1) = π/2 — केवल π/2, अन्य सभी कोण (5π/2...) छोड़ दो!</li>\n<li>सावधान: sin⁻¹x का अर्थ 1/sin x <b>नहीं</b> (वह cosec x है) — यह प्रतिलोम <b>फलन</b> है, व्युत्क्रम नहीं!</li>\n</ul>\n<p class=\"small-note\">💡 सामान्य फलन कोण से मान देता है; प्रतिलोम मान से कोण देता है — कोण एक निश्चित क्षेत्र से आता है।</p>"
   },
   {
    "h": "2️⃣ मुख्य मान शाखाएं — सबसे महत्वपूर्ण तालिका ⭐⭐",
    "body": "<ul>\n<li><b>sin⁻¹x:</b> प्रांत [−1, 1], परिसर <b>[−π/2, π/2]</b>।</li>\n<li><b>cos⁻¹x:</b> प्रांत [−1, 1], परिसर <b>[0, π]</b>।</li>\n<li><b>tan⁻¹x:</b> प्रांत R, परिसर <b>(−π/2, π/2)</b>।</li>\n<li><b>cot⁻¹x:</b> प्रांत R, परिसर <b>(0, π)</b>।</li>\n<li><b>sec⁻¹x:</b> प्रांत (−∞, −1] ∪ [1, ∞), परिसर <b>[0, π] − {π/2}</b>।</li>\n<li><b>cosec⁻¹x:</b> प्रांत (−∞, −1] ∪ [1, ∞), परिसर <b>[−π/2, π/2] − {0}</b>।</li>\n<li>याद रखने की युक्ति: <b>sin, tan, cosec की शाखा −π/2 से π/2</b>; <b>cos, cot, sec की 0 से π</b>।</li>\n</ul>\n<p class=\"small-note\">🎯 यह तालिका = अध्याय के 80% अंक! जिस अर्धवृत्त में फलन एकैकी है, वही शाखा।</p>"
   },
   {
    "h": "3️⃣ मान निकालना — चरण-दर-चरण विधि",
    "body": "<ul>\n<li><b>चरण 1:</b> वह कोण सोचो जिसका त्रिकोणमितीय मान दिया हो — sin⁻¹(√3/2) → sin(π/3) = √3/2।</li>\n<li><b>चरण 2 ⭐:</b> जांचो कि कोण <b>मुख्य शाखा</b> में है या नहीं। π/3 ∈ [−π/2, π/2] ✓ → उत्तर π/3।</li>\n<li><b>ऋणात्मक इनपुट:</b> sin⁻¹(−1/2) = <b>−π/6</b> (शाखा में); cos⁻¹(−1/2) = <b>2π/3</b> (क्योंकि 2π/3 ∈ [0, π])।</li>\n<li><b>मानक मान याद करो:</b> 0, 1/2, 1/√2, √3/2, 1 — तुरंत आने चाहिए।</li>\n<li><b>tan⁻¹(−√3)</b> = <b>−π/3</b> (शाखा (−π/2, π/2) में)।</li>\n</ul>\n<p class=\"small-note\">💡 सदैव 2 प्रश्न: (1) किस कोण का मान यह है? (2) क्या वह शाखा के अंदर है? नहीं, तो अंदर वाला तुल्य कोण लो।</p>"
   },
   {
    "h": "4️⃣ आलेख और व्यवहार",
    "body": "<ul>\n<li><b>sin⁻¹x:</b> बढ़ता वक्र, (−1, −π/2) से (1, π/2) — मूल बिंदु से होकर।</li>\n<li><b>cos⁻¹x:</b> घटता वक्र — (−1, π) से (1, 0)। x बढ़ने पर मान <b>घटता</b> है।</li>\n<li><b>tan⁻¹x:</b> पूरी वास्तविक रेखा पर S-आकार, ±π/2 की ओर अग्रसर (अनंतस्पर्शी)।</li>\n<li>प्रतिलोम त्रिकोणमितीय फलन अपनी शाखा पर <b>निरंतर वर्धमान या ह्रासमान</b> — इसीलिए एकैकी।</li>\n<li>प्रांत के बाहर अपरिभाषित: sin⁻¹(2) लिखना ही गलत है!</li>\n</ul>\n<p class=\"small-note\">💡 sin⁻¹ ↑, cos⁻¹ ↓, tan⁻¹ S-आकार ±π/2 की दीवारों के साथ।</p>"
   },
   {
    "h": "5️⃣ पाठ्यक्रम टिप्पणी और परीक्षा पैटर्न",
    "body": "<ul>\n<li><b>युक्तिसंगत पाठ्यक्रम ⭐:</b> प्रतिलोम त्रिकोणमितीय फलनों के <b>प्राथमिक गुणधर्म</b> NCERT/CBSE से <b>हटा दिए गए</b> हैं।</li>\n<li><b>अब क्या आता है:</b> मुख्य मान, प्रांत/परिसर, सरल मूल्यांकन।</li>\n<li><b>बोर्ड टिप:</b> उत्तर सदैव <b>मुख्य मान</b> में, रेडियन में दो।</li>\n<li><b>सामान्य गलती:</b> cos⁻¹(−1/2) = −π/3 लिखना — −π/3 शाखा [0, π] में नहीं! सही: <b>2π/3</b>।</li>\n<li>JEE में समाकलन/अवकलन में प्रतिलोम त्रिकोणमिति आती रहती है — शाखा की अवधारणा काम आएगी।</li>\n</ul>\n<p class=\"small-note\">🎯 सूत्र-भारी सर्वसमिकाएं गईं — शाखा तालिका + मुख्य मान अभ्यास = पूर्ण अंक।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ The Core Idea — Reversing a Trig Function",
    "body": "<ul>\n<li><b>Idea:</b> sin(x) = y means x = sin⁻¹(y) — the inverse function hands the angle BACK. \"Which angle has sine 1/2?\" → sin⁻¹(1/2) = π/6.</li>\n<li><b>Problem:</b> trig functions are periodic → infinitely many angles give the same value. To build an inverse, we RESTRICT the domain so the function becomes one-one.</li>\n<li><b>Principal value branch ⭐:</b> that restricted domain where the function is one-one and onto. The answer from that branch is the <b>principal value</b>.</li>\n<li>sin⁻¹(1) = π/2, only π/2 — every other angle (5π/2, 9π/2...) is ignored!</li>\n<li>Notation alert: sin⁻¹x is NOT 1/sin x (that is cosec x) — it is an inverse FUNCTION, not a reciprocal!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: the normal function turns an angle into a value; the inverse turns a value into an angle — from one fixed \"preferred zone\".</p>"
   },
   {
    "h": "2️⃣ Principal Value Branches — The Most Important Table ⭐⭐",
    "body": "<ul>\n<li><b>sin⁻¹x:</b> domain [−1, 1], range (principal branch) <b>[−π/2, π/2]</b>.</li>\n<li><b>cos⁻¹x:</b> domain [−1, 1], range <b>[0, π]</b>.</li>\n<li><b>tan⁻¹x:</b> domain R (all reals!), range <b>(−π/2, π/2)</b>.</li>\n<li><b>cot⁻¹x:</b> domain R, range <b>(0, π)</b>.</li>\n<li><b>sec⁻¹x:</b> domain (−∞, −1] ∪ [1, ∞), range <b>[0, π] − {π/2}</b>.</li>\n<li><b>cosec⁻¹x:</b> domain (−∞, −1] ∪ [1, ∞), range <b>[−π/2, π/2] − {0}</b>.</li>\n<li>Memory trick: <b>sin, tan, cosec take −π/2 to π/2</b> (right half of the circle); <b>cos, cot, sec take 0 to π</b> (upper half). sec/cosec exclude the midpoint (π/2 or 0)!</li>\n</ul>\n<p class=\"small-note\">🎯 This table = 80% of the chapter's marks! Don't memorize blindly — understand: whichever half-circle makes the function one-one, that is the branch.</p>"
   },
   {
    "h": "3️⃣ Finding Values — Step-by-Step",
    "body": "<ul>\n<li><b>Step 1:</b> think of the angle whose trig value is given — sin⁻¹(√3/2) → sin(π/3) = √3/2.</li>\n<li><b>Step 2 ⭐:</b> check the angle lies in the PRINCIPAL BRANCH. π/3 ∈ [−π/2, π/2] ✓ → answer π/3.</li>\n<li><b>Negative input:</b> sin⁻¹(−1/2): sin(−π/6) = −1/2 and −π/6 is in the branch → <b>−π/6</b>. cos⁻¹(−1/2): cos(2π/3) = −1/2, 2π/3 ∈ [0, π] ✓ → <b>2π/3</b>.</li>\n<li><b>Memorize standard values:</b> 0, 1/2, 1/√2, √3/2, 1 → the π/6, π/4, π/3, π/2 family — must be instant.</li>\n<li><b>tan⁻¹(−√3):</b> tan(−π/3) = −√3 → <b>−π/3</b> (inside the branch (−π/2, π/2)).</li>\n</ul>\n<p class=\"small-note\">💡 Always ask 2 questions: (1) which angle has this value? (2) is it inside the branch? If not, take the equivalent angle that is.</p>"
   },
   {
    "h": "4️⃣ Graphs and Behaviour",
    "body": "<ul>\n<li><b>sin⁻¹x graph:</b> rising curve from (−1, −π/2) to (1, π/2) — passes through the origin.</li>\n<li><b>cos⁻¹x graph:</b> falling curve — (−1, π) to (1, 0). As x grows, the value DROPS (opposite of sin⁻¹!).</li>\n<li><b>tan⁻¹x graph:</b> rising S-curve over the whole real line, approaching ±π/2 on both sides (asymptotes) — never touching them.</li>\n<li>Inverse trig functions are <b>strictly increasing or decreasing</b> on their branch — that is why they are one-one.</li>\n<li>Outside the domain the function is undefined: writing sin⁻¹(2) is simply wrong — 2 is not in [−1, 1]!</li>\n</ul>\n<p class=\"small-note\">💡 Remember by graph: sin⁻¹ ↑, cos⁻¹ ↓, tan⁻¹ S-shape with walls at ±π/2.</p>"
   },
   {
    "h": "5️⃣ Syllabus Note and Typical Exam Pattern",
    "body": "<ul>\n<li><b>Rationalized syllabus ⭐:</b> the <b>elementary properties</b> of inverse trig functions (addition formulas, sin⁻¹x + cos⁻¹x = π/2 type identities, 2tan⁻¹x conversions) are <b>DELETED</b> from NCERT/CBSE — their proofs and simplification questions no longer come.</li>\n<li><b>What still comes:</b> finding principal values, asking domain/range, simple evaluation (sin⁻¹(1/2), cos⁻¹(−√3/2) type), and branch-based one-liners.</li>\n<li><b>Board tip:</b> always give the answer as the PRINCIPAL VALUE, in radians (write π/6, not 30°, unless degrees are asked).</li>\n<li><b>Common mistake:</b> writing cos⁻¹(−1/2) = −π/3 — −π/3 is NOT in the branch [0, π]! Correct: 2π/3.</li>\n<li>For JEE the chapter is small but inverse trig keeps appearing in integration/differentiation — the branch concept helps there.</li>\n</ul>\n<p class=\"small-note\">🎯 Formula-heavy identities are gone, the chapter is concept-focused — branch table + principal value practice = full marks.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Concept",
    "items": [
     "Inverse = value se angle",
     "Domain restrict karke one-one banate",
     "sin⁻¹x ≠ 1/sin x"
    ]
   },
   {
    "h": "Branches ⭐⭐",
    "items": [
     "sin⁻¹: [−π/2, π/2]",
     "cos⁻¹: [0, π]",
     "tan⁻¹: (−π/2, π/2)"
    ]
   },
   {
    "h": "Branches 2 ⭐",
    "items": [
     "cot⁻¹: (0, π), domain R",
     "sec⁻¹: [0,π] − {π/2}",
     "cosec⁻¹: [−π/2,π/2] − {0}"
    ]
   },
   {
    "h": "Evaluation ⭐",
    "items": [
     "Angle socho → branch check karo",
     "Negative input: branch wala equivalent angle",
     "Answer radians me, principal value"
    ]
   },
   {
    "h": "Syllabus ⭐",
    "items": [
     "Elementary properties DELETED",
     "Domain/range + principal values focus",
     "sin⁻¹ ↑, cos⁻¹ ↓, tan⁻¹ S-shape"
    ]
   }
  ],
  "hi": [
   {
    "h": "अवधारणा",
    "items": [
     "प्रतिलोम = मान से कोण",
     "प्रांत प्रतिबंधित → एकैकी",
     "sin⁻¹x ≠ 1/sin x"
    ]
   },
   {
    "h": "शाखाएं ⭐⭐",
    "items": [
     "sin⁻¹: [−π/2, π/2]",
     "cos⁻¹: [0, π]",
     "tan⁻¹: (−π/2, π/2)"
    ]
   },
   {
    "h": "शाखाएं 2 ⭐",
    "items": [
     "cot⁻¹: (0, π)",
     "sec⁻¹: [0,π] − {π/2}",
     "cosec⁻¹: [−π/2,π/2] − {0}"
    ]
   },
   {
    "h": "मूल्यांकन ⭐",
    "items": [
     "कोण सोचो → शाखा जांचो",
     "ऋणात्मक: शाखा वाला तुल्य कोण",
     "उत्तर रेडियन में, मुख्य मान"
    ]
   },
   {
    "h": "पाठ्यक्रम ⭐",
    "items": [
     "प्राथमिक गुणधर्म हटाए गए",
     "प्रांत/परिसर + मुख्य मान",
     "sin⁻¹ ↑, cos⁻¹ ↓, tan⁻¹ S"
    ]
   }
  ],
  "en": [
   {
    "h": "Concept",
    "items": [
     "Inverse = value → angle",
     "Restrict domain to make one-one",
     "sin⁻¹x ≠ 1/sin x"
    ]
   },
   {
    "h": "Branches ⭐⭐",
    "items": [
     "sin⁻¹: [−π/2, π/2]",
     "cos⁻¹: [0, π]",
     "tan⁻¹: (−π/2, π/2)"
    ]
   },
   {
    "h": "Branches 2 ⭐",
    "items": [
     "cot⁻¹: (0, π), domain R",
     "sec⁻¹: [0,π] − {π/2}",
     "cosec⁻¹: [−π/2,π/2] − {0}"
    ]
   },
   {
    "h": "Evaluation ⭐",
    "items": [
     "Find angle → check branch",
     "Negative input: equivalent angle in branch",
     "Answer in radians, principal value"
    ]
   },
   {
    "h": "Syllabus ⭐",
    "items": [
     "Elementary properties DELETED",
     "Domain/range + principal values focus",
     "sin⁻¹ ↑, cos⁻¹ ↓, tan⁻¹ S-shape"
    ]
   }
  ]
 },
 "practice": [
  [
   "sin⁻¹(1/2) ki principal value kya hai?",
   "sin(π/6) = 1/2 aur π/6 ∈ [−π/2, π/2] → <b>π/6</b>."
  ],
  [
   "cos⁻¹(−1/2) ka principal value?",
   "cos(2π/3) = −1/2 aur 2π/3 ∈ [0, π] → <b>2π/3</b>. (−π/3 mat likhna — branch me nahi!)"
  ],
  [
   "tan⁻¹(1) ka principal value?",
   "tan(π/4) = 1, π/4 ∈ (−π/2, π/2) → <b>π/4</b>."
  ],
  [
   "tan⁻¹x ka domain aur range?",
   "Domain <b>R (saare reals)</b>, range <b>(−π/2, π/2)</b>."
  ],
  [
   "sin⁻¹(−√3/2) kya hai?",
   "sin(−π/3) = −√3/2, −π/3 branch me → <b>−π/3</b>."
  ],
  [
   "cos⁻¹(0) ka value?",
   "cos(π/2) = 0, π/2 ∈ [0, π] → <b>π/2</b>."
  ],
  [
   "sec⁻¹x ka domain kya hai?",
   "<b>(−∞, −1] ∪ [1, ∞)</b> — |x| ≥ 1, kyunki sec ki range [−1, 1] ke bahar hoti hai."
  ],
  [
   "sin⁻¹(2) defined hai?",
   "<b>Nahi</b> — 2 domain [−1, 1] ke bahar hai. Kisi angle ka sine 2 ho hi nahi sakta!"
  ],
  [
   "cosec⁻¹(2) ka principal value?",
   "cosec(π/6) = 2, π/6 ∈ [−π/2, π/2] − {0} → <b>π/6</b>."
  ],
  [
   "sin⁻¹x + cos⁻¹x = π/2 identity ab bhi syllabus me hai?",
   "<b>Nahi</b> — elementary properties rationalized syllabus me <b>delete</b> ho chuki hain. Ab principal values aur domain/range pe focus hai."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-3/",
  "title": "Matrices"
 }
}

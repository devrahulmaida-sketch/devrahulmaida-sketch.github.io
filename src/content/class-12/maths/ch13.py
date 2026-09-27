# Class 12 Maths, Chapter 13 - Probability
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 13,
 "title_en": "Probability",
 "title_hi": "प्रायिकता",
 "tagline": "Conditional probability se Bayes' theorem tak — board ka last boss",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 13: Probability — long + short notes in Hindi, English, Hinglish. Conditional probability, multiplication theorem, independent events, total probability, Bayes' theorem, random variables and mean.",
 "video": None,
 "card_tag": "Conditional probability se Bayes' theorem tak — board ka last boss",
 "card_topics": [
  "🎲 Conditional probability",
  "🔗 Independent events",
  "🌳 Total probability + Bayes",
  "📊 Distributions + mean"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Conditional Probability — 'Diya Gaya Hai Ki...' ⭐⭐",
    "body": "<ul>\n<li><b>Concept ⭐⭐:</b> P(A|B) = event A ki probability <b>jab B ho CHUKA hai</b> — extra information se sample space SIKUD jaata hai!</li>\n<li><b>Formula ⭐⭐:</b> <b>P(A|B) = P(A ∩ B) / P(B)</b>, jahan P(B) ≠ 0. \"B ke hone pe A ki probability\".</li>\n<li>Example: die pe 4 aaya hai (B). Even number aane ki probability? P(A|B) = P({4})/P({2,4,6})... wait — B = {4} diya hai to P(even | {4} aaya) = <b>1</b> (4 to even hai hi!). Sample space ab sirf {4}.</li>\n<li><b>Shrink the universe ⭐:</b> B ke hone ke baad sample space = sirf B. Us chhote universe me A wale outcomes count karo — formula ka yehi matlab hai.</li>\n<li>Properties: P(S|B) = 1; P(A′|B) = 1 − P(A|B); P((A ∪ B)|C) = P(A|C) + P(B|C) − P((A ∩ B)|C).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: \"diya gaya hai ki\" = duniya chhoti ho gayi. Ab sirf B wali duniya me A kitna likely hai — bas yehi hisaab hai.</p>"
   },
   {
    "h": "2️⃣ Multiplication Theorem aur Independent Events ⭐⭐",
    "body": "<ul>\n<li><b>Multiplication theorem ⭐:</b> P(A ∩ B) = <b>P(A)·P(B|A)</b> = P(B)·P(A|B) — \"pehle A, phir A ke saath B\" style me dono ka joint chance.</li>\n<li><b>Independent events ⭐⭐:</b> ek event ka hona doosre ki probability CHANGE na kare — <b>P(A|B) = P(A)</b> ya <b>P(A ∩ B) = P(A)·P(B)</b>. (Toss + die: coin ka result die ko affect nahi karta!)</li>\n<li><b>Independent vs mutually exclusive ⭐⭐:</b> MUTUALLY EXCLUSIVE = saath ho hi nahi sakte (P(A∩B) = 0). INDEPENDENT = ek doosre ko affect nahi karte. DONO ALAG concepts hain — non-trivial events dono ek saath nahi ho sakte! (Exam trap!)</li>\n<li>Teen events independent: P(A∩B∩C) = P(A)P(B)P(C) + SAARE pairs bhi independent honi chahiye (pairwise + mutual!).</li>\n<li>Example: 2 cards WITHOUT replacement — draws independent NAHI (pehla card deck badal deta hai). WITH replacement — independent!</li>\n</ul>\n<p class=\"small-note\">🎯 \"Without replacement\" dekho to independence check zaroor karo — yahi boards ka favourite confusion point hai.</p>"
   },
   {
    "h": "3️⃣ Total Probability Theorem ⭐⭐",
    "body": "<ul>\n<li><b>Setup:</b> sample space EVENTS E₁, E₂, ..., Eₙ me partition ho (sab disjoint, milke poora S) — jaise 3 machines, 2 bags, alag routes.</li>\n<li><b>Theorem ⭐⭐:</b> P(A) = <b>P(E₁)P(A|E₁) + P(E₂)P(A|E₂) + ... + P(Eₙ)P(A|Eₙ)</b> — har raaste ka (probability × uss raaste pe A ka chance), sab ADD karo!</li>\n<li>Example: 2 bags — Bag I: 3 red, 2 black; Bag II: 2 red, 3 black. Bag randomly choose (1/2 each) → P(red) = (1/2)(3/5) + (1/2)(2/5) = <b>1/2</b>.</li>\n<li><b>Tree diagram ⭐:</b> branches banao — pehle partition (E₁, E₂), phir har branch pe A ya A′. Multiply along branch, add across branches — theorem visual ban jaata hai!</li>\n<li>Kab use kare: jab event A ke hone ke <b>MULTIPLE raaste</b> hon aur har raaste ka apna chance ho.</li>\n</ul>\n<p class=\"small-note\">💡 Total probability = \"sab raaston ka hisaab jod do\". Weighted average jaisi cheez — har raasta apne weight ke saath contribute karta hai.</p>"
   },
   {
    "h": "4️⃣ Bayes' Theorem — Result Se Wapsi ⭐⭐",
    "body": "<ul>\n<li><b>Question type:</b> event A ho GAYA (defective item mil gaya!) — ab poocho: wo kis RAASTE (machine/bag) se aaya hoga? = <b>reverse (posterior) probability</b>.</li>\n<li><b>Formula ⭐⭐:</b> P(Eᵢ|A) = <b>P(Eᵢ)P(A|Eᵢ) / [Σⱼ P(Eⱼ)P(A|Eⱼ)]</b> — \"us raaste ka contribution ÷ total probability (denominator = total probability theorem!)\".</li>\n<li><b>Steps ⭐:</b> (1) Partitions E₁, E₂... aur unki PRIOR probabilities likho. (2) Har Eᵢ pe P(A|Eᵢ) likho. (3) Denominator = total probability nikalo. (4) Ratio = answer.</li>\n<li>Example: machines M1 (60% output, 1% defective), M2 (40% output, 2% defective). Defective item mila → P(M1 se) = (0.6×0.01)/(0.6×0.01 + 0.4×0.02) = 0.006/0.014 = <b>3/7</b>.</li>\n<li><b>Real life:</b> medical tests, spam filters, fault detection — sab Bayes pe chalte hain!</li>\n</ul>\n<p class=\"small-note\">🎯 Bayes = \"hisaab ulta karo\". Pehle total probability se denominator banao — 90% students ka step yahi hai. Denominator = question ka half work done!</p>"
   },
   {
    "h": "5️⃣ Random Variables aur Probability Distribution ⭐",
    "body": "<ul>\n<li><b>Random variable X ⭐:</b> experiment ke har outcome ko ek NUMBER assign karta hai — 2 coins me heads ka count: X = 0, 1, 2.</li>\n<li><b>Probability distribution ⭐:</b> har value xᵢ ke saath uski probability P(X = xᵢ) ki <b>table</b>. Rules: har P(xᵢ) ≥ 0 aur <b>ΣP(xᵢ) = 1</b> (ye check exam me puchte hain!).</li>\n<li><b>Mean / Expectation ⭐⭐:</b> <b>E(X) = μ = Σ xᵢ·P(xᵢ)</b> — value × probability ka sum = \"long-run average\".</li>\n<li>Example: X = heads in 2 tosses → distribution: P(0) = 1/4, P(1) = 1/2, P(2) = 1/4 → E(X) = 0(1/4) + 1(1/2) + 2(1/4) = <b>1</b>. (2 tosses me average 1 head — obvious sa, par prove ho gaya!)</li>\n<li><b>Syllabus note ⭐:</b> random variable ka <b>VARIANCE</b> (aur binomial distribution) rationalized NCERT se <b>DELETE</b> — sirf distribution + MEAN padhna hai.</li>\n</ul>\n<p class=\"small-note\">💡 E(X) = \"expected value\" — ek baar ka guaranteed nahi, LAMBE run ka average. Distribution table + Σxᵢpᵢ = chapter ka last formula!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ सप्रतिबंध प्रायिकता — 'दिया गया है कि...' ⭐⭐",
    "body": "<ul>\n<li><b>अवधारणा ⭐⭐:</b> P(A|B) = घटना A की प्रायिकता <b>जब B हो चुकी है</b> — अतिरिक्त सूचना से प्रतिदर्श समष्टि <b>सिकुड़</b> जाती है!</li>\n<li><b>सूत्र ⭐⭐:</b> <b>P(A|B) = P(A ∩ B) / P(B)</b>, जहां P(B) ≠ 0।</li>\n<li>उदाहरण: पासे पर B = सम संख्या {2,4,6} दी गई। P(4 आया | B) = P({4})/P({2,4,6}) = <b>1/3</b>।</li>\n<li><b>ब्रह्मांड सिकोड़ो ⭐:</b> B के बाद प्रतिदर्श समष्टि = केवल B — उसमें A वाले परिणाम गिनो।</li>\n<li>गुण: P(S|B) = 1; P(A′|B) = 1 − P(A|B)।</li>\n</ul>\n<p class=\"small-note\">💡 \"दिया गया है कि\" = दुनिया छोटी हो गई। अब B वाली दुनिया में A कितना संभावित?</p>"
   },
   {
    "h": "2️⃣ गुणन प्रमेय और स्वतंत्र घटनाएं ⭐⭐",
    "body": "<ul>\n<li><b>गुणन प्रमेय ⭐:</b> P(A ∩ B) = <b>P(A)·P(B|A)</b> = P(B)·P(A|B)।</li>\n<li><b>स्वतंत्र घटनाएं ⭐⭐:</b> एक का होना दूसरी की प्रायिकता <b>न</b> बदले — <b>P(A ∩ B) = P(A)·P(B)</b>।</li>\n<li><b>स्वतंत्र बनाम परस्पर अपवर्जी ⭐⭐:</b> अपवर्जी = साथ हो ही नहीं सकतीं (P(A∩B) = 0)। स्वतंत्र = प्रभाव नहीं डालतीं। <b>दोनों अलग अवधारणाएं!</b> (परीक्षा जाल!)</li>\n<li>उदाहरण: प्रतिस्थापन <b>बिना</b> पत्ते निकालना — खींचे स्वतंत्र <b>नहीं</b>; प्रतिस्थापन <b>सहित</b> — स्वतंत्र!</li>\n</ul>\n<p class=\"small-note\">🎯 \"बिना प्रतिस्थापन\" देखो तो स्वतंत्रता जांचो — बोर्ड का प्रिय भ्रम बिंदु!</p>"
   },
   {
    "h": "3️⃣ कुल प्रायिकता प्रमेय ⭐⭐",
    "body": "<ul>\n<li><b>व्यवस्था:</b> प्रतिदर्श समष्टि घटनाओं E₁, E₂, ..., Eₙ में <b>विभाजित</b> (सब असंयुक्त, मिलकर पूरी S)।</li>\n<li><b>प्रमेय ⭐⭐:</b> P(A) = <b>P(E₁)P(A|E₁) + P(E₂)P(A|E₂) + ... + P(Eₙ)P(A|Eₙ)</b> — प्रत्येक रास्ते का (प्रायिकता × उस रास्ते पर A), सब जोड़ो!</li>\n<li>उदाहरण: 2 थैले — I: 3 लाल, 2 काले; II: 2 लाल, 3 काले। P(लाल) = (1/2)(3/5) + (1/2)(2/5) = <b>1/2</b>।</li>\n<li><b>वृक्ष आरेख ⭐:</b> शाखाएं बनाओ — शाखा पर गुणा, शाखाओं के बीच जोड़!</li>\n</ul>\n<p class=\"small-note\">💡 कुल प्रायिकता = \"सभी रास्तों का हिसाब जोड़ो\" — भारित औसत जैसा।</p>"
   },
   {
    "h": "4️⃣ बेज प्रमेय — परिणाम से वापसी ⭐⭐",
    "body": "<ul>\n<li><b>प्रश्न प्रकार:</b> घटना A हो <b>गई</b> (दोषपूर्ण वस्तु मिली!) — कौन-से <b>रास्ते</b> (मशीन/थैले) से आई? = <b>उत्तर प्रायिकता</b>।</li>\n<li><b>सूत्र ⭐⭐:</b> P(Eᵢ|A) = <b>P(Eᵢ)P(A|Eᵢ) / [Σⱼ P(Eⱼ)P(A|Eⱼ)]</b> — हर = कुल प्रायिकता प्रमेय!</li>\n<li><b>चरण ⭐:</b> (1) विभाजन E₁, E₂... और उनकी <b>पूर्व</b> प्रायिकताएं लिखो। (2) प्रत्येक पर P(A|Eᵢ)। (3) हर = कुल प्रायिकता। (4) अनुपात = उत्तर।</li>\n<li>उदाहरण: M1 (60% उत्पादन, 1% दोषपूर्ण), M2 (40%, 2%)। दोषपूर्ण मिली → P(M1) = 0.006/0.014 = <b>3/7</b>।</li>\n</ul>\n<p class=\"small-note\">🎯 बेज = \"हिसाब उल्टा करो\"। हर = कुल प्रायिकता — यही आधा काम!</p>"
   },
   {
    "h": "5️⃣ यादृच्छिक चर और प्रायिकता बंटन ⭐",
    "body": "<ul>\n<li><b>यादृच्छिक चर X ⭐:</b> प्रत्येक परिणाम को एक <b>संख्या</b> देता है — 2 सिक्कों में चितों की संख्या: X = 0, 1, 2।</li>\n<li><b>प्रायिकता बंटन ⭐:</b> प्रत्येक xᵢ के साथ P(X = xᵢ) की <b>तालिका</b>। नियम: P(xᵢ) ≥ 0 और <b>ΣP(xᵢ) = 1</b>।</li>\n<li><b>माध्य / प्रत्याशा ⭐⭐:</b> <b>E(X) = μ = Σ xᵢ·P(xᵢ)</b> — \"दीर्घावधि का औसत\"।</li>\n<li>उदाहरण: 2 टॉस में चित → P(0)=1/4, P(1)=1/2, P(2)=1/4 → E(X) = 0 + 1/2 + 1/2 = <b>1</b>।</li>\n<li><b>पाठ्यक्रम टिप्पणी ⭐:</b> <b>प्रसरण (variance)</b> और द्विपद बंटन NCERT से <b>हटाए गए</b> — केवल बंटन + माध्य।</li>\n</ul>\n<p class=\"small-note\">💡 E(X) = \"अपेक्षित मान\" — लंबे रन का औसत। तालिका + Σxᵢpᵢ = अंतिम सूत्र!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Conditional Probability — 'Given That...' ⭐⭐",
    "body": "<ul>\n<li><b>Concept ⭐⭐:</b> P(A|B) = the probability of A <b>given that B has ALREADY happened</b> — extra information SHRINKS the sample space!</li>\n<li><b>Formula ⭐⭐:</b> <b>P(A|B) = P(A ∩ B) / P(B)</b>, where P(B) ≠ 0. \"The probability of A, given B\".</li>\n<li>Example: a die shows an even number (B = {2,4,6}). What is P(it is 4 | B)? = P({4})/P({2,4,6}) = <b>1/3</b>. The universe is now only {2,4,6}.</li>\n<li><b>Shrink the universe ⭐:</b> once B happens, the sample space is just B. Count A's outcomes inside that small universe — that is exactly what the formula does.</li>\n<li>Properties: P(S|B) = 1; P(A′|B) = 1 − P(A|B); P((A ∪ B)|C) = P(A|C) + P(B|C) − P((A ∩ B)|C).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: \"given that\" = the world got smaller. Now, within B's world, how likely is A — that is the whole calculation.</p>"
   },
   {
    "h": "2️⃣ Multiplication Theorem and Independent Events ⭐⭐",
    "body": "<ul>\n<li><b>Multiplication theorem ⭐:</b> P(A ∩ B) = <b>P(A)·P(B|A)</b> = P(B)·P(A|B) — \"first A, then B given A\" gives the joint chance of both.</li>\n<li><b>Independent events ⭐⭐:</b> one event's outcome does NOT change the other's probability — <b>P(A|B) = P(A)</b> or <b>P(A ∩ B) = P(A)·P(B)</b>. (A coin toss and a die roll don't affect each other!)</li>\n<li><b>Independent vs mutually exclusive ⭐⭐:</b> MUTUALLY EXCLUSIVE = cannot happen together (P(A∩B) = 0). INDEPENDENT = do not affect each other. These are DIFFERENT concepts — non-trivial events cannot be both! (Exam trap!)</li>\n<li>Three independent events: P(A∩B∩C) = P(A)P(B)P(C), AND all pairs must also be independent (pairwise + mutual!).</li>\n<li>Example: 2 cards drawn WITHOUT replacement — the draws are NOT independent (the first card changes the deck). WITH replacement — independent!</li>\n</ul>\n<p class=\"small-note\">🎯 Spot \"without replacement\" and you know independence fails — the favourite confusion point of boards.</p>"
   },
   {
    "h": "3️⃣ Theorem of Total Probability ⭐⭐",
    "body": "<ul>\n<li><b>Setup:</b> the sample space is PARTITIONED into events E₁, E₂, ..., Eₙ (all disjoint, together covering S) — like 3 machines, 2 bags, different routes.</li>\n<li><b>Theorem ⭐⭐:</b> P(A) = <b>P(E₁)P(A|E₁) + P(E₂)P(A|E₂) + ... + P(Eₙ)P(A|Eₙ)</b> — for every route, take (probability × chance of A on that route) and ADD them all!</li>\n<li>Example: 2 bags — Bag I: 3 red, 2 black; Bag II: 2 red, 3 black. A bag is chosen randomly (1/2 each) → P(red) = (1/2)(3/5) + (1/2)(2/5) = <b>1/2</b>.</li>\n<li><b>Tree diagram ⭐:</b> draw branches — first the partition (E₁, E₂), then on each branch A or A′. Multiply along a branch, add across branches — the theorem turns visual!</li>\n<li>Use it when event A can happen via MULTIPLE routes, each with its own chance.</li>\n</ul>\n<p class=\"small-note\">💡 Total probability = \"add up the account of every route\". Like a weighted average — each route contributes with its own weight.</p>"
   },
   {
    "h": "4️⃣ Bayes' Theorem — Walking Back from the Result ⭐⭐",
    "body": "<ul>\n<li><b>Question type:</b> event A has HAPPENED (a defective item turned up!) — now ask: which ROUTE (machine/bag) did it most likely come from? = the <b>reverse (posterior) probability</b>.</li>\n<li><b>Formula ⭐⭐:</b> P(Eᵢ|A) = <b>P(Eᵢ)P(A|Eᵢ) / [Σⱼ P(Eⱼ)P(A|Eⱼ)]</b> — \"that route's contribution ÷ the total probability (the denominator IS the total probability theorem!)\".</li>\n<li><b>Steps ⭐:</b> (1) Write the partitions E₁, E₂... and their PRIOR probabilities. (2) Write P(A|Eᵢ) for each. (3) Compute the denominator = total probability. (4) The ratio = the answer.</li>\n<li>Example: machines M1 (60% of output, 1% defective), M2 (40% of output, 2% defective). A defective item is found → P(from M1) = (0.6×0.01)/(0.6×0.01 + 0.4×0.02) = 0.006/0.014 = <b>3/7</b>.</li>\n<li><b>Real life:</b> medical tests, spam filters, fault detection — all run on Bayes!</li>\n</ul>\n<p class=\"small-note\">🎯 Bayes = \"do the math in reverse\". Build the denominator with total probability first — that is half the work of the question!</p>"
   },
   {
    "h": "5️⃣ Random Variables and Probability Distributions ⭐",
    "body": "<ul>\n<li><b>Random variable X ⭐:</b> assigns a NUMBER to every outcome of an experiment — the count of heads in 2 coin tosses: X = 0, 1, 2.</li>\n<li><b>Probability distribution ⭐:</b> a <b>table</b> pairing each value xᵢ with its probability P(X = xᵢ). Rules: every P(xᵢ) ≥ 0 and <b>ΣP(xᵢ) = 1</b> (exams ask you to check this!).</li>\n<li><b>Mean / Expectation ⭐⭐:</b> <b>E(X) = μ = Σ xᵢ·P(xᵢ)</b> — the sum of value × probability = the \"long-run average\".</li>\n<li>Example: X = heads in 2 tosses → distribution: P(0) = 1/4, P(1) = 1/2, P(2) = 1/4 → E(X) = 0(1/4) + 1(1/2) + 2(1/4) = <b>1</b>. (An average of 1 head in 2 tosses — obvious, but now proven!)</li>\n<li><b>Syllabus note ⭐:</b> the <b>VARIANCE</b> of a random variable (and the binomial distribution) are <b>DELETED</b> from rationalized NCERT — only distributions + the MEAN remain.</li>\n</ul>\n<p class=\"small-note\">💡 E(X) = the \"expected value\" — not a guarantee for one trial, but the LONG-run average. Distribution table + Σxᵢpᵢ = the chapter's last formula!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Conditional ⭐⭐",
    "items": [
     "P(A|B) = P(A∩B)/P(B)",
     "Sample space shrink hojata hai",
     "P(A′|B) = 1 − P(A|B)"
    ]
   },
   {
    "h": "Independent ⭐⭐",
    "items": [
     "P(A∩B) = P(A)P(B)",
     "Independent ≠ mutually exclusive!",
     "Without replacement → dependent"
    ]
   },
   {
    "h": "Total prob ⭐⭐",
    "items": [
     "P(A) = Σ P(Eᵢ)P(A|Eᵢ)",
     "Raaston ka weighted sum",
     "Tree diagram banao"
    ]
   },
   {
    "h": "Bayes ⭐⭐",
    "items": [
     "P(Eᵢ|A) = P(Eᵢ)P(A|Eᵢ)/Σ(...)",
     "Denominator = total probability",
     "'A ho gaya, kaunsa E?' type"
    ]
   },
   {
    "h": "Distribution ⭐",
    "items": [
     "ΣP(xᵢ) = 1 check",
     "Mean E(X) = Σ xᵢP(xᵢ)",
     "Variance DELETED"
    ]
   }
  ],
  "hi": [
   {
    "h": "सप्रतिबंध ⭐⭐",
    "items": [
     "P(A|B) = P(A∩B)/P(B)",
     "प्रतिदर्श समष्टि सिकुड़ती है",
     "P(A′|B) = 1 − P(A|B)"
    ]
   },
   {
    "h": "स्वतंत्र ⭐⭐",
    "items": [
     "P(A∩B) = P(A)P(B)",
     "स्वतंत्र ≠ परस्पर अपवर्जी!",
     "बिना प्रतिस्थापन → आश्रित"
    ]
   },
   {
    "h": "कुल प्रायिकता ⭐⭐",
    "items": [
     "P(A) = Σ P(Eᵢ)P(A|Eᵢ)",
     "रास्तों का भारित योग",
     "वृक्ष आरेख बनाओ"
    ]
   },
   {
    "h": "बेज ⭐⭐",
    "items": [
     "P(Eᵢ|A) = P(Eᵢ)P(A|Eᵢ)/Σ(...)",
     "हर = कुल प्रायिकता",
     "'A हो गई, कौन-सा E?'"
    ]
   },
   {
    "h": "बंटन ⭐",
    "items": [
     "ΣP(xᵢ) = 1 जांच",
     "माध्य E(X) = Σ xᵢP(xᵢ)",
     "प्रसरण हटाया गया"
    ]
   }
  ],
  "en": [
   {
    "h": "Conditional ⭐⭐",
    "items": [
     "P(A|B) = P(A∩B)/P(B)",
     "Sample space shrinks",
     "P(A′|B) = 1 − P(A|B)"
    ]
   },
   {
    "h": "Independent ⭐⭐",
    "items": [
     "P(A∩B) = P(A)P(B)",
     "Independent ≠ mutually exclusive!",
     "Without replacement → dependent"
    ]
   },
   {
    "h": "Total prob ⭐⭐",
    "items": [
     "P(A) = Σ P(Eᵢ)P(A|Eᵢ)",
     "Weighted sum over routes",
     "Draw a tree diagram"
    ]
   },
   {
    "h": "Bayes ⭐⭐",
    "items": [
     "P(Eᵢ|A) = P(Eᵢ)P(A|Eᵢ)/Σ(...)",
     "Denominator = total probability",
     "'A happened — which E?'"
    ]
   },
   {
    "h": "Distribution ⭐",
    "items": [
     "Check ΣP(xᵢ) = 1",
     "Mean E(X) = Σ xᵢP(xᵢ)",
     "Variance DELETED"
    ]
   }
  ]
 },
 "practice": [
  [
   "P(A) = 0.5, P(B) = 0.4, P(A ∩ B) = 0.2. P(A|B) nikalo.",
   "P(A|B) = P(A ∩ B)/P(B) = 0.2/0.4 = <b>1/2</b>."
  ],
  [
   "A aur B independent hain, P(A) = 1/2, P(B) = 1/3. P(A ∩ B)?",
   "Independent → P(A)·P(B) = (1/2)(1/3) = <b>1/6</b>."
  ],
  [
   "P(A ∩ B) = 0 ka matlab A, B independent hain?",
   "<b>Nahi</b> — wo <b>mutually exclusive</b> hain! Independent ke liye P(A∩B) = P(A)P(B) chahiye. Alag concepts!"
  ],
  [
   "Die pe even aane ki condition hai. 6 aane ki probability?",
   "Sample space ab {2, 4, 6} → P(6 | even) = <b>1/3</b>."
  ],
  [
   "Bag I: 3 red 2 black; Bag II: 2 red 3 black; bag randomly. P(red)?",
   "(1/2)(3/5) + (1/2)(2/5) = 3/10 + 2/10 = <b>1/2</b> (total probability)."
  ],
  [
   "Total probability theorem ka formula bolo.",
   "P(A) = <b>Σ P(Eᵢ)·P(A|Eᵢ)</b> — partitions E₁...Eₙ pe."
  ],
  [
   "Bayes' theorem kab use hota hai?",
   "Jab event A <b>ho chuka ho</b> aur poochna ho ki wo <b>kis wajah/route (Eᵢ)</b> se aaya — reverse probability."
  ],
  [
   "Bayes formula ke denominator me kya hota hai?",
   "<b>Total probability</b> — Σⱼ P(Eⱼ)P(A|Eⱼ). Pehle yehi nikalo!"
  ],
  [
   "Distribution me P(X=0)=0.2, P(X=1)=0.5, P(X=2)=0.3. Valid hai?",
   "<b>Haan</b> — sab ≥ 0 aur sum = 0.2 + 0.5 + 0.3 = <b>1</b> ✓."
  ],
  [
   "Upar wale X ka mean nikalo.",
   "E(X) = 0(0.2) + 1(0.5) + 2(0.3) = <b>1.1</b>."
  ]
 ],
 "topic_strip": None,
 "next": None
}

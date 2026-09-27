# Class 11 Maths, Chapter 14 - Probability
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 14,
 "title_en": "Probability",
 "title_hi": "प्रायिकता",
 "tagline": "Chance ka hisaab — sample space, events aur addition rule",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 14: Probability — long + short notes in Hindi, English, Hinglish. Random experiments, sample space, events, classical probability, addition rule.",
 "video": None,
 "card_tag": "Chance ka hisaab — sample space, events aur addition rule",
 "card_topics": [
  "🎲 Sample space + events",
  "🃏 Cards, coins, dice",
  "➕ Addition rule",
  "🎯 'At least one' trick"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Probability — Uncertainty Ka Measurement",
    "body": "<p>Coin uchhalo — heads ya tails? Dice fenko — 1 se 6 kuch bhi? Life uncertain hai, lekin <b>probability</b> us uncertainty ko NUMBER deta hai: 0 (impossible) se 1 (certain) tak. Ye chapter sochne ka tareeka hai — cards, dice, coins ke through hum real life ke \"chance\" ko samajhte hain. JEE me probability + permutations ka combo sabse zyada aata hai.</p>\n<ul>\n<li><b>Random experiment:</b> jiska result pehle se pakka na ho — coin toss, dice roll, card nikalna.</li>\n<li><b>Outcome:</b> ek possible result — coin pe H ya T.</li>\n<li><b>Sample space (S) ⭐:</b> SAARE possible outcomes ka set — dice ke liye S = {1, 2, 3, 4, 5, 6}.</li>\n<li><b>Event:</b> sample space ka koi subset — \"even number aana\" = {2, 4, 6}.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: sample space = pura menu, event = tumhara order — order menu ka hi hissa ho sakta hai!</p>"
   },
   {
    "h": "2️⃣ Events ke Types ⭐",
    "body": "<ul>\n<li><b>Simple event:</b> sirf ek outcome — {5} dice pe.</li>\n<li><b>Compound event:</b> multiple outcomes — {2, 4, 6}.</li>\n<li><b>Sure event:</b> pura sample space — probability 1.</li>\n<li><b>Impossible event (φ):</b> koi outcome nahi — probability 0. (Dice pe 7 aana!)</li>\n<li><b>Complementary event (A′) ⭐:</b> A na hona — \"even na aana\" = odd aana = {1, 3, 5}.</li>\n<li><b>Mutually exclusive ⭐:</b> dono saath nahi ho sakte — A ∩ B = φ (coin pe H aur T ek saath?).</li>\n<li><b>Exhaustive events:</b> milke pura sample space cover karein — {even}, {odd} dice pe.</li>\n</ul>\n<p class=\"small-note\">🎯 Mutually exclusive vs independent ALAG cheezein hain (independent 12th me) — abhi sirf exclusive yaad rakho: overlap zero!</p>"
   },
   {
    "h": "3️⃣ Classical Probability — Basic Formula ⭐",
    "body": "<ul>\n<li><b>Formula ⭐:</b> P(E) = n(E)/n(S) = favourable outcomes ÷ total outcomes — jab sab outcomes EQUALLY likely hon (fair coin, fair dice, well-shuffled cards).</li>\n<li><b>Coin:</b> P(H) = 1/2. <b>Dice:</b> P(3) = 1/6, P(even) = 3/6 = 1/2.</li>\n<li><b>Cards (52) ⭐:</b> P(king) = 4/52 = 1/13, P(heart) = 13/52 = 1/4, P(red) = 26/52 = 1/2.</li>\n<li><b>Range:</b> 0 ≤ P(E) ≤ 1 — iske bahar kabhi nahi!</li>\n<li><b>Complement rule ⭐:</b> P(A′) = 1 − P(A) — \"na hone\" ki probability = 1 minus \"hone\" ki. Bahut kaam aata hai!</li>\n<li><b>Odds:</b> P(E) = 3/4 to odds in favour = 3:1 (favourable : unfavourable).</li>\n</ul>\n<p class=\"small-note\">💡 Cards yaad karo: 52 total, 4 suits (13 each), 26 red + 26 black, 12 face cards (J, Q, K × 4), 4 aces!</p>"
   },
   {
    "h": "4️⃣ Addition Rule — A Ya B Ki Probability ⭐",
    "body": "<ul>\n<li><b>General rule ⭐:</b> P(A ∪ B) = P(A) + P(B) − P(A ∩ B) — overlap double-count ho jaata hai, isliye minus!</li>\n<li><b>Mutually exclusive hon to ⭐:</b> P(A ∪ B) = P(A) + P(B) (overlap zero hai hi).</li>\n<li><b>Three events:</b> P(A∪B∪C) = P(A) + P(B) + P(C) − P(A∩B) − P(B∩C) − P(C∩A) + P(A∩B∩C).</li>\n<li><b>A but not B:</b> P(A − B) = P(A) − P(A ∩ B).</li>\n<li><b>Complement se jodo ⭐:</b> P(A ∪ B) = 1 − P(A′ ∩ B′) — \"kam se kam ek\" wale questions me super useful!</li>\n</ul>\n<p class=\"small-note\">🎯 \"At least one\" dekhte hi complement socho: P(kam se kam ek) = 1 − P(koi bhi nahi) — calculation aadhi!</p>"
   },
   {
    "h": "5️⃣ Exam Patterns — Probability ka Paper",
    "body": "<ul>\n<li><b>Sample space likho:</b> 2 coins, 2 dice, coin + dice — tabular form fastest (2 dice = 36 outcomes!).</li>\n<li><b>Direct P(E) = n(E)/n(S) ⭐:</b> count favourable, divide by total — counting chapter yahin kaam aata hai.</li>\n<li><b>Cards/coins/dice classics:</b> \"dono dice pe sum 8\", \"ek card king ya heart\" — addition rule.</li>\n<li><b>At least one ⭐:</b> complement method.</li>\n<li><b>Balls from a bag ⭐:</b> \"3 red, 4 blue me se 2 balls\" — C(n,r) se count karo dono side.</li>\n<li><b>Letters/digits:</b> \"word ke letters arrange, vowels saath\" — permutations + probability combo.</li>\n</ul>\n<p class=\"small-note\">💡 Probability = counting ÷ counting. P&amp;C chapter strong hai to ye chapter FREE marks hai!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ प्रायिकता — अनिश्चितता का माप",
    "body": "<p>सिक्का उछालो — चित या पट? जीवन अनिश्चित है, पर <b>प्रायिकता (probability)</b> उस अनिश्चितता को संख्या देती है: 0 (असंभव) से 1 (निश्चित) तक। JEE में प्रायिकता + क्रमचय-संचय का संयोजन सर्वाधिक आता है।</p>\n<ul>\n<li><b>यादृच्छिक प्रयोग:</b> जिसका परिणाम पूर्वनिश्चित न हो — सिक्का, पासा, ताश।</li>\n<li><b>परिणाम (outcome):</b> एक संभव परिणाम।</li>\n<li><b>प्रतिदर्श समष्टि (S) ⭐:</b> सभी संभव परिणामों का समुच्चय — पासे के लिए S = {1,2,3,4,5,6}।</li>\n<li><b>घटना (event):</b> प्रतिदर्श समष्टि का उपसमुच्चय — \"सम संख्या\" = {2,4,6}।</li>\n</ul>\n<p class=\"small-note\">💡 प्रतिदर्श समष्टि = पूरा मेन्यू, घटना = आपका ऑर्डर!</p>"
   },
   {
    "h": "2️⃣ घटनाओं के प्रकार ⭐",
    "body": "<ul>\n<li><b>सरल घटना:</b> एक परिणाम — {5}।</li>\n<li><b>मिश्र घटना:</b> अनेक परिणाम — {2,4,6}।</li>\n<li><b>निश्चित घटना:</b> पूरी समष्टि — P = 1। <b>असंभव (φ):</b> P = 0 (पासे पर 7!)।</li>\n<li><b>पूरक घटना (A′) ⭐:</b> A न होना — \"सम न आना\" = विषम = {1,3,5}।</li>\n<li><b>परस्पर अपवर्जी ⭐:</b> साथ नहीं हो सकतीं — A ∩ B = φ।</li>\n<li><b>संपूर्ण घटनाएँ:</b> मिलकर पूरी समष्टि — {सम}, {विषम}।</li>\n</ul>\n<p class=\"small-note\">🎯 अपवर्जी = overlap शून्य — बस यही याद रखो!</p>"
   },
   {
    "h": "3️⃣ परंपरागत प्रायिकता — मूल सूत्र ⭐",
    "body": "<ul>\n<li><b>सूत्र ⭐:</b> P(E) = n(E)/n(S) = अनुकूल परिणाम ÷ कुल परिणाम — जब सभी परिणाम समसंभाव्य हों।</li>\n<li><b>सिक्का:</b> P(H) = 1/2। <b>पासा:</b> P(सम) = 1/2।</li>\n<li><b>ताश (52) ⭐:</b> P(बादशाह) = 1/13, P(पान) = 1/4, P(लाल) = 1/2।</li>\n<li><b>परिसर:</b> 0 ≤ P(E) ≤ 1।</li>\n<li><b>पूरक नियम ⭐:</b> P(A′) = 1 − P(A)।</li>\n<li><b>संयोग (odds):</b> P(E) = 3/4 → पक्ष में 3:1।</li>\n</ul>\n<p class=\"small-note\">💡 ताश याद रखो: 52, 4 suits × 13, 26 लाल + 26 काले, 12 चेहरा पत्ते, 4 इक्के!</p>"
   },
   {
    "h": "4️⃣ योग नियम — A या B की प्रायिकता ⭐",
    "body": "<ul>\n<li><b>सामान्य नियम ⭐:</b> P(A ∪ B) = P(A) + P(B) − P(A ∩ B) — overlap दोबारा जुड़ जाता है, इसलिए घटाओ!</li>\n<li><b>अपवर्जी हों तो ⭐:</b> P(A ∪ B) = P(A) + P(B)।</li>\n<li><b>तीन घटनाएँ:</b> P(A∪B∪C) = P(A)+P(B)+P(C) − P(A∩B) − P(B∩C) − P(C∩A) + P(A∩B∩C)।</li>\n<li><b>A पर B नहीं:</b> P(A − B) = P(A) − P(A ∩ B)।</li>\n<li><b>पूरक से ⭐:</b> P(A ∪ B) = 1 − P(A′ ∩ B′) — \"कम से कम एक\" प्रश्नों में!</li>\n</ul>\n<p class=\"small-note\">🎯 \"कम से कम एक\" देखते ही पूरक सोचो: 1 − P(कोई नहीं) — गणना आधी!</p>"
   },
   {
    "h": "5️⃣ परीक्षा के पैटर्न",
    "body": "<ul>\n<li><b>प्रतिदर्श समष्टि:</b> 2 सिक्के, 2 पासे — सारणी सबसे तेज़ (2 पासे = 36)।</li>\n<li><b>सीधा P(E) = n(E)/n(S) ⭐:</b> अनुकूल गिनो, कुल से भाग।</li>\n<li><b>ताश/सिक्का/पासा क्लासिक:</b> \"दोनों पासों पर योग 8\", \"बादशाह या पान\"।</li>\n<li><b>कम से कम एक ⭐:</b> पूरक विधि।</li>\n<li><b>थैली से गेंदें ⭐:</b> \"3 लाल, 4 नीली में से 2\" — C(n,r) से गिनती।</li>\n</ul>\n<p class=\"small-note\">💡 प्रायिकता = गिनती ÷ गिनती। P&amp;C पक्की तो यह अध्याय मुफ्त अंक!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Probability — Measuring Uncertainty",
    "body": "<p>Toss a coin — heads or tails? Roll a die — anything from 1 to 6? Life is uncertain, but <b>probability</b> turns that uncertainty into a NUMBER: from 0 (impossible) to 1 (certain). This chapter is a way of thinking — through cards, dice, and coins we learn to understand \"chance\" in real life. JEE loves the probability + permutations combo.</p>\n<ul>\n<li><b>Random experiment:</b> one whose result isn't fixed in advance — coin toss, dice roll, drawing a card.</li>\n<li><b>Outcome:</b> a single possible result — H or T on a coin.</li>\n<li><b>Sample space (S) ⭐:</b> the set of ALL possible outcomes — for a die, S = {1, 2, 3, 4, 5, 6}.</li>\n<li><b>Event:</b> any subset of the sample space — \"getting an even number\" = {2, 4, 6}.</li>\n</ul>\n<p class=\"small-note\">💡 Feel it: the sample space is the full menu; an event is your order — your order can only come from the menu!</p>"
   },
   {
    "h": "2️⃣ Types of Events ⭐",
    "body": "<ul>\n<li><b>Simple event:</b> a single outcome — {5} on a die.</li>\n<li><b>Compound event:</b> multiple outcomes — {2, 4, 6}.</li>\n<li><b>Sure event:</b> the whole sample space — probability 1.</li>\n<li><b>Impossible event (φ):</b> no outcomes — probability 0. (Rolling a 7 on a die!)</li>\n<li><b>Complementary event (A′) ⭐:</b> A not happening — \"not even\" = odd = {1, 3, 5}.</li>\n<li><b>Mutually exclusive ⭐:</b> can't happen together — A ∩ B = φ (H and T on one coin toss?).</li>\n<li><b>Exhaustive events:</b> together they cover the whole sample space — {even}, {odd} on a die.</li>\n</ul>\n<p class=\"small-note\">🎯 Mutually exclusive ≠ independent (that's Class 12) — for now: exclusive means zero overlap!</p>"
   },
   {
    "h": "3️⃣ Classical Probability — the Basic Formula ⭐",
    "body": "<ul>\n<li><b>Formula ⭐:</b> P(E) = n(E)/n(S) = favourable outcomes ÷ total outcomes — valid when all outcomes are EQUALLY likely (fair coin, fair die, well-shuffled cards).</li>\n<li><b>Coin:</b> P(H) = 1/2. <b>Die:</b> P(3) = 1/6, P(even) = 3/6 = 1/2.</li>\n<li><b>Cards (52) ⭐:</b> P(king) = 4/52 = 1/13, P(heart) = 13/52 = 1/4, P(red) = 26/52 = 1/2.</li>\n<li><b>Range:</b> 0 ≤ P(E) ≤ 1 — never outside this!</li>\n<li><b>Complement rule ⭐:</b> P(A′) = 1 − P(A) — \"not happening\" = 1 minus \"happening\". Hugely useful!</li>\n<li><b>Odds:</b> if P(E) = 3/4, odds in favour are 3:1 (favourable : unfavourable).</li>\n</ul>\n<p class=\"small-note\">💡 Memorise the deck: 52 total, 4 suits (13 each), 26 red + 26 black, 12 face cards (J, Q, K × 4), 4 aces!</p>"
   },
   {
    "h": "4️⃣ Addition Rule — Probability of A or B ⭐",
    "body": "<ul>\n<li><b>General rule ⭐:</b> P(A ∪ B) = P(A) + P(B) − P(A ∩ B) — the overlap gets double-counted, so subtract it!</li>\n<li><b>If mutually exclusive ⭐:</b> P(A ∪ B) = P(A) + P(B) (overlap is zero anyway).</li>\n<li><b>Three events:</b> P(A∪B∪C) = P(A) + P(B) + P(C) − P(A∩B) − P(B∩C) − P(C∩A) + P(A∩B∩C).</li>\n<li><b>A but not B:</b> P(A − B) = P(A) − P(A ∩ B).</li>\n<li><b>Complement trick ⭐:</b> P(A ∪ B) = 1 − P(A′ ∩ B′) — super useful for \"at least one\" questions!</li>\n</ul>\n<p class=\"small-note\">🎯 The moment you see \"at least one\", think complement: P(at least one) = 1 − P(none) — half the calculation!</p>"
   },
   {
    "h": "5️⃣ Exam Patterns — Probability in Papers",
    "body": "<ul>\n<li><b>Write the sample space:</b> 2 coins, 2 dice, coin + die — tabular form is fastest (2 dice = 36 outcomes!).</li>\n<li><b>Direct P(E) = n(E)/n(S) ⭐:</b> count favourable, divide by total — the counting chapter pays off here.</li>\n<li><b>Cards/coins/dice classics:</b> \"sum of 8 on two dice\", \"a king or a heart\" — addition rule.</li>\n<li><b>At least one ⭐:</b> complement method.</li>\n<li><b>Balls from a bag ⭐:</b> \"2 balls from 3 red, 4 blue\" — count both sides with C(n,r).</li>\n<li><b>Letters/digits:</b> \"letters of a word arranged with vowels together\" — permutations + probability combo.</li>\n</ul>\n<p class=\"small-note\">💡 Probability = counting ÷ counting. If P&amp;C is strong, this chapter is FREE marks!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics ⭐",
    "items": [
     "P(E) = n(E)/n(S)",
     "0 ≤ P ≤ 1",
     "S = saare outcomes, E = subset"
    ]
   },
   {
    "h": "Events ⭐",
    "items": [
     "Impossible: φ, P=0; Sure: S, P=1",
     "Mutually exclusive: A∩B = φ",
     "Complement: P(A′) = 1 − P(A)"
    ]
   },
   {
    "h": "Addition ⭐",
    "items": [
     "P(A∪B) = P(A)+P(B)−P(A∩B)",
     "Exclusive: P(A∪B) = P(A)+P(B)",
     "A−B: P(A) − P(A∩B)"
    ]
   },
   {
    "h": "Cards (52) ⭐",
    "items": [
     "4 suits × 13",
     "12 face cards, 4 aces",
     "26 red + 26 black"
    ]
   },
   {
    "h": "Tricks",
    "items": [
     "'At least one' → 1 − P(none)",
     "2 dice → 36 outcomes table",
     "P&C se counting"
    ]
   }
  ],
  "hi": [
   {
    "h": "आधार ⭐",
    "items": [
     "P(E) = n(E)/n(S)",
     "0 ≤ P ≤ 1",
     "S = सभी परिणाम, E = उपसमुच्चय"
    ]
   },
   {
    "h": "घटनाएँ ⭐",
    "items": [
     "असंभव: P=0; निश्चित: P=1",
     "अपवर्जी: A∩B = φ",
     "पूरक: P(A′) = 1 − P(A)"
    ]
   },
   {
    "h": "योग ⭐",
    "items": [
     "P(A∪B) = P(A)+P(B)−P(A∩B)",
     "अपवर्जी: P(A∪B) = P(A)+P(B)",
     "A−B: P(A) − P(A∩B)"
    ]
   },
   {
    "h": "ताश (52) ⭐",
    "items": [
     "4 suits × 13",
     "12 चेहरा, 4 इक्के",
     "26 लाल + 26 काले"
    ]
   },
   {
    "h": "तरकीबें",
    "items": [
     "'कम से कम एक' → 1 − P(कोई नहीं)",
     "2 पासे → 36 परिणाम",
     "P&C से गिनती"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics ⭐",
    "items": [
     "P(E) = n(E)/n(S)",
     "0 ≤ P ≤ 1",
     "S = all outcomes, E = subset"
    ]
   },
   {
    "h": "Events ⭐",
    "items": [
     "Impossible: φ, P=0; Sure: S, P=1",
     "Mutually exclusive: A∩B = φ",
     "Complement: P(A′) = 1 − P(A)"
    ]
   },
   {
    "h": "Addition ⭐",
    "items": [
     "P(A∪B) = P(A)+P(B)−P(A∩B)",
     "Exclusive: P(A∪B) = P(A)+P(B)",
     "A−B: P(A) − P(A∩B)"
    ]
   },
   {
    "h": "Cards (52) ⭐",
    "items": [
     "4 suits × 13",
     "12 face cards, 4 aces",
     "26 red + 26 black"
    ]
   },
   {
    "h": "Tricks",
    "items": [
     "'At least one' → 1 − P(none)",
     "2 dice → 36-outcome table",
     "Count via P&C"
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
 "next": None
}

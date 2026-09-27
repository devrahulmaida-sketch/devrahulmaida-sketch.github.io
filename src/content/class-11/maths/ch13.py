# Class 11 Maths, Chapter 13 - Statistics
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 13,
 "title_en": "Statistics",
 "title_hi": "सांख्यिकी",
 "tagline": "Data kitna scattered hai — variance, SD aur CV ka khel",
 "jee": "MEDIUM",
 "meta_desc": "Class 11 Maths Chapter 13: Statistics — long + short notes in Hindi, English, Hinglish. Dispersion, mean deviation, variance, standard deviation, coefficient of variation.",
 "video": None,
 "card_tag": "Data kitna scattered hai — variance, SD aur CV ka khel",
 "card_topics": [
  "📊 Dispersion + range",
  "📏 Mean deviation",
  "📈 Variance + standard deviation",
  "⚖️ CV for consistency"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Statistics — Data Ko Samajhne Ka Tool",
    "body": "<p>Marks, rainfall, prices, cricket scores — duniya data se chalti hai. <b>Statistics</b> bataata hai data ka CENTRE kahan hai (mean, median, mode — Class 9/10 me padha) aur kitna BIKHRA hua hai (dispersion — is chapter ka focus). Do teams ka average same ho sakta hai, lekin ek consistent ho, doosri upar-neeche — ye farak dispersion bataata hai!</p>\n<ul>\n<li><b>Dispersion (scatter):</b> data mean se kitna door-door hai.</li>\n<li><b>Measures:</b> Range, Mean Deviation, Variance, Standard Deviation.</li>\n<li><b>Consistent vs variable ⭐:</b> kam dispersion = zyada consistent/reliable.</li>\n<li><b>Real use:</b> share market risk (SD hi volatility hai!), quality control, sports analysis.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: average dono dost ke 70 hai — ek har paper me 68-72 laata hai, doosra 40 se 100 tak. Kaun zyada reliable? Pehla — kyunki uska dispersion kam!</p>"
   },
   {
    "h": "2️⃣ Range aur Mean Deviation",
    "body": "<ul>\n<li><b>Range:</b> maximum − minimum — sabse simple, lekin sirf 2 extreme values use karta hai (bechare baaki data ka koi role nahi!).</li>\n<li><b>Mean Deviation about mean ⭐:</b> har value ka mean se distance (absolute, sign ignore), phir unka average. Formula: M.D. = (1/n) Σ|xᵢ − x̄|.</li>\n<li><b>Mean Deviation about median:</b> same, bas median se — (1/n) Σ|xᵢ − M|.</li>\n<li><b>Grouped data (discrete):</b> M.D. = Σfᵢ|xᵢ − x̄| / Σfᵢ — frequencies se multiply.</li>\n<li><b>Continuous series:</b> class ka mid-point xᵢ use karo, baaki same.</li>\n</ul>\n<p class=\"small-note\">💡 Absolute value kyun? Kyunki +5 aur −5 cancel ho jaate — humein sirf DOORI chahiye, direction nahi!</p>"
   },
   {
    "h": "3️⃣ Variance aur Standard Deviation ⭐",
    "body": "<p>Chapter ka hero! Mean deviation ka absolute value thoda clumsy hai (maths me |x| se kaam karna mushkil) — isliye square karte hain.</p>\n<ul>\n<li><b>Variance (σ²) ⭐:</b> σ² = (1/n) Σ(xᵢ − x̄)² — squared deviations ka average.</li>\n<li><b>Standard Deviation (σ) ⭐:</b> variance ka square root — σ = √[(1/n) Σ(xᵢ − x̄)²]. Units original data jaisi hi (marks ka SD marks me!).</li>\n<li><b>Shortcut formula ⭐:</b> σ² = (1/n) Σxᵢ² − x̄² — pehle squares ka mean, minus mean ka square!</li>\n<li><b>Grouped data:</b> σ² = (1/N) Σfᵢxᵢ² − x̄², jahan N = Σfᵢ.</li>\n<li><b>Properties ⭐:</b> har value me SAME number add karo → σ unchanged! Har value ko a se multiply karo → σ multiply by |a|.</li>\n</ul>\n<p class=\"small-note\">🎯 Board question pakka: \"5 observations ka mean 4.4, Σx² = ... variance nikalo\" — shortcut formula seedha lagao!</p>"
   },
   {
    "h": "4️⃣ Coefficient of Variation (CV) ⭐",
    "body": "<p>Do alag datasets compare karni ho (alag means, alag units) to raw SD se kaam nahi chalega — isliye <b>CV</b>:</p>\n<ul>\n<li><b>CV ⭐:</b> CV = (σ / x̄) × 100 — percentage me dispersion.</li>\n<li><b>Rule ⭐:</b> jiska CV KAM, wo zyada CONSISTENT/homogeneous; jiska CV zyada, wo zyada variable.</li>\n<li><b>Kab use karo:</b> jab means different hon ya units alag hon (marks vs heights!).</li>\n<li>Same mean ho to direct SD compare kar sakte ho — CV ki zaroorat nahi.</li>\n</ul>\n<p class=\"small-note\">💡 Example: Team A (mean 50, σ 5, CV 10%) vs Team B (mean 30, σ 4, CV 13.3%) — B ka σ kam hai lekin A zyada consistent, kyunki CV matter karta hai!</p>"
   },
   {
    "h": "5️⃣ Exam Patterns — Statistics ka Paper",
    "body": "<ul>\n<li><b>Mean deviation nikalo:</b> ungrouped (|xᵢ − x̄| average) ya grouped (frequencies ke saath).</li>\n<li><b>Variance/SD ⭐:</b> direct ya shortcut formula — calculation heavy, steps dikhao.</li>\n<li><b>Shortcut method (assumed mean):</b> bade numbers pe u = xᵢ − A leke simplify.</li>\n<li><b>CV se consistency ⭐:</b> do series compare — CV kam = consistent.</li>\n<li><b>Properties wale:</b> \"har observation 3 se badha diya\" → mean +3, σ same; \"double kiya\" → σ double.</li>\n<li><b>Missing frequency:</b> mean/variance conditions se equation banake solve.</li>\n</ul>\n<p class=\"small-note\">💡 Calculation mistakes is chapter ke asli villain hain — table banao (xᵢ, fᵢ, fᵢxᵢ, xᵢ², fᵢxᵢ² columns) aur galti zero!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ सांख्यिकी — डेटा समझने का उपकरण",
    "body": "<p>अंक, वर्षा, मूल्य, क्रिकेट स्कोर — दुनिया डेटा से चलती है। <b>सांख्यिकी</b> बताती है डेटा का केंद्र कहाँ है और कितना <b>बिखरा</b> हुआ है (विक्षेपण — इस अध्याय का विषय)। दो टीमों का औसत समान हो सकता है, पर एक सुसंगत हो, दूसरी अस्थिर — यही अंतर विक्षेपण बताता है!</p>\n<ul>\n<li><b>विक्षेपण (dispersion):</b> डेटा माध्य से कितना दूर-दूर है।</li>\n<li><b>माप:</b> परास, माध्य विचलन, प्रसरण, मानक विचलन।</li>\n<li><b>सुसंगत बनाम परिवर्ती ⭐:</b> कम विक्षेपण = अधिक सुसंगत।</li>\n<li><b>उपयोग:</b> शेयर जोखिम (SD ही अस्थिरता!), गुणवत्ता नियंत्रण, खेल विश्लेषण।</li>\n</ul>\n<p class=\"small-note\">💡 दोनों दोस्तों के औसत 70 — एक 68-72 लाता है, दूसरा 40 से 100 तक। कौन विश्वसनीय? पहला — विक्षेपण कम!</p>"
   },
   {
    "h": "2️⃣ परास और माध्य विचलन",
    "body": "<ul>\n<li><b>परास (Range):</b> अधिकतम − न्यूनतम — सरल, पर केवल 2 चरम मान प्रयोग करता है।</li>\n<li><b>माध्य विचलन (माध्य से) ⭐:</b> M.D. = (1/n) Σ|xᵢ − x̄| — माध्य से दूरियों का औसत।</li>\n<li><b>माध्यिका से माध्य विचलन:</b> (1/n) Σ|xᵢ − M|।</li>\n<li><b>वर्गीकृत डेटा:</b> M.D. = Σfᵢ|xᵢ − x̄| / Σfᵢ।</li>\n<li><b>संतत श्रेणी:</b> वर्ग का मध्य-बिंदु xᵢ प्रयोग करो।</li>\n</ul>\n<p class=\"small-note\">💡 निरपेक्ष मान क्यों? +5 और −5 कट जाते — हमें केवल दूरी चाहिए, दिशा नहीं!</p>"
   },
   {
    "h": "3️⃣ प्रसरण और मानक विचलन ⭐",
    "body": "<ul>\n<li><b>प्रसरण (σ²) ⭐:</b> σ² = (1/n) Σ(xᵢ − x̄)² — वर्गित विचलनों का औसत।</li>\n<li><b>मानक विचलन (σ) ⭐:</b> σ = √[(1/n) Σ(xᵢ − x̄)²] — इकाइयाँ मूल डेटा जैसी।</li>\n<li><b>लघु सूत्र ⭐:</b> σ² = (1/n) Σxᵢ² − x̄² — वर्गों का माध्य, ऋण माध्य का वर्ग!</li>\n<li><b>वर्गीकृत डेटा:</b> σ² = (1/N) Σfᵢxᵢ² − x̄², N = Σfᵢ।</li>\n<li><b>गुण ⭐:</b> सभी में समान संख्या जोड़ो → σ अपरिवर्तित! सभी को a से गुणा → σ, |a| गुना।</li>\n</ul>\n<p class=\"small-note\">🎯 बोर्ड प्रश्न पक्का: \"माध्य 4.4, Σx² दिया है — प्रसरण निकालो\" — लघु सूत्र लगाओ!</p>"
   },
   {
    "h": "4️⃣ विचरण गुणांक (CV) ⭐",
    "body": "<ul>\n<li><b>CV ⭐:</b> CV = (σ / x̄) × 100 — प्रतिशत में विक्षेपण।</li>\n<li><b>नियम ⭐:</b> CV कम = अधिक सुसंगत; CV अधिक = अधिक परिवर्ती।</li>\n<li><b>कब:</b> जब माध्य भिन्न हों या इकाइयाँ अलग हों।</li>\n<li>माध्य समान हो तो सीधे σ तुलना करो।</li>\n</ul>\n<p class=\"small-note\">💡 टीम A (CV 10%) बनाम टीम B (CV 13.3%) — A अधिक सुसंगत, चाहे B का σ कम हो!</p>"
   },
   {
    "h": "5️⃣ परीक्षा के पैटर्न",
    "body": "<ul>\n<li><b>माध्य विचलन:</b> अवर्गीकृत/वर्गीकृत।</li>\n<li><b>प्रसरण/σ ⭐:</b> प्रत्यक्ष या लघु सूत्र — गणना भारी, चरण दिखाओ।</li>\n<li><b>कल्पित माध्य विधि:</b> u = xᵢ − A से सरलीकरण।</li>\n<li><b>CV से तुलना ⭐:</b> CV कम = सुसंगत।</li>\n<li><b>गुण प्रश्न:</b> \"सबमें 3 जोड़ा\" → माध्य +3, σ समान।</li>\n</ul>\n<p class=\"small-note\">💡 गणना गलतियाँ असली खलनायक — सारणी बनाओ (xᵢ, fᵢ, fᵢxᵢ, xᵢ², fᵢxᵢ²)!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Statistics — the Tool for Understanding Data",
    "body": "<p>Marks, rainfall, prices, cricket scores — the world runs on data. <b>Statistics</b> tells you where the data's CENTRE sits (mean, median, mode — done in Classes 9/10) and how SPREAD OUT it is (dispersion — this chapter's focus). Two teams can have the same average, yet one is consistent and the other erratic — dispersion reveals that difference!</p>\n<ul>\n<li><b>Dispersion (scatter):</b> how far the data lies from the mean.</li>\n<li><b>Measures:</b> Range, Mean Deviation, Variance, Standard Deviation.</li>\n<li><b>Consistent vs variable ⭐:</b> less dispersion = more consistent/reliable.</li>\n<li><b>Real uses:</b> stock-market risk (SD literally IS volatility!), quality control, sports analysis.</li>\n</ul>\n<p class=\"small-note\">💡 Feel it: both friends average 70 — one always scores 68-72, the other swings 40 to 100. Who's more reliable? The first — lower dispersion!</p>"
   },
   {
    "h": "2️⃣ Range and Mean Deviation",
    "body": "<ul>\n<li><b>Range:</b> maximum − minimum — simplest, but uses only the 2 extreme values (the rest get no say!).</li>\n<li><b>Mean Deviation about the mean ⭐:</b> take each value's distance from the mean (absolute, ignore sign), then average them. M.D. = (1/n) Σ|xᵢ − x̄|.</li>\n<li><b>Mean Deviation about the median:</b> same idea, from the median — (1/n) Σ|xᵢ − M|.</li>\n<li><b>Grouped data (discrete):</b> M.D. = Σfᵢ|xᵢ − x̄| / Σfᵢ — multiply by frequencies.</li>\n<li><b>Continuous series:</b> use each class's mid-point as xᵢ, rest is the same.</li>\n</ul>\n<p class=\"small-note\">💡 Why absolute values? Because +5 and −5 would cancel — we only care about DISTANCE, not direction!</p>"
   },
   {
    "h": "3️⃣ Variance and Standard Deviation ⭐",
    "body": "<p>The hero of the chapter! The absolute value in mean deviation is clumsy to work with mathematically — so we square the deviations instead.</p>\n<ul>\n<li><b>Variance (σ²) ⭐:</b> σ² = (1/n) Σ(xᵢ − x̄)² — the average of squared deviations.</li>\n<li><b>Standard Deviation (σ) ⭐:</b> the square root of variance — σ = √[(1/n) Σ(xᵢ − x̄)²]. Units match the original data (SD of marks is in marks!).</li>\n<li><b>Shortcut formula ⭐:</b> σ² = (1/n) Σxᵢ² − x̄² — mean of squares, minus the square of the mean!</li>\n<li><b>Grouped data:</b> σ² = (1/N) Σfᵢxᵢ² − x̄², where N = Σfᵢ.</li>\n<li><b>Properties ⭐:</b> add the SAME number to every value → σ unchanged! Multiply every value by a → σ multiplies by |a|.</li>\n</ul>\n<p class=\"small-note\">🎯 Guaranteed board question: \"mean is 4.4, Σx² given — find variance\" — apply the shortcut formula directly!</p>"
   },
   {
    "h": "4️⃣ Coefficient of Variation (CV) ⭐",
    "body": "<p>To compare two different datasets (different means or units), raw SD won't do — hence the <b>CV</b>:</p>\n<ul>\n<li><b>CV ⭐:</b> CV = (σ / x̄) × 100 — dispersion as a percentage.</li>\n<li><b>Rule ⭐:</b> LOWER CV = MORE consistent/homogeneous; higher CV = more variable.</li>\n<li><b>When to use:</b> when means differ or units differ (marks vs heights!).</li>\n<li>If means are equal, compare SDs directly — no CV needed.</li>\n</ul>\n<p class=\"small-note\">💡 Example: Team A (mean 50, σ 5, CV 10%) vs Team B (mean 30, σ 4, CV 13.3%) — B has lower σ but A is MORE consistent, because CV is what counts!</p>"
   },
   {
    "h": "5️⃣ Exam Patterns — Statistics in Papers",
    "body": "<ul>\n<li><b>Find the mean deviation:</b> ungrouped (average of |xᵢ − x̄|) or grouped (with frequencies).</li>\n<li><b>Variance/SD ⭐:</b> direct or shortcut formula — calculation-heavy, so show your steps.</li>\n<li><b>Assumed-mean shortcut:</b> with big numbers, set u = xᵢ − A to simplify.</li>\n<li><b>Consistency via CV ⭐:</b> compare two series — lower CV = consistent.</li>\n<li><b>Property questions:</b> \"every observation increased by 3\" → mean +3, σ unchanged; \"doubled\" → σ doubles.</li>\n<li><b>Missing frequency:</b> build equations from the mean/variance conditions and solve.</li>\n</ul>\n<p class=\"small-note\">💡 Calculation slips are the real villain here — build a table (xᵢ, fᵢ, fᵢxᵢ, xᵢ², fᵢxᵢ² columns) and errors drop to zero!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics",
    "items": [
     "Dispersion = data kitna scattered",
     "Kam dispersion = zyada consistent",
     "Range = max − min"
    ]
   },
   {
    "h": "Mean Deviation",
    "items": [
     "M.D. = (1/n)Σ|xᵢ − x̄|",
     "Median se bhi nikal sakte",
     "Grouped: Σf|x − x̄|/Σf"
    ]
   },
   {
    "h": "Variance/SD ⭐",
    "items": [
     "σ² = (1/n)Σ(xᵢ − x̄)²",
     "σ² = (Σxᵢ²)/n − x̄² (shortcut)",
     "σ = √variance"
    ]
   },
   {
    "h": "CV ⭐",
    "items": [
     "CV = (σ/x̄) × 100",
     "CV kam = zyada consistent",
     "Alag units/means → CV use karo"
    ]
   },
   {
    "h": "Properties ⭐",
    "items": [
     "Sab me +a → σ unchanged",
     "Sab ×a → σ × |a|",
     "Table method = no mistakes"
    ]
   }
  ],
  "hi": [
   {
    "h": "आधार",
    "items": [
     "विक्षेपण = डेटा कितना बिखरा",
     "कम विक्षेपण = अधिक सुसंगत",
     "परास = max − min"
    ]
   },
   {
    "h": "माध्य विचलन",
    "items": [
     "M.D. = (1/n)Σ|xᵢ − x̄|",
     "माध्यिका से भी",
     "वर्गीकृत: Σf|x − x̄|/Σf"
    ]
   },
   {
    "h": "प्रसरण/σ ⭐",
    "items": [
     "σ² = (1/n)Σ(xᵢ − x̄)²",
     "σ² = (Σxᵢ²)/n − x̄²",
     "σ = √प्रसरण"
    ]
   },
   {
    "h": "CV ⭐",
    "items": [
     "CV = (σ/x̄) × 100",
     "CV कम = अधिक सुसंगत",
     "अलग इकाइयाँ → CV"
    ]
   },
   {
    "h": "गुण ⭐",
    "items": [
     "सबमें +a → σ समान",
     "सब ×a → σ × |a|",
     "सारणी विधि = शून्य गलती"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics",
    "items": [
     "Dispersion = how scattered data is",
     "Less dispersion = more consistent",
     "Range = max − min"
    ]
   },
   {
    "h": "Mean Deviation",
    "items": [
     "M.D. = (1/n)Σ|xᵢ − x̄|",
     "Also computable about median",
     "Grouped: Σf|x − x̄|/Σf"
    ]
   },
   {
    "h": "Variance/SD ⭐",
    "items": [
     "σ² = (1/n)Σ(xᵢ − x̄)²",
     "σ² = (Σxᵢ²)/n − x̄² (shortcut)",
     "σ = √variance"
    ]
   },
   {
    "h": "CV ⭐",
    "items": [
     "CV = (σ/x̄) × 100",
     "Lower CV = more consistent",
     "Different units/means → use CV"
    ]
   },
   {
    "h": "Properties ⭐",
    "items": [
     "All +a → σ unchanged",
     "All ×a → σ × |a|",
     "Table method = no mistakes"
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
  "href": "/class-11/maths/ch-14/",
  "title": "Probability"
 }
}

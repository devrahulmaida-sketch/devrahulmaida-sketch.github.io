# Class 12 Maths, Chapter 12 - Linear Programming
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 12,
 "title_en": "Linear Programming",
 "title_hi": "रैखिक प्रोग्रामन",
 "tagline": "Graph banao, corners dhundo, best answer pao — sabse scoring chapter",
 "jee": "MEDIUM",
 "meta_desc": "Class 12 Maths Chapter 12: Linear Programming — long + short notes in Hindi, English, Hinglish. Objective function, constraints, feasible region, corner point method, bounded and unbounded regions.",
 "video": None,
 "card_tag": "Graph banao, corners dhundo, best answer pao — sabse scoring chapter",
 "card_topics": [
  "🎯 Objective function + constraints",
  "📊 Feasible region graph",
  "📍 Corner point method",
  "♾️ Bounded vs unbounded"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ LPP Kya Hai — Best Possible Answer Nikalna ⭐",
    "body": "<ul>\n<li><b>Linear Programming Problem (LPP):</b> kisi cheez ko <b>MAXIMIZE ya MINIMIZE</b> karna (profit, cost, output) jab conditions LINEAR inequalities me di ho — \"limited resources me best result\".</li>\n<li><b>Objective function ⭐:</b> jo maximize/minimize karna hai — <b>Z = ax + by</b> form me (jaise Z = 50x + 40y = total profit).</li>\n<li><b>Constraints ⭐:</b> linear inequalities jo x aur y pe limits lagati hain — resources, time, capacity (2x + 3y ≤ 120 type).</li>\n<li><b>Non-negativity ⭐:</b> <b>x ≥ 0, y ≥ 0</b> hamesha add hoti hai — cheezein negative me ban hi nahi sakti!</li>\n<li>\"Linear\" isliye — saari equations/inequalities FIRST DEGREE ki hain (koi x², xy nahi).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: factory me 2 products, limited material/time — kitna-kya banaye ki profit MAX? Yehi LPP solve karta hai.</p>"
   },
   {
    "h": "2️⃣ Inequalities Ka Graph — Feasible Region Banana ⭐⭐",
    "body": "<ul>\n<li><b>Step 1:</b> har inequality ko pehle EQUATION ki tarah plot karo — line banao (2 points se: x = 0 aur y = 0 rakhke intercepts nikal lo!).</li>\n<li><b>Step 2 ⭐:</b> kaunsa SIDE shade karna hai? Test point (0, 0) daalo — inequality TRUE → origin wala side; FALSE → doosra side. (Line origin se guzre to (1, 0) try karo.)</li>\n<li><b>≤ type:</b> line + uske neeche/origin side. <b>≥ type:</b> line + upar/door wala side. Line SOLID banti hai (= included hai na!).</li>\n<li><b>Feasible region ⭐⭐:</b> SAARI inequalities ka <b>COMMON region</b> — jahan sab conditions ek saath satisfy hoti hain. x ≥ 0, y ≥ 0 ki wajah se FIRST QUADRANT me hi rahega.</li>\n<li>Feasible region ke andar/par har point ek <b>feasible solution</b> hai; bahar koi bhi point constraints tod deta hai.</li>\n</ul>\n<p class=\"small-note\">🎯 Drawing tip: scale sahi lo, har line label karo, feasible region dark shade karo — boards me graph ke marks hote hain!</p>"
   },
   {
    "h": "3️⃣ Corner Point Method — Answer Corners Pe! ⭐⭐",
    "body": "<ul>\n<li><b>Fundamental theorem ⭐⭐:</b> bounded feasible region me objective function ka MAX/MIN hamesha kisi <b>CORNER POINT (vertex)</b> pe milta hai — andar kahin nahi!</li>\n<li><b>Method ⭐⭐:</b> (1) Feasible region banao. (2) Saare <b>corner points</b> nikalo (lines ki pairwise intersections solve karke!). (3) Har corner pe Z ka value nikalo. (4) Sabse bada = maximum, sabse chhota = minimum.</li>\n<li>Corner points nikalne ke liye do-do lines ki equations SIMULTANEOUSLY solve karo — (x, y) intersection aa jaayega.</li>\n<li>Example: Z = 3x + 4y, corners (0,0), (4,0), (2,3), (0,5) → Z: 0, 12, 18, 20 → <b>max 20 at (0, 5), min 0 at (0, 0)</b>.</li>\n<li><b>Table banao ⭐:</b> corner | Z-value — examiner ko clean presentation chahiye, aur tumhe confusion se bachav.</li>\n</ul>\n<p class=\"small-note\">💡 Kyun corners pe? Z = ax + by lines ke parallel family hai — Z badhate jao to line slide hoti hai, region chhodne se PEHLE corner pe rukti hai!</p>"
   },
   {
    "h": "4️⃣ Bounded vs Unbounded Regions ⭐",
    "body": "<ul>\n<li><b>Bounded region ⭐:</b> feasible region ek CLOSED polygon (har taraf se ghera hua) — max AUR min dono exist karte hain, corners pe.</li>\n<li><b>Unbounded region ⭐:</b> region ek ya zyada direction me OPEN jaata hai (infinity tak) — max/min exist kar sakte hain ya nahi, CAREFULLY check karo!</li>\n<li><b>Unbounded me rule ⭐⭐:</b> corners pe Z ke extreme value ke baad EK EXTRA STEP: Z &gt; M (max ke liye) ya Z &lt; m (min ke liye) wali line ka <b>open half-plane</b> feasible region ko kaate ya nahi — kaate to max/min EXIST NAHI karta!</li>\n<li>Example: minimize Z = 3x + 5y, unbounded region, min corner pe m = 26 → check: 3x + 5y &lt; 26 ka half-plane region se overlap? Nahi → min = 26 confirmed.</li>\n<li>Boards me ZYADATAR bounded region hi aata hai — par unbounded wala extra-check wala question 5-marker me pucha gaya hai, taiyaar raho.</li>\n</ul>\n<p class=\"small-note\">🎯 Unbounded = \"region khula hai\" — answer confirm karne se pehle half-plane overlap test ZAROORI hai. Ye step marks ka deciding factor hai!</p>"
   },
   {
    "h": "5️⃣ Syllabus Note aur Exam Pattern",
    "body": "<ul>\n<li><b>Rationalized syllabus ⭐:</b> LPP ki <b>mathematical formulation</b> (word problem se constraints khud banana — diet problem, manufacturing problem types) NCERT se <b>DELETE</b> ho gaya hai.</li>\n<li><b>Ab kya aata hai ⭐:</b> constraints AUR objective function <b>ready-made diye hote hain</b> — tumhe sirf graph bana ke solve karna hai (graphical method, 2 variables).</li>\n<li><b>Weightage:</b> ~5 marks — ek fixed 5-marker: \"Solve graphically: Maximize Z = ... subject to ...\".</li>\n<li><b>Steps recap:</b> lines plot → shade → feasible region → corners → Z table → answer (value + point dono likho!).</li>\n<li><b>Common mistakes:</b> feasible region galat shade karna; corner points adhoore nikalna; answer me point (x, y) mention na karna — sirf Z ka value nahi, KAHAN milta hai wo bhi chahiye!</li>\n</ul>\n<p class=\"small-note\">💡 LPP ab \"graph padhna + corners pe arithmetic\" — chapter chhota aur scoring hai, pakka 5 marks!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ रैखिक प्रोग्रामन क्या है — सर्वोत्तम उत्तर निकालना ⭐",
    "body": "<ul>\n<li><b>रैखिक प्रोग्रामन समस्या (LPP):</b> किसी राशि को <b>अधिकतम या न्यूनतम</b> करना (लाभ, लागत) जबकि शर्तें रैखिक असमिकाओं में हों।</li>\n<li><b>उद्देश्य फलन ⭐:</b> जिसे अधिकतम/न्यूनतम करना है — <b>Z = ax + by</b>।</li>\n<li><b>प्रतिबंध ⭐:</b> रैखिक असमिकाएं — संसाधन, समय, क्षमता की सीमाएं।</li>\n<li><b>अऋणात्मकता ⭐:</b> <b>x ≥ 0, y ≥ 0</b> सदैव जुड़ती है!</li>\n<li>\"रैखिक\" क्योंकि सभी समीकरण <b>प्रथम घात</b> के हैं।</li>\n</ul>\n<p class=\"small-note\">💡 सीमित संसाधनों में सर्वोत्तम परिणाम — यही LPP है।</p>"
   },
   {
    "h": "2️⃣ असमिकाओं का आलेख — सुसंगत क्षेत्र बनाना ⭐⭐",
    "body": "<ul>\n<li><b>चरण 1:</b> प्रत्येक असमिका को पहले <b>समीकरण</b> की तरह खींचो (x = 0 और y = 0 रखकर अंतःखंड निकालो)।</li>\n<li><b>चरण 2 ⭐:</b> कौन-सा पक्ष छायांकित करें? परीक्षण बिंदु (0, 0) डालो — सत्य → मूल बिंदु वाला पक्ष; असत्य → दूसरा।</li>\n<li><b>सुसंगत क्षेत्र ⭐⭐:</b> सभी असमिकाओं का <b>उभयनिष्ठ क्षेत्र</b> — x ≥ 0, y ≥ 0 से <b>प्रथम चतुर्थांश</b> में।</li>\n<li>क्षेत्र के अंदर/पर प्रत्येक बिंदु एक <b>सुसंगत हल</b> है।</li>\n</ul>\n<p class=\"small-note\">🎯 पैमाना सही लो, रेखाएं लेबल करो, क्षेत्र गहरा छायांकित करो — आलेख के अंक हैं!</p>"
   },
   {
    "h": "3️⃣ कोना-बिंदु विधि — उत्तर कोनों पर! ⭐⭐",
    "body": "<ul>\n<li><b>मूल प्रमेय ⭐⭐:</b> परिबद्ध सुसंगत क्षेत्र में अधिकतम/न्यूनतम सदैव किसी <b>कोना-बिंदु (शीर्ष)</b> पर मिलता है!</li>\n<li><b>विधि ⭐⭐:</b> (1) क्षेत्र बनाओ। (2) सभी <b>कोना-बिंदु</b> निकालो (रेखाओं के प्रतिच्छेदन से)। (3) प्रत्येक पर Z निकालो। (4) सबसे बड़ा = अधिकतम, सबसे छोटा = न्यूनतम।</li>\n<li>उदाहरण: Z = 3x + 4y, कोने (0,0), (4,0), (2,3), (0,5) → Z: 0, 12, 18, 20 → <b>अधिकतम 20, (0, 5) पर</b>।</li>\n<li><b>तालिका बनाओ ⭐:</b> कोना | Z-मान — स्पष्ट प्रस्तुति = पूर्ण अंक।</li>\n</ul>\n<p class=\"small-note\">💡 Z = ax + by समांतर रेखाओं का परिवार है — रेखा क्षेत्र छोड़ने से पहले कोने पर रुकती है!</p>"
   },
   {
    "h": "4️⃣ परिबद्ध बनाम अपरिबद्ध क्षेत्र ⭐",
    "body": "<ul>\n<li><b>परिबद्ध क्षेत्र ⭐:</b> बंद बहुभुज — अधिकतम और न्यूनतम <b>दोनों</b> मौजूद।</li>\n<li><b>अपरिबद्ध क्षेत्र ⭐:</b> क्षेत्र किसी दिशा में <b>खुला</b> — अधिकतम/न्यूनतम हो भी सकता है, नहीं भी!</li>\n<li><b>अपरिबद्ध में नियम ⭐⭐:</b> कोनों के बाद एक अतिरिक्त जांच: Z &lt; m (न्यूनतम के लिए) के अर्ध-समतल का क्षेत्र से <b>अतिव्यापन</b> — हो तो न्यूनतम मौजूद <b>नहीं</b>!</li>\n<li>बोर्ड में अधिकतर परिबद्ध क्षेत्र आता है — पर अपरिबद्ध वाला प्रश्न भी पूछा गया है।</li>\n</ul>\n<p class=\"small-note\">🎯 अपरिबद्ध = अतिरिक्त अर्ध-समतल जांच अनिवार्य — यही अंकों का निर्णायक चरण!</p>"
   },
   {
    "h": "5️⃣ पाठ्यक्रम टिप्पणी और परीक्षा पैटर्न",
    "body": "<ul>\n<li><b>युक्तिसंगत पाठ्यक्रम ⭐:</b> LPP का <b>गणितीय सूत्रीकरण</b> (शाब्दिक प्रश्न से प्रतिबंध बनाना) NCERT से <b>हटाया गया</b>।</li>\n<li><b>अब क्या आता है ⭐:</b> प्रतिबंध और उद्देश्य फलन <b>तैयार दिए होते हैं</b> — केवल आलेखीय विधि से हल करना है (2 चर)।</li>\n<li><b>अंक:</b> ~5 — निश्चित 5-अंकीय: \"आलेखीय विधि से हल करो...\"।</li>\n<li><b>सामान्य गलतियां:</b> क्षेत्र गलत छायांकित करना; कोने अधूरे; उत्तर में बिंदु (x, y) न लिखना।</li>\n</ul>\n<p class=\"small-note\">💡 LPP = \"आलेख + कोनों की अंकगणित\" — छोटा और स्कोरिंग अध्याय!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ What Is an LPP — Finding the Best Possible Answer ⭐",
    "body": "<ul>\n<li><b>Linear Programming Problem (LPP):</b> <b>MAXIMIZING or MINIMIZING</b> something (profit, cost, output) when the conditions are given as LINEAR inequalities — \"the best result within limited resources\".</li>\n<li><b>Objective function ⭐:</b> what you maximize/minimize — in the form <b>Z = ax + by</b> (like Z = 50x + 40y = total profit).</li>\n<li><b>Constraints ⭐:</b> the linear inequalities that limit x and y — resources, time, capacity (like 2x + 3y ≤ 120).</li>\n<li><b>Non-negativity ⭐:</b> <b>x ≥ 0, y ≥ 0</b> is always added — you cannot make a negative number of things!</li>\n<li>\"Linear\" because every equation/inequality is of the FIRST DEGREE (no x², no xy).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: a factory with 2 products and limited material/time — how much of each should it make for MAX profit? That is what an LPP solves.</p>"
   },
   {
    "h": "2️⃣ Graphing Inequalities — Building the Feasible Region ⭐⭐",
    "body": "<ul>\n<li><b>Step 1:</b> first plot each inequality as an EQUATION — draw the line (use the intercepts: set x = 0, then y = 0!).</li>\n<li><b>Step 2 ⭐:</b> which SIDE to shade? Plug the test point (0, 0) — inequality TRUE → the origin side; FALSE → the other side. (If the line passes through the origin, try (1, 0).)</li>\n<li><b>≤ type:</b> the line plus the side below/toward the origin. <b>≥ type:</b> the line plus the side above/away. The line stays SOLID (equality is included!).</li>\n<li><b>Feasible region ⭐⭐:</b> the region COMMON to ALL the inequalities — where every condition holds at once. Thanks to x ≥ 0, y ≥ 0, it lies in the FIRST QUADRANT.</li>\n<li>Every point inside/on the feasible region is a <b>feasible solution</b>; any point outside breaks a constraint.</li>\n</ul>\n<p class=\"small-note\">🎯 Drawing tip: use a proper scale, label every line, shade the feasible region dark — boards award marks for the graph!</p>"
   },
   {
    "h": "3️⃣ The Corner Point Method — Answers Live at Corners! ⭐⭐",
    "body": "<ul>\n<li><b>Fundamental theorem ⭐⭐:</b> in a bounded feasible region, the MAX/MIN of the objective function is ALWAYS attained at a <b>CORNER POINT (vertex)</b> — never inside!</li>\n<li><b>Method ⭐⭐:</b> (1) Draw the feasible region. (2) Find ALL the <b>corner points</b> (solve the lines' pairwise intersections!). (3) Evaluate Z at each corner. (4) The largest = maximum, the smallest = minimum.</li>\n<li>To get corner points, solve the pairs of line equations SIMULTANEOUSLY — the intersection (x, y) comes out.</li>\n<li>Example: Z = 3x + 4y with corners (0,0), (4,0), (2,3), (0,5) → Z: 0, 12, 18, 20 → <b>max 20 at (0, 5), min 0 at (0, 0)</b>.</li>\n<li><b>Make a table ⭐:</b> corner | Z-value — the examiner wants a clean presentation, and it saves you from confusion.</li>\n</ul>\n<p class=\"small-note\">💡 Why corners? Z = ax + by is a family of parallel lines — as Z grows the line slides, and it stops at a corner JUST before leaving the region!</p>"
   },
   {
    "h": "4️⃣ Bounded vs Unbounded Regions ⭐",
    "body": "<ul>\n<li><b>Bounded region ⭐:</b> the feasible region is a CLOSED polygon (fenced on all sides) — both max AND min exist, at corners.</li>\n<li><b>Unbounded region ⭐:</b> the region stays OPEN in one or more directions (runs to infinity) — a max/min may or may not exist; check CAREFULLY!</li>\n<li><b>Rule for unbounded regions ⭐⭐:</b> after computing the extreme corner value, ONE EXTRA STEP: check whether the open half-plane Z &gt; M (for max) or Z &lt; m (for min) <b>overlaps</b> the feasible region — if it does, the max/min DOES NOT exist!</li>\n<li>Example: minimize Z = 3x + 5y on an unbounded region, corner min m = 26 → check: does 3x + 5y &lt; 26 overlap the region? No → min = 26 confirmed.</li>\n<li>Boards mostly give bounded regions — but the unbounded extra-check question HAS appeared as a 5-marker; stay prepared.</li>\n</ul>\n<p class=\"small-note\">🎯 Unbounded = \"the region is open\" — the half-plane overlap test is MANDATORY before confirming the answer. This step decides your marks!</p>"
   },
   {
    "h": "5️⃣ Syllabus Note and Exam Pattern",
    "body": "<ul>\n<li><b>Rationalized syllabus ⭐:</b> the <b>mathematical formulation</b> of LPPs (building constraints yourself from a word problem — diet problems, manufacturing problems) is <b>DELETED</b> from NCERT.</li>\n<li><b>What comes now ⭐:</b> constraints AND the objective function are given <b>ready-made</b> — you only solve graphically (the graphical method, 2 variables).</li>\n<li><b>Weightage:</b> ~5 marks — one fixed 5-marker: \"Solve graphically: Maximize Z = ... subject to ...\".</li>\n<li><b>Steps recap:</b> plot lines → shade → feasible region → corners → Z table → answer (write BOTH the value and the point!).</li>\n<li><b>Common mistakes:</b> shading the wrong region; missing corner points; not stating WHERE the optimum occurs — the point (x, y) matters, not just Z!</li>\n</ul>\n<p class=\"small-note\">💡 LPP is now \"read a graph + corner arithmetic\" — a small, high-scoring chapter. A guaranteed 5 marks!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics ⭐",
    "items": [
     "Z = ax + by optimize karo",
     "Constraints = linear inequalities",
     "x ≥ 0, y ≥ 0 hamesha"
    ]
   },
   {
    "h": "Graph ⭐⭐",
    "items": [
     "Line banao, (0,0) test karo",
     "Feasible region = common area",
     "First quadrant me hoga"
    ]
   },
   {
    "h": "Corner method ⭐⭐",
    "items": [
     "Max/min corners pe hi",
     "Har corner pe Z nikalo",
     "Table: corner | Z"
    ]
   },
   {
    "h": "Unbounded ⭐",
    "items": [
     "Region open ho to extra check",
     "Half-plane overlap test",
     "Overlap → max/min exist nahi"
    ]
   },
   {
    "h": "Syllabus ⭐",
    "items": [
     "Formulation DELETED",
     "Ready-made problems solve karo",
     "Fixed 5-marker"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल ⭐",
    "items": [
     "Z = ax + by अनुकूलित करो",
     "प्रतिबंध = रैखिक असमिकाएं",
     "x ≥ 0, y ≥ 0 सदैव"
    ]
   },
   {
    "h": "आलेख ⭐⭐",
    "items": [
     "रेखा खींचो, (0,0) जांचो",
     "सुसंगत क्षेत्र = उभयनिष्ठ",
     "प्रथम चतुर्थांश में"
    ]
   },
   {
    "h": "कोना विधि ⭐⭐",
    "items": [
     "अधिकतम/न्यूनतम कोनों पर",
     "प्रत्येक कोने पर Z",
     "तालिका: कोना | Z"
    ]
   },
   {
    "h": "अपरिबद्ध ⭐",
    "items": [
     "क्षेत्र खुला → अतिरिक्त जांच",
     "अर्ध-समतल अतिव्यापन परीक्षण",
     "अतिव्यापन → हल मौजूद नहीं"
    ]
   },
   {
    "h": "पाठ्यक्रम ⭐",
    "items": [
     "सूत्रीकरण हटाया गया",
     "तैयार प्रश्न हल करो",
     "निश्चित 5-अंकीय"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics ⭐",
    "items": [
     "Optimize Z = ax + by",
     "Constraints = linear inequalities",
     "x ≥ 0, y ≥ 0 always"
    ]
   },
   {
    "h": "Graph ⭐⭐",
    "items": [
     "Draw line, test (0,0)",
     "Feasible region = common area",
     "Stays in the first quadrant"
    ]
   },
   {
    "h": "Corner method ⭐⭐",
    "items": [
     "Max/min only at corners",
     "Evaluate Z at each corner",
     "Table: corner | Z"
    ]
   },
   {
    "h": "Unbounded ⭐",
    "items": [
     "Open region → extra check",
     "Half-plane overlap test",
     "Overlap → max/min does not exist"
    ]
   },
   {
    "h": "Syllabus ⭐",
    "items": [
     "Formulation DELETED",
     "Solve ready-made problems",
     "Fixed 5-marker"
    ]
   }
  ]
 },
 "practice": [
  [
   "LPP me objective function kya hota hai?",
   "<b>Z = ax + by</b> — jo cheez maximize/minimize karni hai (profit, cost...)."
  ],
  [
   "x ≥ 0, y ≥ 0 kyun likhte hain?",
   "<b>Non-negativity constraints</b> — real life me cheezein negative nahi ban sakti. Isse region first quadrant me aata hai."
  ],
  [
   "Inequality ka kaunsa side shade karein kaise pata?",
   "Test point <b>(0, 0)</b> inequality me daalo — true → origin side, false → opposite side."
  ],
  [
   "Feasible region kya hai?",
   "SAARI constraints (inequalities) ka <b>common region</b> — jahan sab conditions ek saath satisfy hoti hain."
  ],
  [
   "Bounded region me max/min kahan milta hai?",
   "Hamesha kisi <b>corner point</b> pe — feasible region ke vertices pe Z check karo."
  ],
  [
   "Z = 4x + 3y ke corners (0,0), (5,0), (0,6) pe values?",
   "Z: 0, 20, 18 → <b>max = 20 at (5, 0)</b>; min = 0 at (0, 0)."
  ],
  [
   "Corner points kaise nikalte hain?",
   "Do-do boundary lines ki equations <b>simultaneously solve</b> karke — intersections hi corners hain."
  ],
  [
   "Unbounded region me minimum confirm karne ka extra step?",
   "Z < m wala <b>half-plane</b> feasible region ko overlap karta hai ya nahi — <b>overlap nahi</b> to min confirmed."
  ],
  [
   "Answer me sirf Z ka value likhna kaafi hai?",
   "<b>Nahi</b> — point (x, y) bhi likhna zaroori hai jahan optimum milta hai."
  ],
  [
   "Diet problem type formulation questions ab aate hain?",
   "<b>Nahi</b> — mathematical formulation of LPP rationalized syllabus se <b>delete</b> ho gaya. Ready-made problems solve karne hain."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-13/",
  "title": "Probability"
 }
}

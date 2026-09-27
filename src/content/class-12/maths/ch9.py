# Class 12 Maths, Chapter 9 - Differential Equations
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 9,
 "title_en": "Differential Equations",
 "title_hi": "अवकल समीकरण",
 "tagline": "Order-degree se lekar variable separable, homogeneous aur linear DE tak",
 "jee": "HIGH",
 "meta_desc": "Class 12 Maths Chapter 9: Differential Equations — long + short notes in Hindi, English, Hinglish. Order, degree, general and particular solutions, variable separable, homogeneous and linear differential equations, integrating factor.",
 "video": None,
 "card_tag": "Order-degree se lekar variable separable, homogeneous aur linear DE tak",
 "card_topics": [
  "🔢 Order & degree",
  "✅ General vs particular",
  "✂️ Variable separable + homogeneous",
  "📏 Linear DE + IF formula"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Differential Equation Kya Hai — Derivatives Wali Equation ⭐",
    "body": "<ul>\n<li><b>Definition:</b> equation jisme independent variable (x), dependent variable (y) AUR y ke <b>derivatives</b> (dy/dx, d²y/dx²...) aate hon. Example: dy/dx + 2y = eˣ.</li>\n<li><b>Kahan use hoti hai:</b> population growth, cooling, radioactive decay, motion — jahan \"rate of change\" ka rule ho, wahan DE!</li>\n<li><b>Order ⭐:</b> equation me sabse HIGH derivative ki order. dy/dx + y = 0 → order <b>1</b>; d²y/dx² + y = 0 → order <b>2</b>.</li>\n<li><b>Degree ⭐:</b> highest derivative ki POWER (equation ko derivatives me polynomial banake, fractions/radicals clear karke!). (d²y/dx²)³ + dy/dx = 0 → order 2, degree <b>3</b>.</li>\n<li><b>Degree kab defined NAHI:</b> jab derivative ke andar sin/log ho — sin(dy/dx) = x ki degree nahi hoti (polynomial nahi ban sakta)!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: order = \"kitni baar differentiate kiya\", degree = \"highest derivative ki ghata\". Pehle equation ko saaf-suthra banao, phir count karo!</p>"
   },
   {
    "h": "2️⃣ Solutions — General aur Particular ⭐⭐",
    "body": "<ul>\n<li><b>General solution:</b> DE ka solution jisme <b>arbitrary constants</b> (C₁, C₂...) hon. Order n ki DE ke general solution me EXACTLY <b>n arbitrary constants</b> hote hain! ⭐</li>\n<li><b>Particular solution:</b> general solution me constants ko SPECIFIC values deke mila — initial conditions (jaise y(0) = 2) se nikalte hain.</li>\n<li><b>Verify karna ⭐:</b> diya gaya function solution hai ya nahi — differentiate karke DE me DAAL do, satisfy ho gayi to solution hai. (Boards me direct 2-marker!)</li>\n<li>Example: y = Aeˣ + Be⁻ˣ, d²y/dx² − y = 0 ka solution hai — do baar differentiate karke check karo: y″ = y ✓.</li>\n<li>Solution bhi ek FUNCTION hai, number nahi — family of curves (har C ke liye ek curve!).</li>\n</ul>\n<p class=\"small-note\">🎯 Order = constants ka count. Order 2 DE ka general solution me 2 constants — nahi mile to solution incomplete hai!</p>"
   },
   {
    "h": "3️⃣ Variable Separable — Sabse Pehli Method ⭐⭐",
    "body": "<ul>\n<li><b>Idea:</b> x wali terms + dx ek taraf, y wali terms + dy doosri taraf — phir <b>dono taraf integrate</b> karo. Sabse simple aur sabse zyada use hone wali method!</li>\n<li><b>Steps ⭐:</b> (1) dy/dx = f(x)·g(y) form me lao. (2) dy/g(y) = f(x)dx. (3) ∫ dy/g(y) = ∫ f(x) dx + C. (4) y ke liye solve karo (agar possible ho).</li>\n<li>Example: dy/dx = y → dy/y = dx → ln|y| = x + C → <b>y = Aeˣ</b> (A = e^C — growth/decay equation!).</li>\n<li>Example: dy/dx = x/y → y dy = x dx → y²/2 = x²/2 + C → <b>y² − x² = 2C</b>.</li>\n<li><b>Particular solution:</b> initial condition (x₀, y₀) daal ke C nikalo — wahi 3-marker ka second half hota hai.</li>\n</ul>\n<p class=\"small-note\">💡 Variable separable = \"alag-alag karo, phir dono side integral\". DE solve karne ka default pehla attempt yahi hona chahiye!</p>"
   },
   {
    "h": "4️⃣ Homogeneous Differential Equations ⭐",
    "body": "<ul>\n<li><b>Pehchan ⭐:</b> dy/dx = F(y/x) form me likhi ja sake — ya har term ki TOTAL DEGREE same ho (x² + y², xy sab degree 2). Ratio y/x hi hero hai.</li>\n<li><b>Method ⭐⭐:</b> substitute <b>y = vx</b> (matlab v = y/x). Tab <b>dy/dx = v + x·dv/dx</b> — ye substitution DE ko variable separable me convert kar deta hai!</li>\n<li><b>Steps:</b> (1) y = vx daalo. (2) v + x dv/dx = F(v) milega. (3) x dv/dx = F(v) − v → separate karo: dv/(F(v) − v) = dx/x. (4) Integrate, phir v = y/x wapas daalo.</li>\n<li>x = vy substitution bhi kabhi-kabhi easy padta hai (dx/dy form me) — dono try kar sakte ho.</li>\n<li>Example: dy/dx = (x² + y²)/(2xy) → y = vx → v + x dv/dx = (1 + v²)/(2v) → x dv/dx = (1 − v²)/(2v) → separable!</li>\n</ul>\n<p class=\"small-note\">🎯 Homogeneous = \"har term same degree\" → y = vx daalo → separable ban jaata hai. Conversion hi asli trick hai!</p>"
   },
   {
    "h": "5️⃣ Linear Differential Equations — IF Wala Game ⭐⭐",
    "body": "<ul>\n<li><b>Standard form ⭐⭐:</b> <b>dy/dx + P(x)·y = Q(x)</b> — y aur dy/dx dono FIRST power me, saath me multiply nahi (y·dy/dx = NOT linear!).</li>\n<li><b>Integrating Factor (IF) ⭐⭐:</b> <b>IF = e^(∫P dx)</b> — puri equation ko IF se multiply karo, LHS exact derivative ban jaata hai: d/dx[y·IF] = Q·IF.</li>\n<li><b>Solution ⭐⭐:</b> <b>y·IF = ∫(Q·IF) dx + C</b> — formula ratt lo, boards me direct 5-marker!</li>\n<li>Example: dy/dx + y = eˣ → IF = e^∫dx = eˣ → y·eˣ = ∫e²ˣ dx = e²ˣ/2 + C → <b>y = eˣ/2 + Ce⁻ˣ</b>.</li>\n<li><b>Second type:</b> dx/dy + P(y)·x = Q(y) — same game, roles swap: IF = e^∫P dy, solution x·IF = ∫(Q·IF) dy + C.</li>\n<li>Pehle equation ko standard form me LAANA zaroori hai — dy/dx ka coefficient 1 karo, warna P galat banega!</li>\n</ul>\n<p class=\"small-note\">💡 Linear DE ka flow: standard form → P pehchano → IF nikalo → formula lagao → C nikalo. Machine jaisa process, practice se pakka!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ अवकल समीकरण क्या है — अवकलजों वाला समीकरण ⭐",
    "body": "<ul>\n<li><b>परिभाषा:</b> समीकरण जिसमें x, y <b>और</b> y के अवकलज (dy/dx, d²y/dx²...) आते हों। उदाहरण: dy/dx + 2y = eˣ।</li>\n<li><b>उपयोग:</b> जनसंख्या वृद्धि, शीतलन, रेडियोधर्मी क्षय, गति — जहां \"परिवर्तन दर\" का नियम हो।</li>\n<li><b>कोटि (order) ⭐:</b> सबसे उच्च अवकलज की कोटि। d²y/dx² + y = 0 → कोटि <b>2</b>।</li>\n<li><b>घात (degree) ⭐:</b> उच्चतम अवकलज की <b>घात</b> (समीकरण को अवकलजों में बहुपद बनाकर!)। (d²y/dx²)³ → घात <b>3</b>।</li>\n<li><b>घात परिभाषित नहीं:</b> sin(dy/dx) = x जैसे में — बहुपद नहीं बनता!</li>\n</ul>\n<p class=\"small-note\">💡 कोटि = \"कितनी बार अवकलन\", घात = \"उच्चतम अवकलज की घात\"।</p>"
   },
   {
    "h": "2️⃣ हल — व्यापक और विशिष्ट ⭐⭐",
    "body": "<ul>\n<li><b>व्यापक हल:</b> हल जिसमें <b>स्वेच्छ अचर</b> (C₁, C₂...) हों। कोटि n के समीकरण के व्यापक हल में ठीक <b>n अचर</b>! ⭐</li>\n<li><b>विशिष्ट हल:</b> अचरों को विशिष्ट मान देकर मिला — प्रारंभिक प्रतिबंधों (y(0) = 2) से।</li>\n<li><b>सत्यापन ⭐:</b> दिया फलन हल है या नहीं — अवकलन करके समीकरण में <b>रखो</b>, संतुष्ट हुई तो हल है।</li>\n<li>उदाहरण: y = Aeˣ + Be⁻ˣ, समीकरण d²y/dx² − y = 0 का हल है — y″ = y ✓।</li>\n</ul>\n<p class=\"small-note\">🎯 कोटि = अचरों की संख्या। कोटि 2 → 2 अचर!</p>"
   },
   {
    "h": "3️⃣ चर-पृथक्करण — सबसे पहली विधि ⭐⭐",
    "body": "<ul>\n<li><b>विचार:</b> x-पद + dx एक ओर, y-पद + dy दूसरी ओर — फिर <b>दोनों ओर समाकलन</b>।</li>\n<li><b>चरण ⭐:</b> (1) dy/dx = f(x)·g(y) रूप में लाओ। (2) dy/g(y) = f(x)dx। (3) दोनों ओर ∫ + C। (4) y के लिए हल करो।</li>\n<li>उदाहरण: dy/dx = y → dy/y = dx → ln|y| = x + C → <b>y = Aeˣ</b>।</li>\n<li>उदाहरण: dy/dx = x/y → y dy = x dx → <b>y² − x² = 2C</b>।</li>\n<li><b>विशिष्ट हल:</b> प्रारंभिक प्रतिबंध (x₀, y₀) से C निकालो।</li>\n</ul>\n<p class=\"small-note\">💡 चर-पृथक्करण = \"अलग करो, दोनों ओर समाकलन\" — हमेशा पहला प्रयास!</p>"
   },
   {
    "h": "4️⃣ समघातीय अवकल समीकरण ⭐",
    "body": "<ul>\n<li><b>पहचान ⭐:</b> dy/dx = F(y/x) रूप में लिखी जा सके — या प्रत्येक पद की <b>कुल घात</b> समान हो।</li>\n<li><b>विधि ⭐⭐:</b> प्रतिस्थापन <b>y = vx</b> (अर्थात v = y/x)। तब <b>dy/dx = v + x·dv/dx</b> — समीकरण चर-पृथक्करणीय बन जाता है!</li>\n<li><b>चरण:</b> (1) y = vx रखो। (2) v + x dv/dx = F(v) मिलेगा। (3) dv/(F(v) − v) = dx/x। (4) समाकलन करके v = y/x वापस रखो।</li>\n<li>x = vy प्रतिस्थापन भी कभी आसान पड़ता है।</li>\n</ul>\n<p class=\"small-note\">🎯 समघातीय = \"हर पद समान घात\" → y = vx → पृथक्करणीय। रूपांतरण ही असली चाल!</p>"
   },
   {
    "h": "5️⃣ रैखिक अवकल समीकरण — IF का खेल ⭐⭐",
    "body": "<ul>\n<li><b>मानक रूप ⭐⭐:</b> <b>dy/dx + P(x)·y = Q(x)</b> — y और dy/dx दोनों प्रथम घात में, साथ गुणित नहीं।</li>\n<li><b>समाकलन गुणक (IF) ⭐⭐:</b> <b>IF = e^(∫P dx)</b> — गुणा करने पर बायां पक्ष ठीक अवकलज बनता है: d/dx[y·IF] = Q·IF।</li>\n<li><b>हल ⭐⭐:</b> <b>y·IF = ∫(Q·IF) dx + C</b> — सूत्र कंठस्थ करो, सीधा 5-अंकीय!</li>\n<li>उदाहरण: dy/dx + y = eˣ → IF = eˣ → y·eˣ = e²ˣ/2 + C → <b>y = eˣ/2 + Ce⁻ˣ</b>।</li>\n<li><b>दूसरा रूप:</b> dx/dy + P(y)·x = Q(y) — IF = e^∫P dy, हल x·IF = ∫(Q·IF) dy + C।</li>\n</ul>\n<p class=\"small-note\">💡 प्रवाह: मानक रूप → P पहचानो → IF निकालो → सूत्र → C।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ What Is a Differential Equation — An Equation with Derivatives ⭐",
    "body": "<ul>\n<li><b>Definition:</b> an equation containing the independent variable (x), dependent variable (y) AND <b>derivatives</b> of y (dy/dx, d²y/dx²...). Example: dy/dx + 2y = eˣ.</li>\n<li><b>Where it is used:</b> population growth, cooling, radioactive decay, motion — wherever there is a rule about a \"rate of change\", there is a DE!</li>\n<li><b>Order ⭐:</b> the order of the HIGHEST derivative in the equation. dy/dx + y = 0 → order <b>1</b>; d²y/dx² + y = 0 → order <b>2</b>.</li>\n<li><b>Degree ⭐:</b> the POWER of the highest derivative (after writing the equation as a polynomial in derivatives — clear fractions and radicals!). (d²y/dx²)³ + dy/dx = 0 → order 2, degree <b>3</b>.</li>\n<li><b>Degree NOT defined when:</b> a derivative sits inside sin/log — sin(dy/dx) = x has no degree (it is not a polynomial in derivatives)!</li>\n</ul>\n<p class=\"small-note\">💡 Feel: order = \"how many times differentiated\", degree = \"the power of the highest derivative\". Clean the equation first, then count!</p>"
   },
   {
    "h": "2️⃣ Solutions — General and Particular ⭐⭐",
    "body": "<ul>\n<li><b>General solution:</b> a solution containing <b>arbitrary constants</b> (C₁, C₂...). A DE of order n has EXACTLY <b>n arbitrary constants</b> in its general solution! ⭐</li>\n<li><b>Particular solution:</b> obtained by giving the constants SPECIFIC values — computed from initial conditions (like y(0) = 2).</li>\n<li><b>Verifying ⭐:</b> to check whether a given function is a solution — differentiate it and PLUG it into the DE. Satisfied? It is a solution. (A direct 2-marker in boards!)</li>\n<li>Example: y = Aeˣ + Be⁻ˣ solves d²y/dx² − y = 0 — differentiate twice and check: y″ = y ✓.</li>\n<li>A solution is a FUNCTION, not a number — a family of curves (one curve per C!).</li>\n</ul>\n<p class=\"small-note\">🎯 Order = count of constants. The general solution of an order-2 DE holds 2 constants — missing one means the solution is incomplete!</p>"
   },
   {
    "h": "3️⃣ Variable Separable — The First Method to Try ⭐⭐",
    "body": "<ul>\n<li><b>Idea:</b> push x-terms + dx to one side, y-terms + dy to the other — then <b>integrate both sides</b>. The simplest and most-used method!</li>\n<li><b>Steps ⭐:</b> (1) Bring the DE to dy/dx = f(x)·g(y). (2) Write dy/g(y) = f(x)dx. (3) ∫ dy/g(y) = ∫ f(x) dx + C. (4) Solve for y (if possible).</li>\n<li>Example: dy/dx = y → dy/y = dx → ln|y| = x + C → <b>y = Aeˣ</b> (A = e^C — the growth/decay equation!).</li>\n<li>Example: dy/dx = x/y → y dy = x dx → y²/2 = x²/2 + C → <b>y² − x² = 2C</b>.</li>\n<li><b>Particular solution:</b> plug the initial condition (x₀, y₀) to find C — that is the second half of a 3-marker.</li>\n</ul>\n<p class=\"small-note\">💡 Variable separable = \"separate, then integrate both sides\". This should always be your first attempt at solving a DE!</p>"
   },
   {
    "h": "4️⃣ Homogeneous Differential Equations ⭐",
    "body": "<ul>\n<li><b>Identifying ⭐:</b> the DE can be written as dy/dx = F(y/x) — or every term has the same TOTAL DEGREE (x² + y², xy are all degree 2). The ratio y/x is the hero.</li>\n<li><b>Method ⭐⭐:</b> substitute <b>y = vx</b> (so v = y/x). Then <b>dy/dx = v + x·dv/dx</b> — this substitution converts the DE into a variable-separable one!</li>\n<li><b>Steps:</b> (1) Plug y = vx. (2) You get v + x dv/dx = F(v). (3) So x dv/dx = F(v) − v → separate: dv/(F(v) − v) = dx/x. (4) Integrate, then put v = y/x back.</li>\n<li>Substituting x = vy can also be easier at times (the dx/dy form) — both are worth trying.</li>\n<li>Example: dy/dx = (x² + y²)/(2xy) → y = vx → v + x dv/dx = (1 + v²)/(2v) → x dv/dx = (1 − v²)/(2v) → separable!</li>\n</ul>\n<p class=\"small-note\">🎯 Homogeneous = \"every term has the same degree\" → plug y = vx → it turns separable. The conversion is the real trick!</p>"
   },
   {
    "h": "5️⃣ Linear Differential Equations — The IF Game ⭐⭐",
    "body": "<ul>\n<li><b>Standard form ⭐⭐:</b> <b>dy/dx + P(x)·y = Q(x)</b> — y and dy/dx both in the FIRST power, never multiplied together (y·dy/dx = NOT linear!).</li>\n<li><b>Integrating Factor (IF) ⭐⭐:</b> <b>IF = e^(∫P dx)</b> — multiplying the whole equation by IF turns the LHS into an exact derivative: d/dx[y·IF] = Q·IF.</li>\n<li><b>Solution ⭐⭐:</b> <b>y·IF = ∫(Q·IF) dx + C</b> — memorize the formula; a direct 5-marker in boards!</li>\n<li>Example: dy/dx + y = eˣ → IF = e^∫dx = eˣ → y·eˣ = ∫e²ˣ dx = e²ˣ/2 + C → <b>y = eˣ/2 + Ce⁻ˣ</b>.</li>\n<li><b>Second type:</b> dx/dy + P(y)·x = Q(y) — same game with swapped roles: IF = e^∫P dy, solution x·IF = ∫(Q·IF) dy + C.</li>\n<li>You MUST bring the equation to standard form first — make the coefficient of dy/dx equal to 1, otherwise P will be wrong!</li>\n</ul>\n<p class=\"small-note\">💡 Linear DE flow: standard form → identify P → find IF → apply the formula → find C. A machine-like process; drill it!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basics ⭐",
    "items": [
     "DE = derivatives wali equation",
     "Order = highest derivative",
     "Degree = highest derivative ki power"
    ]
   },
   {
    "h": "Solutions ⭐",
    "items": [
     "General: n order → n constants",
     "Particular: initial condition se",
     "Verify: DE me daal ke check"
    ]
   },
   {
    "h": "Separable ⭐⭐",
    "items": [
     "x ek taraf, y doosri taraf",
     "dy/g(y) = f(x)dx → integrate",
     "dy/dx = y → y = Aeˣ"
    ]
   },
   {
    "h": "Homogeneous ⭐",
    "items": [
     "F(y/x) form ya same degree",
     "y = vx substitute karo",
     "dy/dx = v + x dv/dx"
    ]
   },
   {
    "h": "Linear ⭐⭐",
    "items": [
     "dy/dx + Py = Q",
     "IF = e^∫P dx",
     "y·IF = ∫(Q·IF)dx + C"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल ⭐",
    "items": [
     "DE = अवकलजों वाला समीकरण",
     "कोटि = उच्चतम अवकलज",
     "घात = उच्चतम अवकलज की घात"
    ]
   },
   {
    "h": "हल ⭐",
    "items": [
     "व्यापक: कोटि n → n अचर",
     "विशिष्ट: प्रारंभिक प्रतिबंध से",
     "सत्यापन: समीकरण में रखो"
    ]
   },
   {
    "h": "पृथक्करण ⭐⭐",
    "items": [
     "x एक ओर, y दूसरी ओर",
     "dy/g(y) = f(x)dx → समाकलन",
     "dy/dx = y → y = Aeˣ"
    ]
   },
   {
    "h": "समघातीय ⭐",
    "items": [
     "F(y/x) रूप",
     "y = vx प्रतिस्थापन",
     "dy/dx = v + x dv/dx"
    ]
   },
   {
    "h": "रैखिक ⭐⭐",
    "items": [
     "dy/dx + Py = Q",
     "IF = e^∫P dx",
     "y·IF = ∫(Q·IF)dx + C"
    ]
   }
  ],
  "en": [
   {
    "h": "Basics ⭐",
    "items": [
     "DE = equation with derivatives",
     "Order = highest derivative",
     "Degree = power of the highest derivative"
    ]
   },
   {
    "h": "Solutions ⭐",
    "items": [
     "General: order n → n constants",
     "Particular: from initial conditions",
     "Verify: plug into the DE"
    ]
   },
   {
    "h": "Separable ⭐⭐",
    "items": [
     "x one side, y the other",
     "dy/g(y) = f(x)dx → integrate",
     "dy/dx = y → y = Aeˣ"
    ]
   },
   {
    "h": "Homogeneous ⭐",
    "items": [
     "F(y/x) form or same degree",
     "Substitute y = vx",
     "dy/dx = v + x dv/dx"
    ]
   },
   {
    "h": "Linear ⭐⭐",
    "items": [
     "dy/dx + Py = Q",
     "IF = e^∫P dx",
     "y·IF = ∫(Q·IF)dx + C"
    ]
   }
  ]
 },
 "practice": [
  [
   "d²y/dx² + (dy/dx)³ + y = 0 ka order aur degree?",
   "Order <b>2</b> (highest derivative d²y/dx²), degree <b>1</b> (uski power 1)."
  ],
  [
   "(dy/dx)² + sin(dy/dx) = 0 ki degree kya hai?",
   "<b>Defined nahi</b> — sin(dy/dx) ki wajah se derivatives me polynomial nahi banta."
  ],
  [
   "Order 3 ki DE ke general solution me kitne arbitrary constants?",
   "<b>3</b> — order hi constants ka count hota hai."
  ],
  [
   "y = 3eˣ solution hai kya dy/dx = y ka?",
   "<b>Haan</b> — dy/dx = 3eˣ = y ✓. (Ye particular solution hai, C = 3.)"
  ],
  [
   "dy/dx = x/y ko solve karo.",
   "y dy = x dx → y²/2 = x²/2 + C → <b>y² = x² + 2C</b>."
  ],
  [
   "dy/dx = y ka general solution?",
   "dy/y = dx → ln|y| = x + C → <b>y = Aeˣ</b>."
  ],
  [
   "Homogeneous DE me kaunsa substitution lagate hain?",
   "<b>y = vx</b> — phir dy/dx = v + x·dv/dx, aur equation separable ban jaati hai."
  ],
  [
   "dy/dx + 2y = 0 ka IF kya hai?",
   "IF = e^∫2 dx = <b>e²ˣ</b>. (Solution: y = Ce⁻²ˣ.)"
  ],
  [
   "Linear DE ka standard form bolo.",
   "<b>dy/dx + P(x)·y = Q(x)</b> — aur solution y·IF = ∫(Q·IF) dx + C, jahan IF = e^∫P dx."
  ],
  [
   "dy/dx + y = eˣ solve karo.",
   "IF = eˣ → y·eˣ = ∫e²ˣ dx = e²ˣ/2 + C → <b>y = eˣ/2 + Ce⁻ˣ</b>."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/maths/ch-10/",
  "title": "Vector Algebra"
 }
}

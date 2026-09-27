# Class 12 Chemistry, Chapter 3 - Chemical Kinetics
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 3,
 "title_en": "Chemical Kinetics",
 "title_hi": "रासायनिक बलगतिकी",
 "tagline": "Rate of reaction, order, integrated equations, Arrhenius aur collision theory",
 "jee": "HIGH",
 "meta_desc": "Class 12 Chemistry Chapter 3: Chemical Kinetics — long + short notes in Hindi, English, Hinglish. Rate of reaction, rate law, order vs molecularity, zero & first order integrated equations, half-life, Arrhenius equation, activation energy, collision theory, catalyst.",
 "video": None,
 "card_tag": "Rate of reaction, order, integrated equations, Arrhenius aur collision theory",
 "card_topics": [
  "⚡ Rate + order",
  "🧮 Zero/first order",
  "🌡️ Arrhenius + Ea",
  "💥 Collision theory"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Rate of Reaction — Kitni Tez Chalti Hai",
    "body": "<ul>\n<li><b>Chemical kinetics:</b> reaction ki <b>speed (rate)</b> aur uske mechanism ka study. Thermodynamics batata hai reaction &lt;i&gt;hogi ya nahi&lt;/i&gt;; kinetics batata hai &lt;i&gt;kitni tez&lt;/i&gt; hogi.</li>\n<li><b>Rate:</b> concentration me change ÷ time. <b>Rate = −Δ[reactant]/Δt = +Δ[product]/Δt</b>. Unit: mol L⁻¹ s⁻¹ (ya M/s).</li>\n<li><b>Average rate:</b> poore time interval pe — r_avg = Δ[x]/Δt. <b>Instantaneous rate:</b> ek particular instant pe — r_inst = −d[R]/dt (graph ki slope, tangent).</li>\n<li><b>Stoichiometry se rate ⭐:</b> aA + bB → cC + dD ke liye <b>rate = −(1/a)d[A]/dt = −(1/b)d[B]/dt = +(1/c)d[C]/dt = +(1/d)d[D]/dt</b>. Coefficients se divide karna mat bhoolo — numerical me yahi galti hoti hai!</li>\n</ul>\n<p class=\"small-note\">💡 Rate = \"speedometer\" — average = poore trip ki speed, instantaneous = abhi is second ki speed. Coefficient se divide karna yaad rakho (N₂ + 3H₂ → 2NH₃ me sabki rate alag dikhti, par stoichiometric rate ek hoti hai)!</p>"
   },
   {
    "h": "2️⃣ Rate Law, Order aur Molecularity ⭐⭐",
    "body": "<ul>\n<li><b>Rate law:</b> experiment se milta hai — <b>Rate = k·[A]ˣ·[B]ʸ</b>. x, y = A, B ke respect me order. <b>Overall order = x + y</b>. yeh coefficients se NAHI aata (experimental hota hai)!</li>\n<li><b>Rate constant (k):</b> jab [A]=[B]=1 M, to rate = k. k sirf <b>temperature</b> pe depend karta hai, concentration pe nahi. <b>k ki unit order se nikalti:</b> order 0 → mol L⁻¹ s⁻¹; order 1 → s⁻¹; order 2 → L mol⁻¹ s⁻¹.</li>\n<li><b>Order vs Molecularity ⭐:</b> <b>Order</b> = rate law me powers ka sum (experimental, fractional/0 ho sakta, <b>elementary step ke liye hi define</b> nahi hota complex me). <b>Molecularity</b> = elementary step me takrane wale molecules ki ginti (theoretical, hamesha whole number 1/2/3, 0 ya fractional kabhi nahi). Complex reaction ki molecularity = uske <b>slowest step</b> ki.</li>\n<li><b>Integrated example:</b> complex reaction ke liye order alag ho sakta molecularity se — isliye order experimental hai.</li>\n</ul>\n<p class=\"small-note\">💡 Order = \"experiment ka result\" (fractional bhi ho sakta), Molecularity = \"theory ka count\" (hamesha integer). Complex reaction ka rate = sabse SLOW step decide karta hai (jaise traffic me sabse slow gaadi)!</p>"
   },
   {
    "h": "3️⃣ Zero Order aur First Order — Integrated Equations ⭐⭐",
    "body": "<ul>\n<li><b>Zero order:</b> rate reactant concentration pe <b>depend nahi</b> karta. Rate = k. <b>Integrated: [R] = [R]₀ − kt</b>. Graph: [R] vs t → straight line, slope = −k. <b>t₁/₂ = [R]₀/2k</b> (half-life initial concentration pe DEPEND karti). Example: NH₃ decomposition on Pt, photochemical (H₂+Cl₂).</li>\n<li><b>First order ⭐⭐:</b> rate ∝ [R]. Rate = k[R]. <b>Integrated: k = (2.303/t)·log([R]₀/[R])</b> ya ln[R] = ln[R]₀ − kt. Graph: log[R]₀/[R] vs t → straight line through origin, slope = k/2.303. <b>t₁/₂ = 0.693/k</b> (initial concentration pe DEPEND NAHI karta — constant!).</li>\n<li><b>First order examples:</b> radioactive decay, N₂O₅ decomposition, H₂O₂ decomposition. Radioactive decay ka half-life hamesha constant hota (first order) — yahi exam me puchte hain.</li>\n<li><b>Pseudo first order:</b> do reactants me se ek bahut zyada excess me ho (jaise pani) to uski concentration ~constant maan lo — overall reaction first order jaisa behave karta. Example: ester hydrolysis, sucrose inversion.</li>\n</ul>\n<p class=\"small-note\">💡 First order = \"half-life fixed\" (0.693/k — jitna bhi shuru karo, aadha hone ka time same). Zero order = \"half-life badhti\" (concentration pe depend). Formulas rat lo: [R]=[R]₀−kt (zero), k=(2.303/t)log([R]₀/[R]) (first)!</p>"
   },
   {
    "h": "4️⃣ Temperature ka Effect aur Arrhenius Equation ⭐⭐",
    "body": "<ul>\n<li><b>Temperature badhao → rate badhao:</b> generally har 10°C rise pe rate ~<b>double</b> ho jata (temperature coefficient ≈ 2-3).</li>\n<li><b>Arrhenius equation ⭐⭐:</b> <b>k = A·e^(−Ea/RT)</b>. A = frequency/pre-exponential factor (collisions ki frequency), Ea = <b>activation energy</b> (minimum energy jo molecules ko chahiye reaction ke liye), R = gas constant, T = Kelvin.</li>\n<li><b>Log form ⭐:</b> log k = log A − (Ea/2.303RT). Do temperatures pe: <b>log(k₂/k₁) = (Ea/2.303R)·[(1/T₁) − (1/T₂)]</b>. Yahan se Ea nikalta — numerical favourite!</li>\n<li><b>Activation energy:</b> reactants → products jaane me jo <b>energy barrier</b> cross karna padta. Activated complex (transition state) peak pe hota. Ea zyada → reaction slow (thandi me aur slow). Catalyst Ea GHATA deta (alternate path) → rate badh jata.</li>\n</ul>\n<p class=\"small-note\">💡 Ea = \"deewar ki height\" — jitni oonchi deewar, utne kam molecules paar kar paate (slow reaction). Arrhenius k=A·e^(−Ea/RT) yaad rakho, log wala formula Ea ke numericals me har saal aata hai!</p>"
   },
   {
    "h": "5️⃣ Collision Theory aur Catalyst — Kyun Takraana Zaroori",
    "body": "<ul>\n<li><b>Collision theory:</b> reaction tabhi hoti jab molecules <b>takrate hain</b> — lekin har collision effective nahi. Do shartein: <b>(1) proper orientation</b> (sahi angle se takrana) aur <b>(2) energy ≥ activation energy (Ea)</b>.</li>\n<li><b>Effective collisions:</b> in dono sharton wali collisions hi reaction deti. <b>Rate = (collision frequency Z) × (fraction of molecules with E≥Ea, e^(−Ea/RT)) × (orientation factor P)</b>.</li>\n<li><b>Catalyst ⭐:</b> reaction ki speed badhata (ya ghatata) bina khud consume hue, aur <b>equilibrium ko shift nahi karta</b> — sirf equilibrium tak <b>jaldi</b> pahunchata. Alternate path deta with <b>lower activation energy</b>. Positive catalyst (speed up, jaise Fe in Haber), negative/inhibitor (slow down).</li>\n<li><b>Temperature ka role:</b> T badhane pe zyada molecules ko Ea se upar energy milti (Maxwell-Boltzmann curve shift) → effective collisions badhti → rate badhti.</li>\n</ul>\n<p class=\"small-note\">💡 Collision theory = \"basketball\" — ball (molecule) ko hoop (reaction) me daalne ke liye sahi angle (orientation) + kaafi force (Ea) dono chahiye. Catalyst = nichla basket (kam Ea) — asaan ho gaya!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ अभिक्रिया की दर",
    "body": "<ul>\n<li><b>दर = −Δ[अभिकारक]/Δt</b>। औसत दर (पूरे अंतराल) और तात्क्षणिक दर (−d[R]/dt, ढलान)। <b>स्टोइकियोमेट्री:</b> rate = −(1/a)d[A]/dt (गुणांक से भाग)।</li>\n</ul>\n<p class=\"small-note\">💡 गुणांक से भाग देना याद रखें।</p>"
   },
   {
    "h": "2️⃣ दर नियम, कोटि और अणुकता ⭐⭐",
    "body": "<ul>\n<li><b>Rate = k[A]ˣ[B]ʸ</b>; कोटि = x+y (प्रायोगिक, भिन्नात्मक संभव)। <b>अणुकता</b> = elementary चरण में टकराने वाले अणु (पूर्णांक 1/2/3)। जटिल अभिक्रिया की दर = सबसे <b>धीमा चरण</b>।</li>\n</ul>\n<p class=\"small-note\">💡 कोटि प्रायोगिक, अणुकता सैद्धांतिक।</p>"
   },
   {
    "h": "3️⃣ शून्य और प्रथम कोटि ⭐⭐",
    "body": "<ul>\n<li><b>शून्य:</b> [R]=[R]₀−kt; t₁/₂=[R]₀/2k। <b>प्रथम:</b> k=(2.303/t)log([R]₀/[R]); <b>t₁/₂=0.693/k</b> (स्थिर)। रेडियोधर्मी क्षय = प्रथम कोटि।</li>\n</ul>\n<p class=\"small-note\">💡 प्रथम कोटि का अर्ध-आयु स्थिर।</p>"
   },
   {
    "h": "4️⃣ Arrhenius समीकरण ⭐⭐",
    "body": "<ul>\n<li><b>k = A·e^(−Ea/RT)</b>। Ea = सक्रियण ऊर्जा। <b>log(k₂/k₁)=(Ea/2.303R)(1/T₁−1/T₂)</b>। उत्प्रेरक Ea घटाता है।</li>\n</ul>\n<p class=\"small-note\">💡 Ea = ऊर्जा अवरोध।</p>"
   },
   {
    "h": "5️⃣ संघट्ट सिद्धांत और उत्प्रेरक",
    "body": "<ul>\n<li>प्रभावी संघट्ट के लिए <b>उचित दिशा + E≥Ea</b> चाहिए। <b>उत्प्रेरक:</b> कम Ea वाला वैकल्पिक पथ देता है, साम्य को shift नहीं करता, केवल जल्दी पहुँचाता है।</li>\n</ul>\n<p class=\"small-note\">💡 उत्प्रेरक रास्ता आसान बनाता है।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Rate of Reaction",
    "body": "<ul>\n<li><b>Rate = −Δ[reactant]/Δt</b> (units mol L⁻¹ s⁻¹). Average rate over an interval; instantaneous rate = −d[R]/dt (slope). <b>Stoichiometry:</b> for aA+bB→cC+dD, rate = −(1/a)d[A]/dt = +(1/c)d[C]/dt — divide by coefficients.</li>\n</ul>\n<p class=\"small-note\">💡 Always divide by the stoichiometric coefficient.</p>"
   },
   {
    "h": "2️⃣ Rate Law, Order & Molecularity ⭐⭐",
    "body": "<ul>\n<li><b>Rate = k[A]ˣ[B]ʸ</b>; order = x+y (experimental, can be fractional/zero). k depends only on temperature; its unit comes from the order. <b>Molecularity</b> = molecules colliding in an elementary step (always 1/2/3). A complex reaction's rate is set by its <b>slowest step</b>.</li>\n</ul>\n<p class=\"small-note\">💡 Order is experimental; molecularity is theoretical.</p>"
   },
   {
    "h": "3️⃣ Zero & First Order ⭐⭐",
    "body": "<ul>\n<li><b>Zero order:</b> [R]=[R]₀−kt; t₁/₂=[R]₀/2k (depends on [R]₀). <b>First order:</b> k=(2.303/t)log([R]₀/[R]); <b>t₁/₂=0.693/k</b> (constant). Radioactive decay and N₂O₅ decomposition are first order. Pseudo first order: one reactant in large excess.</li>\n</ul>\n<p class=\"small-note\">💡 First-order half-life is constant.</p>"
   },
   {
    "h": "4️⃣ Arrhenius Equation ⭐⭐",
    "body": "<ul>\n<li><b>k = A·e^(−Ea/RT)</b>. Ea = activation energy, A = frequency factor. <b>log(k₂/k₁)=(Ea/2.303R)(1/T₁−1/T₂)</b>. A catalyst lowers Ea via an alternative path, increasing rate.</li>\n</ul>\n<p class=\"small-note\">💡 Ea is the energy barrier.</p>"
   },
   {
    "h": "5️⃣ Collision Theory & Catalyst",
    "body": "<ul>\n<li>A reaction needs an <b>effective collision</b>: proper orientation + energy ≥ Ea. A <b>catalyst</b> offers a lower-Ea path, speeds attainment of equilibrium, but does <b>not</b> shift equilibrium.</li>\n</ul>\n<p class=\"small-note\">💡 Catalyst lowers the barrier, not the destination.</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Rate",
    "items": [
     "Rate = −Δ[R]/Δt",
     "Average vs instantaneous",
     "Coefficient se divide (aA+bB→cC)"
    ]
   },
   {
    "h": "Order/Molecularity ⭐",
    "items": [
     "Rate = k[A]ˣ[B]ʸ; order=x+y",
     "Order experimental (fractional ok)",
     "Molecularity integer (1/2/3)",
     "Complex ka rate = slowest step"
    ]
   },
   {
    "h": "Zero Order",
    "items": [
     "[R]=[R]₀−kt",
     "t₁/₂ = [R]₀/2k",
     "Half-life ∝ [R]₀"
    ]
   },
   {
    "h": "First Order ⭐⭐",
    "items": [
     "k=(2.303/t)log([R]₀/[R])",
     "t₁/₂ = 0.693/k (constant)",
     "Radioactive decay = first order"
    ]
   },
   {
    "h": "Arrhenius ⭐⭐",
    "items": [
     "k = A·e^(−Ea/RT)",
     "log(k₂/k₁)=(Ea/2.303R)(1/T₁−1/T₂)",
     "Catalyst Ea ghatata"
    ]
   },
   {
    "h": "Collision",
    "items": [
     "Orientation + E≥Ea = effective",
     "Catalyst = lower Ea path",
     "Equilibrium shift nahi karta"
    ]
   }
  ],
  "hi": [
   {
    "h": "दर",
    "items": [
     "Rate=−Δ[R]/Δt",
     "गुणांक से भाग"
    ]
   },
   {
    "h": "कोटि",
    "items": [
     "कोटि=x+y (प्रायोगिक)",
     "अणुकता पूर्णांक",
     "धीमा चरण निर्णायक"
    ]
   },
   {
    "h": "प्रथम कोटि",
    "items": [
     "k=(2.303/t)log([R]₀/[R])",
     "t₁/₂=0.693/k"
    ]
   },
   {
    "h": "Arrhenius",
    "items": [
     "k=A·e^(−Ea/RT)",
     "उत्प्रेरक Ea घटाता"
    ]
   }
  ],
  "en": [
   {
    "h": "Rate",
    "items": [
     "Rate=−Δ[R]/Δt",
     "divide by coefficient"
    ]
   },
   {
    "h": "Order",
    "items": [
     "order=x+y (experimental)",
     "molecularity integer",
     "slowest step decides"
    ]
   },
   {
    "h": "First order",
    "items": [
     "k=(2.303/t)log([R]₀/[R])",
     "t₁/₂=0.693/k"
    ]
   },
   {
    "h": "Arrhenius",
    "items": [
     "k=A·e^(−Ea/RT)",
     "catalyst lowers Ea"
    ]
   }
  ]
 },
 "practice": [
  [
   "Rate of reaction ka expression aur unit?",
   "<b>Rate = −Δ[R]/Δt</b>; unit mol L⁻¹ s⁻¹. Stoichiometric coefficient se divide karna padta hai."
  ],
  [
   "Order aur molecularity me do differences.",
   "Order: <b>experimental</b>, fractional/zero ho sakta. Molecularity: <b>theoretical</b>, hamesha whole number (1/2/3)."
  ],
  [
   "First order reaction ki integrated rate equation aur half-life.",
   "<b>k=(2.303/t)·log([R]₀/[R])</b>; <b>t₁/₂ = 0.693/k</b> (initial concentration pe depend nahi karta)."
  ],
  [
   "Zero order reaction ki half-life.",
   "<b>t₁/₂ = [R]₀/2k</b> — initial concentration ke proportional."
  ],
  [
   "Radioactive decay kaunsi order ki hoti hai aur kyun?",
   "<b>First order</b> — iska half-life constant hota hai (initial amount pe nirbhar nahi)."
  ],
  [
   "Arrhenius equation likho aur har term batao.",
   "<b>k = A·e^(−Ea/RT)</b>; A = frequency factor, Ea = activation energy, R = gas constant, T = Kelvin."
  ],
  [
   "Do temperatures pe rate constant ka relation?",
   "<b>log(k₂/k₁) = (Ea/2.303R)·(1/T₁ − 1/T₂)</b> — yahan se Ea nikalta."
  ],
  [
   "Catalyst reaction ko kaise fast karta hai?",
   "<b>Activation energy kam</b> karke alternate path deta hai — zyada effective collisions. Equilibrium shift NAHI karta, sirf jaldi pahunchata."
  ],
  [
   "Effective collision ke liye kya zaroori?",
   "<b>Proper orientation</b> aur <b>energy ≥ activation energy</b> dono."
  ],
  [
   "Pseudo first order reaction kya hoti? Example.",
   "Do reactants me ek bahut excess me ho (jaise H₂O) to uski conc. ~constant — reaction first order jaisa behave karti. Example: <b>sucrose inversion / ester hydrolysis</b>."
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-12/chemistry/ch-4/",
  "title": "The d- and f-Block Elements"
 }
}

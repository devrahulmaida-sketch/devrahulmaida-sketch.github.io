# Class 11 Maths, Chapter 10 - Conic Sections
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 10,
 "title_en": "Conic Sections",
 "title_hi": "शंकु परिच्छेद",
 "tagline": "Circle, parabola, ellipse, hyperbola — cone ki chaar kahaniyan",
 "jee": "HIGH",
 "meta_desc": "Class 11 Maths Chapter 10: Conic Sections — long + short notes in Hindi, English, Hinglish. Circle, parabola, ellipse, hyperbola equations, foci, eccentricity, latus rectum.",
 "video": None,
 "card_tag": "Circle, parabola, ellipse, hyperbola — cone ki chaar kahaniyan",
 "card_topics": [
  "⭕ Circle equations",
  "🔦 Parabola: focus + directrix",
  "🪐 Ellipse: e < 1",
  "♾️ Hyperbola: e > 1"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Conic Sections — Cone Kaatne Se Bane Curves",
    "body": "<p>Ek double cone ko plane se alag-alag angles pe kaato — chaar famous curves milte hain. Isliye inhe <b>conic sections</b> kehte hain. Ye chapter coordinate geometry ka crown hai: circle, parabola, ellipse, hyperbola — sab ke equations, foci, eccentricity. JEE me guaranteed questions.</p>\n<ul>\n<li><b>Circle:</b> plane cone ke axis ke perpendicular — bilkul horizontal cut.</li>\n<li><b>Parabola:</b> plane cone ki slant side ke parallel.</li>\n<li><b>Ellipse:</b> plane thoda tilted — closed oval curve.</li>\n<li><b>Hyperbola:</b> plane dono cones ko kaate — do open branches.</li>\n<li><b>Degenerate cases:</b> vertex se guzarne pe point, line, ya pair of lines ban jaata hai.</li>\n</ul>\n<p class=\"small-note\">💡 Real life: planets ke orbits ellipses hain, satellite dishes parabolas, cooling towers hyperbolas, aur headlights parabolic mirrors!</p>"
   },
   {
    "h": "2️⃣ Circle — Sabse Simple Conic ⭐",
    "body": "<ul>\n<li><b>Definition:</b> ek fixed point (centre) se fixed distance (radius) pe sab points ka set.</li>\n<li><b>Standard equation ⭐:</b> (x − h)² + (y − k)² = r² — centre (h, k), radius r.</li>\n<li><b>Centre origin pe:</b> x² + y² = r².</li>\n<li><b>General form ⭐:</b> x² + y² + 2gx + 2fy + c = 0 — centre (−g, −f), radius = √(g² + f² − c).</li>\n<li><b>Diameter form:</b> (x − x₁)(x − x₂) + (y − y₁)(y − y₂) = 0 — (x₁,y₁) aur (x₂,y₂) diameter ke ends.</li>\n<li><b>Condition check:</b> g² + f² − c &gt; 0 hona chahiye real circle ke liye.</li>\n</ul>\n<p class=\"small-note\">💡 General form me centre nikalna: x aur y ke coefficients aadhe karke sign palto — 2g → −g, 2f → −f!</p>"
   },
   {
    "h": "3️⃣ Parabola — Focus-Directrix ka Balance ⭐",
    "body": "<ul>\n<li><b>Definition ⭐:</b> ek fixed point (<b>focus</b>) aur ek fixed line (<b>directrix</b>) se BARABAR distance wale points ka set.</li>\n<li><b>Standard forms (4):</b> y² = 4ax (right), y² = −4ax (left), x² = 4ay (up), x² = −4ay (down).</li>\n<li><b>y² = 4ax ke facts ⭐:</b> vertex (0,0), focus (a, 0), directrix x = −a, axis = x-axis.</li>\n<li><b>Latus rectum ⭐:</b> focus se guzarne wala chord perpendicular to axis — length = <b>4a</b>. Ends: (a, 2a) aur (a, −2a).</li>\n<li><b>Eccentricity:</b> parabola ke liye hamesha e = 1.</li>\n<li><b>Focal distance:</b> parabola pe koi point (x, y) ka focus se distance = x + a.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: focus torch ka bulb hai, parabola uska reflector — saari rays parallel nikalti hain. Isliye headlights parabolic!</p>"
   },
   {
    "h": "4️⃣ Ellipse — Stretched Circle ⭐",
    "body": "<ul>\n<li><b>Definition ⭐:</b> do fixed points (<b>foci</b>) se distances ka SUM constant (= 2a) — ellipse.</li>\n<li><b>Standard equation ⭐:</b> x²/a² + y²/b² = 1 (a &gt; b) — major axis x pe: length 2a, minor axis: 2b.</li>\n<li><b>Foci:</b> (±c, 0), jahan <b>c² = a² − b²</b> ⭐ (ellipse me c chhota hota hai a se).</li>\n<li><b>Eccentricity ⭐:</b> e = c/a &lt; 1. e jitna chhota, ellipse utna round; e = 0 pe circle!</li>\n<li><b>Latus rectum:</b> 2b²/a.</li>\n<li><b>Vertical ellipse:</b> x²/b² + y²/a² = 1 — major axis y pe, foci (0, ±c).</li>\n<li><b>String trick:</b> do pins (foci) pe dhaaga bandho, pencil se khincho — ellipse ban jaata hai!</li>\n</ul>\n<p class=\"small-note\">🎯 Kepler's first law: planets Sun ke around ELLIPSE me chalte hain, Sun ek focus pe. Isliye ellipse samajhna zaroori!</p>"
   },
   {
    "h": "5️⃣ Hyperbola — Do Branches Wala Curve ⭐",
    "body": "<ul>\n<li><b>Definition ⭐:</b> do foci se distances ka DIFFERENCE constant (= 2a) — hyperbola.</li>\n<li><b>Standard equation ⭐:</b> x²/a² − y²/b² = 1 — transverse axis x pe (length 2a), conjugate axis (2b).</li>\n<li><b>Foci ⭐:</b> (±c, 0), jahan <b>c² = a² + b²</b> — PLUS sign! (ellipse ka minus se confuse mat hona!)</li>\n<li><b>Eccentricity:</b> e = c/a &gt; 1 ⭐ (hyperbola me e hamesha 1 se bada).</li>\n<li><b>Latus rectum:</b> 2b²/a (ellipse jaisa hi formula).</li>\n<li><b>Asymptotes:</b> y = ±(b/a)x — lines jinke kareeb branches jaati hain par kabhi touch nahi karti.</li>\n<li><b>Rectangular hyperbola:</b> a = b → x² − y² = a² ya xy = c² — asymptotes perpendicular.</li>\n</ul>\n<p class=\"small-note\">💡 Memory trick: ellipse SUBTRACT (c² = a² − b², e &lt; 1, \"kam\"), hyperbola ADD (c² = a² + b², e &gt; 1, \"zyada\")!</p>"
   },
   {
    "h": "6️⃣ Exam Patterns — Conics ka Game Plan",
    "body": "<ul>\n<li><b>Equation nikalo:</b> given focus/vertex/directrix/eccentricity conditions se.</li>\n<li><b>Elements find karo ⭐:</b> equation dekhke focus, directrix, axis, latus rectum, eccentricity — sabse common question.</li>\n<li><b>Identify the conic:</b> general second-degree equation dekhke — x² aur y² ke coefficients dekho (same sign+coeff → circle; ek square → parabola; +/+ different → ellipse; +/− → hyperbola).</li>\n<li><b>Circle through 3 points:</b> general form me substitute karke g, f, c solve karo.</li>\n<li><b>Latus rectum se equation:</b> 4a ya 2b²/a se a, b back-calculate.</li>\n</ul>\n<p class=\"small-note\">💡 Pehle standard form yaad karo (har conic ka ek table), phir \"equation → elements\" aur \"elements → equation\" dono direction practice karo!</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ शंकु परिच्छेद — शंकु काटने से बने वक्र",
    "body": "<p>दोहरे शंकु को समतल से अलग-अलग कोणों पर काटो — चार प्रसिद्ध वक्र मिलते हैं: वृत्त, परवलय, दीर्घवृत्त, अतिपरवलय। JEE में निश्चित प्रश्न।</p>\n<ul>\n<li><b>वृत्त (Circle):</b> समतल शंकु के अक्ष के लंबवत काट।</li>\n<li><b>परवलय (Parabola):</b> समतल शंकु की तिर्यक भुजा के समांतर।</li>\n<li><b>दीर्घवृत्त (Ellipse):</b> समतल थोड़ा तिरछा — बंद अंडाकार वक्र।</li>\n<li><b>अतिपरवलय (Hyperbola):</b> समतल दोनों शंकुओं को काटे — दो खुली शाखाएँ।</li>\n<li><b>अपभ्रष्ट (degenerate):</b> शीर्ष से गुजरने पर बिंदु, रेखा या रेखा-युग्म।</li>\n</ul>\n<p class=\"small-note\">💡 वास्तविक जीवन: ग्रहों की कक्षाएँ दीर्घवृत्त, सैटेलाइट डिश परवलय, कूलिंग टावर अतिपरवलय!</p>"
   },
   {
    "h": "2️⃣ वृत्त — सबसे सरल शंकु परिच्छेद ⭐",
    "body": "<ul>\n<li><b>परिभाषा:</b> एक निश्चित बिंदु (केंद्र) से निश्चित दूरी (त्रिज्या) पर सभी बिंदुओं का समुच्चय।</li>\n<li><b>मानक समीकरण ⭐:</b> (x − h)² + (y − k)² = r² — केंद्र (h, k), त्रिज्या r।</li>\n<li><b>केंद्र मूलबिंदु पर:</b> x² + y² = r²।</li>\n<li><b>व्यापक रूप ⭐:</b> x² + y² + 2gx + 2fy + c = 0 — केंद्र (−g, −f), त्रिज्या = √(g² + f² − c)।</li>\n<li><b>व्यास रूप:</b> (x − x₁)(x − x₂) + (y − y₁)(y − y₂) = 0।</li>\n<li><b>शर्त:</b> g² + f² − c &gt; 0 वास्तविक वृत्त के लिए।</li>\n</ul>\n<p class=\"small-note\">💡 केंद्र निकालना: x और y के गुणांक आधे करके चिह्न बदलो!</p>"
   },
   {
    "h": "3️⃣ परवलय — नाभि-नियता संतुलन ⭐",
    "body": "<ul>\n<li><b>परिभाषा ⭐:</b> एक निश्चित बिंदु (<b>नाभि/focus</b>) और एक निश्चित रेखा (<b>नियता/directrix</b>) से समान दूरी वाले बिंदुओं का समुच्चय।</li>\n<li><b>मानक रूप (4):</b> y² = 4ax (दाएँ), y² = −4ax (बाएँ), x² = 4ay (ऊपर), x² = −4ay (नीचे)।</li>\n<li><b>y² = 4ax के तथ्य ⭐:</b> शीर्ष (0,0), नाभि (a, 0), नियता x = −a, अक्ष = x-अक्ष।</li>\n<li><b>नाभिलंब जीवा (Latus rectum) ⭐:</b> नाभि से गुजरने वाली अक्ष-लंबवत जीवा — लंबाई <b>4a</b>।</li>\n<li><b>उत्केंद्रता:</b> परवलय के लिए e = 1।</li>\n</ul>\n<p class=\"small-note\">💡 नाभि बल्ब है, परवलय परावर्तक — सभी किरणें समांतर निकलती हैं। इसलिए हेडलाइट्स परवलयिक!</p>"
   },
   {
    "h": "4️⃣ दीर्घवृत्त — खिंचा हुआ वृत्त ⭐",
    "body": "<ul>\n<li><b>परिभाषा ⭐:</b> दो नाभियों से दूरियों का योग अचर (= 2a)।</li>\n<li><b>मानक समीकरण ⭐:</b> x²/a² + y²/b² = 1 (a &gt; b) — दीर्घ अक्ष 2a, लघु अक्ष 2b।</li>\n<li><b>नाभियाँ:</b> (±c, 0), जहाँ <b>c² = a² − b²</b> ⭐</li>\n<li><b>उत्केंद्रता ⭐:</b> e = c/a &lt; 1। e छोटा → अधिक गोल; e = 0 पर वृत्त!</li>\n<li><b>नाभिलंब जीवा:</b> 2b²/a।</li>\n<li><b>ऊर्ध्व दीर्घवृत्त:</b> x²/b² + y²/a² = 1 — दीर्घ अक्ष y पर।</li>\n</ul>\n<p class=\"small-note\">🎯 केपलर का नियम: ग्रह सूर्य के चारों ओर दीर्घवृत्त में चलते हैं, सूर्य एक नाभि पर!</p>"
   },
   {
    "h": "5️⃣ अतिपरवलय — दो शाखाओं वाला वक्र ⭐",
    "body": "<ul>\n<li><b>परिभाषा ⭐:</b> दो नाभियों से दूरियों का अंतर अचर (= 2a)।</li>\n<li><b>मानक समीकरण ⭐:</b> x²/a² − y²/b² = 1 — अनुप्रस्थ अक्ष 2a, संयुग्मी अक्ष 2b।</li>\n<li><b>नाभियाँ ⭐:</b> (±c, 0), जहाँ <b>c² = a² + b²</b> — PLUS चिह्न! (दीर्घवृत्त के minus से भ्रम नहीं!)</li>\n<li><b>उत्केंद्रता:</b> e = c/a &gt; 1 ⭐</li>\n<li><b>नाभिलंब जीवा:</b> 2b²/a।</li>\n<li><b>अनंतस्पर्शी (Asymptotes):</b> y = ±(b/a)x — शाखाएँ इनके निकट जाती हैं पर स्पर्श नहीं करतीं।</li>\n<li><b>समकोणिक अतिपरवलय:</b> a = b → x² − y² = a² या xy = c²।</li>\n</ul>\n<p class=\"small-note\">💡 याद रखो: दीर्घवृत्त घटाव (e &lt; 1), अतिपरवलय जोड़ (e &gt; 1)!</p>"
   },
   {
    "h": "6️⃣ परीक्षा के पैटर्न",
    "body": "<ul>\n<li><b>समीकरण निकालो:</b> नाभि/शीर्ष/नियता/उत्केंद्रता की शर्तों से।</li>\n<li><b>अवयव ज्ञात करो ⭐:</b> समीकरण से नाभि, नियता, अक्ष, नाभिलंब जीवा, उत्केंद्रता — सबसे आम प्रश्न।</li>\n<li><b>वक्र पहचानो:</b> x², y² के गुणांक देखो (समान → वृत्त; एक वर्ग → परवलय; +/+ भिन्न → दीर्घवृत्त; +/− → अतिपरवलय)।</li>\n<li><b>3 बिंदुओं से वृत्त:</b> व्यापक रूप में रखकर g, f, c हल करो।</li>\n</ul>\n<p class=\"small-note\">💡 पहले मानक रूपों की तालिका याद करो, फिर दोनों दिशाओं में अभ्यास करो!</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Conic Sections — Curves from Slicing a Cone",
    "body": "<p>Slice a double cone with a plane at different angles and you get four famous curves — that's why they're called <b>conic sections</b>. This chapter is the crown of coordinate geometry: circle, parabola, ellipse, hyperbola, with their equations, foci, and eccentricity. Guaranteed JEE questions.</p>\n<ul>\n<li><b>Circle:</b> plane perpendicular to the cone's axis — a straight horizontal cut.</li>\n<li><b>Parabola:</b> plane parallel to the cone's slant side.</li>\n<li><b>Ellipse:</b> plane slightly tilted — a closed oval curve.</li>\n<li><b>Hyperbola:</b> plane cuts both cones — two open branches.</li>\n<li><b>Degenerate cases:</b> cutting through the vertex gives a point, a line, or a pair of lines.</li>\n</ul>\n<p class=\"small-note\">💡 Real life: planetary orbits are ellipses, satellite dishes are parabolas, cooling towers are hyperbolas, and headlights use parabolic mirrors!</p>"
   },
   {
    "h": "2️⃣ Circle — the Simplest Conic ⭐",
    "body": "<ul>\n<li><b>Definition:</b> the set of all points at a fixed distance (radius) from a fixed point (centre).</li>\n<li><b>Standard equation ⭐:</b> (x − h)² + (y − k)² = r² — centre (h, k), radius r.</li>\n<li><b>Centre at origin:</b> x² + y² = r².</li>\n<li><b>General form ⭐:</b> x² + y² + 2gx + 2fy + c = 0 — centre (−g, −f), radius = √(g² + f² − c).</li>\n<li><b>Diameter form:</b> (x − x₁)(x − x₂) + (y − y₁)(y − y₂) = 0 — where (x₁,y₁) and (x₂,y₂) are the diameter's ends.</li>\n<li><b>Condition:</b> g² + f² − c &gt; 0 for a real circle.</li>\n</ul>\n<p class=\"small-note\">💡 Centre from general form: halve the x and y coefficients and flip their signs — 2g → −g, 2f → −f!</p>"
   },
   {
    "h": "3️⃣ Parabola — the Focus-Directrix Balance ⭐",
    "body": "<ul>\n<li><b>Definition ⭐:</b> the set of points EQUIDISTANT from a fixed point (the <b>focus</b>) and a fixed line (the <b>directrix</b>).</li>\n<li><b>Standard forms (4):</b> y² = 4ax (opens right), y² = −4ax (left), x² = 4ay (up), x² = −4ay (down).</li>\n<li><b>Facts about y² = 4ax ⭐:</b> vertex (0,0), focus (a, 0), directrix x = −a, axis = x-axis.</li>\n<li><b>Latus rectum ⭐:</b> the chord through the focus perpendicular to the axis — length <b>4a</b>. Ends: (a, 2a) and (a, −2a).</li>\n<li><b>Eccentricity:</b> always e = 1 for a parabola.</li>\n<li><b>Focal distance:</b> the distance from a point (x, y) on the parabola to the focus is x + a.</li>\n</ul>\n<p class=\"small-note\">💡 Feel it: the focus is the bulb, the parabola its reflector — all rays exit parallel. That's why headlights are parabolic!</p>"
   },
   {
    "h": "4️⃣ Ellipse — the Stretched Circle ⭐",
    "body": "<ul>\n<li><b>Definition ⭐:</b> the SUM of distances from two fixed points (the <b>foci</b>) is constant (= 2a).</li>\n<li><b>Standard equation ⭐:</b> x²/a² + y²/b² = 1 (a &gt; b) — major axis 2a, minor axis 2b.</li>\n<li><b>Foci:</b> (±c, 0), where <b>c² = a² − b²</b> ⭐ (c is smaller than a in an ellipse).</li>\n<li><b>Eccentricity ⭐:</b> e = c/a &lt; 1. Smaller e means rounder; e = 0 gives a circle!</li>\n<li><b>Latus rectum:</b> 2b²/a.</li>\n<li><b>Vertical ellipse:</b> x²/b² + y²/a² = 1 — major axis on y, foci (0, ±c).</li>\n<li><b>String trick:</b> tie a loop of string around two pins (foci) and pull it taut with a pencil — you draw an ellipse!</li>\n</ul>\n<p class=\"small-note\">🎯 Kepler's first law: planets move in ELLIPSES with the Sun at one focus. That's why the ellipse matters!</p>"
   },
   {
    "h": "5️⃣ Hyperbola — the Two-Branch Curve ⭐",
    "body": "<ul>\n<li><b>Definition ⭐:</b> the DIFFERENCE of distances from two foci is constant (= 2a).</li>\n<li><b>Standard equation ⭐:</b> x²/a² − y²/b² = 1 — transverse axis 2a, conjugate axis 2b.</li>\n<li><b>Foci ⭐:</b> (±c, 0), where <b>c² = a² + b²</b> — PLUS sign! (Don't confuse with the ellipse's minus!)</li>\n<li><b>Eccentricity:</b> e = c/a &gt; 1 ⭐ (always greater than 1 for a hyperbola).</li>\n<li><b>Latus rectum:</b> 2b²/a (same formula as the ellipse).</li>\n<li><b>Asymptotes:</b> y = ±(b/a)x — lines the branches approach but never touch.</li>\n<li><b>Rectangular hyperbola:</b> a = b → x² − y² = a² or xy = c² — perpendicular asymptotes.</li>\n</ul>\n<p class=\"small-note\">💡 Memory trick: ellipse SUBTRACTS (c² = a² − b², e &lt; 1), hyperbola ADDS (c² = a² + b², e &gt; 1)!</p>"
   },
   {
    "h": "6️⃣ Exam Patterns — the Conics Game Plan",
    "body": "<ul>\n<li><b>Find the equation:</b> from given focus/vertex/directrix/eccentricity conditions.</li>\n<li><b>Find the elements ⭐:</b> given the equation, extract focus, directrix, axis, latus rectum, eccentricity — the most common question.</li>\n<li><b>Identify the conic:</b> look at the x² and y² coefficients (same sign and value → circle; only one square → parabola; +/+ different → ellipse; +/− → hyperbola).</li>\n<li><b>Circle through 3 points:</b> substitute into the general form and solve for g, f, c.</li>\n<li><b>Latus rectum to equation:</b> back-calculate a and b from 4a or 2b²/a.</li>\n</ul>\n<p class=\"small-note\">💡 First memorise the standard-form table, then practise both directions: equation → elements and elements → equation!</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Circle ⭐",
    "items": [
     "(x−h)²+(y−k)² = r²",
     "x²+y²+2gx+2fy+c = 0",
     "Centre (−g,−f), r = √(g²+f²−c)"
    ]
   },
   {
    "h": "Parabola ⭐",
    "items": [
     "y² = 4ax: focus (a,0), directrix x=−a",
     "e = 1",
     "Latus rectum = 4a"
    ]
   },
   {
    "h": "Ellipse ⭐",
    "items": [
     "x²/a² + y²/b² = 1",
     "c² = a² − b², e = c/a < 1",
     "Foci (±c, 0), LR = 2b²/a"
    ]
   },
   {
    "h": "Hyperbola ⭐",
    "items": [
     "x²/a² − y²/b² = 1",
     "c² = a² + b², e = c/a > 1",
     "Asymptotes y = ±(b/a)x"
    ]
   },
   {
    "h": "Identify",
    "items": [
     "x²,y² same → circle",
     "Ek square → parabola",
     "+/+ diff → ellipse, +/− → hyperbola"
    ]
   }
  ],
  "hi": [
   {
    "h": "वृत्त ⭐",
    "items": [
     "(x−h)²+(y−k)² = r²",
     "x²+y²+2gx+2fy+c = 0",
     "केंद्र (−g,−f), r = √(g²+f²−c)"
    ]
   },
   {
    "h": "परवलय ⭐",
    "items": [
     "y² = 4ax: नाभि (a,0), नियता x=−a",
     "e = 1",
     "नाभिलंब जीवा = 4a"
    ]
   },
   {
    "h": "दीर्घवृत्त ⭐",
    "items": [
     "x²/a² + y²/b² = 1",
     "c² = a² − b², e < 1",
     "नाभिलंब जीवा = 2b²/a"
    ]
   },
   {
    "h": "अतिपरवलय ⭐",
    "items": [
     "x²/a² − y²/b² = 1",
     "c² = a² + b², e > 1",
     "अनंतस्पर्शी y = ±(b/a)x"
    ]
   },
   {
    "h": "पहचान",
    "items": [
     "समान गुणांक → वृत्त",
     "एक वर्ग → परवलय",
     "+/+ → दीर्घवृत्त, +/− → अतिपरवलय"
    ]
   }
  ],
  "en": [
   {
    "h": "Circle ⭐",
    "items": [
     "(x−h)²+(y−k)² = r²",
     "x²+y²+2gx+2fy+c = 0",
     "Centre (−g,−f), r = √(g²+f²−c)"
    ]
   },
   {
    "h": "Parabola ⭐",
    "items": [
     "y² = 4ax: focus (a,0), directrix x=−a",
     "e = 1",
     "Latus rectum = 4a"
    ]
   },
   {
    "h": "Ellipse ⭐",
    "items": [
     "x²/a² + y²/b² = 1",
     "c² = a² − b², e = c/a < 1",
     "Foci (±c, 0), LR = 2b²/a"
    ]
   },
   {
    "h": "Hyperbola ⭐",
    "items": [
     "x²/a² − y²/b² = 1",
     "c² = a² + b², e = c/a > 1",
     "Asymptotes y = ±(b/a)x"
    ]
   },
   {
    "h": "Identify",
    "items": [
     "Same coeffs → circle",
     "One square → parabola",
     "+/+ → ellipse, +/− → hyperbola"
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
  "href": "/class-11/maths/ch-11/",
  "title": "Introduction to 3D Geometry"
 }
}

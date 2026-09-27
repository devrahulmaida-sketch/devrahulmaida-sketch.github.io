# Class 11 Physics, Chapter 2 - Motion in a Straight Line
# Reconstructed from built HTML by tools/scrape_subject.py
CH = {
 "num": 2,
 "title_en": "Motion in a Straight Line",
 "title_hi": "सरल रेखा में गति",
 "tagline": "1D motion — speed, velocity, acceleration, graphs aur free fall ka poora khel",
 "jee": "HIGH",
 "meta_desc": "Class 11 Physics Chapter 2: Motion in a Straight Line — long + short notes in Hindi, English, Hinglish. Distance, displacement, velocity, acceleration, equations of motion, graphs, free fall, relative velocity.",
 "video": {
  "youtube": "Et6bBspbkkU",
  "dur": "1 min 4 sec"
 },
 "card_tag": "1D motion — speed, velocity, acceleration, graphs aur free fall ka poora khel",
 "card_topics": [
  "📏 Distance vs displacement",
  "📈 x-t, v-t graphs",
  "🚗 Equations of motion",
  "🍎 Free fall"
 ],
 "long": {
  "hinglish": [
   {
    "h": "1️⃣ Motion Ka Description — Position, Distance, Displacement",
    "body": "<p>Straight line (1D) motion describe karne ke liye pehle <b>frame of reference</b> chahiye — ek origin aur direction. Position sirf ek number hai (+ ya −), jo batata hai object origin se kitni door hai.</p>\n<ul>\n<li><b>Distance:</b> total path length — scalar, hamesha positive. Delhi se Jaipur aur wapas: distance = 2 × 280 = 560 km.</li>\n<li><b>Displacement:</b> final − initial position — vector (1D me sign hi direction hai). Wapas aa gaye? Displacement = 0!</li>\n<li><b>Average speed</b> = total distance / total time • <b>Average velocity</b> = displacement / time — dono alag ho sakte hain (round trip me avg velocity = 0, avg speed ≠ 0).</li>\n<li><b>Instantaneous velocity:</b> v = dx/dt — x-t graph ka slope. <b>Instantaneous speed</b> = velocity ka magnitude.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: distance odometer hai (kabhi kam nahi hota), displacement seedha arrow initial se final — GPS ka \"aap yahan se wahan\" wala arrow.</p>"
   },
   {
    "h": "2️⃣ Acceleration — Velocity Ki Change Rate",
    "body": "<p><b>Average acceleration</b> = Δv/Δt • <b>instantaneous</b> a = dv/dt. Unit: m/s². Acceleration velocity ke direction me ho ya opposite — dono cases alag hain:</p>\n<ul>\n<li><b>Speed up:</b> a aur v same sign (dono + ya dono −).</li>\n<li><b>Retardation (deceleration):</b> a aur v opposite signs — speed ghatti hai.</li>\n<li>Velocity zero ho sakti hai jab acceleration zero na ho — upar phenki ball highest point pe: v = 0, lekin g neeche abhi bhi lag raha hai! ⭐ (exam trap)</li>\n</ul>\n<p class=\"small-note\">🎯 JEE trap: \"acceleration = 0 ka matlab rest nahi\" — constant velocity pe bhi a = 0 hota hai. Aur \"v = 0 ka matlab a = 0 nahi\" (ball at top).</p>"
   },
   {
    "h": "3️⃣ Equations of Motion — Constant Acceleration Ke 3 Mantra ⭐",
    "body": "<p>Jab acceleration <b>constant</b> ho (aur motion straight line me), teen equations se sab solve hota hai. u = initial velocity, v = final, a = acceleration, t = time, s = displacement:</p>\n<table class=\"tbl\">\n<tr><th>Equation</th><th>Kya missing hai</th><th>Kab use karo</th></tr>\n<tr><td>v = u + at</td><td>s</td><td>velocity-time relation</td></tr>\n<tr><td>s = ut + ½at²</td><td>v</td><td>displacement chahiye</td></tr>\n<tr><td>v² = u² + 2as</td><td>t</td><td>time na diya ho</td></tr>\n</table>\n<ul>\n<li>Har quantity <b>signed</b> hai — direction choose karke +/− consistent rakho (usually upar = +, neeche = −, ya motion direction = +).</li>\n<li><b>n-th second ka distance ⭐:</b> s<sub>n</sub> = u + a(n − ½) = u + (a/2)(2n − 1). Rest se start: s<sub>n</sub> ∝ (2n−1) — odd numbers ka ratio 1:3:5:7!</li>\n<li>Derivation simple: v-t graph ke neeche ka area = displacement.</li>\n</ul>\n<p class=\"small-note\">💡 Feel: teen equations teen locks hain — question me jo 3 cheezein di hain, wohi lock kaunsa khulna hai bata deti hain.</p>"
   },
   {
    "h": "4️⃣ Graphs — x-t, v-t, a-t Ka Khel ⭐",
    "body": "<p>Graphs JEE ka favourite — slope aur area dono meaningful hain:</p>\n<table class=\"tbl\">\n<tr><th>Graph</th><th>Slope batata hai</th><th>Area under curve</th></tr>\n<tr><td>x-t (position-time)</td><td>velocity</td><td>—</td></tr>\n<tr><td>v-t (velocity-time)</td><td>acceleration</td><td>displacement</td></tr>\n<tr><td>a-t</td><td>—</td><td>velocity change</td></tr>\n</table>\n<ul>\n<li><b>x-t graph:</b> straight line = constant velocity; curve (parabola) = acceleration; horizontal = rest. Steeper slope = faster.</li>\n<li><b>v-t graph:</b> horizontal line = uniform velocity (a = 0); sloping straight = constant acceleration; neeche ka area (+/− signs ke saath) = displacement, bina signs ke = distance.</li>\n<li>v-t graph time axis CROSS kare = direction change hua — wahan velocity zero!</li>\n</ul>\n<p class=\"small-note\">🎯 Shortcut: \"slope next quantity, area previous quantity\" — x → v → a chain me.</p>"
   },
   {
    "h": "5️⃣ Free Fall aur Relative Velocity",
    "body": "<p><b>Free fall:</b> sirf gravity ka effect, a = g = 9.8 m/s² neeche (sign convention ke hisaab se −g). Equations of motion me a = ±g rakh do — bas!</p>\n<ul>\n<li><b>Upar phenkna:</b> highest point pe v = 0 (lekin g neeche); time of flight = 2u/g; max height = u²/2g; wapas same point pe speed = u (neeche direction me).</li>\n<li><b>Drop karna:</b> u = 0, h = ½gt² — t = √(2h/g).</li>\n<li><b>Relative velocity (1D) ⭐:</b> v<sub>AB</sub> = v<sub>A</sub> − v<sub>B</sub>. Same direction me overtake slow, opposite direction me relative speed = dono ka sum (trains crossing!).</li>\n</ul>\n<p class=\"small-note\">💡 Feel: lift me ball phenko — ball ko sirf g yaad hai, lift ki motion nahi. Relative velocity = \"uski nazar se main kitna tez hoon\".</p>"
   }
  ],
  "hi": [
   {
    "h": "1️⃣ गति का वर्णन — स्थिति, दूरी, विस्थापन",
    "body": "<p>एक-विमीय (सरल रेखीय) गति का वर्णन करने के लिए <b>निर्देश तंत्र (frame of reference)</b> चाहिए — एक मूल बिंदु और दिशा। स्थिति एक चिह्नयुक्त संख्या है (+ या −)।</p>\n<ul>\n<li><b>दूरी:</b> कुल पथ की लंबाई — अदिश राशि, सदैव धनात्मक।</li>\n<li><b>विस्थापन:</b> अंतिम − प्रारंभिक स्थिति — सदिश राशि (1D में चिह्न ही दिशा है)। प्रारंभिक बिंदु पर वापस आने पर विस्थापन = 0!</li>\n<li><b>औसत चाल</b> = कुल दूरी / कुल समय • <b>औसत वेग</b> = विस्थापन / समय — दोनों भिन्न हो सकते हैं।</li>\n<li><b>तात्क्षणिक वेग:</b> v = dx/dt — x-t ग्राफ का ढलान।</li>\n</ul>\n<p class=\"small-note\">💡 ध्यान रखें: दूरी कभी घटती नहीं, जबकि विस्थापन शून्य भी हो सकता है।</p>"
   },
   {
    "h": "2️⃣ त्वरण — वेग में परिवर्तन की दर",
    "body": "<p><b>औसत त्वरण</b> = Δv/Δt • <b>तात्क्षणिक त्वरण</b> a = dv/dt। मात्रक: m/s²।</p>\n<ul>\n<li><b>चाल बढ़ना:</b> a और v समान चिह्न के हों।</li>\n<li><b>मंदन (retardation):</b> a और v विपरीत चिह्न के हों — चाल घटती है।</li>\n<li>वेग शून्य हो सकता है जब त्वरण शून्य न हो — ऊपर फेंकी गई गेंद उच्चतम बिंदु पर: v = 0, पर g नीचे लगता रहता है! ⭐</li>\n</ul>\n<p class=\"small-note\">🎯 परीक्षा त्रुटि: \"त्वरण = 0 का अर्थ विराम नहीं\" — समान वेग पर भी a = 0 होता है।</p>"
   },
   {
    "h": "3️⃣ गति के समीकरण — नियत त्वरण के तीन सूत्र ⭐",
    "body": "<p>जब त्वरण <b>नियत</b> हो (गति सरल रेखा में), तीन समीकरणों से सभी प्रश्न हल होते हैं। u = प्रारंभिक वेग, v = अंतिम वेग, a = त्वरण, t = समय, s = विस्थापन:</p>\n<table class=\"tbl\">\n<tr><th>समीकरण</th><th>कौन-सी राशि अनुपस्थित</th><th>कब प्रयोग करें</th></tr>\n<tr><td>v = u + at</td><td>s</td><td>वेग-समय संबंध</td></tr>\n<tr><td>s = ut + ½at²</td><td>v</td><td>विस्थापन चाहिए</td></tr>\n<tr><td>v² = u² + 2as</td><td>t</td><td>समय न दिया हो</td></tr>\n</table>\n<ul>\n<li>प्रत्येक राशि <b>चिह्नयुक्त</b> है — दिशा चुनकर +/− सुसंगत रखें।</li>\n<li><b>n वें सेकंड में दूरी ⭐:</b> s<sub>n</sub> = u + (a/2)(2n − 1)। विराम से: s<sub>n</sub> ∝ (2n−1) — 1:3:5:7 का अनुपात!</li>\n<li>व्युत्पत्ति: v-t ग्राफ के नीचे का क्षेत्रफल = विस्थापन।</li>\n</ul>\n<p class=\"small-note\">💡 प्रश्न में दी गई तीन राशियाँ बताती हैं कि कौन-सा सूत्र लगेगा।</p>"
   },
   {
    "h": "4️⃣ ग्राफ — x-t, v-t, a-t ⭐",
    "body": "<p>ग्राफ परीक्षा का प्रिय टॉपिक — ढलान (slope) और क्षेत्रफल (area) दोनों सार्थक हैं:</p>\n<table class=\"tbl\">\n<tr><th>ग्राफ</th><th>ढलान</th><th>वक्र के नीचे क्षेत्रफल</th></tr>\n<tr><td>x-t (स्थिति-समय)</td><td>वेग</td><td>—</td></tr>\n<tr><td>v-t (वेग-समय)</td><td>त्वरण</td><td>विस्थापन</td></tr>\n<tr><td>a-t</td><td>—</td><td>वेग में परिवर्तन</td></tr>\n</table>\n<ul>\n<li><b>x-t ग्राफ:</b> सरल रेखा = नियत वेग; वक्र (परवलय) = त्वरण; क्षैतिज = विराम।</li>\n<li><b>v-t ग्राफ:</b> क्षैतिज रेखा = समान वेग (a = 0); ढलानदार सरल रेखा = नियत त्वरण।</li>\n<li>v-t ग्राफ समय-अक्ष को काटे = दिशा परिवर्तन — वहाँ वेग शून्य!</li>\n</ul>\n<p class=\"small-note\">🎯 सूत्र: \"ढलान अगली राशि, क्षेत्रफल पिछली राशि\" — x → v → a श्रृंखला में।</p>"
   },
   {
    "h": "5️⃣ मुक्त पतन और सापेक्ष वेग",
    "body": "<p><b>मुक्त पतन:</b> केवल गुरुत्व का प्रभाव, a = g = 9.8 m/s² नीचे की ओर। गति के समीकरणों में a = ±g रखें।</p>\n<ul>\n<li><b>ऊपर फेंकना:</b> उच्चतम बिंदु पर v = 0; उड्डयन काल = 2u/g; अधिकतम ऊँचाई = u²/2g; उसी बिंदु पर वापसी चाल = u।</li>\n<li><b>गिराना:</b> u = 0, h = ½gt² — t = √(2h/g)।</li>\n<li><b>सापेक्ष वेग (1D) ⭐:</b> v<sub>AB</sub> = v<sub>A</sub> − v<sub>B</sub>। विपरीत दिशा में सापेक्ष चाल = दोनों का योग (ट्रेनों का क्रॉस करना!)।</li>\n</ul>\n<p class=\"small-note\">💡 सापेक्ष वेग = \"दूसरे की दृष्टि से मेरी चाल\"।</p>"
   }
  ],
  "en": [
   {
    "h": "1️⃣ Describing Motion — Position, Distance, Displacement",
    "body": "<p>To describe motion in a straight line (1D), we first need a <b>frame of reference</b> — an origin and a direction. Position is just a signed number (+ or −) telling how far the object is from the origin.</p>\n<ul>\n<li><b>Distance:</b> total path length — scalar, always positive. Delhi to Jaipur and back: distance = 2 × 280 = 560 km.</li>\n<li><b>Displacement:</b> final − initial position — a vector (in 1D the sign gives direction). Back at the start? Displacement = 0!</li>\n<li><b>Average speed</b> = total distance / total time • <b>average velocity</b> = displacement / time — the two can differ (round trip: avg velocity = 0, avg speed ≠ 0).</li>\n<li><b>Instantaneous velocity:</b> v = dx/dt — the slope of the x-t graph. <b>Instantaneous speed</b> = magnitude of velocity.</li>\n</ul>\n<p class=\"small-note\">💡 Think: distance is the odometer (never decreases); displacement is the straight arrow from start to finish.</p>"
   },
   {
    "h": "2️⃣ Acceleration — Rate of Change of Velocity",
    "body": "<p><b>Average acceleration</b> = Δv/Δt • <b>instantaneous</b> a = dv/dt. Unit: m/s². Acceleration can be along or opposite to velocity:</p>\n<ul>\n<li><b>Speeding up:</b> a and v have the same sign (both + or both −).</li>\n<li><b>Retardation (deceleration):</b> a and v have opposite signs — speed decreases.</li>\n<li>Velocity can be zero while acceleration is not — a ball thrown up at its highest point: v = 0, but g still pulls down! ⭐ (exam trap)</li>\n</ul>\n<p class=\"small-note\">🎯 JEE trap: \"a = 0 does not mean rest\" — uniform velocity also has a = 0. And \"v = 0 does not mean a = 0\" (ball at the top).</p>"
   },
   {
    "h": "3️⃣ Equations of Motion — Three Mantras for Constant Acceleration ⭐",
    "body": "<p>When acceleration is <b>constant</b> (and motion is in a straight line), three equations solve everything. u = initial velocity, v = final velocity, a = acceleration, t = time, s = displacement:</p>\n<table class=\"tbl\">\n<tr><th>Equation</th><th>What is missing</th><th>When to use</th></tr>\n<tr><td>v = u + at</td><td>s</td><td>velocity-time relation</td></tr>\n<tr><td>s = ut + ½at²</td><td>v</td><td>displacement needed</td></tr>\n<tr><td>v² = u² + 2as</td><td>t</td><td>time not given</td></tr>\n</table>\n<ul>\n<li>Every quantity is <b>signed</b> — pick a direction and keep +/− consistent throughout.</li>\n<li><b>Distance in the n-th second ⭐:</b> s<sub>n</sub> = u + (a/2)(2n − 1). From rest: s<sub>n</sub> ∝ (2n−1) — the famous 1:3:5:7 ratio!</li>\n<li>Derivation is simple: area under the v-t graph = displacement.</li>\n</ul>\n<p class=\"small-note\">💡 Think: the three equations are three locks — the three quantities given in a question tell you which lock opens.</p>"
   },
   {
    "h": "4️⃣ Graphs — The x-t, v-t, a-t Game ⭐",
    "body": "<p>Graphs are a JEE favourite — both slope and area carry meaning:</p>\n<table class=\"tbl\">\n<tr><th>Graph</th><th>Slope gives</th><th>Area under curve</th></tr>\n<tr><td>x-t (position-time)</td><td>velocity</td><td>—</td></tr>\n<tr><td>v-t (velocity-time)</td><td>acceleration</td><td>displacement</td></tr>\n<tr><td>a-t</td><td>—</td><td>change in velocity</td></tr>\n</table>\n<ul>\n<li><b>x-t graph:</b> straight line = constant velocity; curve (parabola) = acceleration; horizontal = at rest. Steeper slope = faster.</li>\n<li><b>v-t graph:</b> horizontal line = uniform velocity (a = 0); sloping straight line = constant acceleration; signed area = displacement, unsigned = distance.</li>\n<li>If the v-t graph CROSSES the time axis, the direction changed — velocity was zero there!</li>\n</ul>\n<p class=\"small-note\">🎯 Shortcut: \"slope gives the next quantity, area gives the previous one\" — in the x → v → a chain.</p>"
   },
   {
    "h": "5️⃣ Free Fall and Relative Velocity",
    "body": "<p><b>Free fall:</b> only gravity acts, a = g = 9.8 m/s² downward (or −g by sign convention). Put a = ±g into the equations of motion — done!</p>\n<ul>\n<li><b>Thrown up:</b> at the highest point v = 0 (g still acts down); time of flight = 2u/g; max height = u²/2g; returns to the same point with speed u (downward).</li>\n<li><b>Dropped:</b> u = 0, h = ½gt² — t = √(2h/g).</li>\n<li><b>Relative velocity (1D) ⭐:</b> v<sub>AB</sub> = v<sub>A</sub> − v<sub>B</sub>. Opposite directions: relative speed = sum of both (trains crossing!).</li>\n</ul>\n<p class=\"small-note\">💡 Think: relative velocity is \"how fast I am from their point of view\".</p>"
   }
  ]
 },
 "short": {
  "hinglish": [
   {
    "h": "Basic Terms",
    "items": [
     "Distance: scalar, total path",
     "Displacement: vector, final − initial",
     "Avg velocity = displacement/time; avg speed = distance/time"
    ]
   },
   {
    "h": "Acceleration",
    "items": [
     "a = dv/dt, unit m/s²",
     "a aur v opposite → retardation",
     "v = 0 par a ≠ 0 possible (ball at top) ⭐"
    ]
   },
   {
    "h": "3 Equations ⭐",
    "items": [
     "v = u + at",
     "s = ut + ½at²",
     "v² = u² + 2as",
     "n-th second: u + (a/2)(2n−1)"
    ]
   },
   {
    "h": "Graphs ⭐",
    "items": [
     "x-t slope = velocity",
     "v-t slope = acceleration, area = displacement",
     "v-t axis cross = direction change"
    ]
   },
   {
    "h": "Free Fall",
    "items": [
     "a = ±g = 9.8 m/s²",
     "Max height u²/2g, flight time 2u/g",
     "Relative: v_AB = v_A − v_B"
    ]
   }
  ],
  "hi": [
   {
    "h": "मूल राशियाँ",
    "items": [
     "दूरी: अदिश, कुल पथ",
     "विस्थापन: सदिश, अंतिम − प्रारंभिक",
     "औसत वेग = विस्थापन/समय; औसत चाल = दूरी/समय"
    ]
   },
   {
    "h": "त्वरण",
    "items": [
     "a = dv/dt, मात्रक m/s²",
     "a व v विपरीत → मंदन",
     "v = 0 पर a ≠ 0 संभव (गेंद शीर्ष पर) ⭐"
    ]
   },
   {
    "h": "तीन समीकरण ⭐",
    "items": [
     "v = u + at",
     "s = ut + ½at²",
     "v² = u² + 2as",
     "n वें सेकंड: u + (a/2)(2n−1)"
    ]
   },
   {
    "h": "ग्राफ ⭐",
    "items": [
     "x-t ढलान = वेग",
     "v-t ढलान = त्वरण, क्षेत्रफल = विस्थापन",
     "v-t अक्ष काटना = दिशा परिवर्तन"
    ]
   },
   {
    "h": "मुक्त पतन",
    "items": [
     "a = ±g = 9.8 m/s²",
     "अधिकतम ऊँचाई u²/2g, उड्डयन काल 2u/g",
     "सापेक्ष: v_AB = v_A − v_B"
    ]
   }
  ],
  "en": [
   {
    "h": "Basic Terms",
    "items": [
     "Distance: scalar, total path",
     "Displacement: vector, final − initial",
     "Avg velocity = displacement/time; avg speed = distance/time"
    ]
   },
   {
    "h": "Acceleration",
    "items": [
     "a = dv/dt, unit m/s²",
     "a and v opposite → retardation",
     "v = 0 but a ≠ 0 possible (ball at top) ⭐"
    ]
   },
   {
    "h": "3 Equations ⭐",
    "items": [
     "v = u + at",
     "s = ut + ½at²",
     "v² = u² + 2as",
     "n-th second: u + (a/2)(2n−1)"
    ]
   },
   {
    "h": "Graphs ⭐",
    "items": [
     "x-t slope = velocity",
     "v-t slope = acceleration, area = displacement",
     "v-t axis crossing = direction change"
    ]
   },
   {
    "h": "Free Fall",
    "items": [
     "a = ±g = 9.8 m/s²",
     "Max height u²/2g, flight time 2u/g",
     "Relative: v_AB = v_A − v_B"
    ]
   }
  ]
 },
 "practice": [
  [
   "Ek car Delhi se Jaipur (280 km) jaakar wapas aati hai, total 8 ghante me. Average speed aur average velocity batao.",
   "Average speed = 560/8 = <b>70 km/h</b>. Average velocity = displacement/time = 0/8 = <b>0</b> (wapas same point pe!)."
  ],
  [
   "Ek object rest se 4 m/s² ke constant acceleration se chalta hai. 5 s baad velocity aur displacement?",
   "v = u + at = 0 + 4×5 = <b>20 m/s</b>. s = ut + ½at² = 0 + ½×4×25 = <b>50 m</b>."
  ],
  [
   "x-t graph ka slope kisi instant pe zero hai. Iska kya matlab hai?",
   "Us instant <b>instantaneous velocity = 0</b> — object pal ke liye rest me hai (ya direction change kar raha hai)."
  ],
  [
   "Ball ko 20 m/s se upar phenka (g = 10 m/s²). Maximum height aur total flight time?",
   "h = u²/2g = 400/20 = <b>20 m</b>. T = 2u/g = 40/10 = <b>4 s</b>."
  ],
  [
   "Train A 60 km/h aur train B 40 km/h opposite directions me aa rahi hain. Crossing ke liye relative speed?",
   "Opposite directions me relative speed = 60 + 40 = <b>100 km/h</b>."
  ],
  [
   "Ek object 10 m/s se chal raha hai, 5 s me retardation se ruk jaata hai. Retardation aur stopping distance?",
   "a = (0−10)/5 = <b>−2 m/s²</b> (retardation 2 m/s²). s = (u+v)/2 × t = 5×5 = <b>25 m</b> (ya v²=u²+2as se)."
  ],
  [
   "v-t graph time axis ke neeche bhi jaata hai. Neeche wala area kya batata hai?",
   "<b>Negative displacement</b> — object opposite direction me chala. Total displacement = + area − (− area); total distance = dono ka sum."
  ],
  [
   "Rest se girte object ka pehle, doosre, teesre second ke distances ka ratio?",
   "s<sub>n</sub> ∝ (2n−1) → <b>1 : 3 : 5</b> (Galileo ka odd-number rule)."
  ],
  [
   "Free fall me 45 m ki building se ball girai (g = 10 m/s²). Zameen tak time aur impact velocity?",
   "t = √(2h/g) = √(90/10) = <b>3 s</b>. v = gt = 10×3 = <b>30 m/s</b> neeche."
  ],
  [
   "Car 20 m/s se 10 s me uniformly 30 m/s ho gayi, fir 20 m/s² retardation se ruki. Acceleration phase ka displacement?",
   "s = (u+v)/2 × t = (20+30)/2 × 10 = <b>250 m</b>. (Acceleration = 1 m/s² tha.)"
  ]
 ],
 "topic_strip": None,
 "next": {
  "href": "/class-11/physics/ch-3/",
  "title": "Motion in a Plane"
 }
}

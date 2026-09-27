"""Site structure config for the Maida builder.
Subject metadata reconstructed from the live subject-index pages."""

# Subjects per built class: slug -> display metadata
SUBJECTS = {
    11: {
        'physics': {'en': 'Physics', 'title_name': 'Physics', 'emoji': '🧲',
            'subtitle': 'NCERT rationalized syllabus (14 units) • CBSE + JEE foundation • Har chapter: long notes + short notes (Hindi/English/Hinglish) + practice', 'meta': 'Class 11 Physics (NCERT/CBSE rationalized) — all 14 chapters with long + short notes in Hindi, English, Hinglish, plus practice questions.', 'unitpill': '14 units', 'chapters': 14},
        'chemistry': {'en': 'Chemistry', 'title_name': 'Chemistry', 'emoji': '⚗️',
            'subtitle': 'NCERT rationalized syllabus (9 units) • CBSE + JEE foundation • Har chapter: video + long notes + short notes (Hindi/English/Hinglish)', 'meta': 'Class 11 Chemistry (NCERT/CBSE rationalized) — all 9 chapters with video, long + short notes in Hindi, English, Hinglish.', 'unitpill': '9 units', 'chapters': 9},
        'biology': {'en': 'Biology', 'title_name': 'Biology', 'emoji': '🧬',
            'subtitle': 'NCERT rationalized syllabus (19 chapters) • CBSE + NEET foundation • Har chapter: long notes + short notes (Hindi/English/Hinglish) + practice', 'meta': 'Class 11 Biology (NCERT/CBSE rationalized) — all 19 chapters with long + short notes in Hindi, English, Hinglish, plus practice questions.', 'unitpill': '19 chapters', 'chapters': 19},
        'maths': {'en': 'Mathematics', 'title_name': 'Maths', 'emoji': '📐',
            'subtitle': 'NCERT rationalized syllabus (14 chapters) • CBSE + JEE foundation • Har chapter: long notes + short notes (Hindi/English/Hinglish) + practice', 'meta': 'Class 11 Maths (NCERT/CBSE rationalized) — all 14 chapters with long + short notes in Hindi, English, Hinglish, plus practice questions.', 'unitpill': '14 chapters', 'chapters': 14},
    },
    12: {
        'physics': {'en': 'Physics', 'title_name': 'Physics', 'emoji': '🧲',
            'subtitle': 'NCERT rationalized syllabus (14 chapters) • CBSE + JEE foundation • Har chapter: long notes + short notes (Hindi/English/Hinglish) + practice', 'meta': 'Class 12 Physics (NCERT/CBSE rationalized) — all 14 chapters with long + short notes in Hindi, English, Hinglish, plus practice questions.', 'unitpill': '14 chapters', 'chapters': 14},
        'chemistry': {'en': 'Chemistry', 'title_name': 'Chemistry', 'emoji': '⚗️',
            'subtitle': 'NCERT rationalized syllabus (10 chapters) • CBSE + JEE foundation • Har chapter: long notes + short notes (Hindi/English/Hinglish) + practice', 'meta': 'Class 12 Chemistry (NCERT/CBSE rationalized) — all 10 chapters with long + short notes in Hindi, English, Hinglish, plus practice questions.', 'unitpill': '10 chapters', 'chapters': 10},
        'biology': {'en': 'Biology', 'title_name': 'Biology', 'emoji': '🧬',
            'subtitle': 'NCERT rationalized syllabus (13 chapters) • CBSE + NEET foundation • Har chapter: long notes + short notes (Hindi/English/Hinglish) + practice', 'meta': 'Class 12 Biology (NCERT/CBSE rationalized) — all 13 chapters with long + short notes in Hindi, English, Hinglish, plus practice questions.', 'unitpill': '13 chapters', 'chapters': 13},
        'maths': {'en': 'Mathematics', 'title_name': 'Maths', 'emoji': '📐',
            'subtitle': 'NCERT rationalized syllabus (13 chapters) • CBSE + JEE foundation • Har chapter: long notes + short notes (Hindi/English/Hinglish) + practice', 'meta': 'Class 12 Maths (NCERT/CBSE rationalized) — all 13 chapters with long + short notes in Hindi, English, Hinglish, plus practice questions.', 'unitpill': '13 chapters', 'chapters': 13},
    },
}

# Subject hindi names (for class pages)
SUBJECT_HI = {'physics': 'भौतिक विज्ञान', 'chemistry': 'रसायन विज्ञान', 'biology': 'जीव विज्ञान', 'maths': 'गणित'}
SUBJECT_LETTER = {'physics': 'P', 'chemistry': 'C', 'biology': 'B', 'maths': 'M'}

# Planned classes (6-10): subject list shown as Coming soon
PLANNED_SUBJECTS = {
    6: [('maths','Mathematics','गणित','M'), ('science','Science','विज्ञान','S'), ('social','Social Science','सामाजिक विज्ञान','S'), ('english','English','अंग्रेज़ी','E'), ('hindi','Hindi','हिन्दी','H')],
    7: [('maths','Mathematics','गणित','M'), ('science','Science','विज्ञान','S'), ('social','Social Science','सामाजिक विज्ञान','S'), ('english','English','अंग्रेज़ी','E'), ('hindi','Hindi','हिन्दी','H')],
    8: [('maths','Mathematics','गणित','M'), ('science','Science','विज्ञान','S'), ('social','Social Science','सामाजिक विज्ञान','S'), ('english','English','अंग्रेज़ी','E'), ('hindi','Hindi','हिन्दी','H')],
    9: [('maths','Mathematics','गणित','M'), ('science','Science','विज्ञान','S'), ('social','Social Science','सामाजिक विज्ञान','S'), ('english','English','अंग्रेज़ी','E'), ('hindi','Hindi','हिन्दी','H')],
    10: [('maths','Mathematics','गणित','M'), ('science','Science','विज्ञान','S'), ('social','Social Science','सामाजिक विज्ञान','S'), ('english','English','अंग्रेज़ी','E'), ('hindi','Hindi','हिन्दी','H')],
}

# Homepage class cards: status per class (live classes link, planned show Coming soon)
LIVE_CLASSES = [11, 12]
CLASS_CARD_TOPICS = {
    11: '📚 Physics, Chemistry, Maths, Biology live — 56 chapters, 3 languages',
    12: '📚 Physics, Chemistry, Maths, Biology live — 50 chapters, 3 languages',
}
PLANNED_CARD_TOPIC = '📚 5 subjects planned (NCERT/CBSE)'

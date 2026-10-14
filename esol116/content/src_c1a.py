# Competency 1 (part A): skills 1.1-1.4 — questions + lessons for NYSTCE ESOL CST (116)
QUESTIONS = []
LESSONS = []

# ---------------- 1.1 Phonology & pronunciation ----------------
QUESTIONS += [
{
 "id": "1.1-01", "skill": "1.1", "type": "application", "difficulty": 1, "diag": 0,
 "stem": "Which of the following words contains exactly three phonemes?",
 "options": ["fox", "clap", "thought", "eight"],
 "answer": 2,
 "why": "Phonemes are counted by sound, not by letter. 'Thought' has seven letters but only three phonemes: /θ/ (spelled th), one vowel (spelled ough), and /t/, so /θɔt/. Digraphs and complex vowel spellings often stand for a single phoneme, while a single letter such as x can stand for two (/ks/).",
 "traps": [
  {"code": "TERM", "pair": "grapheme ↔ phoneme", "note": "Three letters, but x stands for two sounds, /k/ and /s/, so 'fox' has four phonemes: /f/ /ɑ/ /k/ /s/."},
  {"code": "TERM", "pair": "consonant blend ↔ digraph", "note": "A blend like cl is two phonemes, not one, so 'clap' has four: /k/ /l/ /æ/ /p/. Only digraphs such as sh or th spell a single sound."},
  None,
  {"code": "TERM", "pair": "diphthong ↔ two vowels", "note": "The diphthong /eɪ/ counts as one vowel phoneme and gh is silent, so 'eight' has only two phonemes: /eɪ/ and /t/."}
 ],
 "key": "Count phonemes by sound, not letters: thought = /θ/ + vowel + /t/ (3); the x in fox = /ks/ (2)."
},
{
 "id": "1.1-02", "skill": "1.1", "type": "knowledge", "difficulty": 1, "diag": 0,
 "stem": "A teacher points out that the th in 'think' and the th in 'this' sound different. Which of the following best describes these two sounds?",
 "options": [
  "They are two separate phonemes, /θ/ and /ð/, that differ only in voicing.",
  "They are one phoneme, since both are spelled with the same digraph, th.",
  "They are two allophones of /t/ that occur in different word positions.",
  "They are two separate phonemes that differ in their place of articulation."
 ],
 "answer": 0,
 "why": "/θ/ (think) and /ð/ (this) are both made by pushing air between the tongue and the upper teeth (interdental fricatives); the only difference is that /ð/ is voiced, with the vocal folds vibrating. They are separate phonemes because swapping them can change a word, as in the minimal pair 'teeth' /tiθ/ (noun) and 'teethe' /tið/ (verb). Spelling is not evidence: English uses one digraph for two phonemes.",
 "traps": [
  None,
  {"code": "TERM", "pair": "grapheme ↔ phoneme", "note": "Spelling doesn't determine phonemes. The digraph th spells two different phonemes, and the minimal pair teeth/teethe proves they contrast."},
  {"code": "TERM", "pair": "phoneme ↔ allophone", "note": "Allophones are predictable variants of one phoneme that never change meaning. These sounds do change meaning, and neither is a variant of /t/."},
  {"code": "TERM", "pair": "voicing ↔ place of articulation", "note": "Both sounds are made at the same place (tongue at the teeth) in the same manner (fricative); voicing is the only difference."}
 ],
 "key": "/θ/ (think) and /ð/ (this) are separate phonemes that differ only in voicing: teeth vs. teethe."
},
{
 "id": "1.1-03", "skill": "1.1", "type": "knowledge", "difficulty": 1, "diag": 0,
 "stem": "In English, the /p/ in 'pin' is pronounced with a puff of air, [pʰ], while the /p/ in 'spin' has none, [p]. Native speakers hear them as the same sound. Which term best describes [pʰ] and [p] in English?",
 "options": ["a minimal pair", "allophones of one phoneme", "two contrasting phonemes", "sounds in free variation"],
 "answer": 1,
 "why": "Allophones are predictable variants of a single phoneme that never change a word's meaning. English voiceless stops are aspirated at the start of a stressed syllable (pin [pʰɪn]) and unaspirated after /s/ (spin [spɪn]), so the two never contrast. In Hindi, Urdu, Bengali, and Korean, aspiration does distinguish words, which shows that a difference that is 'invisible' in one language can be meaningful in another.",
 "traps": [
  {"code": "TERM", "pair": "minimal pair ↔ allophones", "note": "A minimal pair is two words that differ by one phoneme (pin/bin). [pʰ] and [p] are sounds, not words, and they never create different words in English."},
  None,
  {"code": "TERM", "pair": "phoneme ↔ allophone", "note": "Contrasting phonemes change meaning when swapped. Swapping [pʰ] and [p] in English only sounds odd; it never produces a different word."},
  {"code": "TERM", "pair": "free variation ↔ complementary distribution", "note": "In free variation either sound can occur in the same spot. Here the choice is predictable from position (aspirated initially, unaspirated after /s/)."}
 ],
 "key": "Allophones are predictable variants of one phoneme ([pʰ] in pin, [p] in spin); they never change meaning."
},
{
 "id": "1.1-04", "skill": "1.1", "type": "analysis", "difficulty": 2, "diag": 1,
 "stimulus": "Oral reading record, grade 4 Integrated ENL (Emerging; home language Spanish)\nText: “The students speak Spanish at school.”\nStudent: “The estudents espeak Espanish at eschool.”",
 "stem": "Which of the following best explains the pattern in this student's oral reading?",
 "options": [
  "Spanish words cannot begin with /s/ followed by a consonant, so the student adds a vowel before the cluster.",
  "Spanish lacks the /s/ phoneme, so the student substitutes the closest Spanish sound sequence for it.",
  "The student may have a reading disability, since the added sounds do not appear in the printed words.",
  "The student is simplifying each cluster by deleting a consonant, a common strategy in early speech."
 ],
 "answer": 0,
 "why": "Every language has phonotactic rules about which sound sequences may occur. Spanish has /s/ and has clusters like /pl/ and /tr/, but no Spanish word begins with /s/ + consonant (compare estudiante, España, escuela). The student repairs the unfamiliar English cluster by inserting /e/ before it, a process called epenthesis. This is negative transfer of L1 syllable structure, not a reading problem.",
 "traps": [
  None,
  {"code": "TERM", "pair": "phoneme inventory ↔ phonotactics", "note": "Spanish has the /s/ phoneme (sí, casa), and the student pronounces it. The problem is where /s/ may occur, a phonotactic constraint, not a missing sound."},
  {"code": "MISREFERRAL", "note": "The pattern is systematic and predicted by the home language's sound rules, which is typical L2 transfer. Calling it a disability confuses a language difference with a disorder."},
  {"code": "TERM", "pair": "epenthesis ↔ deletion", "note": "Nothing is deleted; the student keeps every consonant and adds a vowel. Inserting a sound to repair a cluster is epenthesis."}
 ],
 "key": "Spanish speakers' 'espeak/estudent' is epenthesis: L1 phonotactics forbid word-initial /s/ + consonant."
},
{
 "id": "1.1-05", "skill": "1.1", "type": "application", "difficulty": 2, "diag": 0,
 "stimulus": "A grade 6 student (Transitioning; home language Spanish) tells the class, “I leave in Queens with my grandmother,” meaning live. In other lessons, he pronounces 'ship' and 'sheep' the same way.",
 "stem": "Which minimal pair would be most useful for targeted practice of the contrast behind these errors?",
 "options": ["fill / fell", "leave / leaf", "fill / feel", "live / lives"],
 "answer": 2,
 "why": "Both errors show the student merging /ɪ/ (live, ship) and /i/ (leave, sheep). Spanish has a five-vowel system with a single high front vowel, so this English contrast is new. A minimal pair is two words that differ in exactly one phoneme in the same position, and 'fill / feel' isolates exactly the /ɪ/–/i/ contrast the student needs.",
 "traps": [
  {"code": "PARTIAL", "note": "'Fill / fell' is a true minimal pair, but it contrasts /ɪ/ with /ɛ/, not the /ɪ/–/i/ contrast this student is merging."},
  {"code": "LITERAL", "note": "This pair borrows a word from the stimulus but contrasts final /v/ and /f/ (voicing). The student's problem is the vowel, not the final consonant."},
  None,
  {"code": "TERM", "pair": "minimal pair ↔ inflected form", "note": "'Live / lives' differ by an added morpheme, not by one substituted phoneme in the same position, so it isn't a minimal pair and doesn't target the vowel."}
 ],
 "key": "Choose minimal pairs that isolate the exact merged contrast: /ɪ/–/i/ → fill/feel, ship/sheep, live/leave."
},
{
 "id": "1.1-06", "skill": "1.1", "type": "analysis", "difficulty": 3, "diag": 0,
 "stimulus": "Teacher says | Student writes\nright | light\nload | road\ncollect | correct\nglass | grass",
 "stem": "A grade 7 Transitioning student whose home language is Korean produced these spellings on a dictation task. The pattern is most likely the result of which of the following?",
 "options": [
  "In Korean, [l] and an r-like flap [ɾ] are variants of one phoneme, so the English /r/–/l/ contrast is hard to perceive.",
  "Korean has neither an r-like nor an l-like sound, so the student is guessing between two unfamiliar sounds.",
  "The student is reversing letters while writing, which is an early sign of a visual-processing disability.",
  "English spelling is irregular, so the student cannot reliably predict which letter represents each sound."
 ],
 "answer": 0,
 "why": "Korean has one liquid phoneme (ㄹ) that is pronounced as a flap [ɾ] in some positions and as [l] in others. Because the difference is predictable by position, Korean speakers learn to ignore it, so English minimal pairs like right/light and collect/correct can sound alike. When two sounds are allophones in the L1 but separate phonemes in English, learners struggle both to hear and to produce the contrast.",
 "traps": [
  None,
  {"code": "TERM", "pair": "missing sound ↔ missing contrast", "note": "Korean speakers do produce both [l] and an r-like flap. What Korean lacks is a meaningful contrast between them, so the student needs perception practice, not new sounds."},
  {"code": "MISREFERRAL", "note": "The substitutions go both ways and only between r and l, exactly where Korean merges the sounds. That's predictable L1 transfer, not evidence of a disability."},
  {"code": "LITERAL", "note": "English spelling is irregular in many places, but r and l are spelled consistently. The errors follow sounds the student can't yet distinguish."}
 ],
 "key": "Two L1 allophones become one category for the learner: Korean ㄹ covers [l] and [ɾ], so right/light merge."
},
{
 "id": "1.1-07", "skill": "1.1", "type": "scenario", "difficulty": 2, "diag": 0,
 "stimulus": "During a grade 5 science discussion, a student (Emerging; home language Arabic) says, “We put the blant by the window,” and later asks, “Can I have a ben?”",
 "stem": "The ENL teacher wants to address this pronunciation pattern. Which approach would be most effective?",
 "options": [
  "Correct each mispronounced word immediately whenever the student speaks in discussions, so the model is heard often.",
  "Assign a daily list of forty words beginning with p for the student to read aloud until the sound becomes automatic.",
  "Practice pairs like pea/bee and pack/back, show the burst of air for /p/ with a paper strip, then use the words in unit sentences.",
  "Refer the student to the speech-language pathologist, since the substitution has continued for months despite modeling."
 ],
 "answer": 2,
 "why": "Arabic has /b/ but no /p/ phoneme, so learners often substitute /b/ for English /p/. Effective pronunciation work makes the contrast perceptible (minimal pairs), adds a physical cue (word-initial English /p/ is voiceless and aspirated, so a paper strip moves), and then moves quickly into meaningful use. This is negative transfer of the L1 sound inventory and a normal part of acquisition.",
 "traps": [
  {"code": "OVERCORRECT", "note": "Constant public correction interrupts meaning-focused talk and raises the affective filter, and it gives no targeted perception or production practice."},
  {"code": "ISOLATED", "note": "Repeating a word list with no contrast and no context rarely transfers to spontaneous speech, and it never lets the student hear /p/ against /b/."},
  None,
  {"code": "MISREFERRAL", "note": "Substituting /b/ for /p/ is a predictable L1-transfer pattern for Arabic speakers. Persistence over a few months is typical and doesn't by itself suggest a speech disorder."}
 ],
 "key": "Arabic lacks /p/: use minimal pairs (pea/bee) plus an aspiration cue, then meaningful practice, not drills or referral."
},
]

# ---- END QUESTIONS ----

import json, pathlib
pathlib.Path(__file__).with_name("c1a.json").write_text(json.dumps({"questions": QUESTIONS, "lessons": LESSONS}, ensure_ascii=False, indent=1))

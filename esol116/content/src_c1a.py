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
{
 "id": "1.1-08", "skill": "1.1", "type": "analysis", "difficulty": 2, "diag": 2,
 "stimulus": "During a grade 8 social studies presentation, a student (Transitioning; home language Bengali) says, “Many families in the Sahara live in the de-ZERT.” Several classmates look puzzled, and one asks, “Like cake?”",
 "stem": "The classmates' confusion is best explained by which feature of English pronunciation?",
 "options": [
  "intonation, because the student used a rising pitch at the end of a statement",
  "word stress, because stress placement can distinguish one English word from another",
  "vowel epenthesis, because the student added an extra syllable to the word",
  "allophonic variation, because the final /t/ in the word was not fully released"
 ],
 "answer": 1,
 "why": "English has lexical (word) stress, and moving it can change the word: DEsert (dry land) vs. desSERT (sweet course), or noun–verb pairs like REcord/reCORD and PERmit/perMIT. Stress also changes vowel quality, because unstressed vowels often reduce to schwa /ə/. Listeners rely heavily on stress patterns to recognize words, so misplaced stress can block comprehension even when every individual sound is accurate.",
 "traps": [
  {"code": "TERM", "pair": "word stress ↔ intonation", "note": "Intonation is the pitch pattern across a whole utterance; nothing in the scenario describes pitch. The problem is which syllable within one word was stressed."},
  None,
  {"code": "TERM", "pair": "epenthesis ↔ word stress", "note": "No syllable was added; 'desert' and 'dessert' both have two. Only the stressed syllable moved."},
  {"code": "TERM", "pair": "allophone ↔ word stress", "note": "How the final /t/ is released never changes which word an English listener hears. The confusion came from stress placement."}
 ],
 "key": "English word stress can change the word: DEsert vs. desSERT, REcord (noun) vs. reCORD (verb)."
},
{
 "id": "1.1-09", "skill": "1.1", "type": "analysis", "difficulty": 3, "diag": 0,
 "stimulus": "Grade 3 student (Emerging; home language Mandarin), same day\nOral retell: “Yesterday I walk to the par with my frien. We jump in the lea.”\nWritten retell: “Yesterday I walked to the park with my friend. We jumped in the leaves.”",
 "stem": "Based on both samples, which of the following is the most accurate interpretation of the student's oral omissions?",
 "options": [
  "The student has not yet acquired the regular past tense, as the oral forms 'walk' and 'jump' show.",
  "Mandarin syllables allow few final consonants, so the student drops word-final consonants and clusters in speech.",
  "Mandarin verbs take no tense endings, so the student is transferring L1 grammar by leaving off -ed.",
  "The omissions occur across many different words, which suggests a speech sound disorder needing evaluation."
 ],
 "answer": 1,
 "why": "Mandarin syllables can end only in a vowel or a nasal (/n/ or /ŋ/), so English final stops, fricatives, and clusters are hard to pronounce. The key evidence is that the student drops final consonants in words with no grammatical ending (park, friend) and keeps a final /n/ (frien), while writing walked and jumped correctly. That points to phonological transfer of syllable structure, not a missing grammar rule.",
 "traps": [
  {"code": "LITERAL", "note": "The oral sample alone suggests this, but the written retell shows walked and jumped used correctly. The omissions follow sound patterns, not grammar knowledge."},
  None,
  {"code": "PARTIAL", "note": "Mandarin does lack tense inflection, and that can cause grammatical omissions, but this student also drops non-grammatical finals (park, friend) and marks past tense correctly in writing."},
  {"code": "MISREFERRAL", "note": "The omissions are systematic and match Mandarin syllable structure, the hallmark of L1 transfer. They don't suggest a speech disorder."}
 ],
 "key": "Compare oral and written evidence: dropped finals in speech but correct -ed in writing means phonological transfer, not missing grammar."
},
{
 "id": "1.1-10", "skill": "1.1", "type": "application", "difficulty": 3, "diag": 0,
 "stem": "Using C for a consonant phoneme and V for a vowel phoneme, which word has the syllable structure CCCVCC?",
 "options": ["splash", "stamps", "thrown", "strict"],
 "answer": 3,
 "why": "Syllable structure is described by phonemes, not letters. 'Strict' is /s t r ɪ k t/: three consonants before the vowel and two after. English allows up to three consonants at the start of a syllable (in that case the first is always /s/) and up to four at the end (texts), which is why learners whose languages favor simple CV or CVC syllables, such as Japanese or Mandarin, find English clusters difficult.",
 "traps": [
  {"code": "TERM", "pair": "digraph ↔ consonant cluster", "note": "'Splash' begins with a three-consonant cluster, but sh is a single phoneme, /ʃ/, so the word is CCCVC."},
  {"code": "LITERAL", "note": "'Stamps' has five consonants, but they fall two before the vowel and three after (/s t æ m p s/), so it is CCVCCC, the mirror image."},
  {"code": "TERM", "pair": "grapheme ↔ phoneme", "note": "'Thrown' looks consonant-heavy, but th = /θ/ and ow = /oʊ/, so it is /θ r oʊ n/, only CCVC."}
 ],
 "key": "Analyze syllables by phonemes: strict = /strɪkt/ = CCCVCC. Three-consonant onsets in English always begin with /s/."
},
{
 "id": "1.1-11", "skill": "1.1", "type": "analysis", "difficulty": 2, "diag": 0,
 "stimulus": "A grade 10 student (Expanding; home language Spanish) reads aloud, “The banana is on the table.” The teacher notes that the student gives every syllable about the same length and a full vowel, saying [ba-na-na] with a clear [a] in each syllable.",
 "stem": "The student's reading suggests a need for instruction in which feature of English pronunciation?",
 "options": [
  "aspiration of voiceless stops at the beginning of stressed syllables",
  "contrastive stress to highlight new information within a sentence",
  "reduction of unstressed vowels to schwa in a stress-timed rhythm",
  "rising intonation at the end of yes/no questions"
 ],
 "answer": 2,
 "why": "English is often described as stress-timed: stressed syllables are longer and louder, and many unstressed vowels reduce to schwa /ə/, so banana is /bəˈnænə/. Spanish is syllable-timed, with syllables of similar length and full vowels even when unstressed. Transferring that rhythm makes English sound choppy and can reduce intelligibility, so teaching stress and schwa (for example, tapping the stressed syllable) is high-yield.",
 "traps": [
  {"code": "PARTIAL", "note": "Aspiration is a real English feature some learners miss, but the teacher's notes describe equal syllable length and full vowels, which point to rhythm and vowel reduction."},
  {"code": "TERM", "pair": "sentence stress ↔ word rhythm", "note": "Contrastive stress highlights one word in a sentence for meaning. The issue here is rhythm inside words: unstressed syllables aren't being reduced."},
  None,
  {"code": "LITERAL", "note": "The sentence is a statement, so question intonation has nothing to do with this evidence."}
 ],
 "key": "English is stress-timed: unstressed vowels reduce to schwa (/bəˈnænə/). Syllable-timed L1s like Spanish give every syllable full weight."
},
{
 "id": "1.1-12", "skill": "1.1", "type": "application", "difficulty": 2, "diag": 0,
 "stem": "A teacher says to a student, “You turned in your permission slip, didn't you?” with falling intonation on the tag. What does the falling intonation most likely signal?",
 "options": [
  "The teacher expects the student to confirm something the teacher already believes is true.",
  "The teacher is genuinely unsure and is asking the student for new information.",
  "No difference in meaning, since the words of the tag alone make the sentence a question.",
  "The teacher is using contrastive stress to emphasize the word 'permission.'"
 ],
 "answer": 0,
 "why": "Intonation, the rise and fall of pitch across an utterance, carries meaning beyond the words. With a falling tag, the speaker is fairly sure and expects agreement; with a rising tag, the speaker is genuinely uncertain and wants information. ELLs may miss these cues or transfer L1 pitch patterns, so intonation is worth teaching explicitly in real exchanges.",
 "traps": [
  None,
  {"code": "TERM", "pair": "falling tag ↔ rising tag", "note": "That meaning goes with rising intonation on the tag, which signals real uncertainty. A falling tag signals that the speaker expects confirmation."},
  {"code": "LITERAL", "note": "The words are identical either way; the pitch pattern is what tells the listener whether the speaker is checking a belief or truly asking."},
  {"code": "TERM", "pair": "intonation ↔ contrastive stress", "note": "Contrastive stress makes one word prominent (the PERMISSION slip, not the lunch form). The stem describes pitch on the tag, which is intonation."}
 ],
 "key": "Falling tag = the speaker expects confirmation; rising tag = a genuine question. Intonation carries meaning."
},
{
 "id": "1.1-13", "skill": "1.1", "type": "analysis", "difficulty": 3, "diag": 0,
 "stimulus": "Word | Student's pronunciation\nbag | [bæk]\nhis | [hɪs]\ncard | [kɑrt]\nlove | [lʌf]",
 "stem": "A grade 9 Expanding student whose home language is Russian reads a word list aloud. Voiced consonants at the beginning and in the middle of words are accurate (boy, ladder, visit), but the teacher records the pronunciations above. Which of the following best explains this pattern?",
 "options": [
  "Russian has no voiced consonants, so the student substitutes voiceless ones in every position.",
  "The student is still in the silent period and is not yet ready for pronunciation instruction.",
  "The student cannot hear voicing differences in any position, which suggests an auditory processing problem.",
  "Russian makes voiced consonants voiceless at the end of a word, and the student is transferring that rule."
 ],
 "answer": 3,
 "why": "Russian, like Polish and German, has final devoicing: voiced consonants such as /b d g z v/ become voiceless at the end of a word, so Russian хлеб ('bread') ends in [p]. Because this student voices consonants correctly at the beginning and middle of words, the issue is a positional L1 rule transferred to English. It can merge pairs like bag/back and his/hiss, so it's worth targeting with final-position minimal pairs.",
 "traps": [
  {"code": "LITERAL", "note": "Russian has plenty of voiced consonants, and the student produces them correctly at the start and middle of words. Only word-final position is affected."},
  {"code": "WRONG_LEVEL", "note": "An Expanding ninth grader who reads aloud is far past the silent period, and pronunciation can be addressed at every level."},
  {"code": "MISREFERRAL", "note": "Correct voicing in initial and medial positions shows the student hears and makes the contrast. A position-specific pattern that matches the L1 is transfer, not a processing problem."},
  None
 ],
 "key": "Russian final devoicing makes 'bag' sound like 'back': a positional L1 rule, not a missing sound."
},
{
 "id": "1.1-14", "skill": "1.1", "type": "analysis", "difficulty": 1, "diag": 0,
 "stimulus": "Teacher says | Student writes\nshop | chop\nwash | wach\nshoe | choo",
 "stem": "A grade 2 Entering student whose home language is Spanish produces these spellings on a weekly spelling check. The pattern most likely reflects which of the following?",
 "options": [
  "The student does not yet know the letter-sound correspondence for the letters s and h.",
  "The student is confusing two allophones of a single English phoneme.",
  "The student is reversing digraphs, which is an early warning sign of dyslexia.",
  "Most varieties of Spanish have /tʃ/ but no /ʃ/, so the student hears English /ʃ/ as /tʃ/."
 ],
 "answer": 3,
 "why": "/ʃ/ (shoe) and /tʃ/ (chew) are separate phonemes in English, as the minimal pair share/chair shows. Most varieties of Spanish have /tʃ/ (spelled ch, as in chico) but no /ʃ/ phoneme, so the new sound is mapped onto the closest familiar one, and the spelling follows what the student hears. This is transfer from the L1 phoneme inventory, best addressed with listening discrimination and minimal pairs.",
 "traps": [
  {"code": "LITERAL", "note": "The student consistently writes ch, the spelling of the sound she hears. That points to a perception pattern, not a random gap in letter-sound knowledge."},
  {"code": "TERM", "pair": "phoneme ↔ allophone", "note": "In English, /ʃ/ and /tʃ/ are separate phonemes (share vs. chair). Treating them as allophones misreads the contrast."},
  {"code": "MISREFERRAL", "note": "A consistent substitution that matches the home language's sound system is typical L2 transfer. It is not a reversal and not a sign of dyslexia."},
  None
 ],
 "key": "Most Spanish varieties have /tʃ/ but no /ʃ/; sh-to-ch spellings reflect transfer from the L1 phoneme inventory."
},
]

# ---------------- 1.2 Morphology & word formation ----------------
QUESTIONS += [
{
 "id": "1.2-01", "skill": "1.2", "type": "application", "difficulty": 1, "diag": 0,
 "stimulus": "The teacher's students walked home.",
 "stem": "Which bound morpheme in this sentence is derivational?",
 "options": ["the -s in students", "the -ed in walked", "the -'s in teacher's", "the -er in teacher"],
 "answer": 3,
 "why": "Derivational morphemes create a new word and often change its part of speech: -er turns the verb teach into the noun teacher. The other three are inflectional: plural -s, past tense -ed, and possessive -'s add grammatical information without creating a new word. English has only eight inflectional morphemes, and all of them are suffixes.",
 "traps": [
  {"code": "TERM", "pair": "inflectional ↔ derivational", "note": "Plural -s is one of the eight inflectional morphemes. 'Students' is still the same noun, just marked for number."},
  {"code": "TERM", "pair": "inflectional ↔ derivational", "note": "Past tense -ed is inflectional. 'Walked' is still a form of the verb walk, not a new word."},
  {"code": "TERM", "pair": "inflectional ↔ derivational", "note": "Possessive -'s is inflectional. It marks a grammatical relationship and doesn't create a new dictionary word."},
  None
 ],
 "key": "Derivational morphemes make new words (teach → teacher); inflectional ones (-s, -'s, -ed) only mark grammar."
},
{
 "id": "1.2-02", "skill": "1.2", "type": "application", "difficulty": 2, "diag": 1,
 "stem": "Which of the following words contains exactly four morphemes?",
 "options": ["caterpillars", "mistreatments", "unbreakable", "rewritten"],
 "answer": 1,
 "why": "A morpheme is the smallest unit of meaning. 'Mistreatments' = mis- ('wrongly') + treat (free root) + -ment (derivational, verb → noun) + -s (inflectional plural): four morphemes in only three syllables. Counting morphemes means finding meaningful parts, not counting beats or letters.",
 "traps": [
  {"code": "TERM", "pair": "syllable ↔ morpheme", "note": "'Caterpillars' has four syllables but only two morphemes: caterpillar (its pieces carry no meaning on their own) + plural -s."},
  None,
  {"code": "TERM", "pair": "syllable ↔ morpheme", "note": "'Unbreakable' has four syllables but three morphemes: un- + break + -able."},
  {"code": "PARTIAL", "note": "Close, but 'rewritten' has three morphemes: re- + write + -en (past participle). The doubled t is spelling, not a separate morpheme."}
 ],
 "key": "Count morphemes by units of meaning: mis-treat-ment-s = 4, even though the word has only 3 syllables."
},
{
 "id": "1.2-03", "skill": "1.2", "type": "scenario", "difficulty": 2, "diag": 2,
 "stem": "During a grade 5 Integrated ENL lesson, a student says, “Taller and teacher both end in -er, so they have the same kind of ending.” Which response best reflects accurate morphological analysis?",
 "options": [
  "Yes. Both are derivational suffixes, because each one adds meaning to the base word.",
  "No. Comparative -er in taller is inflectional; agentive -er in teacher is derivational.",
  "Yes. Both are inflectional suffixes, because both are added to the end of a base word.",
  "No. The -er in taller is a free morpheme, but the -er in teacher is a bound morpheme."
 ],
 "answer": 1,
 "why": "The two endings sound the same but are different morphemes. Comparative -er is one of English's eight inflectional morphemes: tall and taller are both adjectives. Agentive -er is derivational: it creates a new word in a new class (teach, a verb → teacher, a noun). A quick test: if the part of speech changes or a new dictionary entry results, the morpheme is derivational.",
 "traps": [
  {"code": "TERM", "pair": "inflectional ↔ derivational", "note": "Both endings add meaning, so 'adds meaning' can't be the test. Comparative -er keeps tall an adjective, which makes it inflectional."},
  None,
  {"code": "TERM", "pair": "suffix ↔ inflection", "note": "Many derivational morphemes are suffixes too (-ness, -ful, agentive -er). Position at the end of a word doesn't make a morpheme inflectional."},
  {"code": "TERM", "pair": "free ↔ bound", "note": "Neither -er can stand alone as a word, so both are bound. The real difference is inflectional vs. derivational."}
 ],
 "key": "Same sound, different morphemes: comparative -er (taller) is inflectional; agentive -er (teacher) is derivational."
},
{
 "id": "1.2-04", "skill": "1.2", "type": "knowledge", "difficulty": 1, "diag": 0,
 "stem": "Which of the following words consists only of free morphemes?",
 "options": ["bookcase", "bookings", "rebooked", "booklets"],
 "answer": 0,
 "why": "A free morpheme can stand alone as a word; a bound morpheme cannot. 'Bookcase' is a compound of two free morphemes, book + case. Each of the other words contains bound morphemes: -ing and -s, re- and -ed, and -let and -s.",
 "traps": [
  None,
  {"code": "TERM", "pair": "free ↔ bound", "note": "The -ing and -s in 'bookings' are bound suffixes that can't stand alone, even though book is free."},
  {"code": "TERM", "pair": "free ↔ bound", "note": "The prefix re- and the suffix -ed are bound morphemes; only book is free."},
  {"code": "TERM", "pair": "compound ↔ derivation", "note": "'Booklet' looks like book + let, but -let is a bound diminutive suffix (as in piglet), not the free word let."}
 ],
 "key": "Free morphemes stand alone (book, case); a compound such as bookcase joins two free morphemes."
},
{
 "id": "1.2-05", "skill": "1.2", "type": "application", "difficulty": 1, "diag": 0,
 "stimulus": "Word wall, grade 6 Stand-alone ENL\nbrunch (breakfast + lunch)\nmotel (motor + hotel)\nsmog (smoke + fog)\nSpanglish (Spanish + English)",
 "stem": "All of the words on this word wall were formed by which word-formation process?",
 "options": ["compounding", "clipping", "blending", "back-formation"],
 "answer": 2,
 "why": "Blending fuses parts of two words into one new word, usually the beginning of one and the end of the other: br(eakfast) + (l)unch. Compounding, by contrast, joins two whole words (notebook, classroom). Blends are a quick way to show students that English vocabulary keeps growing through predictable processes.",
 "traps": [
  {"code": "TERM", "pair": "compounding ↔ blending", "note": "Compounding combines whole words (classroom, notebook). These words fuse only parts of each source word."},
  {"code": "TERM", "pair": "clipping ↔ blending", "note": "Clipping shortens a single word (laboratory → lab). Each of these words merges two different source words."},
  None,
  {"code": "TERM", "pair": "back-formation ↔ blending", "note": "Back-formation removes a supposed affix from one word (editor → edit). Nothing was removed from a single word here."}
 ],
 "key": "Blend = parts of two words fused (brunch, smog); compound = two whole words joined (notebook)."
},
{
 "id": "1.2-06", "skill": "1.2", "type": "application", "difficulty": 3, "diag": 0,
 "stimulus": "A grade 11 student asks, “Did 'editor' come from 'edit,' the way 'teacher' came from 'teach'?” The teacher explains that 'editor' actually came first; 'edit' was created later when speakers removed what looked like the suffix -or.",
 "stem": "The teacher is describing which word-formation process?",
 "options": ["back-formation", "clipping", "derivation", "conversion"],
 "answer": 0,
 "why": "Back-formation creates a new word by removing what speakers take to be an affix, usually producing a verb from a noun: editor → edit, babysitter → babysit, donation → donate. Clipping also shortens words, but it keeps the same meaning and part of speech (laboratory → lab). Back-formation produces a different word, typically in a new class.",
 "traps": [
  None,
  {"code": "TERM", "pair": "clipping ↔ back-formation", "note": "Clipping shortens a word without changing its meaning or class (examination → exam). 'Edit' is a new verb formed from the noun editor."},
  {"code": "TERM", "pair": "derivation ↔ back-formation", "note": "Ordinary derivation adds an affix (teach → teacher). Here an apparent affix was taken away, so the process runs in reverse."},
  {"code": "TERM", "pair": "conversion ↔ back-formation", "note": "Conversion changes a word's class with no change in form (a text → to text). 'Edit' is shorter than 'editor.'"}
 ],
 "key": "Back-formation removes a 'suffix' to coin a new word (editor → edit); clipping only shortens the same word (exam)."
},
{
 "id": "1.2-07", "skill": "1.2", "type": "knowledge", "difficulty": 1, "diag": 0,
 "stem": "Which word is correctly paired with the process that formed it?",
 "options": ["laser — blending", "notebook — back-formation", "babysit — acronym", "exam — clipping"],
 "answer": 3,
 "why": "'Exam' is a clipping of 'examination': part of the word is cut off while the meaning and word class stay the same, as in lab, gym, and flu. Laser is an acronym (light amplification by stimulated emission of radiation), notebook is a compound of two free words, and babysit is a back-formation from babysitter.",
 "traps": [
  {"code": "TERM", "pair": "acronym ↔ blend", "note": "'Laser' was built from the first letters of a phrase and is pronounced as a word, which makes it an acronym. A blend fuses parts of two words (smog)."},
  {"code": "TERM", "pair": "compound ↔ back-formation", "note": "'Notebook' joins two free words, note + book, so it's a compound. Nothing was removed."},
  {"code": "TERM", "pair": "back-formation ↔ acronym", "note": "'Babysit' was formed by removing -er from babysitter (back-formation). It isn't built from initial letters."},
  None
 ],
 "key": "Clipping cuts a word but keeps its meaning and class: examination → exam, laboratory → lab."
},
]

# ---- END QUESTIONS ----

import json, pathlib
pathlib.Path(__file__).with_name("c1a.json").write_text(json.dumps({"questions": QUESTIONS, "lessons": LESSONS}, ensure_ascii=False, indent=1))

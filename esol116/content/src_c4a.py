# -*- coding: utf-8 -*-
"""NYSTCE ESOL CST (116) content: Competency 4, part A.

Skills 4.1 (Next Gen ELA & NLAP), 4.2 (oral language), 4.3 (foundational
literacy & L1-L2 transfer), 4.4 (vocabulary). Writes c4a.json next to this file.
"""


def Q(id, typ, diff, stem, opts, ans, why, traps, key, stim=None, diag=0):
    """Build one question dict. traps: list aligned with opts; None for the key,
    (code, note) or (code, pair, note) for each wrong option."""
    tr = []
    for t in traps:
        if t is None:
            tr.append(None)
        elif len(t) == 2:
            tr.append({"code": t[0], "note": t[1]})
        else:
            tr.append({"code": t[0], "pair": t[1], "note": t[2]})
    d = {"id": id, "skill": id.split("-")[0], "type": typ, "difficulty": diff, "diag": diag}
    if stim:
        d["stimulus"] = stim
    d.update(stem=stem, options=opts, answer=ans, why=why, traps=tr, key=key)
    return d


QUESTIONS = []

# ---------------------------------------------------------------- 4.1
QUESTIONS += [
Q("4.1-01", "knowledge", 1,
  stem="Which of the following best describes the purpose of New York State's New Language Arts Progressions (NLAP)?",
  opts=[
    "They provide a separate, simplified set of ELA standards that ELLs work through first and then set aside once they finally reach the Commanding level.",
    "They show, for each grade-level standard, what ELLs can do at each of the five proficiency levels, with scaffolds that decrease as proficiency grows.",
    "They convert a student's NYSESLAT scale score into a recommended independent reading level for selecting classroom texts.",
    "They lay out the order in which ELLs should master English grammar structures before they begin reading grade-level texts.",
  ],
  ans=1,
  why="The NLAP take each grade-level standard and describe how an ELL at Entering, Emerging, Transitioning, Expanding, and Commanding can demonstrate it, in receptive (listening/reading) and productive (speaking/writing) modalities. The standard itself never changes; the amount and type of linguistic scaffolding does, moving from substantial support at Entering to independence at Commanding. That is how NYS keeps ELL instruction rigorous and grade-level.",
  traps=[
    ("LOWER_RIGOR", "There is no separate, simplified ELA standard set for ELLs. The NLAP keep the grade-level standard and change only the supports."),
    None,
    ("TERM", "NLAP ↔ NYSESLAT", "The NYSESLAT measures English proficiency; the NLAP are a planning tool. Neither converts scores into reading levels."),
    ("ISOLATED", "The NLAP integrate language with grade-level content. They do not sequence grammar in isolation or make grade-level texts wait for grammar mastery."),
  ],
  key="NLAP: the same grade-level standard at five proficiency levels, with scaffolds shrinking from Entering (substantial) to Commanding (independent)."),

Q("4.1-02", "scenario", 2, diag=1,
  stim="Unit standard (grade 3 ELA): Describe a character's traits, motivations, or feelings, using details from the text.\nStudent: Marisol | Home language: Spanish | NYSESLAT level: Emerging",
  stem="Marisol is in a grade 3 Integrated ENL/ELA class that is reading a chapter book for this unit. Which support is most consistent with the New Language Arts Progressions for Marisol's level?",
  opts=[
    "Give Marisol an easier picture book on a different topic so that she can practice describing characters using a text that matches her current independent reading level.",
    "Ask Marisol to write an independent paragraph about the character's traits with evidence, then give her detailed feedback on her grammar and spelling.",
    "Have Marisol use pre-taught trait words and sentence starters to complete a partly filled character chart, then discuss it with a partner in English or Spanish.",
    "Have Marisol complete a matching worksheet of common adjectives and their definitions while the rest of the class discusses the character's motivations.",
  ],
  ans=2,
  why="At Emerging, the NLAP have students meet the same grade-level standard with structured supports: pre-taught words and phrases, sentence starters, partially completed graphic organizers, and partner talk, with the home language as a resource. Marisol still describes the grade-level character using text details; the scaffolds carry the language load. Nothing about the thinking is watered down.",
  traps=[
    ("LOWER_RIGOR", "Switching to an easier, unrelated text lowers the content expectation. The NLAP keep the grade-level text and standard and add language scaffolds instead."),
    ("WRONG_LEVEL", "An unsupported paragraph is a Commanding-level expectation, and grammar-focused feedback puts form ahead of the analytical goal."),
    None,
    ("ISOLATED", "Decontextualized adjective matching pulls her out of the grade-level discussion and does not build the language of character analysis in context."),
  ],
  key="For an Emerging ELL, keep the grade-level text and standard; add pre-taught words, sentence starters, partly completed organizers, and partner talk."),

Q("4.1-03", "application", 3,
  stem="An ENL teacher studying the NLAP for a grade 6 reading standard notices that it has both a receptive and a productive progression. Which of the following best explains why a reading standard includes a productive progression?",
  opts=[
    "Students show what they understood from reading by speaking or writing, so the productive progression describes how they can express that understanding at each level.",
    "The productive progression describes how fluently students read the text aloud, while the receptive progression describes how well they read it silently.",
    "The productive progression applies only to Expanding and Commanding students, because Entering and Emerging students are still in a mainly receptive, silent stage of learning.",
    "The productive progression lists the vocabulary and grammar that students must master before they are allowed to begin the receptive reading tasks.",
  ],
  ans=0,
  why="In the NLAP, the receptive modalities are listening and reading, and the productive modalities are speaking and writing. A reading standard is demonstrated when students talk or write about the text (answering questions, citing evidence, summarizing), so the productive progression shows how an ELL at each level can express comprehension. Examples range from labeling a chart with pre-taught words at Entering to writing with starters at higher levels. Both progressions span all five levels.",
  traps=[
    None,
    ("TERM", "productive ↔ oral reading fluency", "Reading aloud is still reading, a receptive skill. 'Productive' in the NLAP means speaking and writing, not oral versus silent reading."),
    ("WRONG_LEVEL", "Every level has a productive progression. Entering students produce language too, such as words, phrases, and labels, with substantial support."),
    ("EXCLUSION", "The progressions are parallel descriptions, not a gate. No list of forms must be mastered before students may engage with the reading."),
  ],
  key="NLAP receptive = listening/reading; productive = speaking/writing. Reading standards have productive progressions because students show comprehension by talking or writing."),

Q("4.1-04", "scenario", 2,
  stem="A grade 5 Integrated ENL/ELA co-teaching team is planning a lesson on comparing how two authors present the same historical event. The ELLs in the class range from Entering to Expanding. Which planning approach best reflects the NLAP?",
  opts=[
    "Give every ELL the identical comparison chart and the identical set of sentence frames so that all students in the class receive equal and consistent support.",
    "Have the Entering students work on a separate phonics unit at the back table while the rest of the class compares the two texts with the co-teacher.",
    "Replace both texts with a single adapted summary written at a grade 2 level so that every ELL in the class can follow the lesson without difficulty.",
    "Keep both texts and the comparison task for everyone, and tier the supports by level, from visuals and home-language partners to frames to a blank organizer.",
  ],
  ans=3,
  why="The NLAP hold the grade-level standard constant across all five levels and vary the linguistic scaffolds. Differentiating supports by proficiency level within the same task keeps the lesson rigorous for everyone. Entering students might use visuals, a bilingual glossary, and a home-language partner; Emerging and Transitioning students might use sentence frames; Expanding students might need only a blank graphic organizer. Identical supports under-serve some students and over-scaffold others.",
  traps=[
    ("ONE_SIZE", "'Equal' support is not equitable. An Expanding student needs far less scaffolding than an Entering student, and the NLAP describe different supports at each level."),
    ("EXCLUSION", "Pulling Entering students into an unrelated phonics unit removes them from grade-level work the NLAP say they can access with substantial support."),
    ("LOWER_RIGOR", "A grade 2 summary lowers the content for every ELL, including students who could handle the grade-level texts with scaffolds."),
    None,
  ],
  key="Same standard, same texts, tiered supports: differentiate the scaffolds by proficiency level instead of changing the task."),

Q("4.1-05", "knowledge", 1,
  stem="A teacher in a Transitional Bilingual Education (TBE) program is planning Spanish language arts instruction aligned to the grade-level standards. Which NYS resource is designed specifically to guide this home-language instruction?",
  opts=[
    "The New Language Arts Progressions (NLAP)",
    "The NYSESLAT scoring rubrics for speaking and writing",
    "The Home Language Arts Progressions (HLAP)",
    "The Culturally Responsive-Sustaining Education Framework",
  ],
  ans=2,
  why="The HLAP parallel the NLAP but describe standards-based language arts development in the home language, so they guide home language arts in TBE and Dual Language programs. The NLAP address English as the new language. Both use the same five proficiency levels and keep the grade-level standard constant.",
  traps=[
    ("TERM", "NLAP ↔ HLAP", "The NLAP describe progress in English, the new language. Home-language arts instruction is guided by the HLAP."),
    ("TERM", "HLAP ↔ NYSESLAT rubrics", "NYSESLAT rubrics score English speaking and writing on the state test. They are not a planning guide for home-language instruction."),
    None,
    ("PARTIAL", "The CR-SE Framework supports culturally responsive teaching in every program, but it is not a standards-based language progression."),
  ],
  key="NLAP = English as a new language; HLAP = home language arts (TBE/Dual Language). Both use the same five levels."),

Q("4.1-06", "analysis", 2,
  stim="Grade 4 ELA standard: Determine a theme of a story and summarize the text.\nColleague's planning notes:\n- Commanding/Expanding: write a theme statement and a summary that cites details.\n- Transitioning: complete a summary frame with key details from the story.\n- Entering/Emerging: copy this week's vocabulary words and draw a picture of each one.",
  stem="An ENL teacher reviews these planning notes. Based on the NLAP, which of the following is the most significant concern?",
  opts=[
    "The Transitioning task should require a complete written summary without a frame, since Transitioning students are close to exiting ELL status.",
    "The Entering/Emerging task is not connected to the standard; those students should also work on theme and summary, with heavier scaffolds.",
    "The notes group Entering and Emerging students together, so the main fix is to split them into two separate vocabulary-copying groups.",
    "The plan should postpone theme work for all ELLs until they have mastered the vocabulary words for the unit and can use them correctly.",
  ],
  ans=1,
  why="Under the NLAP, students at every level, including Entering and Emerging, work toward the same grade-level standard. An Entering student might identify a theme by sorting pre-taught words, phrases, or pictures on a graphic organizer, in English and/or the home language. Copying vocabulary disconnected from theme and summary lowers the expectation. The Transitioning frame and the near-independent Expanding/Commanding task are appropriate.",
  traps=[
    ("WRONG_LEVEL", "Transitioning students still benefit from supports such as summary frames. Exit also requires Commanding, or Expanding plus a qualifying ELA score, so they are not necessarily close to exiting."),
    None,
    ("LITERAL", "Grouping the two levels is a minor detail. Two separate copying tasks would still leave both groups disconnected from the standard."),
    ("EXCLUSION", "Delaying theme work until vocabulary is mastered denies access to grade-level thinking. Vocabulary should be taught within the grade-level task."),
  ],
  key="Every proficiency level works on the same grade-level standard; lower levels get heavier scaffolds, not unrelated tasks."),

Q("4.1-07", "scenario", 2,
  stem="Farid, a grade 7 student who arrived from Afghanistan two months ago, is literate in Dari and placed at the Entering level on the NYSITELL. His ELA class is analyzing how an author develops the central idea of an informational article. Which approach best reflects NYS expectations for Farid's participation?",
  opts=[
    "Excuse Farid from the article until he reaches the Emerging level, and have him work independently in a language-learning app during the ELA period.",
    "Give Farid alphabet and phonics worksheets so that he can build basic English skills before he attempts any grade-level reading.",
    "Give Farid an easier article on a different topic that contains mostly familiar words, so that he can read it independently.",
    "Provide key ideas in Dari, visuals, and pre-taught phrases, and have Farid sort them on an organizer with a partner to identify the central idea.",
  ],
  ans=3,
  why="The NLAP describe Entering students meeting the same standard with substantial support: pre-taught words and phrases, visuals, graphic organizers, and the home language. Farid's Dari literacy is an asset; a home-language summary or bilingual glossary lets him engage with the central idea while he builds English. The Blueprint for ELL/MLL Success calls for rigorous, grade-level instruction for every ELL from the start.",
  traps=[
    ("EXCLUSION", "Waiting for a higher level shuts Farid out of grade-level learning. The NLAP describe how Entering students participate now."),
    ("ISOLATED", "He may need some explicit work on the Latin alphabet, but making grade-level reading wait for basic drills ignores his Dari literacy and the NLAP's scaffolded access."),
    ("LOWER_RIGOR", "An easier, unrelated text lowers the cognitive demand. The goal is scaffolded access to the grade-level article and standard."),
    None,
  ],
  key="Entering ELLs engage the grade-level standard now, with substantial scaffolds and home-language support. Do not wait or simplify."),
]
QUESTIONS += [
Q("4.1-08", "application", 1,
  stem="A student scored at the Emerging level on last spring's NYSESLAT. If she advances one level this year, which proficiency level should her teachers use next when they set her NLAP targets?",
  opts=[
    "Transitioning",
    "Developing",
    "Expanding",
    "Intermediate Fluency",
  ],
  ans=0,
  why="NYS uses five proficiency levels, in this order: Entering, Emerging, Transitioning, Expanding, Commanding. The NLAP and NYSESLAT use the same five levels, so the next target after Emerging is Transitioning. 'Developing' is a WIDA level used in other states, and 'Intermediate Fluency' is a Krashen–Terrell Natural Approach stage.",
  traps=[
    None,
    ("TERM", "NYS levels ↔ WIDA levels", "'Developing' is a WIDA level name used in other states. NYS does not use it."),
    ("NYS_POLICY", "Expanding is two levels above Emerging. The order is Entering, Emerging, Transitioning, Expanding, Commanding."),
    ("TERM", "NYS levels ↔ Natural Approach stages", "'Intermediate Fluency' is a Krashen–Terrell stage of acquisition, not a NYS proficiency level."),
  ],
  key="NYS levels in order: Entering → Emerging → Transitioning → Expanding → Commanding."),

Q("4.1-09", "application", 2, diag=2,
  stim="Grade 4 ELA standard: Compare and contrast the point of view from which different stories are narrated, including the difference between first- and third-person narration.",
  stem="Co-teachers are planning a lesson for this standard. Following the NLAP, they first identify the linguistic demands of the task. Which of the following is the most relevant linguistic demand to plan for?",
  opts=[
    "Spelling the names of the characters and settings correctly in written responses",
    "Using irregular past-tense verbs accurately when retelling the main events of each of the two stories in order",
    "Using compare/contrast language (both, unlike) and pronouns that mark first- vs. third-person narration",
    "Memorizing glossary definitions of literary terms before reading either story",
  ],
  ans=2,
  why="Each NLAP standard lists its linguistic demands: the language functions, forms, and vocabulary the task requires. Comparing and contrasting point of view requires compare/contrast connectors and the pronouns (I/we versus he/she/they) that signal first- versus third-person narration. Identifying these demands tells co-teachers exactly which language to model, practice, and scaffold.",
  traps=[
    ("LITERAL", "Spelling character names is a surface detail with no connection to the thinking or language that this standard demands."),
    ("PARTIAL", "Past-tense accuracy matters for retelling, but retelling is not the task. Comparing points of view hinges on contrast language and narrative pronouns."),
    None,
    ("ISOLATED", "Memorizing definitions out of context does not prepare students to use the language of comparison in discussion and writing."),
  ],
  key="Plan from the standard's linguistic demands: the functions, forms, and vocabulary the task requires (e.g., compare/contrast connectors)."),

Q("4.1-10", "scenario", 3,
  stem="Wen, a grade 8 student whose home language is Mandarin, scored at the Expanding level on the NYSESLAT. In ELA she still receives a word bank, sentence frames for every response, and a fully completed graphic organizer for each essay. Based on the NLAP, which adjustment is most appropriate?",
  opts=[
    "Continue all of Wen's current supports for the rest of the year, since reducing any of them could lower her confidence before she reaches the Commanding level.",
    "Fade the routine supports and keep targeted scaffolds only for newly complex language, such as frames for counterclaims, so she works more independently.",
    "Remove every support at once and treat Wen exactly like her non-ELL classmates, since Expanding students no longer receive ENL services.",
    "Replace the sentence frames with Mandarin translations of every essay prompt and reading assignment so that she can work comfortably.",
  ],
  ans=1,
  why="The NLAP show scaffolding decreasing as proficiency grows. Expanding students work with increasing independence and need targeted support mainly for new, complex language demands. Over-scaffolding (frames for everything, organizers already filled in) limits productive language growth. Expanding students in grades K–8 still receive 180 minutes per week of Integrated ENL, so supports should be reduced and targeted, not eliminated.",
  traps=[
    ("WRONG_LEVEL", "Entering-style supports at Expanding hold Wen back. The NLAP expect increasing independence at this level."),
    None,
    ("NYS_POLICY", "Expanding students are still ELLs and still receive Integrated ENL (180 minutes per week in K–8), so abruptly removing all support is not appropriate."),
    ("PARTIAL", "Her home language remains a valuable resource, but translating everything does not build the independent academic English that the Expanding level targets."),
  ],
  key="As proficiency rises, fade routine scaffolds and target support only at new, complex language demands."),

Q("4.1-11", "knowledge", 1,
  stem="Which statement best reflects how the Next Generation ELA Learning Standards apply to ELLs in New York State?",
  opts=[
    "ELLs are held to the same grade-level standards as all students, and teachers use resources such as the NLAP to plan the scaffolds that give them access.",
    "ELLs follow a separate set of English proficiency standards in place of the Next Generation ELA standards until they exit ELL status.",
    "ELLs at the Entering and Emerging levels are exempt from grade-level ELA standards and focus only on social language until they reach the Transitioning level.",
    "ELLs work on grade-level ELA standards only during Integrated ENL, while Stand-alone ENL time is reserved for grammar drills and pronunciation.",
  ],
  ans=0,
  why="NYS expects every ELL to engage with the grade-level Next Generation standards; the Blueprint for ELL/MLL Success states that instruction is rigorous and grade-level. The NLAP show how students at each proficiency level can meet those standards with appropriate scaffolds. Even Stand-alone ENL is meant to develop the English students need for success in core content, not to run decontextualized drills.",
  traps=[
    None,
    ("NYS_POLICY", "No separate standard set replaces the Next Generation ELA standards for ELLs. The NLAP are built on the grade-level standards themselves."),
    ("EXCLUSION", "No proficiency level is exempt from grade-level standards. Lower levels receive more scaffolding, not a different curriculum."),
    ("ISOLATED", "Stand-alone ENL still develops language for academic content. Reducing it to drills contradicts NYS's integrated, standards-based approach."),
  ],
  key="All ELLs work toward the same Next Gen grade-level standards; the NLAP show the scaffolds for each level."),

Q("4.1-12", "scenario", 3,
  stim="Teacher observation notes (Pablo, grade 6, home language Spanish)\n- Follows grade-level read-alouds and class discussions; answers comprehension questions orally with light support\n- Writing sample: 'The boy is sad. He lose the dog. He look the dog in the park.'",
  stem="How should Pablo's ELA teacher use the NLAP to plan for him?",
  opts=[
    "Plan all of Pablo's tasks from the progression for his overall NYSESLAT level, because the NLAP assign one proficiency level to each student.",
    "Hold Pablo's listening and reading tasks to lower expectations until his writing catches up, so that his targets are consistent across modalities.",
    "Refer Pablo for a learning-disability evaluation, because the gap between his comprehension and his writing suggests a processing problem.",
    "Use higher-level indicators for his receptive tasks and lower-level indicators, with more scaffolding, for his productive writing tasks.",
  ],
  ans=3,
  why="Proficiency is rarely even across modalities; receptive skills (listening, reading) often develop ahead of productive skills (speaking, writing). Because the NLAP describe receptive and productive progressions separately, a teacher can set a higher target with lighter scaffolds for Pablo's comprehension and give his writing more structure (models, frames, organizers). Using one level for everything would under-challenge one modality and under-support the other.",
  traps=[
    ("ONE_SIZE", "An overall level is a starting point, but planning every task from it ignores the clear difference between Pablo's receptive and productive skills."),
    ("LOWER_RIGOR", "Holding back his stronger comprehension to match his writing lowers expectations where he is ready for more."),
    ("MISREFERRAL", "Receptive skills that outpace productive skills are a typical second-language pattern, not evidence of a disability."),
    None,
  ],
  key="Receptive skills often run ahead of productive skills; set NLAP targets separately for each modality."),

Q("4.1-13", "scenario", 2,
  stem="Paw Htoo, a grade 2 student whose home language is Karen, is at the Entering level. His class is writing informative texts about animals that name a topic, supply some facts, and provide a closing. Which task is most consistent with the NLAP for Paw Htoo?",
  opts=[
    "Copy the teacher's model paragraph about frogs into his notebook to practice letter formation and spacing.",
    "Label a picture of the animal with pre-taught words and complete cloze sentences ('A frog can ___.') from a word bank, talking through ideas first.",
    "Write a complete informative paragraph on his own, since writing in a new language develops fastest through lots of independent practice and correction.",
    "Draw a picture of his favorite animal while the class writes, and join the writing unit once he reaches the Emerging level.",
  ],
  ans=1,
  why="At Entering, NLAP indicators typically involve labeling, using pre-taught words and phrases, word banks, cloze sentences, and visuals, with home-language support where possible. Paw Htoo is still producing informative writing about the grade-level topic, naming the animal and supplying facts, but the scaffolds make it possible. Copying a model is passive, and an independent paragraph is far beyond his current level.",
  traps=[
    ("PASSIVE", "Copying a model involves no composing or language choices, so it does not address the informative-writing standard."),
    None,
    ("WRONG_LEVEL", "Independent paragraph writing matches the Commanding level. An Entering student needs substantial scaffolds to produce informative text."),
    ("EXCLUSION", "Postponing participation until a higher level shuts him out of grade-level writing that he can do now with support."),
  ],
  key="Entering writers meet the standard through labels, word banks, cloze sentences, and visuals, not copying and not unsupported paragraphs."),

Q("4.1-14", "application", 3,
  stem="An ENL teacher wants to track whether her Transitioning grade 3 students are progressing on a speaking-and-listening standard about asking and answering questions during discussions. Which use of the NLAP is most appropriate?",
  opts=[
    "Use the Commanding-level indicator as the checklist for every student, so that all students are measured against the same high bar.",
    "Have students check off which question words (who, what, where, why) they used after each discussion, and track their weekly totals.",
    "Turn the Transitioning and Expanding indicators for that standard into an observation checklist, and note when students show next-level behaviors.",
    "Wait for the spring NYSESLAT results, since progress on the progressions can be measured reliably only by the state's annual English proficiency test.",
  ],
  ans=2,
  why="Because the NLAP spell out what students at each level can do for a specific standard, teachers can use the indicators as formative success criteria. The teacher observes whether a Transitioning student is beginning to show the next level's (Expanding) behaviors. This gives ongoing, standard-specific evidence that drives instruction, which an annual test or a count of question words cannot provide.",
  traps=[
    ("ONE_SIZE", "One Commanding-level bar for everyone hides real progress and ignores the level-specific descriptions the NLAP provide."),
    ("PARTIAL", "Self-assessment is valuable, but counting question words captures a narrow form, not whether students ask and answer relevant questions as the standard requires."),
    None,
    ("ASSESS_INVALID", "The NYSESLAT is an annual summative measure of overall proficiency. It cannot provide ongoing, standard-specific formative evidence."),
  ],
  key="NLAP indicators make good formative success criteria: observe whether students show the next level's behaviors on a given standard."),
]

# ---------------------------------------------------------------- 4.2
QUESTIONS += [
Q("4.2-01", "scenario", 2, diag=1,
  stim="Partner talk, grade 4 Integrated ENL/ELA\nTeacher prompt: Which character made the better choice, Lily or her brother? Why?\nAhmed (Emerging): I like Lily.\nPartner: Why?\nAhmed: Lily... good. Is good.",
  stem="Ahmed, whose home language is Arabic, has clear ideas about the story but struggles to express them. Based on the exchange, which of the following would best help Ahmed participate more fully in the next partner discussion?",
  opts=[
    "Let Ahmed mainly listen to his partner's ideas for now, since he will absorb the language over time and begin to speak up when he is ready.",
    "Correct each of Ahmed's incomplete sentences as soon as he says them, so that he hears and learns the correct English forms right away.",
    "Model the task, give Ahmed opinion-and-reason frames ('I think ___ made a better choice because ___'), and let him rehearse before talking.",
    "Have Ahmed complete a worksheet on character-trait adjectives at his seat instead of joining the partner discussion with his classmates.",
  ],
  ans=2,
  why="Ahmed has an opinion but lacks the language to state and justify it. Sentence frames matched to the language function (stating an opinion and giving a reason), plus modeling and a chance to rehearse, give him the structure to produce extended academic talk while he thinks about the text. This builds output and interaction rather than waiting for language to emerge or drilling words in isolation.",
  traps=[
    ("PASSIVE", "Ahmed is past the silent period and already trying to speak. Just listening gives him no structure for producing an opinion with a reason."),
    ("OVERCORRECT", "Correcting every utterance focuses on form over meaning and raises anxiety. It also doesn't give him the language he needs to justify an opinion."),
    None,
    ("ISOLATED", "An isolated adjective worksheet removes him from the interaction and does not teach the language of opinion and justification."),
  ],
  key="Match sentence frames to the language function (e.g., opinion + reason), model them, and let students rehearse before discussion."),

Q("4.2-02", "application", 2,
  stem="During a novel discussion, a teacher asks, 'Who can add on to what Yuki just said?' and later, 'Carlos, can you put Omar's idea in your own words?' These talk moves most directly promote which dimension of Accountable Talk?",
  opts=[
    "Accountability to the learning community",
    "Accountability to accurate knowledge",
    "Accountability to rigorous thinking",
    "Accountability to standard English conventions",
  ],
  ans=0,
  why="Accountable Talk (Resnick and colleagues) has three dimensions: accountability to the learning community (listening to and building on others' ideas), to accurate knowledge (getting facts and evidence right), and to rigorous thinking (reasoning logically). Adding on and restating a peer's idea require students to listen closely to classmates and engage with their thinking, which is the learning-community dimension. For ELLs, these moves also provide repeated, meaningful exposure to peers' language.",
  traps=[
    None,
    ("TERM", "learning community ↔ accurate knowledge", "Accountability to knowledge concerns factual accuracy and evidence. These moves focus on attending to peers' ideas."),
    ("TERM", "learning community ↔ rigorous thinking", "Accountability to rigorous thinking concerns logical reasoning and justification. Restating and adding on are about engaging with classmates."),
    ("OVERCORRECT", "Accountable Talk is about ideas and reasoning, not grammatical correctness. Treating it as a correctness standard confuses form with meaning."),
  ],
  key="Accountable Talk: to the learning community (build on peers), to accurate knowledge (evidence), to rigorous thinking (reasoning)."),

Q("4.2-03", "application", 1,
  stem="An ENL teacher wants a speaking activity that maximizes negotiation of meaning (clarification requests, comprehension checks, and confirmation checks) between partners. Which activity best meets this goal?",
  opts=[
    "Students repeat a model dialogue chorally after the teacher until they can say it smoothly and with correct intonation.",
    "The teacher asks the class questions about a picture and calls on volunteers to answer them in complete sentences.",
    "Partners write a short dialogue together and then take turns reading their finished script aloud to the class.",
    "Partners each hold half of the information about a map and must ask and answer questions to complete it.",
  ],
  ans=3,
  why="In an information-gap task, each partner has information the other needs, so they must communicate to finish. That genuine need drives negotiation of meaning, which Long's Interaction Hypothesis identifies as a key route to comprehensible input and acquisition. Choral repetition, whole-class Q&A, and reading a script aloud involve little or no negotiation.",
  traps=[
    ("ISOLATED", "Choral repetition is controlled practice with no communicative need, so nothing is negotiated."),
    ("PASSIVE", "Teacher-led questioning lets only a few volunteers speak, and they answer the teacher rather than negotiating meaning with a partner."),
    ("PARTIAL", "Co-writing involves some interaction, but reading a finished script aloud has no information gap and requires no clarification."),
    None,
  ],
  key="Information-gap tasks create a real need to communicate, which drives negotiation of meaning (Long's Interaction Hypothesis)."),

Q("4.2-04", "analysis", 2,
  stim="Grade 6 partner discussion (both students Transitioning)\nPrompt: Was the narrator's decision to leave home a good one?\nLuis: Yes.\nAmira: Yes, me too.\nLuis: OK.\nAmira: OK. We're done.",
  stem="Based on the transcript, which instructional step would most improve these students' academic conversations?",
  opts=[
    "Give the pair a longer block of discussion time so that they have more opportunities to talk with each other about the prompt.",
    "Model a conversation in a fishbowl and explicitly teach skills such as elaborating, supporting ideas with evidence, and building on a partner's idea.",
    "Have the students write individual answers to the prompt instead, since they are not yet ready to sustain an academic discussion with a partner on their own.",
    "Give the pair a participation grade for each discussion so that they understand the task is important and take it more seriously next time.",
  ],
  ans=1,
  why="The students agree but never explain, elaborate, or use evidence. What's missing is conversation skill, not time or motivation. Modeling (for example, in a fishbowl) and explicitly teaching moves such as elaborating and clarifying, supporting ideas with examples, and building on or challenging a partner's idea gives Transitioning students the tools for real academic conversation. Prompt cards such as 'Can you say more about…?' and 'What in the text makes you think so?' support this.",
  traps=[
    ("PARTIAL", "Time helps only if students know how to extend a conversation. This pair finished early because the skills are missing."),
    None,
    ("EXCLUSION", "Transitioning students can hold academic discussions with instruction and support. Replacing talk with writing removes the practice they need."),
    ("ASSESS_INVALID", "A participation grade rewards compliance but neither teaches nor measures the missing conversation skills."),
  ],
  key="Shallow partner talk signals missing conversation skills; model and explicitly teach moves like elaborating and supporting with evidence."),

Q("4.2-05", "scenario", 2,
  stem="Jun, a grade 7 Expanding student whose home language is Mandarin, often drops final consonants and simplifies final clusters (saying 'pass' for 'passed' and 'ol' for 'old'), which sometimes makes his oral presentations hard to follow. Which approach to pronunciation is most effective?",
  opts=[
    "Practice final consonants in phrases from his upcoming presentation, with modeling, recording, and self-monitoring of the sounds that most affect meaning.",
    "Interrupt Jun during each presentation to correct every dropped sound, so that he hears the correct form at the moment he makes the error.",
    "Have Jun complete several weeks of minimal-pair drills in isolation before he is asked to give any more oral presentations to the class.",
    "Set the goal of eliminating Jun's accent entirely by the end of the year so that classmates and teachers can no longer tell that English is not his first language.",
  ],
  ans=0,
  why="Pronunciation instruction for ELLs targets intelligibility, not accent elimination. Mandarin syllables can end in only a few consonants (mainly /n/ and /ŋ/), so English final consonants and clusters, including past-tense -ed, are a predictable transfer challenge. Practicing those sounds in meaningful phrases Jun actually needs, with modeling and self-monitoring (such as recording himself), connects pronunciation to real communication.",
  traps=[
    None,
    ("OVERCORRECT", "Interrupting a presentation to fix every sound raises anxiety and disrupts communication. Feedback is better given in focused practice."),
    ("ISOLATED", "Weeks of decontextualized drills delay real speaking and transfer poorly to connected speech."),
    ("DEFICIT", "Treating an accent as something to erase is a deficit view. Intelligibility, not a native-like accent, is the appropriate goal."),
  ],
  key="Teach pronunciation in meaningful context, aiming for intelligibility rather than accent elimination; target features that affect meaning."),

Q("4.2-06", "knowledge", 3,
  stem="An ENL teacher wants to help Transitioning high school students be more comprehensible when they present research to the class. Research on pronunciation teaching suggests which focus is likely to have the greatest effect on overall comprehensibility?",
  opts=[
    "Perfecting individual sounds that do not exist in each student's home language, such as /θ/ in 'think' and 'theory'",
    "Reducing each student's accent until it is no longer noticeable to listeners who are native speakers of English",
    "Suprasegmental features such as word stress, sentence stress, rhythm, and pausing between thought groups",
    "Reading the presentation aloud slowly from a script so that every single word is pronounced clearly and separately",
  ],
  ans=2,
  why="Comprehensibility depends heavily on suprasegmentals: stress, rhythm, intonation, and grouping words into thought groups. Misplaced word stress (saying DEvelopment instead of deVELopment) or a lack of pausing can derail a listener more than an imperfect /θ/. Studies such as Derwing, Munro, and Wiebe's found that instruction emphasizing prosody improved learners' comprehensibility in spontaneous speech more than work on individual sounds. Intelligibility, not accent elimination, is the appropriate goal.",
  traps=[
    ("PARTIAL", "Some individual sounds matter, but /θ/ rarely causes breakdowns. Sound-by-sound work usually does less for overall comprehensibility than stress and rhythm."),
    ("DEFICIT", "Accent elimination is neither realistic nor necessary. It frames the student's L1 as a problem instead of targeting intelligibility."),
    None,
    ("ISOLATED", "Word-by-word reading destroys natural stress, rhythm, and thought groups, which makes speech harder rather than easier to follow."),
  ],
  key="For comprehensibility, prioritize suprasegmentals (stress, rhythm, intonation, thought groups) over isolated sounds."),

Q("4.2-07", "scenario", 2, diag=2,
  stem="A grade 7 ENL teacher plans to use a four-minute podcast about a teen inventor with a group of Emerging students. Which plan best supports their listening comprehension?",
  opts=[
    "Play the podcast once without interruption, then give a short quiz to find out how much each student understood independently.",
    "Preview key words with visuals and set a focus question; play it twice (for gist, then details with an organizer); end with partner talk.",
    "Give the students the transcript to read silently instead of listening, since reading is usually easier for them than processing spoken English in real time.",
    "Pre-teach every unfamiliar word in the podcast from a list of written definitions so that no word will be new when students listen.",
  ],
  ans=1,
  why="Effective listening instruction follows a pre-, during-, and post-listening sequence. Pre-listening (background knowledge, key vocabulary, a purpose) lowers the processing load. Multiple listenings with a specific task let students move from gist to detail. Post-listening talk consolidates meaning. Teaching listening this way is different from simply testing it after one exposure.",
  traps=[
    ("PASSIVE", "One unsupported listening followed by a quiz tests listening rather than teaching it, and Emerging students get no scaffolds or interaction."),
    None,
    ("PARTIAL", "A transcript can be a useful support during a second listening, but replacing listening with reading removes the listening practice itself."),
    ("ISOLATED", "Pre-teaching every word from a definition list overloads students and teaches words apart from the context in which they'll hear them."),
  ],
  key="Teach listening in stages: pre-listening (vocabulary, purpose), multiple purposeful listenings (gist, then detail), and post-listening talk."),
]
QUESTIONS += [
Q("4.2-08", "application", 1,
  stem="During an interactive read-aloud of a grade 2 picture book, which teacher move would best invite participation from a student at the Entering level while keeping her engaged with the story?",
  opts=[
    "Ask her, 'Why do you think the author chose to end the story this way?' and wait for her to explain her thinking.",
    "Skip her during questioning until she begins to speak on her own, so that she is not embarrassed in front of classmates.",
    "Ask her to spell aloud one of the key words from the story so that she can practice letter names along with the class.",
    "Point to an illustration and ask, 'Is the bear happy or sad?', accepting a gesture, one word, or her home language.",
  ],
  ans=3,
  why="Entering students can show comprehension through gestures, pointing, yes/no and either/or questions, and one-word answers. An either/or question tied to an illustration lets her take part in thinking about the character while hearing the target words ('happy,' 'sad') modeled in the question itself. Open-ended 'why' questions demand language she doesn't yet have, and skipping her denies her participation.",
  traps=[
    ("WRONG_LEVEL", "An open-ended inference question about author's craft requires extended language beyond the Entering level. It suits Expanding or Commanding students."),
    ("EXCLUSION", "Skipping her removes her from the discussion. Entering students should be invited to participate through low-risk response options."),
    ("ISOLATED", "Spelling a word aloud is unrelated to comprehending the story and does not build oral language around meaning."),
    None,
  ],
  key="Entering students: either/or and yes/no questions with visuals; accept gestures, single words, and home-language responses."),

Q("4.2-09", "scenario", 1,
  stem="Pema, a grade 1 newcomer whose home language is Nepali, has been in school for three weeks. She follows classroom routines and watches her classmates closely but has not yet spoken English in class. Which response by the teacher is most appropriate?",
  opts=[
    "Give rich, comprehensible input and let Pema respond nonverbally (pointing, gestures, drawing), while inviting but not forcing speech in songs and chants.",
    "Refer Pema for a speech-language evaluation, since a child her age would normally be speaking in class after three full weeks in a new school setting.",
    "Require Pema to say one complete English sentence to the class each morning so that she becomes comfortable speaking in front of others.",
    "Seat Pema at a separate table with picture books until she starts speaking, so that she does not feel pressured by group activities.",
  ],
  ans=0,
  why="Many newcomers go through a silent (preproduction) period, building receptive language before they speak. Krashen and Terrell's Natural Approach recommends rich comprehensible input and low-anxiety, nonverbal ways to respond, such as TPR, pointing, and drawing; choral songs and chants offer safe first chances to speak. A three-week silent period is typical second-language behavior, not a sign of a disability.",
  traps=[
    None,
    ("MISREFERRAL", "A silent period in the first weeks of learning a new language is normal and expected; it is not evidence of a speech or language disorder."),
    ("WRONG_LEVEL", "Forcing public speech during the silent period raises the affective filter and mismatches her preproduction stage."),
    ("EXCLUSION", "Isolating her removes the interaction and input she needs. She can participate nonverbally within the group."),
  ],
  key="During the silent period, give comprehensible input and nonverbal response options; invite but don't force speech, and don't refer."),

Q("4.2-10", "analysis", 2,
  stim="Grade 5 ELA, discussing a story's conflict\nTeacher: What caused the problem between the two friends?\nDaniela (Transitioning): Because the girl, she got mad cuz the other girl took her stuff and didn't say nothing.",
  stem="Which teacher response best builds Daniela's academic oral language while keeping the discussion moving?",
  opts=[
    "'Remember, we don't use double negatives in school. Please say your whole sentence again, and this time say it correctly.'",
    "'Great job, Daniela! Who else would like to share an idea about what happened between the two friends?'",
    "'Let's write the correct version of that sentence on the board so that everyone can copy it into their notebooks.'",
    "'So the conflict began when one girl took her friend's belongings without asking. Can you say more, using conflict?'",
  ],
  ans=3,
  why="Revoicing restates the student's idea in academic register ('conflict,' 'belongings,' 'without asking') without making her wrong. It models the target language and checks meaning, and the invitation to say more using the key word pushes her output. Meaning stays first while she moves from everyday to academic language. Stopping to correct the double negative shifts the focus to form and can shut down participation.",
  traps=[
    ("OVERCORRECT", "Correcting the double negative mid-discussion puts form over meaning and may discourage her from contributing again."),
    ("PARTIAL", "Praise supports participation, but the teacher misses the chance to model and elicit the academic language of the discussion."),
    ("PASSIVE", "Copying a corrected sentence turns a discussion into a transcription task with no further output from Daniela."),
    None,
  ],
  key="Revoice students' ideas in academic register, then invite them to extend using the new language. Keep meaning first."),

Q("4.2-11", "knowledge", 1,
  stem="Which statement best describes the appropriate role of sentence frames in developing ELLs' academic oral language?",
  opts=[
    "They should be required in every response at every proficiency level so that students always speak in complete, grammatically correct sentences.",
    "They are mainly a grammar tool and should be used during separate grammar lessons rather than during content discussions.",
    "They provide temporary structure for a language function, such as comparing or justifying, and are faded as students gain independence.",
    "They work best when the teacher reads them aloud and students listen carefully to them as models of correct academic speech.",
  ],
  ans=2,
  why="Sentence frames (for example, 'One similarity between ___ and ___ is ___') supply the academic structure for a specific language function so students can focus on ideas. Like any scaffold, they should match the student's level and be gradually removed: fuller frames for Entering and Emerging students, open starters or none for Expanding and Commanding students. Their value comes from students using them in real discussion.",
  traps=[
    ("ONE_SIZE", "Frames for everyone at every level over-scaffold advanced students and ignore the goal of fading supports."),
    ("ISOLATED", "Frames are meant to support language in content discussions, not to be practiced in separate grammar lessons."),
    None,
    ("PASSIVE", "Frames help only when students use them to produce their own ideas. Listening to the teacher read them provides no output."),
  ],
  key="Sentence frames are temporary, function-specific scaffolds for students' own talk; tier them by level and fade them."),

Q("4.2-12", "scenario", 3,
  stem="A grade 10 ELA teacher is preparing a Socratic seminar on a short story. The class includes several Transitioning ELLs who have strong ideas but rarely speak in whole-class discussions. Which plan would most effectively support their meaningful participation?",
  opts=[
    "Assign the ELLs the role of official note-taker for the seminar so that they can still take part in the discussion without the pressure of speaking aloud.",
    "Have students rehearse ideas and evidence with a partner (in English or a shared home language) and give frames for adding on and challenging.",
    "Call on the ELLs first when the seminar begins, so that they get to speak before the discussion becomes too fast for them to follow.",
    "Revise the seminar questions into literal recall questions so that the ELLs can answer them quickly and confidently in front of the class.",
  ],
  ans=1,
  why="Students who hesitate in fast whole-class talk benefit from oral rehearsal. Practicing ideas with a partner first, where translanguaging is a legitimate tool, lowers anxiety and builds the language they will need. Frames for academic moves (agreeing, adding on, challenging) give them confident entry points. This raises participation without lowering the intellectual demand or sidelining them.",
  traps=[
    ("EXCLUSION", "A note-taker role keeps the ELLs out of the speaking and reasoning that the seminar is designed to develop."),
    None,
    ("PARTIAL", "An early turn can help, but calling on unprepared students puts them on the spot. Without rehearsal and frames, it can raise anxiety."),
    ("LOWER_RIGOR", "Literal recall questions lower the cognitive demand. Transitioning students can handle interpretive questions with scaffolds."),
  ],
  key="Before whole-class discussion, let ELLs rehearse with a partner (home language welcome) and give frames for academic talk moves."),

Q("4.2-13", "application", 3,
  stem="Before Emerging students write an opinion paragraph, their teacher has them explain their opinion and reasons to two different partners, using sentence frames and refining what they say each time. Which principle best explains why this is effective?",
  opts=[
    "Talking with partners mainly increases students' motivation, which matters more than language practice for students at this level.",
    "Speaking is easier than writing, so the oral version of the task can replace the written paragraph for students at the Emerging level.",
    "Repeating the same sentences several times helps students memorize correct forms through habit formation and positive reinforcement.",
    "Oral rehearsal lets students try out and refine the ideas and language they will need, so that speaking serves as a bridge to writing.",
  ],
  ans=3,
  why="Oral language is the foundation for writing. Saying ideas aloud, hearing a partner's version, and sharpening the explanation each time (Zwiers calls a version of this 'Stronger and Clearer Each Time') builds the vocabulary, sentence structures, and organization students then put on paper. Swain's Output Hypothesis also applies: producing language pushes learners to notice gaps and try new forms. The written task stays; talk prepares students for it.",
  traps=[
    ("PARTIAL", "Motivation may rise, but the main benefit is linguistic: rehearsing and refining the language and ideas needed for writing."),
    ("LOWER_RIGOR", "The talk prepares students for writing; it does not replace it. Emerging students can write an opinion paragraph with scaffolds."),
    ("MISAPPLIED_THEORY", "Habit formation through repetition is behaviorism (the Audiolingual Method). Here students revise and extend meaning with each partner instead of repeating a drill."),
    None,
  ],
  key="Talk before writing: oral rehearsal builds the language and ideas students then put on paper (output pushes noticing)."),

Q("4.2-14", "analysis", 3,
  stim="Grade 3 ELA, whole-class discussion\nTeacher: What is the setting of the story?\nStudent 1: A farm.\nTeacher: Good. Who is the main character?\nStudent 2: Rosa.\nTeacher: Right. What problem does she have?\nStudent 3: Her horse.\nTeacher: Yes, her horse ran away. Good.",
  stem="An ENL coach observes this exchange in a class with many ELLs. Which recommendation would most increase the ELLs' academic language use?",
  opts=[
    "Follow up with open-ended prompts and wait time ('Why do you think Rosa…? Say more.'), and have partners turn and talk before sharing.",
    "Ask more questions in the same format, calling on the ELLs more often so that each one gets several turns to answer during the lesson.",
    "Require students to answer in complete sentences that repeat the wording of the teacher's question, such as 'The setting of the story is…'",
    "Praise each correct answer more specifically, such as 'Good job naming the setting,' so that students know exactly what they did well.",
  ],
  ans=0,
  why="The exchange follows the Initiate–Response–Evaluate (IRE) pattern: the teacher asks known-answer questions, students give one-word replies, and the teacher closes each turn. IRE limits student talk to a few words. Open-ended questions, wait time, follow-up moves ('Say more,' 'Why do you think so?'), and turn-and-talk structures give every ELL extended practice producing academic language.",
  traps=[
    None,
    ("PARTIAL", "More turns in the same IRE pattern still yield one-word answers. The structure of the talk, not the number of turns, is the problem."),
    ("OVERCORRECT", "Complete-sentence rules emphasize form over thinking. Students would still be restating recall facts, not extending ideas."),
    ("LITERAL", "This focuses on the wording of the teacher's feedback and misses the real issue: the question pattern that limits student talk."),
  ],
  key="Break the IRE pattern with open questions, wait time, follow-up prompts, and turn-and-talk to extend ELLs' academic talk."),
]

# ---------------------------------------------------------------- 4.3
QUESTIONS += [
Q("4.3-01", "scenario", 2, diag=1,
  stim="Word-reading check, grade 1 (Mateo, home language Spanish)\nTarget word | Mateo read\nship | 'sheep'\nbit | 'beat'\npen | 'pen'\ncap | 'cop'\nhut | 'hot'",
  stem="Based on Mateo's reading, which instructional response is most appropriate?",
  opts=[
    "Refer Mateo for a speech-language evaluation, since he is unable to produce several of the basic vowel sounds that English requires.",
    "Postpone phonics instruction until Mateo's oral English is fluent enough for him to hear the vowel differences on his own.",
    "Have Mateo practice flashcards of nonsense words for each short vowel every day until he can read all of them quickly and accurately on his own.",
    "Teach the short-vowel contrasts explicitly with picture minimal pairs (ship/sheep), mouth-position cues, and sorts, then apply them in text.",
  ],
  ans=3,
  why="Spanish has five vowel phonemes; English has many more, including short (lax) vowels such as /ɪ/, /æ/, and /ʌ/ that Spanish lacks. Mateo is mapping these English vowels onto the nearest Spanish vowels, which is predictable cross-linguistic transfer, not a disorder. Explicit, contrastive instruction with meaningful picture words, articulation cues, and word sorts, followed by reading in connected text, helps him hear and produce the distinctions.",
  traps=[
    ("MISREFERRAL", "Substituting the closest home-language vowel is a typical transfer pattern for Spanish speakers, not evidence of a speech disorder."),
    ("EXCLUSION", "Delaying phonics withholds instruction he needs now. Explicit contrast work is how he will learn to hear the differences."),
    ("ISOLATED", "Nonsense-word flashcards drill speed without meaning or contrast. He needs to hear and see the vowel pairs side by side in real words."),
    None,
  ],
  key="Spanish has 5 vowels; teach the English short-vowel contrasts explicitly with minimal pairs, pictures, articulation cues, and connected text."),

Q("4.3-02", "analysis", 2,
  stim="Journal entry, grade 2 (Valeria, literate in Spanish)\n'Mai bes dei. Ai laik tu plei wit mai frend. Wi jav fan in di park.'",
  stem="Valeria's spellings most likely indicate that she",
  opts=[
    "has a visual-processing difficulty that causes her to confuse and reverse letters, and she should be referred for a formal evaluation",
    "is applying Spanish letter-sound correspondences to English, showing she can segment sounds and use the alphabetic principle",
    "has not yet developed phonological awareness and is guessing at the letters in each word based on their shapes",
    "has fossilized errors in her interlanguage that will be very difficult to change through classroom instruction",
  ],
  ans=1,
  why="Valeria's spellings are systematic: 'ai' for /aɪ/ (mai, laik), 'ei' for /eɪ/ (dei, plei), 'j' for /h/ (jav), and 'i' for /i/ (wi, di) are all regular Spanish spellings. She hears each sound and represents it with the Spanish grapheme she knows, which is strong evidence of phonemic awareness and alphabetic knowledge transferred from Spanish. The next step is explicit instruction in the English spellings for these sounds, contrasted with Spanish.",
  traps=[
    ("MISREFERRAL", "The spellings follow consistent Spanish patterns, so this is logical transfer, not a perceptual disability."),
    None,
    ("LITERAL", "Every sound in every word is represented in order. That reflects strong phonological awareness, not guessing."),
    ("TERM", "transfer ↔ fossilization", "Fossilization describes persistent errors that stop responding to input over time. A second grader's Spanish-based spellings are developmental transfer that responds well to instruction."),
  ],
  key="Systematic Spanish-based invented spellings show phonemic awareness and alphabetic knowledge that transferred; teach English spellings by contrast."),

Q("4.3-03", "application", 1,
  stem="A kindergarten ENL teacher says the word 'ship,' and students push a chip into a box for each sound they hear: /ʃ/ /ɪ/ /p/. No letters are used. Which skill are the students practicing?",
  opts=[
    "Phonics",
    "Morphological awareness",
    "Phonemic awareness",
    "Reading fluency",
  ],
  ans=2,
  why="Phonemic awareness is the ability to hear and manipulate the individual phonemes in spoken words. It is an oral skill, with no print involved. Segmenting 'ship' into three sounds (even though it has four letters) with Elkonin boxes is a classic phonemic-awareness task. Phonics connects those sounds to letters; it begins when letters replace the chips.",
  traps=[
    ("TERM", "phonemic awareness ↔ phonics", "Phonics links sounds to letters in print. This task is purely oral, with chips standing for sounds."),
    ("TERM", "phonemic awareness ↔ morphological awareness", "Morphological awareness concerns meaningful word parts (prefixes, roots, suffixes), not individual sounds."),
    None,
    ("TERM", "phonemic awareness ↔ fluency", "Fluency is accurate, appropriately paced, expressive reading of connected text. No text is being read here."),
  ],
  key="Phonemic awareness is oral manipulation of individual sounds (no print); phonics maps those sounds to letters."),

Q("4.3-04", "scenario", 2,
  stem="Yousef, a grade 5 newcomer, was reading and writing on grade level in Arabic before moving to New York. Which aspect of English literacy will most likely require explicit instruction rather than transferring from his Arabic literacy?",
  opts=[
    "Writing from left to right and representing vowel sounds with letters in every word",
    "Understanding that written symbols represent the sounds of the spoken language",
    "Using strategies such as predicting, rereading, and summarizing to understand a text",
    "Recognizing that texts are organized differently for purposes such as telling stories or reporting facts",
  ],
  ans=0,
  why="Arabic is written right to left in a consonant-based script (an abjad) in which short vowels are usually left unwritten. Directionality and consistent vowel spelling are therefore new, and Arabic-literate learners often omit vowels when spelling English words. By contrast, Yousef's understanding that print represents speech, his comprehension strategies, and his knowledge of text purposes belong to the common underlying proficiency (Cummins) and transfer to English.",
  traps=[
    None,
    ("MISAPPLIED_THEORY", "Arabic is also written with letters that stand for sounds, so the basic alphabetic insight transfers. Re-teaching it ignores Cummins's common underlying proficiency."),
    ("DEFICIT", "Treating a literate student's comprehension strategies as absent undervalues his Arabic literacy. These strategies transfer and should be activated."),
    ("PARTIAL", "Some English genre conventions may need attention, but the core understanding that texts serve different purposes already exists in Arabic and transfers."),
  ],
  key="Arabic literacy transfers concepts and strategies; teach explicitly what differs: left-to-right directionality and written vowels."),

Q("4.3-05", "application", 3,
  stem="Mei, a grade 4 student from mainland China, reads and writes Chinese at grade level and learned Pinyin in school. Which statement best describes what her teacher can expect as Mei learns to read English?",
  opts=[
    "Little will transfer, because Chinese characters are so different from English letters that Mei must learn to read as if for the first time.",
    "Her comprehension strategies and familiarity with Latin letters will help, but she will need explicit teaching of English phoneme-letter mapping.",
    "She will decode English easily, because Pinyin uses the same letters as English and assigns each of them the same sound values as English spelling.",
    "She should learn English words as whole visual shapes, because memorizing whole words matches the way she originally learned to read Chinese.",
  ],
  ans=1,
  why="Chinese characters mainly represent morphemes and syllables rather than individual phonemes, so the English alphabetic code, especially phoneme-level letter-sound mapping, needs explicit teaching. Mei still brings a great deal: she knows how reading works, has comprehension strategies, and recognizes Latin letters from Pinyin. Some Pinyin letters, however, stand for different sounds than in English (x, q, and c, for example). Whole-word memorization alone would not give her the decoding tools English requires.",
  traps=[
    ("DEFICIT", "Grade-level Chinese literacy is a major asset. Concepts about reading, comprehension strategies, and study skills transfer even across very different scripts."),
    None,
    ("LITERAL", "Pinyin shares the letters but not all the sound values (Pinyin x, q, and c differ from English), and English spelling is far less regular."),
    ("MISAPPLIED_THEORY", "Matching instruction to her L1 script misreads transfer theory. English requires phonological decoding, which she must be taught explicitly."),
  ],
  key="Logographic L1 readers bring strong literacy concepts but need explicit instruction in English phoneme-grapheme correspondences."),

Q("4.3-06", "analysis", 2,
  stim="Grade 3 reading data (Andrés, home language Spanish, Transitioning)\nMeasure | Result\nWords correct per minute (grade-level passage) | At the grade-level benchmark\nAccuracy | 97%\nOral retell | Names two characters; cannot explain the main events\nVocabulary check | Did not know 'harvest,' 'stubborn,' or 'barn'",
  stem="Which conclusion and next step are best supported by these data?",
  opts=[
    "Andrés needs additional phonics intervention, since weak decoding is the most common reason that a student's retelling is incomplete.",
    "Andrés should practice reading faster to free up more attention for meaning, so daily timed repeated readings should be his top instructional priority.",
    "Andrés should be moved to easier texts until his retelling improves, since the grade-level passage is clearly too difficult for him.",
    "Andrés decodes accurately, but limited vocabulary and oral language are holding back comprehension, so he needs vocabulary and background building.",
  ],
  ans=3,
  why="Andrés's word-level skills (accuracy and rate) are on target, but his text-level comprehension is not, and he lacks key vocabulary. This is a common ELL profile. The National Literacy Panel on Language-Minority Children and Youth (August & Shanahan, 2006) found that ELLs often develop decoding skills comparable to native speakers' while comprehension lags because of vocabulary and oral language. Instruction should build vocabulary, background knowledge, and discussion of grade-level texts, and fluency checks should always include comprehension.",
  traps=[
    ("LITERAL", "The data show 97% accuracy at benchmark rate, so decoding is not the problem. This option ignores the key evidence."),
    ("MISAPPLIED_THEORY", "Automaticity theory applies when decoding is slow. His rate is already at benchmark; speed won't fix missing word meanings."),
    ("LOWER_RIGOR", "Easier texts would not build the vocabulary and background knowledge he needs. He can access grade-level text with vocabulary support."),
    None,
  ],
  key="ELLs often decode well but lag in comprehension; strong fluency scores with weak retell signal a vocabulary/oral language need."),

Q("4.3-07", "knowledge", 3,
  stem="In the literacy-background categories commonly used in ESL literacy instruction (preliterate, nonliterate, semiliterate, and so on), which term best describes a 15-year-old newcomer who speaks Q'anjob'al, a language with an established written form, but who never attended school and cannot read or write in any language?",
  opts=[
    "Nonliterate",
    "Preliterate",
    "Semiliterate",
    "Non-Roman alphabet literate",
  ],
  ans=0,
  why="In this framework, 'preliterate' describes learners whose home language has no written form or is rarely written; 'nonliterate' describes learners whose language has a written form but who have had no access to literacy instruction; 'semiliterate' describes learners with some limited literacy. Because Q'anjob'al has a written form and the student has had no schooling, 'nonliterate' fits. The distinction matters because it points to a lack of opportunity, not a lack of ability.",
  traps=[
    None,
    ("TERM", "nonliterate ↔ preliterate", "'Preliterate' applies when the home language itself has no written form or is rarely written. Q'anjob'al has an established writing system."),
    ("TERM", "nonliterate ↔ semiliterate", "'Semiliterate' describes learners with some basic literacy. This student cannot read or write in any language."),
    ("TERM", "nonliterate ↔ non-Roman alphabet literate", "That category describes students literate in another alphabet (e.g., Cyrillic, Arabic). This student has no literacy to transfer."),
  ],
  key="Preliterate: L1 not (commonly) written. Nonliterate: L1 is written but no access to schooling. Semiliterate: limited literacy."),
]
QUESTIONS += [
Q("4.3-08", "scenario", 2, diag=2,
  stem="Ousmane, a 14-year-old SIFE whose home language is Wolof, is a skilled oral storyteller but has had little experience with print in any language because of interrupted schooling. Which approach would best begin his English literacy development?",
  opts=[
    "Use kindergarten picture books and nursery rhymes, since his literacy development is at the same stage as a young child's.",
    "Have him complete alphabet-tracing worksheets daily until he knows every letter, before he reads any connected text at all.",
    "Use the Language Experience Approach: he dictates his own experiences, and the transcribed text becomes his reading and phonics material.",
    "Keep him out of his content classes until he can read independently, so that he can focus all of his energy on building basic literacy skills.",
  ],
  ans=2,
  why="The Language Experience Approach turns a student's own oral language and experiences into reading material, so the text is meaningful, age-appropriate, and built on Ousmane's strength in oral storytelling. From his dictated text, the teacher can explicitly teach concepts about print, sight words, and letter-sound patterns. Adolescent SIFE need literacy instruction that respects their age and life experience, not materials designed for young children.",
  traps=[
    ("WRONG_LEVEL", "Materials for young children ignore his age, interests, and life experience. Beginning literacy does not have to mean childish content."),
    ("ISOLATED", "Letter knowledge matters, but tracing worksheets in isolation, with connected text postponed, strips literacy of meaning and delays real reading."),
    None,
    ("EXCLUSION", "Removing a SIFE from content classes denies grade-level learning. Literacy can develop alongside scaffolded content instruction."),
  ],
  key="For preliterate or nonliterate teens, use age-respectful, meaningful text built on their own oral language (Language Experience Approach) plus explicit skills."),

Q("4.3-09", "application", 1,
  stem="In a Spanish–English Dual Language kindergarten, Camila can rhyme, clap syllables, and identify beginning sounds in Spanish words, but she is just beginning to learn English. What is the most accurate expectation about her phonological awareness in English?",
  opts=[
    "Her Spanish phonological skills will interfere with English, so the teacher should focus all of her phonological work on English only.",
    "She will need to develop phonological awareness again from the beginning in English, because it is a language-specific skill.",
    "Because she is still learning English vocabulary, phonological awareness instruction in English should wait until her oral English is stronger.",
    "Much of her phonological awareness will transfer to English, so the teacher can build on it and teach the English sounds that differ.",
  ],
  ans=3,
  why="Research on bilingual children (e.g., Durgunoğlu and colleagues) shows that phonological awareness transfers across languages. A child who can rhyme, segment syllables, and isolate initial sounds in Spanish can apply that awareness to English, which reflects Cummins's common underlying proficiency. The teacher builds on what Camila already knows and explicitly teaches English sounds that Spanish lacks.",
  traps=[
    ("DEFICIT", "Treating Spanish skills as interference is a deficit view. Her Spanish phonological awareness is an asset that supports English."),
    ("MISAPPLIED_THEORY", "Phonological awareness is largely a shared, transferable skill (common underlying proficiency). It does not restart from zero in each language."),
    ("EXCLUSION", "Waiting delays instruction she can benefit from now, especially since she already has the underlying skill in Spanish."),
    None,
  ],
  key="Phonological awareness transfers across languages; build on L1 skills and explicitly teach the new-language sounds that differ."),

Q("4.3-10", "analysis", 3,
  stim="Reading words on a capital-letter word wall (Taras, grade 6, literate in Ukrainian)\nPrinted word | Taras read\nHOT | 'not'\nPEN | 'ren'\nBAT | 'vat'",
  stem="Which explanation best accounts for Taras's errors?",
  opts=[
    "Negative transfer from Cyrillic, in which letters that look like Latin letters (H, P, B) represent different sounds (/n/, /r/, /v/)",
    "A visual-perceptual difficulty that causes him to reverse letters and misread letters that look similar to one another",
    "Limited phonemic awareness, which prevents him from hearing and blending the individual sounds in short, simple words",
    "Interference from Ukrainian vocabulary, since he is substituting familiar Ukrainian words that look or sound like the English words on the wall",
  ],
  ans=0,
  why="In Cyrillic, Н stands for /n/, Р for /r/, and В for /v/, so a Ukrainian reader who sees capital H, P, and B applies his Ukrainian letter-sound knowledge. This is a predictable negative transfer of grapheme-phoneme correspondences, and it shows he is decoding systematically. The teacher should explicitly contrast these look-alike letters in English and Ukrainian.",
  traps=[
    None,
    ("MISREFERRAL", "The errors follow Cyrillic letter values exactly, so this is transfer, not a perceptual disability; referral is unwarranted."),
    ("LITERAL", "He blends three sounds correctly in every word. The problem is which sound he assigns to certain letters, not phonemic awareness."),
    ("TERM", "orthographic transfer ↔ lexical transfer", "'Not,' 'ren,' and 'vat' are produced by decoding with Cyrillic letter values; he is not substituting Ukrainian words."),
  ],
  key="Look-alike letters in other alphabets (Cyrillic H = /n/, P = /r/, B = /v/) cause predictable decoding transfer; contrast them explicitly."),

Q("4.3-11", "scenario", 1,
  stem="A grade 3 ENL teacher wants to build reading fluency (accuracy, appropriate rate, and expression) for a group of Transitioning students. Which approach is most effective?",
  opts=[
    "Daily timed readings of isolated word lists, with the goal of increasing the number of words each student reads per minute",
    "Repeated readings of a familiar, meaningful text with teacher modeling and echo or choral reading, ending in readers' theater",
    "Round-robin reading, in which each student takes a turn reading a paragraph aloud to the group without having practiced it",
    "Independent silent reading of challenging chapter books, since spending more time reading on their own will automatically build fluency",
  ],
  ans=1,
  why="Repeated reading of meaningful text with a fluent model is one of the best-supported fluency practices. Echo and choral reading let ELLs hear and imitate phrasing and expression, and readers' theater gives an authentic reason to reread. Because the text is understood, students practice prosody tied to meaning. Speed drills on word lists ignore expression and comprehension, and round-robin reading gives each student little practice while raising anxiety.",
  traps=[
    ("ISOLATED", "Word-list speed drills build rate without phrasing, expression, or meaning, which are the parts of fluency tied to comprehension."),
    None,
    ("PASSIVE", "In round-robin reading most students just wait their turn. Each reads very little, and cold reading in public raises anxiety."),
    ("PARTIAL", "Wide reading helps over time, but unsupported silent reading of hard text gives no model or feedback for building fluency."),
  ],
  key="Build ELL fluency with modeled, repeated reading of meaningful text (echo, choral, readers' theater), not speed drills."),

Q("4.3-12", "scenario", 1,
  stem="The mother of a first grader whose home language is Bengali tells the ENL teacher, 'We read Bengali storybooks together every night. Should we stop so that she learns English faster?' Which response is best?",
  opts=[
    "'Yes. Switching to English at home will give her more practice and help her catch up to her classmates more quickly.'",
    "'You can continue, but please also read English books with her each night, even if you are not confident reading in English.'",
    "'Please keep reading and talking about books in Bengali; the literacy skills and knowledge she builds will carry over to English.'",
    "'Continue for now, but switch to English once she starts reading chapter books in school, so that the two languages do not get mixed up.'",
  ],
  ans=2,
  why="Cummins's Common Underlying Proficiency and Developmental Interdependence hypotheses explain why home-language literacy supports English literacy. Concepts about print, comprehension strategies, background knowledge, and a love of reading all transfer across languages. Reading in Bengali also maintains family bonds and the child's bilingualism. Advising families to abandon the home language is a deficit view that research does not support.",
  traps=[
    ("DEFICIT", "Replacing the home language at home treats Bengali as an obstacle and cuts off rich language interaction the family can provide."),
    ("PARTIAL", "Continuing is right, but pressing a parent to read in a language she isn't comfortable in can weaken the quality of their shared reading."),
    None,
    ("MISAPPLIED_THEORY", "The languages share an underlying proficiency; continued Bengali literacy supports English rather than 'mixing them up.'"),
  ],
  key="Encourage families to keep reading and talking in the home language; literacy skills and knowledge transfer to English."),

Q("4.3-13", "scenario", 2,
  stem="A grade 1 ENL teacher is planning a phonics lesson on short-a CVC words (mat, fan, bag, ham, rag) for students at the Entering level. Which modification would best support these students?",
  opts=[
    "Confirm each word's meaning with pictures, gestures, or objects, and use the words in short oral sentences before and after decoding.",
    "Replace the real words with nonsense words (zat, mab) so that students focus on decoding without being distracted by meaning.",
    "Postpone the phonics lesson until the students know many more English words, since decoding words they don't yet understand is pointless.",
    "Teach the lesson exactly as written for native English speakers, since the short-a pattern works the same way for all learners.",
  ],
  ans=0,
  why="ELLs benefit from the same explicit, systematic phonics instruction as their peers, but they may not know the meanings of the words they decode. Connecting each word to a picture, gesture, or object and using it orally makes decoding meaningful and builds vocabulary at the same time. Delaying phonics is unnecessary, and nonsense-word practice cannot build the link between decoding and meaning.",
  traps=[
    None,
    ("ISOLATED", "Nonsense words can be useful for assessment, but for ELLs they remove the connection between decoding and meaning."),
    ("EXCLUSION", "Phonics need not wait for a large vocabulary. Teaching meaning alongside decoding develops both."),
    ("ONE_SIZE", "The pattern is the same, but ELLs may not know the words. Ignoring that makes decoding meaningless for them."),
  ],
  key="Teach ELLs systematic phonics with real words whose meanings are made clear through pictures, gestures, and oral use."),

Q("4.3-14", "analysis", 3,
  stim="Oral reading notes (Sofía, grade 3, literate in Spanish)\nText word | Sofía read\nsaid | 'sa-eed'\nknow | 'k-now'\nbread | 'bre-ad'\ncat, map, sit | read correctly",
  stem="Which explanation best accounts for Sofía's reading?",
  opts=[
    "She has not yet learned the alphabetic principle and is guessing at each word from its first letter and overall shape.",
    "She has a phonological processing weakness, shown by her inability to blend the sounds in longer or less familiar words.",
    "She relies on picture and context clues instead of the print, a habit that is common among students who first learned to read in Spanish.",
    "She is applying Spanish's consistent letter-sound mapping to English, whose spelling is far less predictable (a deeper orthography).",
  ],
  ans=3,
  why="Spanish has a shallow (transparent) orthography: nearly every letter is pronounced, and letters map consistently to sounds. Sofía decodes regular CVC words but sounds out every letter in 'said,' 'know,' and 'bread,' just as she would in Spanish. English has a deep orthography, with silent letters, vowel teams, and irregular high-frequency words, so she needs explicit instruction in these patterns and in high-frequency words such as 'said.'",
  traps=[
    ("LITERAL", "She sounds out every letter in order and reads CVC words correctly. That is applying the alphabetic principle, not guessing."),
    ("MISREFERRAL", "She blends sounds successfully; she just pronounces letters English leaves silent or combines. That is transfer, not a processing weakness."),
    ("STEREOTYPE", "This assumes something about how Spanish speakers learn to read. Her errors show letter-by-letter decoding, the opposite of guessing from context."),
    None,
  ],
  key="Spanish spelling is shallow (consistent); English is deep. Teach English vowel teams, silent letters, and irregular high-frequency words explicitly."),
]

# ---------------------------------------------------------------- 4.4
QUESTIONS += [
Q("4.4-01", "analysis", 2, diag=1,
  stim="Passage excerpt (grade 5 Integrated ENL/ELA)\n'The villagers were reluctant to leave their homes, even as the eruption grew more intense. Scientists measured the magma rising beneath the crater and urged everyone to evacuate. But Ana's grandmother insisted that the mountain had always protected them.'",
  stem="The teacher wants to choose three words from this passage for robust, explicit vocabulary instruction. Which set of words is the best choice?",
  opts=[
    "reluctant, urged, insisted",
    "magma, crater, eruption",
    "homes, mountain, grandmother",
    "villagers, scientists, protected",
  ],
  ans=0,
  why="Beck, McKeown, and Kucan recommend focusing robust instruction on Tier 2 words: high-utility words that mature language users meet across many contexts and that matter for understanding the text. 'Reluctant,' 'urged,' and 'insisted' appear across subjects and genres and carry the passage's tension. Tier 3 words such as 'magma' and 'crater' are best taught briefly in context or with a visual. Tier 1 words need little instruction for most students, though an Entering student may need a quick picture.",
  traps=[
    None,
    ("TERM", "Tier 2 ↔ Tier 3", "These are Tier 3, domain-specific words. A quick visual or brief explanation in context is enough, and they have low utility outside earth science."),
    ("TERM", "Tier 2 ↔ Tier 1", "These are Tier 1 everyday words that most students know, or that can be shown with a picture. They don't merit robust instruction."),
    ("PARTIAL", "'Protected' is a reasonable Tier 2 choice, but 'villagers' and 'scientists' are concrete and easily explained, so the set is weaker."),
  ],
  key="Target Tier 2 words (high-utility, cross-content, important to the text) for robust instruction; handle Tier 1 and Tier 3 briefly."),

Q("4.4-02", "scenario", 2, diag=2,
  stim="Journal entry, grade 7 (Lucía, home language Spanish, Transitioning)\n'My aunt is embarrassed, so in May we will have a new baby in the family. I am very excited!'",
  stem="How should the teacher best respond to the word choice in Lucía's journal?",
  opts=[
    "Advise Lucía to stop relying on Spanish to figure out the meanings of English words, since this habit leads to errors like this one.",
    "Circle the word, write 'wrong word' in the margin, and move on to the next journal so that Lucía is not singled out in front of others.",
    "Explain that 'embarazada' and 'embarrassed' are false cognates, add the pair to a class cognate chart, and teach students to check cognates in context.",
    "Give the class a list of 100 Spanish–English false cognates to memorize for a quiz at the end of the week, so that the error is not repeated.",
  ],
  ans=2,
  why="'Embarazada' means 'pregnant,' while 'embarrassed' is 'avergonzado/a.' The pair is a classic false cognate (falso amigo). Lucía is using a powerful strategy, looking for cognates, that works most of the time; she just needs to learn that some look-alikes differ in meaning. Teaching the pair explicitly, keeping a class chart of cognates and false cognates, and teaching students to confirm cognates in context strengthens the strategy rather than discouraging home-language use.",
  traps=[
    ("DEFICIT", "Cognate knowledge is one of a Spanish speaker's greatest vocabulary assets. Discouraging it because of occasional false cognates throws away a powerful strategy."),
    ("PARTIAL", "Marking the error privately avoids embarrassment, but 'wrong word' doesn't explain the false cognate or teach a strategy for next time."),
    None,
    ("ISOLATED", "Memorizing a long decontextualized list is inefficient and quickly forgotten. Students need to learn to verify cognates in context."),
  ],
  key="Treat false cognates (embarazada ≠ embarrassed) as teachable moments; strengthen cognate use by teaching students to verify meaning in context."),

Q("4.4-03", "knowledge", 1,
  stem="According to Beck, McKeown, and Kucan's framework, which group consists entirely of Tier 3 words?",
  opts=[
    "analyze, consequence, fortunate",
    "chlorophyll, sonnet, latitude",
    "happy, table, walk",
    "however, although, therefore",
  ],
  ans=1,
  why="Tier 3 words are low-frequency, domain-specific words tied to a particular subject, such as 'chlorophyll' (science), 'sonnet' (literature), and 'latitude' (geography), and are usually taught when the content calls for them. 'Analyze,' 'consequence,' and 'fortunate' are Tier 2 general academic words. Connectives like 'however' and 'therefore' are also treated as high-utility Tier 2 words for ELLs. 'Happy' and 'walk' are Tier 1 everyday words.",
  traps=[
    ("TERM", "Tier 3 ↔ Tier 2", "These are Tier 2 words: high-utility academic vocabulary used across many subjects, not tied to one domain."),
    None,
    ("TERM", "Tier 3 ↔ Tier 1", "These are Tier 1 basic, everyday words that most students learn through conversation."),
    ("TERM", "domain-specific ↔ general academic connectives", "Transition words appear in every subject. They are high-utility Tier 2 words, not domain-specific Tier 3 terms."),
  ],
  key="Tier 1 = everyday; Tier 2 = high-utility general academic; Tier 3 = low-frequency, domain-specific."),

Q("4.4-04", "application", 3,
  stim="Words from a grade 4 read-aloud, with Spanish equivalents\nEnglish | Spanish\ninformation | información\ncelebration | celebración\nfamous | famoso\ncurious | curioso\nrapidly | rápidamente",
  stem="The class includes many students whose home language is Spanish. Which teaching point would best help these students use cognates to figure out new English words on their own?",
  opts=[
    "Spanish and English share many Latin roots, so students can safely assume that any English word that looks like a Spanish word has the same meaning.",
    "Students should look up each new English word in a bilingual dictionary and write the Spanish translation before they begin reading.",
    "Cognates are learned naturally, so students will recognize them on their own, without instruction, as their English proficiency grows.",
    "Many English suffixes correspond to Spanish ones (-tion/-ción, -ous/-oso, -ly/-mente), so recognizing the pattern can unlock new words.",
  ],
  ans=3,
  why="Explicitly teaching systematic cognate patterns turns a word list into a transferable strategy. Many English–Spanish cognates follow predictable suffix correspondences: -tion/-ción (information/información), -ous/-oso (famous/famoso), -ly/-mente (rapidly/rápidamente), and -ity/-idad (curiosity/curiosidad). ELLs don't automatically notice cognates, so teachers should point them out, teach the patterns, and remind students to verify meanings, since false cognates exist.",
  traps=[
    ("TERM", "cognate ↔ false cognate", "Most look-alikes are true cognates, but 'any word' ignores false cognates such as 'embarazada' and 'éxito.' Students must verify meaning in context."),
    ("PARTIAL", "Bilingual dictionaries are a legitimate support, but translating every word first builds no strategy students can use independently while reading."),
    ("MISAPPLIED_THEORY", "Transfer is not automatic. Research shows ELLs often miss cognates unless they are taught to look for them."),
    None,
  ],
  key="Teach cognate patterns explicitly (-tion/-ción, -ous/-oso, -ly/-mente) and teach students to verify meaning; cognate awareness isn't automatic."),

Q("4.4-05", "scenario", 2,
  stem="Grade 6 Expanding students keep stopping at long words such as 'unpredictable,' 'disagreement,' and 'transportation' while reading a novel. Which strategy will best help them become independent with words like these?",
  opts=[
    "Have students look up every unfamiliar long word in a dictionary and copy its definition into a log before they continue reading.",
    "Give students a list of 50 Latin and Greek roots and their meanings to memorize over the next two weeks for a cumulative test.",
    "Tell students to skip long words while reading, since most of a passage's meaning comes from the shorter words around them.",
    "Model breaking words into prefix, root, and suffix (un-predict-able), inferring the meaning, and checking it against context.",
  ],
  ans=3,
  why="Morphological analysis is a high-yield strategy for ELLs because many academic words are built from a small set of prefixes, roots, and suffixes. Modeling the process with a think-aloud (un- = not, predict = say beforehand, -able = can be) and then checking the inferred meaning in context gives students a tool they can use independently. Memorizing long root lists out of context and copying definitions rarely transfers to reading.",
  traps=[
    ("PARTIAL", "Dictionaries have a place, but looking up every long word interrupts comprehension and builds no independent word-analysis skill."),
    ("ISOLATED", "Memorizing a long root list out of context rarely transfers. Students need guided practice analyzing words as they read."),
    ("LOWER_RIGOR", "Skipping long words gives up on academic vocabulary, and those long words often carry the key meaning."),
    None,
  ],
  key="Teach morphological analysis (prefix-root-suffix) with think-alouds, then confirm meaning in context: a transferable, independent strategy."),

Q("4.4-06", "scenario", 2,
  stim="Sentences from this week's texts\n1. Ana cut the bread with a sharp knife.\n2. There was a sharp rise in temperature overnight.\n3. The author draws a sharp contrast between the two brothers.",
  stem="An ENL teacher notices that her Transitioning students understand 'sharp' in sentence 1 but are confused by sentences 2 and 3. Which instructional approach is most effective?",
  opts=[
    "Make a chart of each meaning with a sentence from the text and a visual, then have students sort new sentences by meaning and write their own.",
    "Tell students to look up 'sharp' in the dictionary and use the first definition listed, since that is the word's most common meaning.",
    "Teach only the academic meanings of 'sharp' from sentences 2 and 3, since students already understand the everyday meaning of the word.",
    "Avoid texts that use words like 'sharp' figuratively until students reach the Commanding level, since such uses are a source of confusion.",
  ],
  ans=0,
  why="Multiple-meaning (polysemous) words are a common stumbling block: students know one meaning and apply it everywhere. Explicitly contrasting the meanings in context, literal ('sharp knife'), sudden ('sharp rise'), and clear or strong ('sharp contrast'), and having students sort and use them builds flexible, deep word knowledge. The familiar meaning becomes a bridge to the new ones.",
  traps=[
    None,
    ("LITERAL", "The first dictionary entry is often not the meaning in the text; it is the meaning students already know, which caused the confusion."),
    ("PARTIAL", "Students need the academic meanings, but contrasting them with the known everyday meaning is what makes the new meanings clear and memorable."),
    ("LOWER_RIGOR", "Avoiding these texts denies access to grade-level language. Multiple-meaning words should be taught, not avoided."),
  ],
  key="Teach multiple-meaning words by contrasting everyday and academic senses in context; use the known meaning as a bridge."),

Q("4.4-07", "scenario", 1,
  stem="A grade 7 class is reading a novel with many idioms, such as 'break the ice' and 'spill the beans.' Which approach best supports the ELLs in the class?",
  opts=[
    "Give students a list of 50 common idioms and their meanings to memorize for a weekly quiz throughout the unit.",
    "Skip over the idioms during discussion, since figurative language is too difficult for ELLs to understand yet.",
    "Discuss each idiom in context, sketch its literal versus figurative meaning, and invite similar home-language expressions.",
    "Have students translate each idiom word for word into their home language to work out what the idiom means.",
  ],
  ans=2,
  why="Idioms are figurative: their meaning can't be worked out from the individual words, so ELLs need them taught in context. Contrasting literal and figurative meanings (a quick sketch of someone literally breaking ice is memorable) and connecting to home-language equivalents make idioms stick. Spanish 'costar un ojo de la cara' ('to cost an eye of the face') parallels 'cost an arm and a leg.' Using the idioms in role-plays or discussion moves them into productive use.",
  traps=[
    ("ISOLATED", "Memorizing a long list of idioms out of context is quickly forgotten and doesn't help students interpret idioms in the novel."),
    ("LOWER_RIGOR", "Skipping figurative language denies access to grade-level text. Idioms should be taught, not avoided."),
    None,
    ("PARTIAL", "Connecting to the home language is valuable, but word-for-word translation fails because an idiom's meaning isn't the sum of its words."),
  ],
  key="Teach idioms in context: contrast literal vs. figurative meaning, connect to home-language equivalents, and use them in talk."),
]
QUESTIONS += [
#@44b
]

# ---------------------------------------------------------------- lessons
LESSONS = []
LESSONS += [
#@L41
]
LESSONS += [
#@L42
]
LESSONS += [
#@L43
]
LESSONS += [
#@L44
]

import json, pathlib
pathlib.Path(__file__).with_name("c4a.json").write_text(json.dumps({"questions": QUESTIONS, "lessons": LESSONS}, ensure_ascii=False, indent=1))

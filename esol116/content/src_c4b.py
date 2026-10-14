# Competency 4 (Instructing ELLs in English Language Arts), skills 4.5, 4.6, 4.7
# Writes c4b.json next to this file.

QUESTIONS = [

# ---------------------------------------------------------------- 4.5 Reading comprehension & complex texts
{
 "id": "4.5-01", "skill": "4.5", "type": "scenario", "difficulty": 2, "diag": 1,
 "stem": "A grade 7 Integrated ENL/ELA class is starting a grade-level historical novel. Several Transitioning ELLs say the first chapter is “too hard” because of unfamiliar historical references and long, descriptive sentences. The co-teachers want these students to meet the grade-level standard for analyzing how the setting shapes the characters. Which plan would be most effective?",
 "options": [
  "Give the ELLs a leveled reader on the same theme, written at their independent reading level, so they can practice analyzing setting in a book they can read on their own.",
  "Keep the novel; front-load key historical background and only a few essential words, then guide rereading of short chunks with text-dependent questions and partner talk.",
  "Have the ELLs listen to an audio recording of each chapter while following along in the book, and then answer the end-of-chapter questions independently.",
  "Pre-teach every unfamiliar word in the chapter by giving students a list of dictionary definitions to study at home the night before each reading."
 ],
 "answer": 1,
 "why": "This plan amplifies rather than simplifies: students stay with the grade-level novel, and the teachers remove barriers instead of removing content. Front-loading historical background builds the schema the chapter assumes, a few essential words keep the vocabulary load manageable, and chunked rereading guided by text-dependent questions and partner talk sends students back to the text for evidence about setting. This is the Blueprint principle that instruction for ELLs is rigorous and grade-level.",
 "traps": [
  {"code": "LOWER_RIGOR", "note": "Swapping in an easier book removes the complex text the standard is about. The students lose access to grade-level language and ideas instead of getting help with them."},
  None,
  {"code": "PARTIAL", "note": "Audio support helps with decoding and fluency, but it does not build the missing historical background or teach students to unpack the dense sentences, and answering alone gives them no interaction."},
  {"code": "ISOLATED", "note": "A long list of dictionary definitions studied out of context overwhelms students and does not build the historical schema. Front-loading should be selective and tied to the text."}
 ],
 "key": "Scaffold the complex grade-level text with background, chunking, text-dependent questions, and talk; don't replace it with an easier one."
},
{
 "id": "4.5-02", "skill": "4.5", "type": "analysis", "difficulty": 3, "diag": 0,
 "stimulus": "Original sentence from a grade 8 class novel:\n“Despite the drought that had withered the crops, the farmers refused to abandon the land their families had worked for generations.”\n\nVersion 1:\n“There was no rain. The crops died. The farmers did not leave their land.”\n\nVersion 2:\n“Despite the drought (a long time with no rain) that had withered (dried up and killed) the crops, the farmers refused to abandon (leave forever) the land. Their families had worked that land for generations, so it was very important to them.”",
 "stem": "An ENL teacher prepares two versions of a sentence from a grade-level novel for a group of Transitioning ELLs. Which of the following best evaluates the two versions?",
 "options": [
  "Version 1 is the stronger scaffold, because short, simple sentences lower the cognitive load and let students focus on the main idea of the passage.",
  "Version 2 is a simplified text, because it splits the original sentence in two and therefore reduces the overall linguistic complexity for students.",
  "Version 2 is an elaborated text: it keeps the original wording and structure but adds glosses and makes the implied reason explicit.",
  "Version 1 suits Transitioning students best, and Version 2 should be saved for Expanding students who are ready to handle longer, denser text."
 ],
 "answer": 2,
 "why": "Walqui's principle “amplify, don't simplify” separates elaboration from simplification. An elaborated text keeps the original vocabulary and sentence structures and adds redundancy—glosses, paraphrases, explicit links—so students get comprehensible input and still meet the academic language they must learn. Version 1 strips out “despite,” “refused,” and the generational reason, so the very relationships a reader has to understand disappear.",
 "traps": [
  {"code": "LOWER_RIGOR", "note": "Simplification deletes the concessive connector “despite” and the farmers' reason for staying. Without those links the text can actually be harder to understand, and students never practice the academic structures."},
  {"code": "TERM", "pair": "elaborated ↔ simplified text", "note": "Version 2 keeps the full original sentence, including the relative clause and “despite.” It adds support rather than taking language away, which is what makes it elaborated."},
  None,
  {"code": "WRONG_LEVEL", "note": "Transitioning students can work with authentic grade-level sentences when glosses and explicit links are added. Holding back the real language until Expanding delays access to the very structures they need."}
 ],
 "key": "Elaborated (amplified) texts add support but keep the original language; simplified texts remove the academic language ELLs need."
},
{
 "id": "4.5-03", "skill": "4.5", "type": "application", "difficulty": 1, "diag": 0,
 "stimulus": "Small-group transcript, grade 5 Integrated ENL/ELA (reciprocal teaching)\nAmina: I don't get “reluctantly” in this sentence. Let's look at the next part. It says he “dragged his feet” and “didn't want to go.” So maybe “reluctantly” means he did it, but he didn't want to.\nTeacher: How did you figure that out?\nAmina: I read the words around it.",
 "stem": "In this exchange, Amina is primarily carrying out which reciprocal teaching strategy?",
 "options": [
  "Clarifying",
  "Predicting",
  "Questioning",
  "Summarizing"
 ],
 "answer": 0,
 "why": "Reciprocal teaching (Palincsar & Brown) rotates four strategies: predicting, questioning, clarifying, and summarizing. Clarifying means noticing a comprehension breakdown—an unknown word or a confusing idea—and repairing it, as Amina does with context clues. For ELLs, the defined roles and modeled language give every student a clear reason and a way to talk about the text.",
 "traps": [
  None,
  {"code": "TERM", "pair": "clarifying ↔ predicting", "note": "Predicting uses text clues to anticipate what will happen next. Amina is working out the meaning of a word already on the page, not forecasting events."},
  {"code": "TERM", "pair": "clarifying ↔ questioning", "note": "In reciprocal teaching, questioning means posing questions about the content for the group to answer. Saying “I don't get this word” and fixing it is a clarifying move."},
  {"code": "TERM", "pair": "clarifying ↔ summarizing", "note": "Summarizing restates the main ideas of a section in a few words. Amina focuses on one word's meaning, not on condensing the passage."}
 ],
 "key": "Reciprocal teaching: predict, question, clarify, summarize. Clarifying repairs a breakdown such as an unknown word."
},
{
 "id": "4.5-04", "skill": "4.5", "type": "application", "difficulty": 1, "diag": 0,
 "stimulus": "Teacher, reading aloud from a grade 6 article projected on the board:\n“‘The town's population dwindled after the factory closed.’ Hmm, I'm not sure what dwindled means. The factory closed, so people probably lost their jobs. Maybe they moved away. I think dwindled means got smaller. Let me keep reading to check… ‘Only a few hundred residents remained.’ Yes, that confirms it.”",
 "stem": "The teacher's main purpose in this segment is most likely to:",
 "options": [
  "check whether students can define the word dwindled before they read the rest of the article on their own",
  "pre-teach a Tier 3 content word that students will need in order to understand the article's main idea",
  "model fluent oral reading so that students hear the correct pronunciation and phrasing of the article",
  "make visible how a proficient reader notices confusion, uses context to repair it, and checks the guess"
 ],
 "answer": 3,
 "why": "A think-aloud makes invisible cognitive work visible: the teacher says out loud how she notices a problem, predicts a meaning from context, and confirms it with later text. For ELLs this turns comprehension monitoring (a CALLA metacognitive strategy) into something concrete they can imitate, and it gives them language for describing their own thinking. The next gradual-release step is for students to try the same moves with a partner.",
 "traps": [
  {"code": "LITERAL", "note": "The teacher, not the students, works through the word, so nothing is being checked. Focusing on the word itself misses that the lesson is about the process."},
  {"code": "TERM", "pair": "Tier 2 ↔ Tier 3", "note": "Dwindled is a Tier 2 word (general academic, used across contexts), not a Tier 3 content-specific term. And the teacher is modeling a strategy, not pre-teaching."},
  {"code": "PARTIAL", "note": "Reading aloud does model fluency, but the deliberate pauses to reason about meaning show that the main purpose is modeling comprehension monitoring."},
  None
 ],
 "key": "Think-alouds make a skilled reader's hidden comprehension strategies visible so students can imitate them."
},
{
 "id": "4.5-05", "skill": "4.5", "type": "application", "difficulty": 2, "diag": 2,
 "stimulus": "Excerpt (grade 8 memoir):\n“For three winters my father worked the night shift and slept through the afternoons. We learned to whisper. We learned to close doors the way you might set down a sleeping baby. When he finally got a day job, the apartment seemed suddenly too loud, as if the walls themselves had forgotten how.”",
 "stem": "A grade 8 Integrated ENL/ELA class will closely reread this excerpt. Which of the following is the best example of a text-dependent question?",
 "options": [
  "Has anyone in your family ever worked at night, and how did that change life in your home?",
  "What kinds of jobs usually require a night shift, and why are those jobs important to a city?",
  "What does comparing closing doors to setting down a sleeping baby suggest about the family?",
  "What are three dictionary meanings of the word shift, and which meaning is the most common?"
 ],
 "answer": 2,
 "why": "A text-dependent question can be answered only with evidence from the text, so it sends students back to the author's words—the core of close reading in the Next Generation ELA Learning Standards. Asking what the “sleeping baby” comparison suggests requires students to analyze figurative language and infer the family's care for the father from specific lines. For ELLs, such questions are paired with rereading, partner talk, and frames such as “The author compares ___ to ___, which shows ___.”",
 "traps": [
  {"code": "PARTIAL", "note": "A personal connection can be a good warm-up, but students can answer it without reading the excerpt at all, so it is not text-dependent."},
  {"code": "LITERAL", "note": "This question grabs the surface topic “night shift” and moves to general knowledge. It can be answered without the text and ignores the author's craft."},
  None,
  {"code": "ISOLATED", "note": "Listing dictionary meanings is decontextualized word work. Close reading asks how words work in this passage, not what they mean in general."}
 ],
 "key": "A text-dependent question cannot be answered without returning to evidence in the text."
},
{
 "id": "4.5-06", "skill": "4.5", "type": "application", "difficulty": 1, "diag": 0,
 "stem": "Emerging ELLs in a grade 4 Integrated ENL/ELA class will read an informational article explaining how cutting down forests causes soil erosion, which in turn causes flooding downstream. Which graphic organizer would best support their comprehension of the text's structure?",
 "options": [
  "A cause-and-effect flow chart with arrows linking each event to its result",
  "A Venn diagram comparing the features of forests and farmland in the region",
  "A timeline showing the years when each area of the forest was cleared",
  "A KWL chart listing what students know, want to know, and have learned"
 ],
 "answer": 0,
 "why": "Graphic organizers help ELLs most when they mirror the text's organizational structure. This article is a causal chain (deforestation → erosion → flooding), so a flow chart with arrows makes the logical relationships visible and supports oral or written retelling with signal words like “causes,” “leads to,” and “as a result.” Matching organizers to structures also teaches students to recognize text structures on their own.",
 "traps": [
  None,
  {"code": "TERM", "pair": "cause-effect ↔ compare-contrast", "note": "A Venn diagram fits a compare-contrast text. This article explains a chain of causes and results, so a Venn diagram would not show its logic."},
  {"code": "TERM", "pair": "cause-effect ↔ sequence", "note": "A timeline shows when things happened. The article's key idea is why one event leads to another, which a timeline does not capture."},
  {"code": "PARTIAL", "note": "A KWL chart activates background knowledge and sets a purpose, but it does not map the causal chain that students need in order to understand this text."}
 ],
 "key": "Match the organizer to the text structure: cause-effect → flow chart; compare-contrast → Venn diagram; sequence → timeline."
},
{
 "id": "4.5-07", "skill": "4.5", "type": "scenario", "difficulty": 2, "diag": 0,
 "stem": "A grade 10 ENL teacher is about to begin a grade-level novel set during the Dust Bowl of the 1930s. Her class includes recent arrivals from Yemen, Ecuador, and Uzbekistan who have strong home-language schooling but little knowledge of U.S. history. Which pre-reading activity would best build the background knowledge the novel requires?",
 "options": [
  "Deliver a detailed lecture on the economic causes of the Great Depression so that students have accurate historical information before they read.",
  "Show photographs and a short video of the Dust Bowl, then have pairs discuss how drought or hard times affected people they know, adding ideas to a concept web.",
  "Skip the historical context and begin reading right away, since the novel's central themes of family loyalty and survival are universal and familiar to all students.",
  "Have students read an encyclopedia entry on the Dust Bowl independently and answer the comprehension questions before beginning the novel."
 ],
 "answer": 1,
 "why": "Schema theory holds that readers understand new text by connecting it to existing knowledge, which is why Building Background is a SIOP component. Visuals make the unfamiliar setting comprehensible without depending on English, and pair talk links that setting to students' own experiences—their funds of knowledge. The concept web then gives them a shared reference and key vocabulary to carry into the novel.",
 "traps": [
  {"code": "PASSIVE", "note": "A detailed lecture is one-way, language-heavy input with no visuals, interaction, or link to students' experiences, so recent arrivals are likely to understand little of it."},
  None,
  {"code": "PARTIAL", "note": "Universal themes are a real bridge, but the plot depends on specific historical conditions. Without that background, students will misread events and characters' choices."},
  {"code": "WRONG_LEVEL", "note": "An unsupported encyclopedia entry is a second dense text at the newcomers' frustration level. It adds reading load instead of building background in a comprehensible way."}
 ],
 "key": "Before a text that assumes unfamiliar historical or cultural knowledge, build background with visuals, discussion, and links to students' lives."
},
{
 "id": "4.5-08", "skill": "4.5", "type": "scenario", "difficulty": 3, "diag": 0,
 "stem": "A grade 3 Integrated ENL/ELA class includes four Entering ELLs whose home language is Bengali. A Bengali-speaking paraprofessional is available for 15 minutes just before and just after the ELA block, when the class will read a grade-level folktale in English. Which use of the paraprofessional would best support both comprehension and English development?",
 "options": [
  "During the lesson, she sits beside the students and translates each of the teacher's sentences into Bengali as the teacher reads aloud and explains the story.",
  "During the ELA block, she takes the students to a separate room to read a Bengali folktale and answer comprehension questions about it in Bengali.",
  "Before the lesson, she drills the students on English vocabulary flash cards with pictures, using words the teacher has selected from the folktale.",
  "Before the lesson, she previews the story's main events in Bengali; the teacher teaches in English; afterward, she reviews the story with them in Bengali."
 ],
 "answer": 3,
 "why": "In the preview-view-review model, the home language frames an English lesson: the preview gives students the gist and key concepts so the English input becomes comprehensible, and the review consolidates and checks understanding. Unlike concurrent translation, it keeps students attending to English because they are not waiting for a sentence-by-sentence translation. It uses the home language as a resource, consistent with the Blueprint and Cummins's Common Underlying Proficiency.",
 "traps": [
  {"code": "TERM", "pair": "concurrent translation ↔ preview-view-review", "note": "Concurrent translation feels supportive, but students learn to tune out the English and wait for the Bengali, so it does little for English development."},
  {"code": "EXCLUSION", "note": "Pulling the students out during ELA removes them from the grade-level lesson and from English instruction instead of making that lesson accessible."},
  {"code": "PARTIAL", "note": "Pre-teaching some vocabulary helps, but drilling English words ignores the paraprofessional's biggest asset, Bengali, which could build understanding of the whole story before the lesson."},
  None
 ],
 "key": "Preview-view-review uses the home language before and after an English lesson; avoid sentence-by-sentence concurrent translation."
},
{
 "id": "4.5-09", "skill": "4.5", "type": "application", "difficulty": 2, "diag": 0,
 "stem": "While choosing a short story for a grade 6 unit, an ELA teacher checks its Lexile measure and then reviews its structure, levels of meaning, and language features. The ENL co-teacher adds that the ELLs in the class have little background knowledge of the story's topic and that the planned task asks them to compare two characters' motives. The ENL teacher's comments address which dimension of text complexity?",
 "options": [
  "Reader and task considerations",
  "Quantitative measures of the text",
  "Qualitative measures of the text",
  "Readability formula results"
 ],
 "answer": 0,
 "why": "The text complexity model used with the NYS standards has three dimensions: quantitative measures (Lexile, sentence length, word frequency), qualitative measures (structure, levels of meaning, language conventionality, knowledge demands), and reader and task considerations (these particular students' knowledge, language, and motivation, plus what the task asks them to do). The ENL teacher is weighing these readers and this task, which is where ESOL expertise usually points to the scaffolds a text will need rather than to rejecting it.",
 "traps": [
  None,
  {"code": "TERM", "pair": "quantitative ↔ reader-and-task", "note": "Quantitative measures, such as the Lexile the ELA teacher already checked, are computed from word and sentence features. They say nothing about these students or this task."},
  {"code": "TERM", "pair": "qualitative ↔ reader-and-task", "note": "Qualitative measures describe features of the text itself, like structure and meaning, which the ELA teacher already reviewed. The ENL teacher is describing the readers and the task."},
  {"code": "TERM", "pair": "readability formula ↔ reader-and-task", "note": "Readability formulas are a kind of quantitative measure based on sentence and word length, not a separate dimension, and they ignore readers and tasks."}
 ],
 "key": "Text complexity has three dimensions: quantitative, qualitative, and reader and task. ELLs' background and the assigned task fall under reader and task."
},
{
 "id": "4.5-10", "skill": "4.5", "type": "application", "difficulty": 1, "diag": 0,
 "stimulus": "Before reading, mark each statement Agree or Disagree. Then discuss your choices with a partner.\n1. It is always wrong to break a promise.\n2. Young people should follow their parents' wishes even when they disagree.\n3. Being honest is more important than being kind.",
 "stem": "A grade 9 ENL teacher gives students this sheet before they read a short story. The primary purpose of this activity is to:",
 "options": [
  "find out whether students understood the plot of the story after they have finished reading it on their own",
  "determine each student's English reading level so that the teacher can assign appropriate texts for the unit",
  "activate students' prior knowledge and opinions about the story's themes and give them a purpose for reading",
  "pre-teach the academic vocabulary that students will encounter in the opening paragraphs of the story"
 ],
 "answer": 2,
 "why": "An anticipation guide is a pre-reading strategy: students take a position on theme-related statements, which activates their schema, sparks discussion, and gives them a reason to read—to see whether the story supports their views. After reading, students revisit the statements and cite evidence for any change in their thinking. Because the statements draw on life experience rather than prior reading, ELLs from any background can contribute.",
 "traps": [
  {"code": "TERM", "pair": "pre-reading ↔ post-reading", "note": "The sheet is used before reading, so it cannot check plot comprehension. Revisiting it afterward is a follow-up, not its primary purpose."},
  {"code": "ASSESS_INVALID", "note": "Agree/disagree opinions give no valid information about reading level. A reading-level decision needs an appropriate reading measure."},
  None,
  {"code": "LITERAL", "note": "The statements present themes, not target vocabulary from the story, so this misreads what the activity is designed to do."}
 ],
 "key": "Anticipation guides activate prior knowledge and set a purpose before reading; students revisit them with text evidence afterward."
},
{
 "id": "4.5-11", "skill": "4.5", "type": "scenario", "difficulty": 3, "diag": 0,
 "stimulus": "Sentence from the grade 8 class text:\n“The settlers, who had been promised fertile land by agents who had never seen the territory, discovered that the soil was too rocky to farm.”",
 "stem": "Expanding ELLs in a grade 8 class can define nearly every word in this sentence, yet in discussion they say that “the agents discovered the soil was rocky.” Which instructional response best addresses the source of their difficulty?",
 "options": [
  "Rewrite the text's long sentences as shorter, simpler sentences so that students can follow the meaning without having to untangle embedded clauses.",
  "Assign a grammar workbook unit on relative clauses, with practice sentences unrelated to the novel, before students continue reading the text.",
  "Pre-teach fertile, territory, and settlers with visuals and student-friendly definitions, and then have the students reread the paragraph.",
  "Lead a sentence deconstruction: chunk the sentence into clauses, ask who did what in each chunk, and discuss which noun each “who” clause describes."
 ],
 "answer": 3,
 "why": "The misreading shows a syntactic breakdown: students cannot tell which noun each relative clause modifies or find the main subject and verb (“The settlers… discovered”). Sentence deconstruction, like Wong Fillmore's “juicy sentence” routine, teaches students to unpack dense academic sentences from the very text they are reading, which builds the skill rather than avoiding it. Knowing every word does not guarantee comprehension when complex syntax carries the meaning.",
 "traps": [
  {"code": "LOWER_RIGOR", "note": "Rewriting the sentences removes the syntax the students need to learn to read. Grade-level texts are full of such sentences, so avoiding them keeps the problem in place."},
  {"code": "ISOLATED", "note": "Workbook drills on unrelated sentences rarely transfer. Students need to untangle relative clauses in the text they are actually reading."},
  {"code": "LITERAL", "note": "The stem says students already know the words. The error is about who did what, a syntax problem, so more vocabulary work misses the evidence."},
  None
 ],
 "key": "When ELLs know the words but still misread a sentence, deconstruct its syntax in context instead of simplifying it."
},
{
 "id": "4.5-12", "skill": "4.5", "type": "analysis", "difficulty": 2, "diag": 0,
 "stimulus": "Reading data, grade 5 (grade-level fiction passage)\nStudent | Word accuracy | Oral reading rate | Retell (0–4) | Inferential questions\nSofia (Expanding, home language Spanish, 4th year of ENL services) | 98% | At grade-level benchmark | 1 | 1 of 5 correct\nTeacher note: Sofia's retell lists details from the first paragraph only. She could not explain why the main character changed her mind.",
 "stem": "Which conclusion and next step are best supported by these data?",
 "options": [
  "Sofia needs more phonics and decoding practice, because accurate word reading is the foundation that her comprehension depends on.",
  "Sofia decodes well but needs comprehension instruction: vocabulary and background building, plus modeled inference and retelling strategies.",
  "Sofia should be referred for a special education evaluation, because a fluent reader who cannot comprehend text may have a learning disability.",
  "Sofia should move to texts two grade levels lower so that she can practice comprehension strategies with easier and shorter material."
 ],
 "answer": 1,
 "why": "Ninety-eight percent accuracy at a grade-level rate, combined with a weak retell and missed inferences, shows that decoding is not the problem; comprehension is. This pattern is common in ELLs whose decoding and conversational English (BICS) outpace academic vocabulary, background knowledge, and inferencing (CALP). Explicit comprehension instruction with grade-level text—think-alouds, story maps, inference frames—targets the actual need.",
 "traps": [
  {"code": "LITERAL", "note": "The data show 98% accuracy at benchmark rate, so decoding is a strength. This answer ignores the key evidence, which is the weak retell and inferencing."},
  None,
  {"code": "MISREFERRAL", "note": "A comprehension gap in a developing ELL is typical of academic language still being acquired. Targeted instruction and progress monitoring come first, not a referral based on one data point."},
  {"code": "LOWER_RIGOR", "note": "Sofia reads grade-level text accurately. Moving her to easier texts lowers expectations instead of teaching the comprehension strategies she needs for grade-level work."}
 ],
 "key": "Fluent, accurate decoding with a weak retell signals a comprehension need, not a phonics need or a disability."
},
{
 "id": "4.5-13", "skill": "4.5", "type": "scenario", "difficulty": 2, "diag": 0,
 "stem": "Dilnoza, a grade 4 Entering ELL who arrived from Uzbekistan two months ago, reads and writes fluently in Uzbek. Her Integrated ENL/ELA class is reading a grade-level informational text about the water cycle and will then explain the process in writing. Which plan best gives Dilnoza meaningful access to this lesson?",
 "options": [
  "Preview the concept through an Uzbek-language video or text, then have her label a water-cycle diagram from a word bank and explain it to a partner using a frame.",
  "Have her work through an English alphabet and phonics workbook at a side table until she knows enough English to take a full part in the class's reading lessons.",
  "Give her the same text and writing prompt as her classmates, without changes, on the expectation that she will acquire English through daily exposure.",
  "Give her a kindergarten picture book about the weather so that she can read a text written at her current English level while the class reads."
 ],
 "answer": 0,
 "why": "Entering students can work with grade-level concepts when the language load is heavily scaffolded. A home-language preview draws on Dilnoza's strong Uzbek literacy (Cummins's Common Underlying Proficiency), so the concept transfers; the labeled diagram, word bank, and frame let her produce English at an Entering level while she thinks about the same content as her peers. This matches the NLAP pattern of substantial support at Entering, not a separate curriculum.",
 "traps": [
  None,
  {"code": "EXCLUSION", "note": "Isolating her with a phonics workbook removes her from grade-level content until she is “ready.” She can learn the concept now with scaffolds."},
  {"code": "ONE_SIZE", "note": "Unmodified grade-level input is not comprehensible at Entering. Exposure without scaffolds ignores her proficiency level and leaves her unable to participate."},
  {"code": "LOWER_RIGOR", "note": "A kindergarten weather book replaces the grade-level concept with much simpler content and underestimates a literate fourth grader."}
 ],
 "key": "At Entering, keep grade-level content and add heavy scaffolds: home-language preview, visuals, word banks, frames, and partner talk."
},
{
 "id": "4.5-14", "skill": "4.5", "type": "application", "difficulty": 3, "diag": 0,
 "stimulus": "Passage: “Lena counted the coins in her jar again: still four dollars short. She looked at the bike in the shop window, then at the Help Wanted sign taped beside it.”\nQuestion: “What will Lena probably do next, and what clues support your answer?”",
 "stem": "A teacher is using the Question-Answer Relationship (QAR) framework with Transitioning ELLs. How should the class classify this question?",
 "options": [
  "Right There, because the words needed to answer it are stated directly in one sentence of the passage",
  "Think and Search, because the reader must put together information from more than one sentence",
  "Author and Me, because the reader combines clues in the text with his or her own knowledge",
  "On My Own, because the reader can answer it from experience without needing to read the passage"
 ],
 "answer": 2,
 "why": "Raphael's QAR framework sorts questions by where the answer comes from: In the Book (Right There; Think and Search) or In My Head (Author and Me; On My Own). Predicting Lena's next step requires combining text clues—four dollars short, a Help Wanted sign—with background knowledge about earning money, so it is Author and Me. Teaching ELLs to classify questions shows them where to look for an answer and when they are expected to infer.",
 "traps": [
  {"code": "TERM", "pair": "Right There ↔ Author and Me", "note": "The passage never states what Lena will do, so the answer cannot be found in a single sentence."},
  {"code": "TERM", "pair": "Think and Search ↔ Author and Me", "note": "Think and Search answers are in the text, spread across sentences. Here the clues are in the text, but the answer itself (taking a job) must come from the reader's knowledge."},
  None,
  {"code": "TERM", "pair": "On My Own ↔ Author and Me", "note": "The question requires the text clues (four dollars short, the sign). An On My Own question could be answered without reading at all."}
 ],
 "key": "QAR: Right There and Think and Search are in the text; Author and Me combines text and reader knowledge; On My Own uses reader knowledge."
},

# ---------------------------------------------------------------- 4.6 Writing development
{
 "id": "4.6-01", "skill": "4.6", "type": "analysis", "difficulty": 2, "diag": 1,
 "stimulus": "Writing sample (grade 4, Transitioning, home language Spanish; personal narrative):\n“Last winter my family go to the mountains in Pennsylvania. First we drive four hours. Is very cold and is snow everywhere. Then my cousin and me make a big snowman. At the end of the day we was tired but very happy. I want to go again next year!”",
 "stem": "Which of the following best describes a strength and a priority need shown in this sample?",
 "options": [
  "Strength: varied complex sentences with embedded clauses; need: organizing the events of the story in a clear, logical order",
  "Strength: a clear, time-ordered sequence of events; need: more vivid descriptive details and dialogue to develop the story",
  "Strength: a clear, time-ordered sequence with transitions; need: consistent past-tense verbs and stated subjects, as in “It is very cold”",
  "Strength: a willingness to take risks writing in English; need: an evaluation for a language disorder, given the many repeated grammar errors"
 ],
 "answer": 2,
 "why": "The sample shows real narrative competence: a time-ordered sequence signaled by “Last winter,” “First,” “Then,” and “At the end of the day,” plus a closing reflection. The most pervasive need is past-tense marking (go, drive, make, was), and “Is very cold” shows a dropped subject consistent with Spanish, which allows subjects to be omitted (“Está nevando” = “It is snowing”). Strong analysis names an asset to build on and a patterned, teachable need—the same thinking the constructed response requires.",
 "traps": [
  {"code": "LITERAL", "note": "This reverses the evidence. The sentences are mostly short and simple, and the sequence of events is already one of the clearest strengths."},
  {"code": "PARTIAL", "note": "The strength is accurate and details would enrich the story, but the need overlooks the verb-tense pattern that runs through every sentence, which is the priority for a Transitioning writer."},
  None,
  {"code": "MISREFERRAL", "note": "The errors are systematic and typical of second-language development, partly shaped by Spanish. Nothing in the sample suggests a language disorder."}
 ],
 "key": "Analyze ELL writing for an asset (such as organization) and a patterned, teachable need (such as past-tense marking), not for every error."
},
{
 "id": "4.6-02", "skill": "4.6", "type": "scenario", "difficulty": 2, "diag": 2,
 "stimulus": "Dialogue journal entry (grade 6, Emerging, home language Haitian Creole):\n“Yesterday I go to my aunt house in Brooklyn. She make diri ak djon djon for my birthday. Is my favorite food. I am very happy.”",
 "stem": "Which teacher reply in the journal best fits the purpose of a dialogue journal?",
 "options": [
  "“Happy birthday! Your aunt made diri ak djon djon for you? What a special gift. My sister made my favorite soup when I went to her house. What do you like best about the rice?”",
  "“Good effort! Remember to write ‘Yesterday I went,’ ‘She made,’ and ‘It is.’ Please rewrite your entry using the correct past-tense verbs and bring it back to me tomorrow morning.”",
  "“Great job! I can tell that you worked hard on your journal this week. Keep it up, and remember to write at least five complete sentences in your next entry.”",
  "“What a fabulous shindig! It sounds like your aunt really went all out and pulled out all the stops to make your big day one to remember forever!”"
 ],
 "answer": 0,
 "why": "A dialogue journal is a private written conversation: the teacher responds to the student's message, not to the errors. The best reply shows genuine interest, stays on the student's topic, naturally models the target forms (“made,” “went”) at a level just beyond the student's own (i+1), and asks a question that invites the student to keep writing. Over time students notice and adopt the modeled forms without the anxiety that red-pen correction can create.",
 "traps": [
  None,
  {"code": "OVERCORRECT", "note": "Turning the journal into a rewrite assignment makes it about form rather than communication, which raises the affective filter and discourages the student from writing freely."},
  {"code": "PARTIAL", "note": "The reply is encouraging, but it ignores what the student said, models no language, and asks no question, so the written conversation stops."},
  {"code": "WRONG_LEVEL", "note": "Idioms such as “went all out” and “pulled out all the stops” are far beyond an Emerging reader. A journal reply should model language just above the student's level."}
 ],
 "key": "In dialogue journals, respond to meaning, model correct forms naturally, and ask a question. Don't correct the errors."
},
{
 "id": "4.6-03", "skill": "4.6", "type": "application", "difficulty": 2, "diag": 0,
 "stem": "In a grade 1 Integrated ENL class, the teacher and students compose a thank-you note to the school custodian on chart paper. Students suggest each sentence and the group rereads it aloud. Students take turns coming to the chart to write letters and words they know, while the teacher writes the rest and briefly teaches spacing and capital letters. This approach is best described as:",
 "options": [
  "shared writing",
  "the Language Experience Approach",
  "guided writing",
  "interactive writing"
 ],
 "answer": 3,
 "why": "Interactive writing is “sharing the pen”: teacher and students compose the message together, students physically write the parts within their reach, and the teacher writes the rest while teaching conventions at the point of need. For young ELLs it connects oral language to print in a meaningful group text that the class rereads many times. On the gradual-release continuum it sits between shared writing (the teacher scribes) and guided or independent writing.",
 "traps": [
  {"code": "TERM", "pair": "interactive writing ↔ shared writing", "note": "In shared writing the teacher holds the pen and scribes the group's ideas. Here the students take turns writing on the chart themselves."},
  {"code": "TERM", "pair": "interactive writing ↔ Language Experience Approach", "note": "In the LEA, students dictate an account of a shared experience and the teacher writes their words to create a reading text. Students do not share the pen."},
  {"code": "TERM", "pair": "interactive writing ↔ guided writing", "note": "In guided writing, each student writes his or her own piece in a small group while the teacher coaches. This scenario is one whole-class text."},
  None
 ],
 "key": "Interactive writing: teacher and students share the pen. Shared writing: the teacher scribes the group's ideas."
},
{
 "id": "4.6-04", "skill": "4.6", "type": "scenario", "difficulty": 2, "diag": 0,
 "stem": "Grade 8 Expanding ELLs write argument essays that state a clear claim and give reasons, but none of the essays acknowledges or responds to an opposing view. Which next step would best help students develop this element of argument writing?",
 "options": [
  "Add a counterclaim row to the essay rubric and return the drafts with a lower score in that category so that students can clearly see what is missing.",
  "Assign a worksheet on contrast transitions such as however, although, and on the other hand, using practice sentences unrelated to the students' essays.",
  "Give each student a complete model essay to copy into a notebook so that students become familiar with the format of a strong argument.",
  "Have students study a mentor essay to see how the writer introduces and rebuts a counterclaim, chart its language, and try those moves in their drafts."
 ],
 "answer": 3,
 "why": "Mentor texts let students read like writers: they notice how a skilled writer handles one specific move—here, acknowledging and rebutting a counterclaim—and then try that move in their own work. For ELLs, naming the move and charting its language (“Some people argue that…; however, the evidence shows…”) makes both the rhetorical purpose and the forms explicit. This connects reading and writing within the grade-level genre.",
 "traps": [
  {"code": "PARTIAL", "note": "A rubric row clarifies the expectation, but it doesn't teach students how to write a counterclaim. Lowering the score without instruction just labels the gap."},
  {"code": "ISOLATED", "note": "Practicing transitions in unrelated sentences is decontextualized. Students need to see how those words do rhetorical work inside an argument."},
  {"code": "PASSIVE", "note": "Copying a model involves no analysis and none of the students' own reasoning. Mentor texts are studied and emulated, not transcribed."},
  None
 ],
 "key": "Use mentor texts to make a specific writing move and its language visible, then have students apply it to their own drafts."
},
{
 "id": "4.6-05", "skill": "4.6", "type": "analysis", "difficulty": 1, "diag": 0,
 "stimulus": "Writing sample (grade 5, Transitioning, home language Bengali):\n“My grandmother lives in Dhaka. She is old. She is very kind. She tells stories. The stories are about her village. I miss her.”",
 "stem": "Which instructional focus would best help this student develop more mature sentences?",
 "options": [
  "Sentence combining with the student's own sentences, using adjectives, and, who, or that to join ideas",
  "Instruction in subject-verb agreement, since agreement errors are the main problem shown in this sample",
  "A rule that every sentence must contain at least fifteen words, so that the student's sentences get longer",
  "Diagramming practice sentences from a grammar textbook to label each subject and each predicate"
 ],
 "answer": 0,
 "why": "The sample is grammatically accurate but made of short, repetitive simple sentences, a common stage as writers gain control. Sentence combining teaches students to merge related ideas with adjectives, conjunctions, and relative clauses (“My kind, elderly grandmother, who lives in Dhaka, tells stories about her village”), building syntactic complexity in meaningful context. Working from the student's own sentences keeps the practice authentic and shows how combining changes emphasis and flow.",
 "traps": [
  None,
  {"code": "LITERAL", "note": "There are no agreement errors here (“She is,” “She tells” are correct). This option doesn't match the evidence in the sample."},
  {"code": "PARTIAL", "note": "It targets the right symptom, short sentences, but gives the student no strategy. Arbitrary length rules tend to produce run-ons rather than well-built complex sentences."},
  {"code": "ISOLATED", "note": "Labeling parts of textbook sentences is decontextualized analysis. It does not teach the student to build longer sentences in her own writing."}
 ],
 "key": "Choppy but accurate simple sentences call for sentence combining, using the student's own writing."
},
{
 "id": "4.6-06", "skill": "4.6", "type": "analysis", "difficulty": 3, "diag": 0,
 "stimulus": "Excerpt from an essay by a grade 10 Expanding ELL (prompt: “Should students be required to do community service?”):\n“There is a saying in my family: a tree is known by its fruit. Since ancient times, people have helped their neighbors in many ways. In my grandfather's village, everyone repaired the well together… [three more paragraphs of stories and examples] …Therefore, I believe that service should be part of every student's education.”\n\nIn a writing conference, the student explains: “In my old school, we learned not to say your opinion at the beginning. You lead the reader to it.”",
 "stem": "Which interpretation of the essay's organization is most appropriate?",
 "options": [
  "The essay shows that the student has not yet developed the ability to think logically and to organize ideas in any language.",
  "The pattern is typical of all writers from the student's language background, so the teacher can expect it from those students.",
  "The organization likely reflects conventions from the student's prior schooling; the teacher should contrast it explicitly with the U.S. early-thesis norm.",
  "The teacher should accept the organization without comment, since asking the student to change it would devalue the student's home culture and identity."
 ],
 "answer": 2,
 "why": "Contrastive rhetoric (Kaplan; now often called intercultural rhetoric) holds that writers may carry organizational conventions from prior schooling, such as opening with a proverb or delaying the main point. The asset-based response treats this as a different, learned convention rather than a deficit, and teaches the U.S. academic expectation of an early, explicit thesis as an added option, for example by comparing the two structures side by side. The student's own explanation is the evidence; the pattern should not be generalized to a whole language group.",
 "traps": [
  {"code": "DEFICIT", "note": "The essay has a deliberate, coherent structure that the student can explain. It reflects a different convention, not an inability to think logically."},
  {"code": "STEREOTYPE", "note": "Contrastive rhetoric has been criticized for exactly this kind of overgeneralization. Writers vary, and the evidence here is one student's own account."},
  None,
  {"code": "LOWER_RIGOR", "note": "Withholding the conventions the student will be judged on, such as on the Regents exam, lowers expectations. Adding a new convention does not erase the old one."}
 ],
 "key": "Unfamiliar essay organization may reflect learned rhetorical conventions; teach the U.S. academic structure explicitly without treating it as a deficit."
},
{
 "id": "4.6-07", "skill": "4.6", "type": "application", "difficulty": 1, "diag": 0,
 "stem": "During a peer conference in a grade 7 Integrated ENL/ELA class, partners use a checklist that asks: “Does the opening grab the reader's attention? Is any part confusing? Where could the writer add an example?” In which stage of the writing process are the students working?",
 "options": [
  "Prewriting",
  "Revising",
  "Editing",
  "Publishing"
 ],
 "answer": 1,
 "why": "Revising improves the content, organization, and clarity of a draft: strengthening an opening, clearing up confusing parts, adding examples. Editing fixes conventions such as spelling, punctuation, and grammar. Keeping the two separate matters for ELLs, because when feedback jumps straight to grammar, students can conclude that writing is about avoiding errors rather than communicating ideas. Checklists with question stems also give ELLs the language to give peer feedback.",
 "traps": [
  {"code": "TERM", "pair": "prewriting ↔ revising", "note": "Prewriting generates and organizes ideas before drafting. These questions assume a draft already exists."},
  None,
  {"code": "TERM", "pair": "revising ↔ editing", "note": "Editing focuses on conventions such as spelling, punctuation, and grammar. These questions are about content and clarity."},
  {"code": "TERM", "pair": "publishing ↔ revising", "note": "Publishing means sharing a finished piece with an audience. The checklist is still improving the draft."}
 ],
 "key": "Revising improves content, organization, and clarity; editing corrects conventions (spelling, punctuation, grammar)."
},
{
 "id": "4.6-08", "skill": "4.6", "type": "scenario", "difficulty": 2, "diag": 0,
 "stimulus": "Paragraph from a grade 9 Transitioning ELL's response to a short story (home language Russian):\n“In the story, the main character is very brave person. She goes to the forest alone for find her brother. When she sees the wolf, she is not run away. This shows that she loves the brother more than she is afraid.”",
 "stem": "The teacher notes that the student's claim is well supported by evidence from the story. Which approach to written feedback would be most effective?",
 "options": [
  "Mark every grammatical error in red and write the correct form above each one so that the student can see all of the mistakes at once.",
  "Praise the well-supported claim, then mark two examples of one pattern, such as missing articles, and have the student find and fix the rest.",
  "Comment on the ideas but avoid mentioning grammar at all, since any attention to language form will discourage the student from writing more.",
  "Rewrite the paragraph in correct English and ask the student to copy the corrected version neatly into the final draft of the response."
 ],
 "answer": 1,
 "why": "Second-language writing research and practice favor focused (selective) corrective feedback: addressing one or two frequent, patterned errors rather than marking everything. Missing articles are a systematic pattern here, consistent with transfer from Russian, which has no articles. Pairing praise for the strong ideas with a limited self-correction task builds noticing and responsibility without overwhelming the writer.",
 "traps": [
  {"code": "OVERCORRECT", "note": "Marking every error buries the strong ideas, overwhelms the student, and gives no priority. The student can't tell which pattern matters most."},
  None,
  {"code": "PARTIAL", "note": "Meaning comes first, but a Transitioning high school writer benefits from focused feedback on patterned errors. Ignoring form entirely can let errors fossilize."},
  {"code": "PASSIVE", "note": "Copying the teacher's correct version requires no noticing or problem solving by the student, so little is learned."}
 ],
 "key": "Give focused feedback: praise the ideas, target one or two patterned errors, and have the student self-correct."
},
{
 "id": "4.6-09", "skill": "4.6", "type": "scenario", "difficulty": 3, "diag": 0,
 "stem": "An ENL teacher uses the teaching-learning cycle of genre-based pedagogy to teach grade 6 Transitioning ELLs to write scientific explanations. Students have built knowledge of the topic through hands-on investigation and have analyzed a model explanation to identify its stages and language features. Which step should come next?",
 "options": [
  "Students independently write their own explanations, using the model text and a rubric as references while they draft.",
  "Students analyze two more model explanations so that they are thoroughly familiar with the genre before writing anything.",
  "The teacher and class write a new explanation together, the teacher guiding structure and language as students contribute ideas.",
  "The teacher reviews the rules for the present tense and the passive voice through a series of sentence-level grammar practice exercises."
 ],
 "answer": 2,
 "why": "The teaching-learning cycle (associated with Rothery, Derewianka, and Gibbons) moves through building the field, deconstruction of a model text, joint construction, and independent construction. Joint construction is the bridge: the teacher shapes the text and thinks aloud about choices while students contribute, so they practice the genre's structure and language with support before writing alone. It is the writing version of gradual release, “we do” before “you do.”",
 "traps": [
  {"code": "WRONG_LEVEL", "note": "This skips the supported step and expects independent performance too early. Transitioning writers need guided practice with the genre first."},
  {"code": "PARTIAL", "note": "More models can help, but students have already deconstructed one. What they need now is supported practice producing the genre, not more analysis."},
  None,
  {"code": "ISOLATED", "note": "Sentence-level grammar drills pull the language out of the genre. In genre pedagogy, grammar is taught as it functions within the text being written."}
 ],
 "key": "Genre cycle: build the field → deconstruct a model → joint construction → independent construction."
},
{
 "id": "4.6-10", "skill": "4.6", "type": "analysis", "difficulty": 2, "diag": 0,
 "stimulus": "Writing sample (grade 6, Transitioning, home language Mandarin; recount):\n“Last Saturday my father take me to the library. We borrow three book about animal. I read one book on the train. It is about a panda who lose her baby. At the end the panda find baby and I feel happy.”",
 "stem": "Which conclusion about this student's writing is best supported by the sample?",
 "options": [
  "The student consistently omits past-tense and plural endings, a pattern consistent with Mandarin, which does not use word endings for tense or plurals.",
  "The errors are random slips that the student will correct easily once reminded to proofread the recount carefully before turning it in for a grade.",
  "The student's limited English vocabulary prevents him from describing the events of the recount clearly and in a logical order.",
  "The repeated grammatical omissions suggest a language-based learning disability that should be formally evaluated by the school's evaluation team."
 ],
 "answer": 0,
 "why": "Every past-tense verb (take, borrow, lose, find, feel) and the plurals “book” and “animal” lack endings, which makes this a systematic error pattern rather than random mistakes (Corder's error/mistake distinction). Mandarin expresses time with time words and particles rather than verb endings and does not require plural marking on nouns, so negative transfer is a likely contributor. The sample also shows strengths—clear sequence and accurate content vocabulary—so instruction can target inflectional endings in the student's own recounts.",
 "traps": [
  None,
  {"code": "TERM", "pair": "error ↔ mistake", "note": "Corder distinguished errors (systematic gaps in the learner's current system) from mistakes (occasional slips). A pattern this consistent is an error, so a proofreading reminder won't fix it."},
  {"code": "LITERAL", "note": "The vocabulary is accurate (library, borrow, panda) and the events are in order. The problem is word endings, not word knowledge."},
  {"code": "MISREFERRAL", "note": "Systematic omission of endings is a normal, often L1-influenced stage of second-language development. It is not evidence of a disability."}
 ],
 "key": "Systematic omission of tense and plural endings is a patterned error, often influenced by Mandarin. Teach the forms; don't refer."
},
{
 "id": "4.6-11", "skill": "4.6", "type": "analysis", "difficulty": 1, "diag": 0,
 "stimulus": "Writing sample (grade 2, Emerging, home language Spanish; written under a drawing of her family at a table):\n“I laik mai famili. Mai mamá cook arroz an beans. On Sonday we go to the parke.”",
 "stem": "Which statement best describes what this sample shows?",
 "options": [
  "The student has a spelling disability and should receive intensive intervention in English letter-sound correspondences.",
  "The student is applying Spanish sound-spelling knowledge to English words and using home-language words to convey meaning.",
  "The student is confusing her two languages and should be told to write only in English to avoid further interference from Spanish.",
  "The student's spelling shows that she has not yet learned that letters represent the sounds in spoken words."
 ],
 "answer": 1,
 "why": "Spellings like “laik,” “mai,” “famili,” and “parke” map English sounds onto Spanish letter-sound patterns (Spanish spells the /aɪ/ sound “ai” and the /i/ sound “i”), which shows solid phonemic awareness and positive transfer of alphabetic knowledge. Writing “arroz” is translanguaging: she uses her full repertoire to keep communicating. The next step is to build on this by explicitly contrasting English and Spanish spelling patterns, not to treat the sample as a deficit.",
 "traps": [
  {"code": "MISREFERRAL", "note": "The spellings are systematic and logical according to Spanish phonics. That is evidence of transfer, not of a disability."},
  None,
  {"code": "DEFICIT", "note": "Using Spanish spelling patterns and words is a resource. Banning the home language treats a normal bilingual strategy as a problem."},
  {"code": "LITERAL", "note": "The opposite is true: she represents nearly every sound with a letter. She just uses Spanish letter-sound rules to do it."}
 ],
 "key": "Invented spellings that follow home-language sound-letter rules show phonemic awareness and positive transfer, not a disability."
},
{
 "id": "4.6-12", "skill": "4.6", "type": "scenario", "difficulty": 2, "diag": 0,
 "stem": "A grade 6 Integrated ENL/ELA class will write an opinion paragraph on whether the school should adopt uniforms. The ELLs in the class are at the Entering, Transitioning, and Expanding levels. Which plan best differentiates writing support by proficiency level?",
 "options": [
  "All ELLs use the same paragraph frame and word bank, so that every student receives an equal amount of support during the task",
  "Entering students copy the teacher's model paragraph, Transitioning students complete a cloze worksheet, and Expanding students write the paragraph on their own",
  "Entering students write independently to build confidence, Transitioning students use frames, and Expanding students get a partly completed paragraph",
  "Entering: illustrated organizer, word bank, frames, and home-language brainstorming; Transitioning: paragraph frame; Expanding: mentor paragraph and checklist"
 ],
 "answer": 3,
 "why": "The NLAP describe the same grade-level standard at every proficiency level, with scaffolding that decreases from substantial support at Entering toward independence at Commanding. Entering writers need visuals, word banks, frames, and home-language planning to express an opinion; Transitioning writers can handle connected sentences with a paragraph frame; Expanding writers benefit from a mentor text and a self-check list that push toward independence. Every student still writes an opinion with reasons—the target stays the same while the support changes.",
 "traps": [
  {"code": "ONE_SIZE", "note": "Identical support ignores proficiency differences. The frame will overwhelm Entering students and hold back Expanding students."},
  {"code": "PASSIVE", "note": "Copying and cloze work leave Entering and Transitioning students with no ideas of their own to express, so they never actually write an opinion."},
  {"code": "WRONG_LEVEL", "note": "The supports are inverted: the least proficient students get the least help, and the most proficient students get the most."},
  None
 ],
 "key": "Keep the same writing task for all ELLs; reduce scaffolds as proficiency rises (word banks and frames → paragraph frames → mentor texts)."
},
{
 "id": "4.6-13", "skill": "4.6", "type": "scenario", "difficulty": 1, "diag": 0,
 "stem": "Hana, a grade 9 Emerging ELL who was a strong writer in Arabic at her previous school, sits silently during the planning stage of an English narrative assignment. Which support would be most effective during prewriting?",
 "options": [
  "Require her to plan in English, since planning in Arabic will slow her progress in learning to write in English.",
  "Assign her a shorter and simpler topic, such as a list of her favorite foods, while her classmates plan their narratives.",
  "Let her brainstorm and outline in Arabic, talk through her ideas with a partner, and then draft in English using frames.",
  "Give her extra time to look up every word she will need in an Arabic-English dictionary before she writes anything down."
 ],
 "answer": 2,
 "why": "Cummins's Common Underlying Proficiency suggests that the composing skills Hana built in Arabic—generating ideas, organizing a narrative—can transfer to English. Planning in her strongest language lets her bring that expertise to the grade-level task, and partner talk plus frames help her carry the ideas into English. This is a purposeful translanguaging scaffold within the writing process, not a lowered expectation.",
 "traps": [
  {"code": "DEFICIT", "note": "Banning Arabic treats her strongest literacy as an obstacle. Planning in Arabic lets her use skills that transfer, so it speeds rather than slows her English writing."},
  {"code": "LOWER_RIGOR", "note": "A list of foods replaces the narrative task with a much simpler one and underestimates a strong writer."},
  None,
  {"code": "PARTIAL", "note": "A bilingual dictionary is a useful tool, but looking up every word before writing stalls idea generation and ignores the composing skills she already has."}
 ],
 "key": "Let ELLs who are literate in the home language plan in it, then draft in English with scaffolds."
},
{
 "id": "4.6-14", "skill": "4.6", "type": "analysis", "difficulty": 3, "diag": 0,
 "stimulus": "Excerpt from an argument essay by a grade 10 student who has received ENL services since kindergarten (most recent NYSESLAT level: Expanding):\n“Kids should totally get more time for lunch cuz 25 minutes is like nothing. Me and my friends are always rushing and stuff, and you can't even finish your food. So basically the school needs to fix it.”",
 "stem": "This writing profile is common among Long-Term ELLs. Which of the following best describes the student's primary language need?",
 "options": [
  "Shifting from a conversational register to the formal word choice and structures expected in a written argument",
  "Basic sentence structure, since most of the student's sentences are incomplete or run together without punctuation",
  "Everyday social vocabulary, since the student lacks the words needed to talk about lunchtime at school",
  "A possible learning disability, since ten years of ENL services have not moved the student to Commanding"
 ],
 "answer": 0,
 "why": "The excerpt is fluent and grammatical as speech, but it uses spoken-register features—“totally,” “cuz,” “like nothing,” “and stuff,” “basically”—in a genre that calls for formal word choice, precise claims, and evidence. This is the classic Long-Term ELL profile: strong conversational English (BICS) with underdeveloped academic language (CALP). Instruction should make register explicit, for example by comparing informal and academic versions of the same argument and analyzing mentor essays.",
 "traps": [
  None,
  {"code": "LITERAL", "note": "The sentences are complete and correctly punctuated. The issue is the register, not basic sentence structure."},
  {"code": "TERM", "pair": "BICS ↔ CALP", "note": "Everyday social language (BICS) is the student's strength. The gap is in academic language (CALP)."},
  {"code": "MISREFERRAL", "note": "Long-term ELL status often reflects inconsistent programs and too little explicit academic-language instruction. Nothing in this sample points to a disability."}
 ],
 "key": "Long-Term ELLs often write fluently in a conversational register; teach academic register explicitly through contrast and mentor texts."
},

# ---------------------------------------------------------------- 4.7 Literature, culture & home language in ELA
{
 "id": "4.7-01", "skill": "4.7", "type": "application", "difficulty": 2, "diag": 1,
 "stem": "In a grade 5 Integrated ENL/ELA class, students write and illustrate books about their families' histories in English and in their home languages, with help from family members. The finished books are read aloud at a family celebration and added to the classroom library. This project is best described as students creating:",
 "options": [
  "dialogue journals that build written fluency through private exchanges with the teacher",
  "Language Experience Approach texts that students dictate to the teacher about a shared event",
  "leveled readers matched to each student's independent reading level for the class library",
  "identity texts that showcase students' linguistic and cultural identities to real audiences"
 ],
 "answer": 3,
 "why": "Identity texts (Cummins & Early) are student creations—written, spoken, visual, or multilingual—into which students invest their identities, and which reflect those identities back in a positive light when shared with real audiences such as peers and families. They let students use their full linguistic repertoire, position the home language as a valuable resource, and bring families in as partners. This reflects the Blueprint principles of leveraging home language and culture and partnering with families.",
 "traps": [
  {"code": "TERM", "pair": "identity text ↔ dialogue journal", "note": "A dialogue journal is an ongoing private written conversation between student and teacher. These books are published works shared with a public audience."},
  {"code": "TERM", "pair": "identity text ↔ Language Experience Approach", "note": "In the LEA, students dictate an account of a shared class experience for the teacher to write down. Here students author bilingual books about their own families."},
  {"code": "LITERAL", "note": "This latches onto the surface detail that the books go into the library. The defining feature is that students invest their identities and languages in the work."},
  None
 ],
 "key": "Identity texts are student-created, often bilingual works that showcase students' identities to real audiences such as families and peers."
},
{
 "id": "4.7-02", "skill": "4.7", "type": "analysis", "difficulty": 2, "diag": 0,
 "stimulus": "Excerpt from a short story read in a grade 8 class:\n“Marcus stared at the empty bleachers. After the homecoming game, everyone had gone to the dance, but he still didn't have a date.”\n\nResponse from an Expanding ELL who arrived from Nepal in grade 7:\n“Marcus is sad because his family went home and forgot him at the stadium.”",
 "stem": "The student reads the excerpt aloud accurately and fluently. Which explanation best accounts for her interpretation?",
 "options": [
  "She has a decoding problem that keeps her from accurately processing each of the words in the story's opening sentences.",
  "She lacks cultural schema for U.S. school traditions like homecoming, so she fills the gap with a scenario she knows.",
  "She has weak inferencing ability, which signals a possible comprehension disability that should be referred for evaluation.",
  "Students from her cultural background are generally not taught to make inferences when they read fiction in school."
 ],
 "answer": 1,
 "why": "Schema theory explains that readers interpret texts through their background knowledge. When a story assumes culturally specific knowledge—homecoming, school dances, having “a date”—a reader without that schema builds a plausible but different meaning. The student is in fact inferring, just from a different cultural frame. The teacher should build the needed cultural background with visuals, a brief explanation, and peer discussion, and invite comparisons with school celebrations students know.",
 "traps": [
  {"code": "LITERAL", "note": "The stem says she reads the excerpt accurately and fluently, so decoding is ruled out by the evidence."},
  None,
  {"code": "MISREFERRAL", "note": "She is inferring; she just lacks the cultural information the author assumes. Missing background knowledge is not evidence of a disability."},
  {"code": "STEREOTYPE", "note": "This makes an unsupported generalization about a whole cultural group. The evidence points to one missing piece of cultural knowledge, not to how she was taught."}
 ],
 "key": "Misreadings of culturally specific situations often reflect missing cultural schema, not weak reading skill; build that background."
},
{
 "id": "4.7-03", "skill": "4.7", "type": "analysis", "difficulty": 1, "diag": 0,
 "stimulus": "Novel excerpt: “Ana had practiced for weeks, but the night before the audition she got cold feet and almost stayed home.”\n\nJournal response from a grade 6 Transitioning ELL: “Ana almost did not go because her feet were cold. She needed warm socks.”",
 "stem": "Which instructional response would best address this misunderstanding?",
 "options": [
  "Give students a list of fifty common English idioms with their definitions to memorize for a quiz at the end of each week.",
  "Postpone instruction in idioms and other figurative language until students reach the Commanding level and can understand them.",
  "Explain that idioms aren't read word by word, use context clues to infer “got nervous,” and compare similar home-language expressions.",
  "Tell the student the correct meaning of the idiom and move on so that the class can finish reading the assigned chapter on schedule today."
 ],
 "answer": 2,
 "why": "Idioms are non-compositional—their meaning is not the sum of their words—so reading “cold feet” literally is a natural, predictable step for ELLs. Effective instruction teaches idioms in context, models using surrounding clues (“practiced for weeks… almost stayed home”) to infer the meaning, and builds cross-linguistic awareness by comparing idioms in students' home languages. Figurative language is part of grade-level ELA, so it is taught with support at every proficiency level.",
 "traps": [
  {"code": "ISOLATED", "note": "Memorizing long lists out of context rarely transfers to reading. Students need to practice inferring idioms from the clues around them in real texts."},
  {"code": "EXCLUSION", "note": "Figurative language appears in grade-level texts at every level. Waiting until Commanding denies students access to literature they are reading now."},
  None,
  {"code": "PARTIAL", "note": "Giving the meaning fixes this one instance but teaches no strategy, so the student will be stuck again at the next idiom."}
 ],
 "key": "Teach idioms in context with clue-based inference and home-language comparisons, not with memorized lists or postponement."
},
{
 "id": "4.7-04", "skill": "4.7", "type": "application", "difficulty": 3, "diag": 0,
 "stem": "An elementary school celebrates diversity with a yearly International Food Fair and a hallway display of famous people from students' home countries, but the ELA curriculum and its texts are unchanged. According to James Banks's approaches to multicultural curriculum reform, the school is working at which level?",
 "options": [
  "The contributions approach",
  "The additive approach",
  "The transformation approach",
  "The social action approach"
 ],
 "answer": 0,
 "why": "Banks describes four levels: contributions (heroes, holidays, foods, and other discrete cultural elements), additive (adding multicultural content, themes, or a unit without changing the curriculum's structure), transformation (restructuring the curriculum so students examine issues from multiple perspectives), and social action (students make decisions and take action on social issues). Food fairs and famous-people displays are the hallmark of the contributions level, sometimes called “heroes and holidays.” The CR-SE Framework's call for an inclusive curriculum points toward the transformation and social action levels.",
 "traps": [
  None,
  {"code": "TERM", "pair": "contributions ↔ additive", "note": "The additive approach adds multicultural content, such as a new book or unit, to the curriculum. Here nothing in the curriculum has changed; only celebrations were added."},
  {"code": "TERM", "pair": "contributions ↔ transformation", "note": "Transformation restructures the curriculum so students study issues from multiple perspectives. This school's curriculum is unchanged."},
  {"code": "TERM", "pair": "contributions ↔ social action", "note": "Social action has students study and act on real social issues. A food fair and a display involve no critical inquiry or action."}
 ],
 "key": "Banks's levels: contributions (heroes, holidays, food) → additive → transformation (multiple perspectives) → social action."
},
{
 "id": "4.7-05", "skill": "4.7", "type": "scenario", "difficulty": 2, "diag": 2,
 "stem": "In a grade 8 Integrated ENL/ELA class, two Emerging ELLs whose home language is Spanish discuss the theme of a grade-level novel in Spanish during small-group work. When it is time to share with the class, they struggle to express their ideas in English. Which teacher response best reflects a translanguaging approach?",
 "options": [
  "Remind them that ELA class is an English-only space, so that they get as much practice speaking and writing in English as possible.",
  "Let them keep discussing in Spanish, but excuse them from sharing with the whole class until they become more proficient in English.",
  "Move each of them into a separate group with English-proficient peers, so that they will need to use English to discuss the theme.",
  "Value the Spanish talk as a tool for analysis, then have them jot key ideas bilingually and rehearse sharing in English with frames."
 ],
 "answer": 3,
 "why": "Translanguaging pedagogy (García; CUNY-NYSIEB) treats bilingual students' full linguistic repertoire as one resource for learning. Discussing theme in Spanish lets these Emerging students do grade-level literary analysis they cannot yet fully express in English, and the teacher then builds a bridge to English with bilingual notes, frames, and rehearsal. The home language supports both the content goal and English development rather than competing with them.",
 "traps": [
  {"code": "DEFICIT", "note": "An English-only rule treats Spanish as an obstacle and shuts down the deep analysis the students were doing. More English time does not help if the thinking stops."},
  {"code": "EXCLUSION", "note": "Excusing them from sharing until they are “more proficient” removes the English output opportunity they need. The teacher should scaffold the sharing, not skip it."},
  {"code": "PARTIAL", "note": "Working with English-proficient peers can be valuable at times, but splitting them up to force English removes the resource that was producing their best analysis."},
  None
 ],
 "key": "Translanguaging uses the home language strategically to deepen thinking, then bridges to English output with scaffolds."
},
{
 "id": "4.7-06", "skill": "4.7", "type": "scenario", "difficulty": 3, "diag": 0,
 "stem": "An ENL teacher sends home dual-language (Bengali–English) editions of the picture books her grade 2 class reads and encourages families to read and talk about the stories in Bengali. A colleague worries that this will slow the children's progress in English reading. Which principle provides the strongest response to the colleague's concern?",
 "options": [
  "Lowering the affective filter at home is the main benefit, since reading with family makes children feel relaxed and confident.",
  "Children acquire conversational English within one to three years, so home reading in Bengali mostly builds social language.",
  "Comprehension skills and concepts developed in the home language transfer to English through a common underlying proficiency.",
  "Contrastive analysis shows that reading in the home language helps children avoid errors caused by first-language interference."
 ],
 "answer": 2,
 "why": "Cummins's Common Underlying Proficiency (the “iceberg”) and Developmental Interdependence hypothesis hold that literacy concepts and comprehension skills learned in one language—predicting, sequencing, understanding story structure, knowing what words mean—are available in the other. Rich home-language reading therefore supports, rather than delays, English reading, which answers the colleague's concern directly. Dual-language books also bring families in as literacy partners and affirm the home language, as the Blueprint calls for.",
 "traps": [
  {"code": "PARTIAL", "note": "Comfort and family connection are real benefits, but they don't answer the concern about English reading. Transfer of comprehension skills does."},
  {"code": "TERM", "pair": "BICS ↔ CALP", "note": "Reading and discussing stories builds literacy and academic language (CALP), not just social language. The BICS timeline is beside the point here."},
  None,
  {"code": "MISAPPLIED_THEORY", "note": "Lado's contrastive analysis predicts errors from differences between two languages. It is not a rationale for home-language reading and says nothing about transfer of comprehension."}
 ],
 "key": "Home-language reading builds transferable comprehension (Cummins's Common Underlying Proficiency); it supports, rather than slows, English literacy."
},
{
 "id": "4.7-07", "skill": "4.7", "type": "analysis", "difficulty": 2, "diag": 0,
 "stimulus": "Notes from a teacher's review of a picture book being considered for a grade 3 unit on families:\n- Written by an author with no stated connection to the culture portrayed\n- Every Mexican character wears a sombrero or poncho and lives in a rural village\n- The story is set in the present day\n- The only character who solves a problem is a visiting American child",
 "stem": "Based on these notes, which evaluation of the book is most accurate?",
 "options": [
  "The book is appropriate, because any representation of Mexican culture will help Mexican students feel welcome in the class.",
  "The book offers a stereotyped single story of Mexican culture and gives the agency to an outsider, so a more authentic text is needed.",
  "The book is acceptable as long as the teacher adds a lesson on Mexican holidays and foods to give students more cultural context.",
  "The illustrations are the main problem, so the teacher can use the book if students listen to the text without seeing the pictures."
 ],
 "answer": 1,
 "why": "Evaluating multicultural literature means checking for authenticity (an insider perspective or careful research), accurate and varied present-day portrayals, and characters from the culture who have agency. A present-day story in which every Mexican character wears traditional dress in a village, and an outsider solves the problem, offers what Chimamanda Ngozi Adichie calls a “single story.” The CR-SE Framework calls for an inclusive curriculum that reflects students' identities accurately and with dignity.",
 "traps": [
  {"code": "STEREOTYPE", "note": "Stereotyped representation is not neutral. It can misinform classmates and tell Mexican students that their lives are seen only through clichés."},
  None,
  {"code": "PARTIAL", "note": "A holidays-and-foods lesson is a contributions-level add-on that leaves the book's stereotypes and outsider-hero plot in place."},
  {"code": "LITERAL", "note": "The text itself is a problem: the characterization, the outsider hero, and the author's lack of connection to the culture. Hiding the pictures fixes none of that."}
 ],
 "key": "Choose multicultural texts with authentic, varied, present-day portrayals and characters with agency; reject stereotyped “single stories.”"
},
{
 "id": "4.7-08", "skill": "4.7", "type": "scenario", "difficulty": 1, "diag": 0,
 "stem": "At family conferences, a grade 3 teacher learns that several students' grandparents tell traditional stories at home in Wolof, Spanish, Fulani, and Haitian Creole. The class is beginning a folktale unit. Which plan best builds on what the teacher learned?",
 "options": [
  "Invite relatives to tell a traditional tale, with an interpreter as needed, then have students compare its elements to a grade-level folktale.",
  "Display a world map that marks the countries the students' families come from, with a flag and a greeting in each home language.",
  "Ask students to translate their grandparents' stories into English at home and turn in written versions before the folktale unit begins.",
  "Assign each student to read the folktales from his or her family's home country, so that every child focuses on his or her own culture."
 ],
 "answer": 0,
 "why": "Funds of knowledge (Moll and colleagues) are the skills and knowledge found in households—here, oral storytelling traditions. Inviting relatives to tell tales positions families as experts and partners, and comparing story elements (characters, problem, lesson) across tales meets the grade-level standard while honoring oral literacy. It is a culturally sustaining move that enriches the unit for every student, not only for the storytellers' grandchildren.",
 "traps": [
  None,
  {"code": "PARTIAL", "note": "A map is welcoming but superficial (a contributions-level gesture). It doesn't use the families' storytelling knowledge in the actual literacy work."},
  {"code": "FAMILY_BARRIER", "note": "This puts the job of translating on young children instead of engaging families directly, and it turns an oral tradition into a written homework burden."},
  {"code": "STEREOTYPE", "note": "Assigning texts by presumed heritage pigeonholes students and denies everyone the cross-cultural comparison that makes the unit rich."}
 ],
 "key": "Build on funds of knowledge by bringing family expertise, such as oral storytelling, into grade-level literacy work."
},
{
 "id": "4.7-09", "skill": "4.7", "type": "analysis", "difficulty": 2, "diag": 0,
 "stimulus": "Draft of a poem by a grade 7 Transitioning ELL (home language Urdu), modeled on George Ella Lyon's poem “Where I'm From”:\n“I am from chai in the morning\nand my nani's stories at night.\nI am from ‘beta, eat more!’\nand cricket in the narrow street.\nI am from two languages\nthat live in one heart.”",
 "stem": "Which response to this draft would best support the student's growth as a writer?",
 "options": [
  "Ask the student to replace “nani” and “beta” with their English equivalents so that every reader in the class can easily understand the poem.",
  "Focus the conference on punctuation and capitalization, since conventions should be correct before any content is revised.",
  "Praise the poem and post it on the bulletin board without any revision, since poetry does not have to follow strict rules.",
  "Affirm the Urdu phrases and imagery, then confer about adding sensory details and context that helps readers infer “nani” and “beta.”"
 ],
 "answer": 3,
 "why": "This is an identity text built on a mentor poem: the student borrows a published poem's structure to express a bicultural identity, and the Urdu words carry meaning and voice that English substitutes would lose. Asset-based feedback affirms these choices and then pushes craft—sensory detail and context clues for readers—so expectations stay high. It treats translanguaging as a legitimate literary device, as many published bilingual authors do.",
 "traps": [
  {"code": "DEFICIT", "note": "Replacing the Urdu words erases the voice and identity that make the poem powerful and signals that the home language doesn't belong in literature."},
  {"code": "OVERCORRECT", "note": "Putting conventions before content reverses the writing process and focuses on form when the poem's meaning and imagery are the point."},
  {"code": "LOWER_RIGOR", "note": "Celebrating the poem is good, but skipping revision denies the student feedback on craft. High expectations include pushing a strong draft further."},
  None
 ],
 "key": "In identity writing, affirm home-language words as craft choices, then push revision for imagery and reader understanding."
},
{
 "id": "4.7-10", "skill": "4.7", "type": "application", "difficulty": 3, "diag": 0,
 "stem": "A middle school ELA teacher's explicit goal is not only to use students' Spanish, Arabic, and Bengali as bridges to English, but also to help students maintain and develop those languages and their communities' literacy practices as valuable in their own right—for example, through bilingual poetry publishing and a heritage-language book club. This goal most closely reflects which framework?",
 "options": [
  "Ladson-Billings's culturally relevant pedagogy",
  "Paris's culturally sustaining pedagogy",
  "Moll's funds of knowledge",
  "Krashen's affective filter hypothesis"
 ],
 "answer": 1,
 "why": "Django Paris proposed culturally sustaining pedagogy, which aims to perpetuate and foster linguistic, literate, and cultural pluralism—treating students' languages and practices as worth sustaining, not only as bridges to dominant English. It builds on Ladson-Billings's culturally relevant pedagogy (academic success, cultural competence, critical consciousness) and Gay's culturally responsive teaching. NYS's Culturally Responsive-Sustaining Education Framework carries the word “sustaining” from this line of work.",
 "traps": [
  {"code": "TERM", "pair": "culturally relevant ↔ culturally sustaining", "note": "Ladson-Billings's framework centers academic success, cultural competence, and critical consciousness. Paris extended it with the explicit goal of sustaining students' languages and cultures."},
  None,
  {"code": "TERM", "pair": "funds of knowledge ↔ culturally sustaining pedagogy", "note": "Funds of knowledge draws on household knowledge and skills as resources for instruction. It does not, by itself, make maintaining heritage languages a goal."},
  {"code": "MISAPPLIED_THEORY", "note": "The affective filter concerns how anxiety blocks input. It is about comfort, not about sustaining languages and cultural practices."}
 ],
 "key": "Culturally sustaining pedagogy (Paris) aims to maintain students' languages and cultures, not just use them as bridges to English."
},
{
 "id": "4.7-11", "skill": "4.7", "type": "scenario", "difficulty": 2, "diag": 0,
 "stem": "Zarghuna, a grade 7 Entering ELL who arrived from Afghanistan with strong literacy in Dari, has followed the class novel through a home-language summary, visuals, and partner discussion. The class is now writing literary analyses of the novel's theme. Which approach would give the teacher the most valid evidence of Zarghuna's literary understanding?",
 "options": [
  "Let her write the analysis in Dari with a short framed summary in English, and have a Dari-speaking colleague help review it.",
  "Grade her analysis written in English with the same rubric as her classmates, so that she is held to the same grade-level expectations.",
  "Excuse her from the analysis for now and have her complete it later, once her English proficiency reaches the Transitioning level.",
  "Replace the analysis with a multiple-choice quiz on vocabulary words from the novel, which she can complete with a bilingual glossary."
 ],
 "answer": 0,
 "why": "Valid assessment measures the intended construct, and here the construct is understanding of theme, not English writing. Letting a literate Entering student respond in her home language separates literary understanding from English proficiency, while the framed English summary still provides evidence of language growth. NYS does not allow translations or glossaries on its ELA tests, but in classroom assessment the teacher can and should gather evidence that shows what the student truly knows.",
 "traps": [
  None,
  {"code": "ASSESS_INVALID", "note": "Grading an Entering student's English essay on the class rubric measures her English proficiency, not her understanding of the theme, so the results would be misleading."},
  {"code": "EXCLUSION", "note": "Postponing the task until she is “more proficient” shuts her out of grade-level work and leaves the teacher with no evidence of her learning."},
  {"code": "LOWER_RIGOR", "note": "A vocabulary quiz replaces literary analysis with recall. It lowers the cognitive demand and doesn't measure understanding of theme."}
 ],
 "key": "To assess an Entering student's literary understanding validly, allow a home-language response; grading English proficiency instead gives invalid results."
},
{
 "id": "4.7-12", "skill": "4.7", "type": "scenario", "difficulty": 2, "diag": 0,
 "stimulus": "Opening stanza of a poem by Emily Dickinson:\n“‘Hope’ is the thing with feathers -\nThat perches in the soul -\nAnd sings the tune without the words -\nAnd never stops - at all -”",
 "stem": "Transitioning ELLs in a grade 7 class say that this poem is “about a bird.” Which next step would best help them analyze its figurative language?",
 "options": [
  "Replace the poem with a simpler one that uses literal language so that students can focus on identifying the main idea.",
  "Explain the meaning of the poem to the class, and then have students copy the explanation into their notebooks for later review.",
  "Have partners list what the bird does in the poem, then explain the comparison with the frame “Hope is like a bird because ___.”",
  "Pre-teach the definitions of perches and soul with visuals so that students understand every word that appears in the poem."
 ],
 "answer": 2,
 "why": "The students' literal reading shows they understand the surface image but not the extended metaphor. Guiding them to map the traits of the image (a bird perches, sings, never stops) onto the idea it represents (hope) teaches the thinking process of figurative analysis, and the frame plus partner talk supports output at the Transitioning level. Students can also share how hope is pictured in poems and sayings in their home languages.",
 "traps": [
  {"code": "LOWER_RIGOR", "note": "Swapping in a literal poem removes the very skill the lesson targets. The students' partial reading shows they are ready to be guided further, not given less."},
  {"code": "PASSIVE", "note": "Students only listen and copy, so they never practice the reasoning that figurative analysis requires."},
  None,
  {"code": "PARTIAL", "note": "Knowing the words helps, but the students already grasp the literal image. The gap is in interpreting the metaphor, which vocabulary alone won't close."}
 ],
 "key": "Teach metaphor by mapping traits of the image onto the idea it stands for, using frames and partner talk, not by replacing the text."
},
{
 "id": "4.7-13", "skill": "4.7", "type": "knowledge", "difficulty": 1, "diag": 0,
 "stem": "Which of the following best describes translanguaging as a pedagogical approach?",
 "options": [
  "Having a bilingual aide translate each of the teacher's sentences into the students' home languages while the teacher is speaking",
  "Purposefully using students' whole linguistic repertoire, not only English, to make meaning, learn content, and grow both languages",
  "Switching between two separate language systems only at moments when a student lacks the English word needed to express an idea",
  "Teaching each language in its own time block and discouraging students from mixing languages during instruction"
 ],
 "answer": 1,
 "why": "Translanguaging (Ofelia García; CUNY-NYSIEB) views bilinguals as having one integrated linguistic repertoire rather than two separate language boxes. As pedagogy, it means deliberately designing opportunities—bilingual discussion, home-language research, multilingual texts—that use all of students' language resources to deepen learning and build English. It differs from concurrent translation, which tends to lead students to tune out the English.",
 "traps": [
  {"code": "TERM", "pair": "translanguaging ↔ concurrent translation", "note": "Sentence-by-sentence translation is concurrent translation. Students learn to wait for their home language, and it is not a planned use of their repertoire."},
  None,
  {"code": "TERM", "pair": "translanguaging ↔ code-switching", "note": "This describes a deficit view of code-switching, as a fallback for missing words. Translanguaging sees one integrated repertoire used purposefully, not as a patch for gaps."},
  {"code": "TERM", "pair": "translanguaging ↔ strict language separation", "note": "Strict separation of languages is a program design choice, as in some dual language models. Translanguaging intentionally brings languages together."}
 ],
 "key": "Translanguaging pedagogy purposefully uses students' whole linguistic repertoire to learn content and develop both languages."
},
{
 "id": "4.7-14", "skill": "4.7", "type": "scenario", "difficulty": 1, "diag": 0,
 "stem": "A grade 11 ELA teacher in Washington Heights, where most of her students are Dominican American, is choosing an anchor text for a unit on identity and voice. Which choice best reflects culturally relevant text selection while keeping the unit rigorous?",
 "options": [
  "A high-interest, low-readability book about a Dominican baseball star, since many of the students enjoy watching and following the sport",
  "A classic canonical novel alone, since students need exposure to the literary works most often taught in American high schools",
  "A Spanish translation of a Shakespeare tragedy, so that students can read a classic work of literature in their heritage language",
  "An acclaimed verse novel by a Dominican American author about a Harlem teen finding her voice in poetry, paired with canonical poems"
 ],
 "answer": 3,
 "why": "Culturally relevant texts act as what Rudine Sims Bishop called “mirrors” that reflect students' lives, as well as “windows” into others' experiences. A complex, award-winning novel by an insider author offers authentic representation and grade-level rigor, and pairing it with canonical poems keeps the unit connected to the wider literary tradition. Relevance should come with complexity, not instead of it, and should not rest on stereotypes about students' interests.",
 "traps": [
  {"code": "STEREOTYPE", "note": "Choosing a baseball book because students are Dominican relies on a cultural stereotype, and a low-readability text also lowers rigor for grade 11."},
  {"code": "PARTIAL", "note": "Canonical works have real value, but using one alone gives students no mirror of their own experience in a unit about identity and voice."},
  {"code": "LITERAL", "note": "This equates cultural relevance with reading in Spanish. Students' language profiles vary, and a translated Shakespeare play neither reflects their lives nor builds English literary analysis."},
  None
 ],
 "key": "Pick complex, authentic texts by insider authors that mirror students' lives, paired with other texts, not stereotyped or watered-down choices."
},

]

LESSONS = []

import json, pathlib
pathlib.Path(__file__).with_name("c4b.json").write_text(json.dumps({"questions": QUESTIONS, "lessons": LESSONS}, ensure_ascii=False, indent=1))

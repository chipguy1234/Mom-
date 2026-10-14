# Source for cr.json: Competency 0007 constructed-response materials (NYSTCE ESOL CST, Field 116).
# Run: python3 src_cr.py  -> writes cr.json next to this file.
import json, pathlib, textwrap


def T(s):
    return textwrap.dedent(s).strip()


LEAD = ("Using your knowledge of English Language Learners, language and literacy development, and "
        "research- and evidence-based practices in ESOL instruction, analyze the information provided about "
        "{who} and write a response of approximately 400–600 words in which you:")

SCENARIOS = []

# ---------------------------------------------------------------------------
# cr1  Grade 5 Integrated ENL/ELA, three students
# ---------------------------------------------------------------------------
SCENARIOS.append(dict(
    id="cr1",
    title="Grade 5 Integrated ENL/ELA: Three Students Respond to a Novel",
    setting="Grade 5 Integrated ENL/ELA (co-taught), October",
    intro=T("""
Ms. Okafor is the ENL teacher in a co-taught grade 5 Integrated ENL/ELA class. It is October, and the class is reading a realistic-fiction novel about Mia, a girl who moves to a new city and slowly adjusts to her new school. To plan instruction, Ms. Okafor has gathered information about three English Language Learners in the class.
"""),
    exhibits=[
        dict(title="Exhibit 1: Student Background (NYSESLAT results from spring of grade 4)", content=T("""
Student | Age | Home language | Years in U.S. schools | Prior schooling and home-language literacy | Listening | Speaking | Reading | Writing
Daniela | 10 | Spanish | 2 (arrived in grade 3) | Attended school in the Dominican Republic, K–2; reads chapter books in Spanish at home | Expanding | Transitioning | Transitioning | Emerging
Bilal | 10 | Urdu | 3 (arrived in grade 2) | Attended school in Pakistan, K–1; reads simple Urdu texts with his father | Expanding | Expanding | Transitioning | Transitioning
Yuxin | 11 | Mandarin | 1 (arrived in grade 4) | Uninterrupted schooling in China through grade 3; strong Chinese literacy; math above grade level | Transitioning | Emerging | Transitioning | Emerging
""")),
        dict(title="Exhibit 2: ENL Teacher Observation Notes (Read-Aloud and Turn-and-Talk)", content=T("""
9/24 – During the read-aloud of Chapter 2, all three students followed closely and reacted at the right moments: Bilal laughed at the dog scene, and Yuxin gasped when Mia got lost on the subway.
9/24 – Turn-and-talk: "What happened on Mia's first day?" Daniela retold the events in order: "First she was nervous, then she got lost, after that a lady help her." She checked one detail with her partner in Spanish first.
9/26 – Bilal retold Chapter 3 to the group in the correct order, using "first," "next," and "at the end." When I asked, "Why did Mia stop talking at dinner?" he said, "She is... sad? Because... I don't know how to say it."
9/26 – Yuxin retold in short phrases while pointing to pages: "Mia move. New school. Lost. Lady help. Happy." The sequence was correct. She jotted notes in Chinese on her sticky note.
9/30 – Listening check (I read a new passage aloud; students answered five sequencing questions): Daniela 5/5, Bilal 5/5, Yuxin 5/5.
9/30 – Whenever I asked a "why" or "how did she change" question, all three gave a one-word feeling ("sad," "happy") or said "because" and stopped.
""")),
        dict(title="Exhibit 3: Writing Samples", content=T("""
Prompt: How does Mia change from the beginning of the book to the end of Chapter 3? Use details from the text to explain your answer.

Daniela: In the beginning Mia is in her old house. She is sad becaus she move. Then she go to the new school and she get lost in the subway. A lady help her. Then she go home and her mom make dinner. At the end of chapter 3 she meet Jada and they play. Mia is happy.

Bilal: First Mia move to the new city. Next she was scared in the new school and the teacher say her name wrong. Next she got lost in the subway. Next a lady help her to go home. Next she meet a frend Jada. In the end Mia is happy now

Yuxin: Mia move. She is sad. She go new school. She lost. A lady help. She meet Jada. She is happy. Mia change.
""")),
        dict(title="Exhibit 4: Text-Based Response Rubric Scores (scale of 1–4)", content=T("""
Criterion | Daniela | Bilal | Yuxin
Recounts key events accurately | 4 | 4 | 3
Explains how and why the character changes | 1 | 1 | 1
Supports ideas with text evidence | 1 | 2 | 1
Uses transitions to connect ideas | 2 | 2 | 1
Conventions of standard English | 2 | 2 | 1
""")),
    ],
    prompt=LEAD.format(who="the three English Language Learners in Ms. Okafor's class"),
    tasks=[
        "identify one significant strength and one significant need that the three students share related to English language development, citing specific evidence from the exhibits;",
        "describe one instructional strategy or activity that would build on the identified strength to address the identified need; and",
        "explain why the strategy or activity you described would be effective, grounded in principles of language acquisition and literacy development.",
    ],
    focus="English language development: shared strength and need (three students)",
    model=T("""
Daniela, Bilal, and Yuxin share a significant strength in comprehending and retelling the sequence of events in a grade-level narrative. They share a significant need in explaining their ideas in writing: moving beyond retelling to explain how and why a character changes, using causal language and text evidence.

The strength appears in every exhibit. In Exhibit 1, Listening is the highest or tied-for-highest NYSESLAT modality for all three (Expanding for Daniela and Bilal, Transitioning for Yuxin). In Exhibit 2, all three scored 5/5 on the sequencing listening check, and each retold a chapter in the correct order: Daniela with "first... then... after that," Bilal with "first," "next," and "at the end," and Yuxin with short phrases and page-pointing. Exhibit 4 confirms this, with scores of 3 or 4 on "recounts key events accurately." Even Yuxin, whose Speaking is Emerging, understood the plot well.

The need is just as consistent. All three writing samples in Exhibit 3 are chronological retellings that never explain the change: Daniela ends with "Mia is happy," Yuxin with "Mia change," and Bilal's sample is a chain of "Next" sentences. In Exhibit 4, all three scored 1 on "explains how and why the character changes." Exhibit 2 shows the same gap orally: asked why, each student gave a one-word feeling or said "because" and stopped, as Bilal did ("Because... I don't know how to say it"). The problem is not comprehension; it is the academic language of explanation.

I would use an oral-rehearsal "talk-to-write" routine with a character-change organizer. First, I would model with a three-part organizer ("At the beginning, Mia felt...", "Now Mia feels...", "What caused the change?"), thinking aloud and noting page numbers. Second, partners would retell a chapter, which is their strength, and then answer "Why?" with frames such as "At the beginning, Mia felt ___ because ___" and "Mia changed when ___. This shows that ___." Daniela and Yuxin could brainstorm in Spanish or Mandarin first. Third, each student would say the full explanation aloud while a partner listens for "because" and a page number. Fourth, we would co-write a model paragraph through shared writing. Finally, students would write independently with a word bank (lonely, confident; because, so, as a result). Yuxin would keep more frames and a bilingual word bank, while Bilal would fade the frames sooner.

This strategy works because it starts from what the students already control. Since they understand the plot, their effort can go to the new language of explanation, which places the task at i+1 (Krashen) and within their zone of proximal development (Vygotsky). The frames and organizer are temporary scaffolds that are removed as independence grows. Saying the explanation aloud before writing provides the pushed output Swain describes, helping students notice the gap between "She is sad" and "She felt lonely because she had no friends." Partner talk adds negotiation of meaning (Long). Finally, home-language brainstorming draws on Cummins' Common Underlying Proficiency: Daniela's and Yuxin's strong home-language literacy lets them reason in their stronger language and carry those ideas into English.
"""),
    modelNotes=[
        "Completeness: Every bullet is answered in its own paragraph (one shared strength, one shared need, one strategy, and an explanation), so a scorer can find each part instantly.",
        "Accuracy: The strength (sequential retelling and listening comprehension) and the need (explaining how and why in writing) are true for all three students, and the response correctly rules out comprehension as the problem.",
        "Depth of Support: It cites all four exhibits by number, with exact scores (5/5, rubric 1s) and short quotations (\"Because... I don't know how to say it\").",
        "Depth of Support: The strategy is concrete and sequenced (model, partner retell, oral rehearsal, shared writing, independent writing) and is differentiated for Yuxin and Bilal.",
        "Accuracy and Depth of Support: Each principle (i+1, ZPD, output, interaction, CUP) is tied to something these students did, not just named.",
    ],
    weak=T("""
The students in this class have strengths and needs. One strength is that they are all hardworking and want to learn English. Daniela checks with her partner, Bilal participates in the group, and Yuxin writes notes on her sticky notes. They all seem to like the book about Mia and pay attention during the read-aloud.

A need the students have is grammar. Daniela writes "she move" and "she go," and Yuxin writes "She go new school." They need to learn the past tense because they are not using it correctly. They also make spelling mistakes like "becaus" and "frend." Their writing is also too short, especially Yuxin's.

To help them, I would use differentiated instruction and scaffolding. I would give them graphic organizers and sentence frames and let them work in groups. I would also do grammar mini-lessons on past tense verbs every day, and they could practice with worksheets. Visuals would help them understand the story better. I could also pair them with English-speaking students who can help them with their writing.

This strategy will be effective because ELLs need scaffolding. According to Krashen, students need comprehensible input, and graphic organizers make the input comprehensible. Vygotsky says students learn in the zone of proximal development. When students work in groups, they lower their affective filter and feel more comfortable. Grammar practice will help them become better writers, and the sentence frames will help them write more. By using these strategies, the students will improve their English and be successful in fifth grade.
"""),
    weakNotes=[
        "Completeness: The \"strength\" (hardworking, likes the book) is a disposition, not a language or literacy skill, so the first task is only partly met.",
        "Accuracy: Past-tense grammar is not the most significant shared need, and it is not fully shared: Bilal writes \"was scared\" and \"got lost.\" The response misses the real pattern, which is that all three retell instead of explaining (rubric scores of 1 in Exhibit 4).",
        "Depth of Support: The evidence is a few quoted errors with no exhibit numbers. Exhibits 2 and 4, including the 5/5 listening scores, are ignored.",
        "Completeness: The \"strategy\" is a list (organizers, frames, groups, worksheets, visuals, peers), not one activity, and none of it builds on a named strength.",
        "Accuracy: Daily grammar worksheets are isolated practice that does not fit a need for explaining ideas in meaningful writing.",
        "Depth of Support: Krashen, Vygotsky, and the affective filter are named without any link to what these students said or wrote.",
    ],
    checklist=[
        "I named ONE strength, stated as a language or literacy skill (e.g., sequential retelling), that all three students share.",
        "I named ONE need that all three share (explaining how and why in writing), not an error only one student makes.",
        "I cited at least two exhibits by number for the strength (e.g., the 5/5 listening checks in Exhibit 2).",
        "I cited at least two exhibits for the need, with a quoted phrase or a rubric score.",
        "I explained that comprehension is NOT the problem, which makes the need sharper.",
        "My strategy is ONE activity described in clear steps (model, partner talk, rehearsal, shared writing, independent writing).",
        "My strategy visibly starts from the strength (retelling) and moves to the need (explaining with \"because\").",
        "I explained effectiveness with at least two named principles, each tied to something these students did.",
        "I stayed within about 400–600 words and used asset-based language.",
    ],
))

# ---------------------------------------------------------------------------
# cr2  Grade 1 Stand-alone ENL, emergent literacy
# ---------------------------------------------------------------------------
SCENARIOS.append(dict(
    id="cr2",
    title="Grade 1 Stand-alone ENL: Emergent Readers and Writers",
    setting="Grade 1 Stand-alone ENL small group, November",
    intro=T("""
Mr. Delgado teaches a Stand-alone ENL group of first graders. Each student attended kindergarten in the same New York City school. In November, Mr. Delgado reviews information about three students to plan the early literacy part of his Stand-alone ENL time.
"""),
    exhibits=[
        dict(title="Exhibit 1: Student Background (NYSESLAT results from spring of kindergarten)", content=T("""
Student | Age | Home language | Time in U.S. schools | Home literacy practices | Listening | Speaking | Reading | Writing
Valeria | 6 | Spanish | 1 year (kindergarten) | Mother sings and recites Spanish rhymes daily; Spanish picture books at home | Transitioning | Transitioning | Emerging | Entering
Abdoulaye | 6 | Wolof (also hears French) | 1 year (kindergarten) | Family tells stories and sings in Wolof; older sister reads in French | Transitioning | Emerging | Entering | Entering
Mykola | 6 | Ukrainian | 9 months (entered kindergarten in January) | Parents read Ukrainian picture books; knows some Cyrillic letters | Emerging | Emerging | Emerging | Entering
""")),
        dict(title="Exhibit 2: Early Literacy Screening (November)", content=T("""
Skill (number correct) | Valeria | Abdoulaye | Mykola
Recognizes rhyming pairs (of 10) | 9 | 8 | 8
Produces a rhyming word (of 5) | 4 | 4 | 3
Claps syllables in spoken words (of 10) | 10 | 10 | 9
Isolates the first sound in a word (of 10) | 6 | 5 | 5
Blends three spoken sounds into a word (of 10) | 3 | 2 | 2
Segments a three-sound word into sounds (of 10) | 1 | 0 | 1
Names uppercase letters (of 26) | 21 | 16 | 14
Gives the sound of a letter (of 26) | 9 | 7 | 6
Concepts about print (front of book, left to right, return sweep) | secure | secure | secure
""")),
        dict(title="Exhibit 3: Teacher Observation Notes", content=T("""
11/4 – Shared reading of a big book with a repeated refrain ("Run, run, as fast as you can!"). By the second reading, all three chimed in on the refrain. Abdoulaye clapped the rhythm without being asked.
11/6 – Choice time: Valeria taught two classmates a Spanish clapping rhyme. Abdoulaye joined in and then sang part of a Wolof song he knows. Mykola recited a Ukrainian counting rhyme. Each kept a steady beat and stressed the rhyming words.
11/7 – Quick oral check. Me: "Cat, hat. Do they rhyme?" All three: "Yes!" Me: "Say a word that rhymes with man." Valeria: "Pan!" Abdoulaye: "Can." Mykola: "Fan."
11/7 – Me: "What sounds do you hear in map?" Valeria: "/m/... map." Abdoulaye: "Map!" Mykola shrugged and repeated, "Map."
11/8 – Mykola labeled his rabbit drawing with the letter P and said, "That's r, rabbit." (In Ukrainian, the Cyrillic letter Р stands for /r/.)
""")),
        dict(title="Exhibit 4: Journal Samples (student writing with the teacher's notes)", content=T("""
Valeria: Drawing of a birthday party. Wrote: MI BRDA KK. Read it to me as "My birthday cake."

Abdoulaye: Detailed drawing of his family at the beach. Wrote: B W. Told me, "This my brother. He jumping in the water. Big wave! My mom say be careful."

Mykola: Drawing of himself and his mother on a slide. Wrote MOM AND (copied from the word wall), then KTPAOS. Read it to me as "Me and my mom go to the park."
""")),
    ],
    prompt=LEAD.format(who="the three English Language Learners in Mr. Delgado's group"),
    tasks=[
        "identify one significant strength and one significant need that the three students share related to early literacy development, citing specific evidence from the exhibits;",
        "describe one instructional strategy or activity that would build on the identified strength to address the identified need; and",
        "explain why the strategy or activity you described would be effective, grounded in principles of language acquisition and early literacy development.",
    ],
    focus="Early literacy: phonological awareness and sound–letter mapping (three students)",
    model=T("""
Valeria, Abdoulaye, and Mykola share a significant strength in phonological awareness at the level of larger sound units, rhyme and syllables, supported by a real love of rhythmic language in English and in their home languages. Their shared need is phoneme-level awareness: hearing, blending, and segmenting the individual sounds in words, which they need in order to connect sounds to letters when they read and write.

The strength shows up across the exhibits. In Exhibit 2, all three recognize rhyming pairs (9, 8, and 8 of 10), produce rhymes (4, 4, and 3 of 5), and clap syllables almost perfectly (10, 10, and 9 of 10). Exhibit 3 confirms this in authentic settings: all three chimed in on the big-book refrain by the second reading, each produced a correct rhyme for "man," and each performed a rhyme or song in Spanish, Wolof, or Ukrainian while keeping the beat. Exhibit 1 shows that rhymes, songs, and stories are part of all three homes.

The need is equally consistent. In Exhibit 2, scores drop sharply at the phoneme level: blending (3, 2, and 2 of 10) and segmenting (1, 0, and 1 of 10). Letter-sound knowledge (9, 7, and 6 of 26) lags well behind letter names. In Exhibit 3, when asked for the sounds in "map," Valeria produced only the first sound, while Abdoulaye and Mykola repeated the whole word. Exhibit 4 shows the effect on writing: each child tells a rich oral message but records only a few letters, such as "B W" for "Big wave" and the random string "KTPAOS."

I would build on the strength with a daily 10- to 15-minute "from rhyme to sounds" routine tied to the chants the children love. First, we chant a familiar verse and clap its syllables. Next, I pull out rhyming words from the chant, such as "man," "can," and "ran," and we split each into onset and rime with hand motions (/m/... /an/). Then, using Elkonin sound boxes, the children say a word slowly and push one counter into a box for each sound: /m/ /a/ /n/. Once they can segment orally, they replace the counters with magnetic letters for sounds they know. Finally, we use interactive writing to compose a new line for the chant, and each child "shares the pen," stretching a word into the boxes before writing it. I would also invite families to send rhymes and would point out that Mykola's Cyrillic Р says /r/, while English P says /p/.

This routine works because phonological awareness develops from larger units to smaller ones, so starting with rhyme and syllables, which these children already control, places phoneme work in their zone of proximal development (Vygotsky). The boxes and counters are concrete scaffolds that make invisible sounds visible and can be faded as skills grow. Phonological awareness also transfers across languages, so the rhyming skill each child built in Spanish, Wolof, or Ukrainian is a resource, consistent with Cummins' Common Underlying Proficiency. Familiar, joyful chants keep the affective filter low (Krashen), and interactive writing applies segmenting to the children's own meaningful messages rather than to isolated drills.
"""),
    modelNotes=[
        "Completeness: It names one shared strength (rhyme and syllable awareness) and one shared need (phoneme-level awareness), then gives one routine and a separate explanation.",
        "Accuracy: The need is set at the right grain size. Letter names are fairly strong, so the response targets phoneme segmenting and sound–letter mapping, where every child scores lowest.",
        "Depth of Support: It uses exact screening numbers from Exhibit 2 and links them to authentic behavior in Exhibits 3 and 4 (chants, \"map,\" \"B W\").",
        "Depth of Support: The routine moves step by step along the phonological-awareness continuum (syllable, onset–rime, phoneme, letter) and ends in meaningful interactive writing.",
        "Accuracy: It treats the home-language rhymes as assets, explains cross-linguistic transfer correctly, and notes the specific Cyrillic look-alike that affects Mykola.",
    ],
    weak=T("""
These students are in first grade and are learning English. Their strength is that they like to sing and draw. In Exhibit 3 they sang songs at choice time, and in Exhibit 4 they drew nice pictures with a lot of details. They are also good at concepts about print because they know the front of the book and read left to right.

Their need is that they do not know their letters and sounds. Mykola only knows 6 letter sounds and Abdoulaye knows 7. Their writing does not make sense, like "KTPAOS," and Abdoulaye only wrote two letters. They need to learn phonics so they can write real words.

I would teach them the alphabet with flashcards every day. I would show each letter and say the sound, and they would repeat it after me. We would sing the alphabet song too, because they like singing. Then they could do phonics worksheets where they circle the picture that starts with the letter. I would also send letter flashcards home so parents can practice, and I would tell the parents to read to their children in English at home so they learn English faster.

This is effective because young children learn language easily, and repetition helps them remember. Phonics is the most important part of learning to read. Using songs will make it fun and lower the affective filter. Over time they will learn all their letter sounds and be able to write words and read books by the end of first grade.
"""),
    weakNotes=[
        "Completeness: \"They like to sing and draw\" is an interest, not an early literacy skill. The response never names the rhyme and syllable awareness documented in Exhibit 2, even though concepts about print is a reasonable partial point.",
        "Accuracy: The need is framed as letter knowledge in general, but the sharper shared need is phoneme awareness (segmenting scores of 1, 0, and 1 of 10). Letter names are actually fairly strong.",
        "Accuracy: Telling parents to read in English is deficit-oriented and throws away the strong home-language rhyme and story practices in Exhibit 1.",
        "Depth of Support: Flashcards and circle-the-picture worksheets are isolated drills. The alphabet song is the only link to the strength, and it does not build phoneme awareness.",
        "Depth of Support: \"Young children learn easily\" and \"phonics is the most important part\" are generalizations, not principles tied to these children's data.",
    ],
    checklist=[
        "I named ONE early literacy strength all three share (rhyme and syllable awareness), not an interest like \"likes to sing.\"",
        "I named ONE shared need at the right grain size: phoneme-level segmenting and blending, which limits sound–letter mapping.",
        "I cited screening numbers from Exhibit 2 for both the strength and the need.",
        "I used Exhibit 3 or 4 to show the same pattern in authentic activities (chants, journal writing).",
        "I treated the home-language rhymes and songs (Exhibits 1 and 3) as assets, not problems.",
        "My strategy is one routine with steps that move from rhyme or syllables to phonemes to letters.",
        "My activity is meaningful and playful for six-year-olds, not a worksheet drill.",
        "I explained why it works using at least two principles (e.g., the PA continuum, transfer, ZPD, affective filter).",
    ],
))

# ---------------------------------------------------------------------------
# cr3  Grade 7 Integrated ENL science, two students
# ---------------------------------------------------------------------------
SCENARIOS.append(dict(
    id="cr3",
    title="Grade 7 Integrated ENL Science: From Lab Bench to Textbook",
    setting="Grade 7 Integrated ENL science (co-taught), unit on physical and chemical changes",
    intro=T("""
Ms. Haddad, an ENL teacher, co-teaches a grade 7 Integrated ENL science class. The class has just finished a set of hands-on investigations of physical and chemical changes and is now reading the textbook section on the same topic. Ms. Haddad has gathered information about two English Language Learners in the class.
"""),
    exhibits=[
        dict(title="Exhibit 1: Student Background (NYSESLAT results from spring of grade 6)", content=T("""
Student | Age | Home language | Time in U.S. schools | Prior schooling | Listening | Speaking | Reading | Writing
Aziz | 12 | Uzbek (also reads Russian) | 1½ years (arrived midway through grade 6) | Uninterrupted schooling in Tashkent in Uzbek; strong science and math background | Transitioning | Emerging | Emerging | Emerging
Valentina | 12 | Spanish | 2 years (arrived at the start of grade 6) | Uninterrupted schooling in Medellín, Colombia; top grades in science | Expanding | Transitioning | Transitioning | Transitioning
""")),
        dict(title="Exhibit 2: Lab Observation Notes", content=T("""
Station 1 (baking soda + vinegar): Both students followed the written procedure, which had picture steps, without help. Before mixing, Aziz predicted, "Gas will come," and he wrote "CO2" on his diagram from memory. Valentina told her partner in Spanish, "Es una reacción química porque se forma una sustancia nueva, el gas."
Station 2 (steel wool in vinegar, with a thermometer): Aziz set up the thermometer, recorded the temperature every minute, and was the first to notice the rise: "Look, hot! 24... 27... 29!"
Station 3 (melting ice): Valentina told her partner, "This is not chemical. It is the same water, only liquid."
Card sort (classify 8 picture cards as physical or chemical change): Aziz 8/8; Valentina 8/8.
Data tables: Both complete and accurate, with correct units.
""")),
        dict(title="Exhibit 3: Textbook Reading Check", content=T("""
Passage (from the class textbook): The formation of a new substance is evidence of a chemical change. When baking soda is combined with vinegar, carbon dioxide gas is produced. The release of energy, in the form of heat or light, may also be observed. In contrast, a change of state, such as the melting of ice, does not result in the formation of a new substance.

Question 1: According to the passage, what is evidence of a chemical change?
Aziz: baking soda
Valentina: the formation

Question 2: Is the melting of ice a chemical change? Use the passage to explain.
Aziz: Yes. Ice is change.
Valentina: Yes, because it is a change of state.

Question 3: What else may be observed during a chemical change?
Aziz: (blank)
Valentina: light
""")),
        dict(title="Exhibit 4: Think-Aloud Excerpts (reading the passage with the ENL teacher)", content=T("""
Aziz (reading "The release of energy, in the form of heat or light, may also be observed"): "Release... I don't know release. Energy, I know, энергия. Observed... somebody see? Who is see it?"
Teacher: "What did you notice at Station 2?"
Aziz: "Ah, it was hot! The steel wool make hot. So this is that?"

Valentina (reading "The formation of a new substance is evidence of a chemical change"): "Formation... like formación? A new substance... is evidence... So if a new thing forms, it is chemical? The sentence is very long. When I get to the end, I forget the beginning."
Valentina (reading "does not result in the formation of a new substance"): "Does not... result... I think it says it makes a new substance."
""")),
    ],
    prompt=LEAD.format(who="the two English Language Learners in Ms. Haddad's class"),
    tasks=[
        "identify one significant strength and one significant need that the two students share related to academic language and literacy in science, citing specific evidence from the exhibits;",
        "describe one instructional strategy or activity that would build on the identified strength to address the identified need; and",
        "explain why the strategy or activity you described would be effective, grounded in principles of language acquisition and content-area literacy.",
    ],
    focus="Academic language of science texts (two students)",
    model=T("""
Aziz and Valentina share a significant strength in their conceptual understanding of physical and chemical change, built through strong prior schooling and shown during hands-on inquiry. Their shared need is comprehending the academic language of science texts, especially nominalizations such as "formation" and "release," passive verbs such as "is produced" and "may be observed," and long sentences that pack several ideas together.

The strength is clear in Exhibits 1 and 2. Both had uninterrupted schooling with strong science backgrounds (Exhibit 1). In the lab, both followed procedures independently, sorted 8 of 8 picture cards correctly, and kept accurate data tables. Aziz predicted "Gas will come," wrote "CO2" from memory, and noticed the temperature rise. Valentina explained chemical change precisely in Spanish ("se forma una sustancia nueva") and said of the ice, "This is not chemical. It is the same water, only liquid." These students know the science.

Yet the reading check in Exhibit 3 makes them look as if they do not. Aziz named "baking soda" as the evidence of chemical change, and Valentina copied "the formation." Both answered that melting ice is a chemical change, which directly contradicts what Valentina said in the lab. Exhibit 4 shows why. Aziz stalled on "release" and "observed" and asked, "Who is see it?" because the passive voice hid the actor. Valentina said, "When I get to the end, I forget the beginning," and read "does not result in the formation" as its opposite. The barrier is the language of the text, not the content.

I would use a lab-to-text "sentence unpacking" activity. First, I would choose four dense sentences from the passage and post each one beside a photo of the matching lab station. Second, pairs would match each sentence to their own data and say what happened in everyday words ("The cup got hot"). Third, we would unpack each sentence with three questions: What happened? What caused it? What is the main idea? Students would turn nominalizations back into verbs ("the formation of a new substance" becomes "a new substance forms") and passives into actives ("carbon dioxide gas is produced" becomes "baking soda and vinegar produce carbon dioxide"). Fourth, they would "repack" a sentence from their own lab notes into textbook style, using a cognate chart for Valentina (formation/formación, substance/sustancia, evidence/evidencia) and Russian or Uzbek notes for Aziz. Finally, each would unpack one sentence in a new paragraph independently.

This activity is effective because known content makes difficult text comprehensible. Cummins' Common Underlying Proficiency explains why: the concepts already exist in both students' minds, so they need only the English forms that express them. The lab is context-embedded, while the textbook is context-reduced; anchoring each sentence to a photo and to the students' own data bridges that gap, in line with Cummins' quadrants. Unpacking directs their attention to how academic English packages meaning, which Schmidt's Noticing Hypothesis treats as necessary for acquiring a form. Pair talk adds negotiation of meaning (Long), and repacking gives pushed output (Swain). Because the content load is light, the language demand stays at i+1.
"""),
    modelNotes=[
        "Completeness: All three tasks are answered in order, with the strength and the need each supported in its own paragraph.",
        "Accuracy: The need is stated precisely (nominalization, passive voice, long sentences) instead of the vague \"vocabulary,\" and the response identifies the contradiction between lab knowledge and reading answers.",
        "Depth of Support: The evidence comes from all four exhibits, including exact card-sort scores, the students' own words, and the think-aloud lines that show where the language breaks down.",
        "Depth of Support: The strategy keeps the grade-level text and works through concrete steps (match, unpack, repack, apply) with home-language supports matched to each student.",
        "Accuracy: The theory is applied correctly. CUP, the context-embedded vs. context-reduced quadrants, noticing, interaction, and output each explain a specific part of the activity.",
    ],
    weak=T("""
Aziz and Valentina are both ELLs in seventh grade science. A strength is that they are good at science labs. They did all the stations and wrote data tables. Also, Valentina can speak Spanish, and Aziz speaks Uzbek and Russian, so they know more than one language.

A need is vocabulary. They did not know words like "release" and "observed." Aziz got all the questions wrong on the reading check, and Valentina got some wrong too. Also, Aziz's writing is very short, like "Ice is change," so he needs to work on writing complete sentences.

To help them, I would give them a vocabulary list with the science words from the chapter, such as formation, substance, evidence, release, produced, and observed. They would look up the definitions in the dictionary and write a sentence for each word. Then they would take a vocabulary quiz on Friday. I would also give them an easier version of the textbook with shorter sentences so they can understand it, and they could read it with a partner.

This will be effective because vocabulary is very important for reading. If students know the words, they will understand the text. Shorter sentences are easier for ELLs to read, which gives them comprehensible input (Krashen). Working with a partner is good because of Vygotsky. With these supports, Aziz and Valentina will do better in science class and on their tests.
"""),
    weakNotes=[
        "Completeness: \"Good at science labs\" points toward the strength but never states the conceptual understanding the lab shows (8/8 card sorts, Valentina's explanation of melting), so it cannot be used later in the strategy.",
        "Accuracy: \"Vocabulary\" is too broad. The exhibits point to sentence-level features such as passive voice, nominalization, and long sentences (\"When I get to the end, I forget the beginning\"), not just unknown words.",
        "Completeness: The response adds a second, unsupported need (complete sentences in writing) instead of one focused need.",
        "Depth of Support: The strategy is isolated (dictionary definitions and a Friday quiz) and lowers rigor with a simplified text instead of scaffolding the grade-level passage.",
        "Depth of Support: The strategy never uses the students' lab knowledge, and \"because of Vygotsky\" is a name with no explanation.",
    ],
    checklist=[
        "I stated the strength as conceptual science understanding shown in hands-on inquiry, with evidence for both students.",
        "I stated the need precisely: comprehending academic science text (nominalization, passive voice, long sentences), not just \"vocabulary.\"",
        "I pointed out the contradiction between the lab evidence (Exhibit 2) and the reading check (Exhibit 3).",
        "I quoted the think-aloud (Exhibit 4) to show which language features cause the breakdown.",
        "My strategy uses the students' own lab experience to unlock the textbook language.",
        "My steps keep the grade-level text instead of replacing it with a simplified version.",
        "I included home-language supports matched to each student (Spanish cognates; Russian or Uzbek notes).",
        "I explained effectiveness with named theory (e.g., CUP, context-embedded vs. context-reduced, noticing) tied to the evidence.",
    ],
))

# ---------------------------------------------------------------------------
# cr4  Grade 9 ELA, Long-Term ELLs
# ---------------------------------------------------------------------------
SCENARIOS.append(dict(
    id="cr4",
    title="Grade 9 ELA: Long-Term ELLs and Written Argument",
    setting="Grade 9 ELA with Integrated ENL (co-taught), argument-writing unit, October",
    intro=T("""
Mr. Brennan teaches a grade 9 ELA class with an ENL co-teacher, Ms. Rahman. The class is in an argument-writing unit built around a news article on whether high schools should ban cell phones during the school day. The co-teachers have gathered information about three students who are Long-Term ELLs.
"""),
    exhibits=[
        dict(title="Exhibit 1: Student Background", content=T("""
Student | Age | Home language | Years in U.S. schools | Home-language literacy | NYSESLAT overall, grades 6 / 7 / 8 | Grade 8 NYSESLAT (Listening / Speaking / Reading / Writing) | Grade 8 NYS ELA test
Kevin | 14 | Spanish | 9 (K–8 in New York City) | Speaks Spanish with his grandmother; does not read or write Spanish | Expanding / Expanding / Expanding | Commanding / Commanding / Expanding / Transitioning | Level 2
Farhana | 14 | Bengali | 9 (K–8) | Speaks Bengali at home; attended weekend Bangla classes for two years; reads simple texts | Expanding / Expanding / Expanding | Commanding / Expanding / Expanding / Transitioning | Level 2
Steeve | 15 | Haitian Creole | 9 (arrived at age 5) | Speaks Haitian Creole at home and some French at church; no formal home-language literacy | Transitioning / Expanding / Expanding | Expanding / Commanding / Transitioning / Transitioning | Level 2
""")),
        dict(title="Exhibit 2: Co-Teacher Observation Notes (Socratic Seminar on the Cell-Phone Article)", content=T("""
– Kevin opened the seminar with a clear claim and two reasons: "Phones shouldn't be banned, because one, emergencies, and two, we use them for school stuff." When a peer disagreed, he answered, "I hear you, but that's a rule problem, not a phone problem."
– Farhana cited the article aloud: "It says, like, 40 percent of teachers think phones are a distraction, so it's not just students complaining." She then challenged Kevin: "But what about kids who can't stop scrolling?"
– Steeve told a story about his cousin's school, where students kept sneaking phones after a ban, and used it as evidence: "So bans don't even work." He drew in a quiet classmate: "What do you think, Ana?"
– All three anticipated the other side aloud at least once (Kevin: "Some people are gonna say phones are distracting, but...").
– Talk was lively and informal ("kinda," "gonna," "like," "stuff"). All three spoke more than the class average.
– Exit reflections. Kevin: "I'm good at arguing. I just hate writing it down." Farhana: "When I write, it sounds like me talking." Steeve: "I don't know the fancy words teachers want."
""")),
        dict(title="Exhibit 3: Argument Essay Excerpts (first body paragraph, first draft)", content=T("""
Kevin: Phones should not be banned in school because like its not fair. Teens need there phones for emergency's and stuff, like what if theres a fire or something and you cant call your mom. Also phones help you in class you can look up things. The school is gonna say phones are distracting but thats not true for everybody so they should just let us have them.

Farhana: In my opinion I think phones are good and bad. Phones can help students learn but some kids are on their phone all day and they dont pay attention so its a problem. The article says 40 percent of teachers say phones are a distraction which is alot. So I think they should have rules but not a ban like you can only use it at lunch.

Steeve: Ok so phones. Everybody got one and schools want to take them away which is crazy. My cousin school banned phones and the kids was still sneaking them so bans dont work. Theres better ways like teaching kids to control theirself and if they cant then the teacher take it.
""")),
        dict(title="Exhibit 4: Argument Rubric Scores (scale of 1–4)", content=T("""
Criterion | Kevin | Farhana | Steeve
Claim | 3 | 3 | 3
Reasons and evidence | 2 | 3 | 2
Counterclaim | 2 | 1 | 1
Formal style and academic vocabulary | 1 | 1 | 1
Organization and transitions | 2 | 2 | 1
Sentence control and conventions | 2 | 2 | 1
""")),
    ],
    prompt=LEAD.format(who="the three Long-Term English Language Learners in Mr. Brennan's class"),
    tasks=[
        "identify one significant strength that the three students share related to English language development, citing specific evidence from the exhibits;",
        "identify one significant need that the three students share related to academic writing, citing specific evidence from the exhibits;",
        "describe one instructional strategy or activity that would build on the identified strength to address the identified need; and",
        "explain why the strategy or activity you described would be effective, grounded in principles of language acquisition and literacy development.",
    ],
    focus="Academic writing for Long-Term ELLs (three students)",
    model=T("""
Kevin, Farhana, and Steeve share a significant strength in oral argumentation: in discussion, they state claims, support them with reasons and evidence, anticipate opposing views, and respond to peers. Their shared need is the academic written register of argument. When they write, they reproduce conversational language, with informal vocabulary, loosely joined sentences, and few formal transitions, so their written arguments are much weaker than their spoken ones.

The strength is documented in Exhibits 1 and 2. All three score Commanding in at least one oral modality and Expanding or higher in both (Exhibit 1). In the seminar (Exhibit 2), Kevin opened with a claim and two reasons and rebutted a peer ("that's a rule problem, not a phone problem"); Farhana cited a statistic from the article and raised a counterargument; and Steeve used his cousin's experience as evidence and drew a classmate in. All three anticipated the other side aloud. These are academic speaking functions, not just social fluency.

The need appears in Exhibits 1, 3, and 4. Writing is the lowest NYSESLAT modality for all three (Transitioning, tied with Reading for Steeve), and all scored Level 2 on the grade 8 ELA test after nine years in U.S. schools. In Exhibit 3, the drafts read like transcripts of talk: "because like its not fair" (Kevin), "In my opinion I think" (Farhana), and "Ok so phones" (Steeve), with run-on sentences throughout. Exhibit 4 confirms the pattern: every student scored 1 on formal style and academic vocabulary, and counterclaims they voiced easily in the seminar earned only 1 or 2 in writing. Farhana names it herself: "When I write, it sounds like me talking."

I would use a "talk-to-text" register-shifting activity built on their seminar contributions. First, I would record a short seminar and give each student a transcript of his or her strongest argument. Second, using a register continuum (talking with friends, then class discussion, then formal essay), we would compare one spoken line with a mentor paragraph and highlight what changes: "gonna say" becomes "may argue," fillers disappear, and ideas are joined with "because," "however," and "as a result." Third, students would rewrite their own claim, reason, and counterclaim as formal sentences, using a phrase bank ("Critics of this policy argue that...; however,..."; "According to the article,..."). Fourth, partners would read drafts aloud and check them against a short list: no fillers, clear sentence boundaries, formal transitions. Finally, students would revise their body paragraphs and add the counterclaim they already voiced.

This approach is effective because it treats their oral skill as the foundation for academic writing rather than as a problem. Cummins' distinction between BICS and CALP explains this profile: Long-Term ELLs often develop strong oral language while academic literacy lags, so they need explicit attention to written academic language. Placing their own words beside a mentor text helps them notice the gap between their language and the target form, which is central to Schmidt's Noticing Hypothesis and Swain's Output Hypothesis. Because the ideas are already theirs, their effort can go to register. Finally, treating informal language as a register suited to other settings, not as "wrong," is asset-based and culturally sustaining, which keeps these experienced students motivated.
"""),
    modelNotes=[
        "Completeness: All four bullets are answered (strength, need, strategy, and explanation), each in a clearly marked paragraph.",
        "Accuracy: The strength is named precisely as oral argumentation, an academic function, rather than \"good English,\" and the need is the written academic register, which fits the classic Long-Term ELL profile.",
        "Depth of Support: It triangulates NYSESLAT modality data, seminar quotations, draft excerpts, rubric scores, and a student reflection.",
        "Depth of Support: The strategy uses the students' own spoken arguments as raw material and moves through clear steps to a revised paragraph.",
        "Accuracy: BICS/CALP, noticing, and output are applied correctly, and informal language is framed as a register, not an error, which is consistent with CR-SE and with language-variation research.",
    ],
    weak=T("""
Kevin, Farhana, and Steeve have been in the United States for a long time, so their strength is that they speak English well and are confident. They talk a lot in class and participate in the seminar, and they are friendly with their classmates. Steeve even helped a quiet student join in.

Their need is grammar and spelling. Kevin writes "there phones" instead of "their phones" and "emergency's." Farhana writes "alot," and Steeve writes "the kids was" and "theirself," which are grammar mistakes. They also do not use capital letters and punctuation correctly, and they got low scores on the rubric.

To fix this, I would correct all of their mistakes in red pen so they can see what they did wrong, and then they would rewrite the essay neatly. I would also give them a grammar packet on subject-verb agreement and homophones like there, their, and they're. They should also read more books at home to improve their writing.

This would be effective because students need to know correct grammar to be good writers, and seeing their errors will help them remember the right way. Krashen says reading gives students input, so reading more books will help them. Long-Term ELLs need extra help with writing so they can pass the Regents exam. If they practice grammar every day, their writing will get better and they will exit ENL.
"""),
    weakNotes=[
        "Completeness: The strength (\"speak English well and are confident\") is vague and partly social. It never names oral argumentation, so the strategy has nothing specific to build on.",
        "Accuracy: The spelling and grammar errors are real but surface-level. The response misses the shared, significant need, which is written academic register (1s on formal style in Exhibit 4).",
        "Accuracy: Calling \"the kids was\" simply a mistake ignores register and language variety, and correcting everything in red pen is overcorrection that can raise anxiety.",
        "Depth of Support: The evidence is a list of errors with no exhibit numbers. The seminar notes and the NYSESLAT speaking–writing gap are ignored.",
        "Depth of Support: The strategy (red pen, grammar packet, reading at home) is isolated and does not use the students' oral strength at all.",
        "Depth of Support: Krashen is cited to justify homework reading, which does not address the identified need.",
    ],
    checklist=[
        "I named oral argumentation (claims, reasons, counterclaims, rebuttals) as the shared strength, not just \"speaks English well.\"",
        "I named written academic register as the shared need and showed that it is the most significant pattern.",
        "I cited NYSESLAT modality data from Exhibit 1 to show the speaking–writing gap.",
        "I quoted at least one line from each student's draft or reflection.",
        "I used the rubric in Exhibit 4 (e.g., 1s on formal style) as evidence.",
        "My strategy uses the students' own spoken arguments as the raw material for writing.",
        "I treated informal language as a register for other settings, not as \"wrong\" or deficient.",
        "I explained the Long-Term ELL profile accurately (BICS vs. CALP) and tied at least one more principle to the evidence.",
    ],
))

# ---------------------------------------------------------------------------
# cr5  High school SIFE newcomers, two students
# ---------------------------------------------------------------------------
SCENARIOS.append(dict(
    id="cr5",
    title="High School SIFE Newcomers: Building Literacy from Life Experience",
    setting="Grade 9 Stand-alone ENL newcomer class with SIFE supports, January",
    intro=T("""
Ms. Petrakis teaches a Stand-alone ENL class for newcomers at a New York City high school. Two of her students were recently identified as Students with Interrupted/Inconsistent Formal Education (SIFE). She has gathered information about them to plan literacy instruction.
"""),
    exhibits=[
        dict(title="Exhibit 1: Student Background", content=T("""
Student | Age | Home language(s) | Time in U.S. schools | Prior schooling and work | Home-language literacy (MLS) | Math placement task | NYSITELL level
Esteban | 16 | Q'anjob'al (also speaks Spanish) | 5 months | Attended school in Spanish in rural Guatemala, grades 1–3; then worked on the family farm and sold produce at the town market | Spanish reading: about grade 2 | Computation at about grade 4 | Entering
Samira | 16 | Arabic | 4 months | Attended school in Yemen, grades 1–2; schooling interrupted by conflict; then sewed and sold clothing with her aunt | Arabic reading: about grade 1 | Computation at about grade 3 | Entering
""")),
        dict(title="Exhibit 2: Teacher Observation Notes", content=T("""
1/8 – Classroom "store" activity with play money: Esteban calculated change in his head faster than any other student and explained his method with gestures and Spanish ("Diez menos siete... three!"). He told me that he handled all the money at his family's market stall.
1/9 – Measuring task: Samira measured fabric strips with a tape measure accurately to the half-centimeter and explained, "This one, 50 centimeter. This one more long, 75." Through an Arabic-speaking classmate, she told the class that she sewed wedding dresses with her aunt and figured out how much cloth to buy.
1/10 – Both students talk eagerly about their work. Esteban: "In my country, I plant corn and coffee. I sell in the market. Saturday, many people." Samira: "I make dress. Very beautiful. My aunt teach me."
1/12 – Both copy accurately from the board, but slowly. Samira copies letter by letter and checks each one.
1/12 – When handed a short printed paragraph, Samira turned the page over. Esteban read the first two words aloud and then stopped.
""")),
        dict(title="Exhibit 3: English Literacy Check (January)", content=T("""
Skill | Esteban | Samira
Gives the sound for each letter (of 26) | 18 (confuses short a, e, and i) | 6
Reads high-frequency words (of 50) | 12 | 3
Decodes consonant-vowel-consonant words (of 10) | 6 | 1
Reads a simple sentence with a picture | with support | not yet
Writes own name and address | yes | name only
""")),
        dict(title="Exhibit 4: Writing Samples (\"Tell about your work in your country\")", content=T("""
Esteban (wrote independently): I work in the campo. I plant corn and cofi. I sel in the market. mi mother an me. Many pipol bay.

Samira (drew a detailed dress with measurements in centimeters and Arabic labels; copied "dress" and "red" from the word wall; then dictated to the teacher): "I make dress for wedding. My aunt and me. I cut, I sew. 3 meter cloth. Very beautiful."
""")),
    ],
    prompt=LEAD.format(who="the two English Language Learners in Ms. Petrakis's class"),
    tasks=[
        "identify one significant strength and one significant need that the two students share related to literacy development, citing specific evidence from the exhibits;",
        "describe one instructional strategy or activity that would build on the identified strength to address the identified need; and",
        "explain why the strategy or activity you described would be effective, grounded in principles of language acquisition and literacy development for students with interrupted formal education.",
    ],
    focus="Foundational literacy for SIFE (two students)",
    model=T("""
Esteban and Samira share a significant strength in the funds of knowledge they bring from work and family responsibilities, especially practical numeracy and measurement, which they eagerly describe orally. Their shared need is foundational English literacy: decoding words and reading simple connected text.

The strength appears throughout the exhibits. Exhibit 1 shows that both students worked for years after their schooling was interrupted, Esteban on a farm and at a market stall and Samira sewing and selling clothing, and both placed higher in math than in home-language reading. In Exhibit 2, Esteban calculated change in his head faster than any classmate, and Samira measured fabric to the half-centimeter and explained, "This one more long, 75." Both talked eagerly about their work in emerging English ("I sell in the market. Saturday, many people"). Exhibit 4 shows the same knowledge on paper: Samira's drawing includes measurements and "3 meter cloth," and Esteban's sample is entirely about his work.

The need is equally clear. Both are SIFE at the Entering level, with home-language reading at about grades 1 to 2 (Exhibit 1). In Exhibit 3, Esteban reads 12 of 50 high-frequency words and decodes 6 of 10 simple words, while Samira reads 3 and decodes 1. In Exhibit 2, Samira turned a printed paragraph face-down and Esteban stopped after two words. Esteban's spellings ("cofi," "sel," "pipol") show that he applies Spanish letter-sound knowledge, which helps him but leaves English vowel patterns to learn.

I would use the Language Experience Approach (LEA), built on their work. First, each student would demonstrate a real task, such as Samira measuring and pricing cloth or Esteban making change at a market, while I introduce key English words with realia and photographs. Second, each student would dictate sentences about the task, and I would write them on chart paper close to how they were spoken ("Samira measures the cloth. She needs 3 meters."). Third, we would read the chart through echo and choral reading while I track the print, and we would reread it daily. Fourth, I would use the text for word work: cutting sentence strips into words to rebuild, highlighting high-frequency words such as "the" and "she," and decoding words from the text such as "cut," "sell," and "red." For Esteban, I would contrast English and Spanish vowel sounds; for Samira, whose first script runs right to left, I would add letter formation and left-to-right tracking. Finally, the typed stories would become a class book, "Our Work," which later supplies math word problems.

LEA is effective because the reading material comes from the students' own language and experience, so it is fully comprehensible, input at Krashen's i+1. Because they already know what the text means, they can focus on decoding. Drawing on their funds of knowledge (Moll) affirms them as capable young adults, which lowers the affective filter for adolescents who may feel embarrassed by beginning reading and reflects the CR-SE Framework. Esteban's Spanish letter-sound knowledge transfers, consistent with Cummins' Common Underlying Proficiency, so instruction can target only what is new. Finally, my scribing and our shared rereading are scaffolds within each student's zone of proximal development that I gradually release as they read and write more independently.
"""),
    modelNotes=[
        "Completeness: It names one shared strength (work-based funds of knowledge, especially numeracy and measurement) and one shared need (foundational English literacy), then gives one strategy and its rationale.",
        "Accuracy: The strategy is age-respectful for 16-year-olds and keeps the students in meaningful, content-connected work, as SIFE research and the CR-SE Framework recommend.",
        "Depth of Support: Evidence is drawn from all four exhibits, with exact literacy-check numbers and the students' own words.",
        "Depth of Support: The LEA steps are concrete (demonstrate, dictate, echo-read, word work, class book) and are differentiated for Spanish transfer and for a new script direction.",
        "Accuracy: Comprehensible input, funds of knowledge, the affective filter, CUP, and the ZPD are each linked to a specific feature of the activity.",
    ],
    weak=T("""
Esteban and Samira are SIFE students, which means they missed a lot of school in their countries. Their strength is that they are good at math. Esteban can count money and Samira can measure things. They are also hard workers and they both like to talk about their jobs.

Their need is that they cannot read or write in English. Samira only knows 6 letter sounds, and Esteban spells words wrong like "cofi" and "pipol." They also did not go to school for many years, so they are behind in all subjects.

Because they are so far behind, I think they should start with the basics. I would give them kindergarten phonics books and alphabet worksheets so they can learn the letters first. They could also use a computer reading program by themselves for 30 minutes a day. When they can read better, they can start learning math and science in English. Samira could also be tested for a learning disability because she is learning very slowly.

This would work because students have to learn the basics before they can learn harder things. The reading program is good because it gives them a lot of practice at their own level. According to Cummins, it takes 5 to 7 years to learn academic language, so they need a lot of practice. The phonics books will also give them comprehensible input, and they will feel successful when they finish each book.
"""),
    weakNotes=[
        "Completeness: \"Good at math\" is close to the strength but is stated generally and is never connected to literacy. The strength is not used in the strategy.",
        "Accuracy: Kindergarten books and alphabet worksheets ignore that these students are 16. Age-inappropriate, isolated materials can embarrass adolescents and reduce engagement.",
        "Accuracy: Delaying math and science until reading improves excludes the students from content learning, and suggesting a disability evaluation after four months confuses typical SIFE literacy development with a disability.",
        "Depth of Support: The response uses a few numbers from Exhibit 3 but never cites an exhibit, and it ignores the oral and work evidence in Exhibits 2 and 4.",
        "Depth of Support: The Cummins 5–7 years figure is accurate but does not explain why this strategy would work, and \"phonics books give comprehensible input\" is unsupported.",
    ],
    checklist=[
        "I named the shared strength as funds of knowledge (work-based numeracy and measurement) that the students can discuss orally.",
        "I named foundational English literacy (decoding and reading connected text) as the shared need.",
        "I cited the SIFE background in Exhibit 1 and specific literacy scores from Exhibit 3.",
        "I quoted the students' own words or writing as evidence (Exhibits 2 and 4).",
        "My strategy is age-respectful for 16-year-olds, not kindergarten materials.",
        "My strategy keeps the students in meaningful learning and does not delay content instruction.",
        "I differentiated for Esteban (Spanish transfer) and Samira (a new script and print direction).",
        "I explained effectiveness with named principles (e.g., comprehensible input, funds of knowledge, CUP, affective filter).",
    ],
))

# ---------------------------------------------------------------------------
# cr6  Grade 3 Dual Language (Spanish/English), one student
# ---------------------------------------------------------------------------
SCENARIOS.append(dict(
    id="cr6",
    title="Grade 3 Dual Language: Building on Spanish Literacy",
    setting="Grade 3 two-way Dual Language (Spanish/English) class, November",
    intro=T("""
Ms. Ortiz teaches English-time literacy in a grade 3 two-way Dual Language program in which students learn in Spanish and English on alternating days. She is analyzing information about one English Language Learner, Camila, to plan English writing instruction. Both writing samples below were written in the same week as part of a personal-narrative unit taught in both languages.
"""),
    exhibits=[
        dict(title="Exhibit 1: Student Background", content=T("""
Item | Information
Age and grade | 8; grade 3
Home language | Spanish (parents speak Spanish at home; an older brother speaks both languages)
Schooling | Born in the Bronx; in the school's two-way Dual Language program since kindergarten
Spanish literacy | Spanish reading inventory: independent at a grade 3 level; Spanish writing: meets grade-level expectations
NYSESLAT (spring of grade 2) | Listening: Expanding; Speaking: Expanding; Reading: Transitioning; Writing: Transitioning
""")),
        dict(title="Exhibit 2: Spanish Personal Narrative (written independently)", content=T("""
El sábado pasado fuimos al parque con toda mi familia. Mi papá preparó sándwiches y mi tía trajo helado de coco.

Primero jugamos fútbol. Mi primo Javier corrió muy rápido, pero se tropezó con una piedra, se cayó y empezó a llorar.
—¡No llores! —le dije—. Yo te ayudo.
Lo llevé donde mi mamá y ella le puso una curita en la rodilla.

Después todos comimos helado debajo de un árbol grande. Cuando regresamos a casa, yo estaba cansada pero muy feliz. ¡Fue el mejor día del otoño!
""")),
        dict(title="Exhibit 3: English Personal Narrative (written independently)", content=T("""
Last saturday I go to the parc whit my family. My dad make sandwichs and my aunt bring ice cream.

First we play soccer. My cousin Javier run very fast but he fall and he start to cry. I say dont cry I will help you. I take him to my mom and she put a band aid on his knee.

Then we eat the ice cream under a big tree. When we come back to my house I was tired but very happy. It was the best day!
""")),
        dict(title="Exhibit 4: Teacher Notes (English Time)", content=T("""
11/12 – Oral retelling of a read-aloud: "The bear go... went into the cave. Then he sleep... he slept all winter." Camila self-corrected two past-tense verbs, but only after pausing.
11/13 – Sharing weekend news: "Yesterday I play with my cousin and we watch a movie." No self-correction.
11/14 – Reading a grade-level English narrative aloud, she read "jumped," "caught," and "ran" correctly and explained that the events "already happened."
11/15 – Writing conference: When I pointed to "fuimos" in her Spanish story, she said, "That's because it already happened. It's pasado." In English she uses "was" and "were" correctly but few other past-tense verbs.
11/15 – Her English narrative follows the same organization as her Spanish one: time-order words, dialogue, and a closing reflection.
""")),
    ],
    prompt=LEAD.format(who="Camila"),
    tasks=[
        "identify one significant strength of the student related to biliteracy development, citing specific evidence from the exhibits;",
        "identify one significant need of the student related to English writing, citing specific evidence from the exhibits;",
        "describe one instructional strategy or activity that would build on the identified strength to address the identified need; and",
        "explain why the strategy or activity you described would be effective, grounded in principles of language acquisition and biliteracy development.",
    ],
    focus="Biliteracy and English writing (one student)",
    model=T("""
Camila has a significant strength in Spanish literacy: strong narrative writing in Spanish, with clear organization and accurate control of past-tense verbs, along with a growing ability to talk about how language works. Her significant need is producing English past-tense verbs, both regular (-ed) and irregular, when she writes about past events.

Her strength is documented in Exhibits 1, 2, and 4. She reads independently at grade level in Spanish and meets grade-level expectations in Spanish writing (Exhibit 1). Her Spanish narrative in Exhibit 2 is well organized, uses correctly punctuated dialogue, and ends with a reflection ("¡Fue el mejor día del otoño!"). It uses past tenses accurately and with variety, including the preterite ("fuimos," "trajo," "se cayó") and the imperfect ("estaba"). In Exhibit 4, she explained that "fuimos" is used "because it already happened," which shows that she understands past time and can reflect on language. Exhibit 4 also notes that her English narrative follows the same organization as her Spanish one, so this strength is already transferring.

Her need is just as clear. In Exhibit 3, nearly every past event is written in the present: "I go," "my dad make," "my aunt bring," "he fall," "we eat." Only "was" is correct. The same pattern appears in her speech in Exhibit 4 ("Yesterday I play... we watch"), where she self-corrects only occasionally and after a pause ("go... went"). Because she reads past-tense verbs correctly and knows the events "already happened," the issue is not understanding past time. She has not yet acquired the English forms for producing it. This is a typical interlanguage pattern, not interference from Spanish, which marks the past clearly.

I would use a Spanish–English "Bridge," a planned cross-linguistic comparison that fits the Dual Language model. First, Camila and a partner would highlight the past-tense verbs in her Spanish narrative. Second, we would build a chart matching each Spanish verb to the verb she wrote for the same event in English and then to the English past form: "fuimos / go / went," "jugamos / play / played," "se cayó / fall / fell." Third, we would discuss the difference: Spanish changes the verb ending, while English adds -ed to regular verbs and uses a new form for irregular ones. She would sort her verbs into "add -ed" and "new word" columns and keep the chart as a personal bilingual reference. Fourth, she would revise her English narrative with a partner, reading it aloud and checking each verb against the chart. Finally, in later drafts, she would underline time words such as "last Saturday" as a cue to check her verbs.

This activity is effective because it starts from Camila's strong Spanish literacy. Cummins' Common Underlying Proficiency and Developmental Interdependence hypotheses explain why her understanding of past time and narrative structure can support English: the Bridge maps known concepts onto new forms. Side-by-side comparison draws her attention to the English forms she is missing, which Schmidt argues is necessary for acquisition, and revising aloud gives pushed output in which she can notice the gap (Swain). Her self-corrections in Exhibit 4 show that the forms are emerging, so focused noticing is at her i+1. Finally, using Spanish as a resource reflects translanguaging pedagogy (García) and the Blueprint's call to leverage home language.
"""),
    modelNotes=[
        "Completeness: Each of the four bullets has its own paragraph: a Spanish literacy strength, an English writing need, one strategy, and the rationale.",
        "Accuracy: It correctly identifies the past-tense pattern as developmental (interlanguage), not as negative transfer, because Spanish marks the past clearly and Camila controls it.",
        "Depth of Support: It compares Exhibits 2 and 3 verb by verb and uses Exhibit 4 to show that she understands past time, which pinpoints the need as production of English forms.",
        "Depth of Support: The Bridge is described in concrete, sequenced steps that end in revision and future self-monitoring.",
        "Accuracy: CUP, Developmental Interdependence, noticing, output, and translanguaging are each linked to her evidence, and the strategy respects the Dual Language model.",
    ],
    weak=T("""
Camila is a good student in the Dual Language program. Her strength is that she can write in two languages. She wrote a story in Spanish and a story in English about the same day at the park, and both of her stories are long and have a lot of details about her family.

Her need is spelling and Spanish interference. She writes "parc" because it is like "parque" in Spanish, "whit" instead of "with," and "sandwichs." She also forgets capital letters, like "saturday." Her verbs are also wrong because Spanish grammar is getting in the way of her English.

I would help Camila by having her write only in English during English time and not use any Spanish, so the two languages do not get mixed up. I would give her a spelling list with the words she misspelled, and she could practice them every night. I would also teach a lesson on capital letters for days of the week. When she writes, I would give her a checklist to edit her work.

This would be effective because separating the languages helps students not confuse them. Contrastive analysis says that the first language causes errors in the second language, so we need to keep them apart. The spelling practice will help her remember the correct spelling. Using a checklist is a good scaffold. Camila will become a better writer in English.
"""),
    weakNotes=[
        "Completeness: \"She can write in two languages\" is true but vague. It never identifies her specific Spanish strengths (organization, accurate past tense, talking about language), so the strategy cannot build on them.",
        "Accuracy: It blames Spanish for her verb errors, but Spanish marks past tense clearly. The pattern is developmental, and her Spanish knowledge is actually a resource.",
        "Accuracy: Keeping Spanish out of her thinking during English time treats the home language as a problem and works against Dual Language biliteracy goals and the Blueprint's call to leverage home language.",
        "Depth of Support: Spelling and capitalization are minor, scattered issues. The most significant pattern, past events written in the present, is mentioned only in passing and without evidence.",
        "Depth of Support: Contrastive Analysis is misapplied to justify separating the languages, and the strategy (spelling list, checklist) is generic and isolated.",
    ],
    checklist=[
        "I named a specific Spanish literacy strength (narrative organization and accurate past tense), not just \"she is bilingual.\"",
        "I named ONE focused need (English past-tense verb forms), not a list of spelling and capitalization errors.",
        "I compared Exhibits 2 and 3 directly to show what transfers and what does not.",
        "I used Exhibit 4 to show that she understands past time, so the need is producing the English forms.",
        "I did not blame Spanish. I described the pattern as developmental and treated Spanish as a resource.",
        "My strategy uses her own Spanish text to teach the English forms (a planned bridge, not random translation).",
        "My strategy fits the Dual Language model and ends in revision or new writing.",
        "I explained effectiveness with named theory (CUP, noticing, output, translanguaging) tied to her evidence.",
    ],
))

# ---------------------------------------------------------------------------
# cr7  Grade 10 Integrated ENL global history, two students
# ---------------------------------------------------------------------------
SCENARIOS.append(dict(
    id="cr7",
    title="Grade 10 Global History: Strong Readers, Quiet Voices",
    setting="Grade 10 Integrated ENL Global History and Geography (co-taught), unit on the Industrial Revolution",
    intro=T("""
Mr. Lindqvist, an ENL teacher, co-teaches a grade 10 Integrated ENL Global History and Geography class. The class is analyzing primary-source documents to answer the question "Did the Industrial Revolution improve life for working people?" The co-teachers have gathered information about two English Language Learners.
"""),
    exhibits=[
        dict(title="Exhibit 1: Student Background (NYSESLAT results from spring of grade 9)", content=T("""
Student | Age | Home language | Time in U.S. schools | Prior schooling | Listening | Speaking | Reading | Writing
Oksana | 15 | Ukrainian (also reads Russian) | 1½ years | Uninterrupted schooling in Kharkiv; studied world history through grade 8 | Transitioning | Emerging | Expanding | Transitioning
Tahmid | 16 | Bengali | 2 years | Uninterrupted Bangla-medium schooling in Dhaka through grade 8; studied history, and English as a subject | Expanding | Transitioning | Expanding | Transitioning
""")),
        dict(title="Exhibit 2: Document Analysis Worksheets (Document 2: excerpt from 1832 testimony by a former child mill worker to a committee of the British Parliament)", content=T("""
Question | Oksana | Tahmid
Historical context | Britain, early 1800s. Factories grew fast and needed many cheap workers, so children worked in textile mills. | The factory system spread to cities. Owners hired children because they could pay them less.
Main idea | Children worked about 14 hours a day and were beaten if they were slow. | Child workers had long hours, dangerous machines, and punishment.
Sourcing: purpose and point of view | He speaks to Parliament to show bad conditions so that a law will change them. He was a victim, so his view is very negative. | The worker wants reform. He may exaggerate, but Documents 3 and 4 show similar conditions, so it is mostly reliable.
Rubric score (1–4) | 4 | 4
""")),
        dict(title="Exhibit 3: Co-Teacher Observation Notes", content=T("""
– In the whole-class discussion, Oksana did not speak during the first 15 minutes. Her documents were heavily annotated with notes in Ukrainian and English.
– In the small-group discussion (Exhibit 4), Tahmid answered in short phrases and looked down at his notes, which listed five well-chosen pieces of evidence with document numbers.
– In a pair task with a Bengali-speaking classmate, Tahmid discussed the documents at length in Bangla, comparing the mills in the documents with garment factories he had read about at home.
– After class, Oksana told me, "I know the answer, but when I speak I need time. They speak so fast, and then the topic is changed."
– Oksana's exit ticket: "I partly disagree with Marcus. Wages rose after 1850, but Document 2 shows children worked 14 hours in dangerous mills, and Document 4 shows cholera in crowded cities. So for workers in the early Industrial Revolution, life became worse."
""")),
        dict(title="Exhibit 4: Small-Group Discussion Transcript", content=T("""
Teacher: Tahmid, what evidence shows that factory conditions were harmful?
Tahmid: Document 2. The children... work long. Many hours.
Marcus: Yeah, but didn't wages go up later? So life got better.
Tahmid: [long pause] Yes... but... [looks at notes]
Teacher: Oksana, do you agree with Marcus?
Oksana: I agree... maybe.
Marcus: See, she agrees.
Oksana: [shakes head slightly; does not speak]
""")),
    ],
    prompt=LEAD.format(who="the two English Language Learners in Mr. Lindqvist's class"),
    tasks=[
        "identify one significant strength and one significant need that the two students share related to English language development, citing specific evidence from the exhibits;",
        "describe one instructional strategy or activity that would build on the identified strength to address the identified need; and",
        "explain why the strategy or activity you described would be effective, grounded in principles of language acquisition and content-area instruction.",
    ],
    focus="Oral academic language in social studies (two students)",
    model=T("""
Oksana and Tahmid share a significant strength in reading and analyzing primary-source documents, supported by strong prior knowledge of history. Their shared need is oral academic language for discussion: stating a claim, citing evidence, and responding to peers, especially disagreeing politely and with reasons, in real time.

The strength is evident in Exhibits 1, 2, and 3. Both had uninterrupted schooling that included history, and Reading is their highest NYSESLAT modality (Expanding) (Exhibit 1). Both earned a 4 on the document analysis in Exhibit 2. They described the historical context accurately, identified the main idea, and evaluated the source: Oksana noted that the speaker "was a victim, so his view is very negative," and Tahmid checked reliability against Documents 3 and 4. Exhibit 3 describes Oksana's heavily annotated documents and Tahmid's notes listing five well-chosen pieces of evidence. Oksana's exit ticket even builds a nuanced argument that weighs Documents 2 and 4 against rising wages.

Their need appears when they must speak. Speaking is the lowest modality for both (Emerging and Transitioning). In Exhibit 4, Tahmid answered in fragments ("The children... work long") and could not respond when Marcus raised wages. Oksana said "I agree... maybe" and then let Marcus misstate her view, although her exit ticket shows she partly disagrees. Her comment in Exhibit 3, "I know the answer, but when I speak I need time," and Tahmid's long discussion in Bangla show that the problem is not ideas or content knowledge. It is the English language of academic discussion under time pressure.

I would use a document-based Structured Academic Controversy (SAC). First, I would form groups of four, made up of two pairs, and assign each pair a position: the Industrial Revolution improved, or worsened, life for workers. Second, pairs would prepare a "talk card" from their annotated documents: a claim, two pieces of evidence with document numbers, and a sentence explaining each. They could draft in Ukrainian or Bangla first. Third, partners would rehearse aloud with frames such as "According to Document __,...", "This shows that...", and "I partly agree with __, but...". Fourth, each pair would present while the other pair listened, paraphrased ("What I heard you say is..."), and then responded. Fifth, pairs would switch positions and argue the other side. Finally, the group would drop the assigned roles and write a consensus statement. I would build in wait time and assess speaking with a short checklist.

The SAC is effective because it turns their reading strength into the content of their talk. Preparing from their own documents gives them something worth saying, and rehearsal with frames lowers the affective filter (Krashen) that Oksana describes. The paraphrase-and-respond structure creates negotiation of meaning, with clarification requests and confirmation checks, which Long's Interaction Hypothesis links to acquisition. Presenting and arguing both sides provides repeated pushed output (Swain) in academic functions such as citing, conceding, and rebutting. Drafting in the home language draws on Cummins' Common Underlying Proficiency, since their historical reasoning already exists in Ukrainian and Bangla. Finally, the structure is a scaffold that can be faded as they gain confidence in open discussion.
"""),
    modelNotes=[
        "Completeness: It names one shared strength (document reading and analysis) and one shared need (oral academic discussion), then gives one strategy and its rationale.",
        "Accuracy: It correctly treats the problem as academic language under time pressure, not shyness, using Oksana's comment and Tahmid's fluent Bangla discussion as proof.",
        "Depth of Support: It contrasts the transcript (Exhibit 4) with the exit ticket and worksheets, which is strong triangulation that the ideas are present but the oral English is not.",
        "Depth of Support: The SAC is described in concrete steps (prepare, rehearse, present, paraphrase, switch, reach consensus) that require speaking rather than letting the students avoid it.",
        "Accuracy: The interaction, output, affective filter, and CUP principles are each tied to a specific structure in the activity.",
    ],
    weak=T("""
Oksana and Tahmid are good students who come from strong schools in their countries. Their strength is writing, because Oksana's exit ticket is very good and they both got 4s on the document worksheet. They also take a lot of notes.

Their need is that they are shy and do not participate in class. Oksana did not talk for 15 minutes, and Tahmid looked at his notes instead of talking. In Exhibit 4, Oksana only said "I agree... maybe." They need more confidence when they speak.

To help them, I would call on them more often so they get used to speaking in front of the class. I would also give participation points so they are motivated to talk. They could practice pronunciation with an app at home, because their accents might make them nervous. Another idea is to let them write their answers instead of speaking, since writing is their strength and they would feel more comfortable.

This would help because practice makes perfect, and the more they speak, the better they will get. According to the affective filter hypothesis, students who are nervous do not learn well, so we need to make them comfortable in class. Participation points are also a good motivation for high school students. With these strategies, Oksana and Tahmid will become more confident speakers and do better in Global History.
"""),
    weakNotes=[
        "Accuracy: The strength is mislabeled as \"writing.\" Exhibit 2 is a reading-analysis task and Writing is only Transitioning for both, so the real strength is reading and analyzing documents (Reading: Expanding).",
        "Accuracy: Framing the need as shyness turns a language need (academic speaking functions) into a personality trait. Oksana's \"I need time\" and Tahmid's fluent Bangla discussion show that it is not shyness.",
        "Depth of Support: Cold-calling and participation points raise anxiety, which contradicts the affective filter principle the response itself cites.",
        "Completeness: The response offers several ideas instead of one, and letting them write instead of speak avoids the need instead of addressing it.",
        "Depth of Support: Pronunciation and \"accents\" are not supported by any exhibit, and \"practice makes perfect\" is not a language acquisition principle.",
    ],
    checklist=[
        "I named the strength as reading and analyzing documents (not \"writing\") and supported it with the Exhibit 2 scores.",
        "I named the need as oral academic language for discussion, not \"shyness\" or \"confidence.\"",
        "I used the NYSESLAT pattern from Exhibit 1 (Reading highest, Speaking lowest).",
        "I quoted the transcript (Exhibit 4) and contrasted it with the exit ticket or Oksana's comment.",
        "My strategy uses the students' document annotations as preparation for speaking.",
        "My strategy includes rehearsal, frames, and wait time instead of cold-calling.",
        "My strategy requires them to speak; it does not let them avoid the need by writing instead.",
        "I explained effectiveness with named principles (interaction, output, affective filter, CUP) tied to the evidence.",
    ],
))

# ---------------------------------------------------------------------------
# cr8  Grade 4 Stand-alone ENL, mixed home languages, three students
# ---------------------------------------------------------------------------
SCENARIOS.append(dict(
    id="cr8",
    title="Grade 4 Stand-alone ENL: Accurate Readers, Missing Words",
    setting="Grade 4 Stand-alone ENL group with mixed home languages, December",
    intro=T("""
Ms. Kowalski teaches a grade 4 Stand-alone ENL group whose members speak different home languages, so English is their shared language in the group. The class is reading a grade-level informational text, "How Animals Survive Winter." She has gathered information about three students to plan reading instruction.
"""),
    exhibits=[
        dict(title="Exhibit 1: Student Background (NYSESLAT results from spring of grade 3)", content=T("""
Student | Age | Home language | Time in U.S. schools | Prior schooling and home-language literacy | Listening | Speaking | Reading | Writing
Yousef | 9 | Arabic | 2 years | Attended school in Egypt, grades 1–2; reads and writes Arabic at about grade level | Transitioning | Transitioning | Transitioning | Emerging
Nusrat | 9 | Bengali | 2 years | Attended school in Bangladesh, grades 1–2; reads Bangla with her mother | Expanding | Transitioning | Transitioning | Transitioning
Jean-Marc | 10 | Haitian Creole (also some French) | 3 years | Attended grade 1 in Haiti, with instruction in French and Haitian Creole | Expanding | Expanding | Transitioning | Transitioning
""")),
        dict(title="Exhibit 2: Running Records on \"How Animals Survive Winter\" (grade 4 informational text)", content=T("""
Student | Accuracy | Self-correction rate | Words per minute | Retelling (key ideas, of 6) | Words flagged with a "?" sticky note
Yousef | 96% | 1:3 | 92 | 2 | survive, scarce, shelter, store
Nusrat | 98% | 1:4 | 101 | 3 | scarce, gather, reduce
Jean-Marc | 97% | 1:3 | 108 | 2 | survive, scarce, store, hibernate
""")),
        dict(title="Exhibit 3: Think-Aloud Excerpts and Teacher Note", content=T("""
Yousef (reading "Food is scarce in winter"): "Scarce... I don't know this word. I read it again... 'scarce in winter.' Scary? Food is scary? No, that doesn't make sense." [puts a "?" sticky note on the word and keeps reading]
Nusrat (reading "Some animals gather food in the fall"): "Gather... like together? I'm not sure. I'll skip it." [Her retelling later leaves out that animals store food.]
Jean-Marc (reading "Animals must survive the cold"): "Survive... in French, survivre? Maybe it means stay alive? I'm not sure, so I'll ask my partner."
Teacher note: All three stop when meaning breaks down and mark the word. Their only fix-up strategies are rereading, skipping, or asking a partner.
""")),
        dict(title="Exhibit 4: Vocabulary and Comprehension Check", content=T("""
Measure | Yousef | Nusrat | Jean-Marc
Tier 2 words from the text: matches word to meaning (of 10) | 3 | 4 | 4
Comprehension questions that do NOT depend on a key word (of 5) | 4 | 5 | 4
Comprehension questions that depend on a key word, e.g., "Why do some animals store food?" (of 5) | 1 | 2 | 1
""")),
    ],
    prompt=LEAD.format(who="the three English Language Learners in Ms. Kowalski's group"),
    tasks=[
        "identify one significant strength and one significant need that the three students share related to reading comprehension, citing specific evidence from the exhibits;",
        "describe one instructional strategy or activity that would build on the identified strength to address the identified need; and",
        "explain why the strategy or activity you described would be effective, grounded in principles of language acquisition and literacy development.",
    ],
    focus="Reading comprehension and vocabulary (three students)",
    model=T("""
Yousef, Nusrat, and Jean-Marc share a significant strength in accurate decoding combined with active self-monitoring: they read grade-level text accurately and notice when a word breaks down meaning. Their shared need is knowledge of general academic (Tier 2) vocabulary, along with strategies for working out unfamiliar words, which limits their comprehension.

The strength is documented in Exhibits 2 and 3. All three read the grade 4 text with 96–98% accuracy and self-corrected at rates of 1:3 or 1:4, so they catch many of their own errors. Each flagged unfamiliar words with sticky notes. The think-alouds in Exhibit 3 show genuine monitoring: Yousef rejected "scary" because "Food is scary? No, that doesn't make sense," and Jean-Marc stopped at "survive" to test a French connection. The teacher notes that all three stop when meaning breaks down. These are the habits of active readers.

The need is equally consistent. Their retellings captured only 2 or 3 of 6 key ideas (Exhibit 2), and they flagged the same high-utility words: "scarce" (all three) and "survive" and "store" (two each). In Exhibit 4, they matched only 3 or 4 of 10 Tier 2 words. Most tellingly, they answered 4 or 5 of 5 questions that did not depend on a key word but only 1 or 2 of 5 that did. Exhibit 3 explains why: their only fix-up strategies are rereading, skipping, or asking a partner, so Nusrat skipped "gather" and lost the idea that animals store food. They know when they don't understand; they don't yet know what to do next.

I would use a "click and clunk" vocabulary routine, adapted from Collaborative Strategic Reading, that builds directly on their habit of flagging words. First, before reading, I would teach four high-utility Tier 2 words from the text (survive, scarce, gather, store) with student-friendly definitions, pictures, gestures, and examples. Students would add home-language equivalents using bilingual glossaries or family help, and Jean-Marc would also note French cognates such as "survivre." Second, during reading, students would keep flagging "clunks," now with a fix-up card: reread the sentence and the ones around it for clues, look for a familiar word part, think of a home-language connection, and then ask a partner or check the glossary. Third, after reading, each student would share one clunk and explain how he or she fixed it, and we would use the target words orally in frames such as "In winter, food is scarce, so animals ___." Finally, we would revisit the words all week through word sorts and quick discussions.

This routine is effective because it turns an existing metacognitive habit into a complete strategy. CALLA (Chamot and O'Malley) calls for explicit teaching of metacognitive strategies; these students already monitor, so adding fix-up strategies completes the cycle. Beck, McKeown, and Kucan show that Tier 2 words carry the most comprehension value and that multiple, rich encounters build lasting knowledge. Pre-teaching key words makes the text comprehensible input at i+1 (Krashen). Linking new words to home-language equivalents draws on Common Underlying Proficiency, since the concepts likely already exist in Arabic, Bengali, and Haitian Creole. Because cognates mainly help Jean-Marc, glossaries support Yousef and Nusrat. Finally, sharing clunks in English, the group's common language, creates authentic negotiation of meaning (Long).
"""),
    modelNotes=[
        "Completeness: Every bullet is answered, and the strength and need are stated as a matched pair: they notice the problem but lack the words and the fix-up strategies.",
        "Accuracy: It pins the need precisely on Tier 2 vocabulary by using Exhibit 4's contrast between questions that depend on a key word and those that do not, rather than calling it \"comprehension\" in general.",
        "Depth of Support: It uses exact running-record data, the flagged-word lists, and quotations from each think-aloud.",
        "Depth of Support: The strategy builds on what the students already do (flagging words) and is laid out step by step with multiple exposures to the target words.",
        "Accuracy: It differentiates home-language support correctly. Cognates help the French and Haitian Creole speaker, while glossaries serve the Arabic and Bengali speakers, avoiding a one-size-fits-all cognate strategy.",
    ],
    weak=T("""
Yousef, Nusrat, and Jean-Marc are good readers. Their strength is fluency because they read 92, 101, and 108 words per minute, which is fast. They also know many words because their accuracy is over 95 percent, and they work hard in class.

Their need is that they do not understand what they read. Their retelling scores were low, only 2 or 3 out of 6, and they got many questions wrong on the comprehension check. They need to work on comprehension so they can understand grade 4 texts.

I would help them by giving them easier books at their independent reading level so they can understand better. I would also teach the main idea strategy, and they could use a graphic organizer to write the main idea and details. Another idea is to have them use cognates to figure out words, since cognates are helpful for ELLs. They could also listen to audiobooks at home.

This will work because when students read books at their level, they understand more and enjoy reading. Graphic organizers are a good scaffold for ELLs. Cognates help ELLs learn English vocabulary faster. According to Krashen's input hypothesis, students need comprehensible input, so easier books will give them input they can understand. With more practice, their comprehension will improve and they will do better on the state test in the spring.
"""),
    weakNotes=[
        "Accuracy: \"They know many words\" contradicts Exhibit 4 (3 or 4 of 10 Tier 2 words), and reading rate alone is a thin strength. The response misses self-monitoring, the strength the strategy should build on.",
        "Accuracy: \"Comprehension\" is too broad. Exhibit 4 shows that they answer questions well unless a key word is involved, so the precise need is Tier 2 vocabulary.",
        "Accuracy: Recommending cognates for all three ignores that Arabic and Bengali share few cognates with English, a one-size-fits-all strategy.",
        "Depth of Support: Easier books lower rigor instead of scaffolding grade-level text, and several unrelated ideas (a main-idea organizer, audiobooks) replace one focused strategy.",
        "Depth of Support: Krashen's input hypothesis is misused to justify simplified text, and the response never cites an exhibit by number.",
    ],
    checklist=[
        "I named self-monitoring with accurate decoding as the shared strength, citing self-correction rates and sticky notes.",
        "I named Tier 2 vocabulary (and word-learning strategies) as the shared need, not \"comprehension\" in general.",
        "I used the contrast in Exhibit 4 (questions that depend on a key word vs. those that do not) to pinpoint the need.",
        "I quoted at least one think-aloud from Exhibit 3.",
        "My strategy builds on what the students already do (flagging words) rather than starting from scratch.",
        "I differentiated home-language supports: cognates for the French and Haitian Creole speaker, glossaries for the Arabic and Bengali speakers.",
        "My strategy keeps the grade-level text and includes multiple exposures to the target words.",
        "I explained effectiveness with named principles (Beck's tiers, CALLA, i+1, CUP) tied to the evidence.",
    ],
))

# ===========================================================================
# CR skill-builder questions (7.1–7.4), 8 per skill
# ===========================================================================
QUESTIONS = [
    # ---------------- 7.1 Identifying significant strengths ----------------
    dict(
        id="7.1-01", skill="7.1", type="analysis", difficulty=1, diag=0,
        stimulus=T("""
Grade 3 ELL (Transitioning), personal narrative:
First my famly and me went to Coney Island. Next we rode the Cyclone and my sister scream very loud. After that we ate hot dogs on the boardwalk. Finally we watch the fireworks and I felt happy and tired. It was the best day of the summer.
"""),
        stem="Which of the following is the most significant strength in this student's writing that a teacher could build on?",
        options=[
            "Consistent control of regular past-tense endings such as -ed throughout the whole piece",
            "Correct capitalization of place names such as Coney Island and the Cyclone",
            "Clear chronological organization signaled by sequence words and a closing sentence",
            "A willingness to write about personal experiences from outside of school",
        ],
        answer=2,
        why="The narrative moves in clear time order (First, Next, After that, Finally) and ends with a concluding sentence. Text organization is a significant, transferable writing skill that a teacher can build on, for example by adding detail or more varied transitions. On the CR, state strengths as language or literacy skills supported by evidence.",
        traps=[
            {"code": "LITERAL", "note": "Irregular past forms are correct (went, rode, ate), but regular endings are missing in 'scream' and 'watch,' so this is not a strength."},
            {"code": "PARTIAL", "note": "The capitalization is accurate, but it is a minor surface feature, not a significant skill to build instruction on."},
            None,
            {"code": "PARTIAL", "note": "Willingness is a disposition, not a language or literacy skill. CR strengths should be stated as skills shown in the evidence."},
        ],
        key="State strengths as specific language or literacy skills visible in the evidence, not dispositions or minor surface features.",
    ),
    dict(
        id="7.1-02", skill="7.1", type="analysis", difficulty=1, diag=0,
        stimulus=T("""
Grade 6 ELL, Spanish, 2 years in U.S. schools
NYSESLAT (spring): Listening, Expanding; Speaking, Expanding; Reading, Emerging; Writing, Emerging
Teacher note: Retells read-alouds in detail and explains her math reasoning aloud to her group; avoids independent reading.
"""),
        stem="Which of the following is the most significant strength the teacher could build on for this student?",
        options=[
            "Oral language: she understands spoken English well and explains her ideas aloud",
            "Independent reading habits that support her comprehension of grade-level texts",
            "Mathematical problem solving that is well above grade-level expectations",
            "Balanced proficiency across all four modalities, as shown by her NYSESLAT results",
        ],
        answer=0,
        why="Listening and Speaking are both Expanding, and the teacher sees detailed retellings and clear oral explanations, while Reading and Writing are Emerging. Her oral language is the significant strength, and it can be used to reach the literacy need, for example through oral rehearsal before writing or discussion before reading. NYSESLAT modality patterns often point to the strength (highest modality) and the need (lowest).",
        traps=[
            None,
            {"code": "LITERAL", "note": "The note says she avoids independent reading, and her Reading level is Emerging. This option contradicts the evidence."},
            {"code": "PARTIAL", "note": "She explains math reasoning aloud, but nothing shows above-grade-level math. The strength to build on is the oral language she uses to explain it."},
            {"code": "LITERAL", "note": "Her scores show a clear gap (Expanding oral skills, Emerging literacy), not balance."},
        ],
        key="Compare NYSESLAT modalities: the highest often signals the strength to build on, and the lowest signals the need.",
    ),
    dict(
        id="7.1-03", skill="7.1", type="analysis", difficulty=2, diag=1,
        stimulus=T("""
Grade 7 Integrated ENL science, small-group talk (two Spanish-speaking ELLs)
Luis: The water goes up, like, it disappears?
Marisol: No, no desaparece. It's evaporación, evaporation. The sun heats it and it changes to gas, vapor de agua. Then up high it gets cold and makes drops again. Condensation, condensación. That's the clouds.
Luis: Ah, okay, so it comes back as rain.
Marisol: Yes. Precipitation.
"""),
        stem="Which of the following is the most significant strength Marisol shows that the teacher could build on?",
        options=[
            "Her accurate pronunciation of multisyllabic English science terms",
            "Her readiness to stop using Spanish now that she knows the English terms",
            "Her patience and leadership in helping a classmate who becomes confused",
            "Her understanding of the water cycle and strategic use of cognates to explain it",
        ],
        answer=3,
        why="Marisol explains the whole water cycle accurately and moves between Spanish and English (evaporación/evaporation, condensación/condensation) to clarify meaning for Luis. That shows both content understanding and strategic translanguaging with cognates, which a teacher can build on with cognate charts and bilingual explanations that lead to English academic writing. Using two languages strategically is an asset, not a deficit.",
        traps=[
            {"code": "LITERAL", "note": "A written transcript can't show pronunciation. This latches onto a surface detail instead of what she actually demonstrates."},
            {"code": "DEFICIT", "note": "Treating Spanish as something to drop treats the home language as a crutch. Her use of both languages is a strength."},
            {"code": "PARTIAL", "note": "She is helpful, but that is a social trait. The CR asks for a strength related to language and literacy development."},
            None,
        ],
        key="Strategic use of the home language and cognates to explain content is a strength (translanguaging), not evidence of weak English.",
    ),
    dict(
        id="7.1-04", skill="7.1", type="analysis", difficulty=2, diag=0,
        stimulus=T("""
Student | Home language | Years in U.S. schools | Evidence from the exhibits
Ahmed | Arabic | 2 | Reads Arabic at grade level; summarizes read-alouds accurately; neat handwriting
Mei | Mandarin | 1 | Strong Chinese literacy; summarizes read-alouds accurately; top math scores
Rosa | Spanish | 3 | Little prior schooling; summarizes read-alouds accurately; enthusiastic in class
"""),
        stem="A constructed-response prompt asks for one significant strength that all three students share. Which strength is best supported by the evidence?",
        options=[
            "Grade-level home-language literacy that can transfer to English reading",
            "Listening comprehension of grade-level texts that are read aloud",
            "Mathematical reasoning that can anchor academic vocabulary instruction",
            "Enthusiasm and a positive attitude toward learning English in class",
        ],
        answer=1,
        why="Only one strength appears for all three students: each summarizes read-alouds accurately, which shows listening comprehension of grade-level text. When a prompt says 'that the students share,' list each student's evidence beside the candidate strength. If one student has no evidence, the strength doesn't qualify. Home-language literacy is a real asset for two students, but not a shared one.",
        traps=[
            {"code": "PARTIAL", "note": "This is true for Ahmed and Mei, but Rosa had little prior schooling, so it isn't shared."},
            None,
            {"code": "LITERAL", "note": "Only Mei's top math scores are mentioned. This latches onto one student's detail."},
            {"code": "PARTIAL", "note": "Enthusiasm is noted only for Rosa, and it is a disposition rather than a language skill."},
        ],
        key="A shared strength must have evidence for every student; check each name before you commit.",
    ),
    dict(
        id="7.1-05", skill="7.1", type="analysis", difficulty=2, diag=2,
        stimulus=T("""
Grade 10 ELL, Karen home language; SIFE; 6 months in U.S. schools; NYSITELL: Entering
Prior schooling: about 3 years at a school in a refugee camp in Thailand
Teacher notes: Reads a few English sight words. Through a Karen-speaking peer, she explained to the class how her family grew vegetables in the camp, including how far apart to plant seedlings and when to water. During a math warm-up, she correctly estimated the area of the school garden plot in square meters.
"""),
        stem="Which of the following is the most significant strength the ENL teacher could build on in planning literacy instruction for this student?",
        options=[
            "Her knowledge of a few English sight words, which shows she is ready for grade-level novels",
            "Her familiarity with U.S.-style school routines from her years of camp schooling",
            "Her practical knowledge of gardening and measurement, which she can explain orally",
            "Her reliance on a Karen-speaking peer, which shows strong social and collaborative skills",
        ],
        answer=2,
        why="Her detailed explanation of gardening and her accurate area estimate show funds of knowledge (Moll): real-world expertise she can talk about. A teacher can build literacy on it, for example through Language Experience Approach texts about gardening, which give her comprehensible, meaningful material for learning to read. For SIFE, background knowledge from work and family life is often the most powerful strength in the exhibits.",
        traps=[
            {"code": "WRONG_LEVEL", "note": "A few sight words is an emerging skill. Treating it as readiness for grade-level novels mismatches her current literacy level."},
            {"code": "LITERAL", "note": "Nothing in the notes says her camp school resembled U.S. routines. This assumes facts not in evidence."},
            None,
            {"code": "PARTIAL", "note": "Working through a peer shows resourcefulness, but it is a social behavior, not the literacy-related strength the task asks for."},
        ],
        key="For SIFE, look for funds of knowledge (work, family, or community expertise) as a strength to build literacy on.",
    ),
    dict(
        id="7.1-06", skill="7.1", type="analysis", difficulty=1, diag=0,
        stimulus=T("""
Grade 2 ELL, Haitian Creole, reading a level-appropriate text aloud
Text: The little dog ran to the park.
Student: The little dog run... ran to the... the park.
Text: He saw a big red ball.
Student: He saw a big... bag... no, ball. Red ball.
Summary: accuracy 94%; self-correction rate 1:2; retold the main events in order.
"""),
        stem="Which reading strength does this record most clearly show?",
        options=[
            "Fluent, expressive phrasing throughout the passage",
            "Accurate decoding of every word on the first attempt",
            "Inferential comprehension of the story's central theme and message",
            "Self-monitoring: noticing when a word doesn't fit and fixing it",
        ],
        answer=3,
        why="He self-corrects 'run' to 'ran' and 'bag' to 'ball,' and a 1:2 self-correction rate means he fixes about one of every two errors he makes. That is self-monitoring: checking that the reading looks right and makes sense. It is a significant strength that a teacher can build on by teaching more fix-up strategies.",
        traps=[
            {"code": "LITERAL", "note": "The pauses and repetitions ('to the... the park') show that the reading is not yet fluent or expressive."},
            {"code": "LITERAL", "note": "He misread 'ran' and 'ball' at first. The strength is that he caught and fixed those errors."},
            {"code": "PARTIAL", "note": "He retold the main events, which shows literal comprehension, but nothing shows inference about theme. Self-correction is the clearer pattern."},
            None,
        ],
        key="A high self-correction rate signals self-monitoring, a strength to build on with explicit fix-up strategies.",
    ),
    dict(
        id="7.1-07", skill="7.1", type="analysis", difficulty=3, diag=0,
        stimulus=T("""
Grade 10 ELL, Spanish; in U.S. schools since kindergarten (Long-Term ELL); NYSESLAT: Speaking, Commanding; Writing, Transitioning
Class debate excerpt:
Student: Okay, so I get what you're saying about the cost, but think about it. If the city doesn't fix the subway now, it's gonna cost way more later. That's literally what the article said about the old bridge upstate. So your point actually helps my side.
"""),
        stem="Which statement of this student's strength would be most useful for planning instruction in written argument?",
        options=[
            "Conversational fluency (BICS) developed through years of social interaction in English",
            "Oral argumentation: conceding a point, rebutting it, and citing a text as evidence",
            "Command of formal academic vocabulary and register in spoken English",
            "A confident, persuasive personality that engages peers during debates",
        ],
        answer=1,
        why="The student concedes ('I get what you're saying'), rebuts ('it's gonna cost way more later'), cites a source ('what the article said'), and turns the opponent's point into support. These are academic argument functions, and they map directly onto the parts of a written argument (claim, counterclaim, evidence, reasoning). Stating the strength this precisely points straight to a strategy, such as turning a discussion transcript into a formal paragraph.",
        traps=[
            {"code": "TERM", "pair": "BICS ↔ CALP", "note": "Calling this social fluency (BICS) undersells it. Conceding, rebutting, and citing evidence are academic language functions that map onto written argument."},
            None,
            {"code": "LITERAL", "note": "'Gonna' and 'literally' show an informal register. The strength is the argument structure, not formal vocabulary."},
            {"code": "PARTIAL", "note": "Confidence may be real, but it describes personality, not a language skill a writing strategy can build on."},
        ],
        key="State strengths precisely, as specific language functions, so they point directly to a strategy.",
    ),
    dict(
        id="7.1-08", skill="7.1", type="analysis", difficulty=3, diag=0,
        stimulus=T("""
Grade 4 Dual Language ELL, Spanish home language
Spanish opinion piece (excerpt): Creo que los perros son las mejores mascotas. Primero, son leales. Por ejemplo, mi perra Luna me espera en la puerta todos los días. Segundo, nos ayudan a hacer ejercicio. En conclusión, los perros son los mejores amigos.
English opinion piece (excerpt): I think cats is the best pets. First, they are very clean. For example my cat Tito wash himself all the days. Second they dont need walks so they are good for familys that work. In conclusion cats are the better pets.
"""),
        stem="Which of the following is the most significant strength to build on in this student's English writing?",
        options=[
            "Transfer of opinion-essay structure (claim, reasons, example, conclusion) from Spanish",
            "Accurate subject–verb agreement in English, carried over from her Spanish writing",
            "Use of a personal example to support a reason, which makes the opinion convincing",
            "Keeping Spanish words out of her English writing, which shows the languages are separate",
        ],
        answer=0,
        why="Both pieces follow the same opinion structure: a claim, reasons marked First and Second, a supporting example, and a conclusion. That is positive transfer of literacy skills from Spanish (Cummins' Common Underlying Proficiency), and it is the most significant strength because it frames the whole piece. A teacher can build on it, for example by using her Spanish piece to plan English reasons and transitions.",
        traps=[
            None,
            {"code": "LITERAL", "note": "'Cats is' and 'Tito wash' show that subject–verb agreement is still developing in English."},
            {"code": "PARTIAL", "note": "The personal example is real and effective, but it is one piece of the larger strength: the whole opinion structure transferred from Spanish."},
            {"code": "DEFICIT", "note": "Treating the absence of Spanish as the strength implies the home language contaminates English. The key strength is the transferred structure."},
        ],
        key="Look for writing structures that transfer from the home language to English; they reflect Common Underlying Proficiency.",
    ),

    # ---------------- 7.2 Identifying significant needs ----------------
    dict(
        id="7.2-01", skill="7.2", type="analysis", difficulty=1, diag=0,
        stimulus=T("""
Grade 4 ELL, Mandarin, Emerging
Journal entry: Yesterday I go park. Play ball with brother. Is fun. Then home, eat dinner.
"""),
        stem="Which of the following is the most significant need shown in this writing sample?",
        options=[
            "Spelling common one- and two-syllable words accurately",
            "Adding figurative language to make the writing more vivid",
            "Organizing the events of the day into a clear beginning, middle, and end",
            "Producing complete sentences with subjects and past-tense verbs",
        ],
        answer=3,
        why="Most sentences lack a subject ('Play ball,' 'Is fun') or a verb ('Then home'), and past events use the base form ('I go'). Mandarin does not mark tense on verbs and allows subjects to be dropped when they are clear from context, so these patterns are expected. Building complete sentences with subjects and past-tense verbs is the most significant need.",
        traps=[
            {"code": "LITERAL", "note": "Every word in the sample is spelled correctly. Spelling is not the issue."},
            {"code": "WRONG_LEVEL", "note": "Figurative language is not a priority for an Emerging writer whose sentences lack subjects and verbs."},
            {"code": "LITERAL", "note": "The entry already follows time order (Yesterday... Then). Organization is not the gap."},
            None,
        ],
        key="Prioritize the need that most limits meaning; for Emerging writers this is often sentence-level structure.",
    ),
    dict(
        id="7.2-02", skill="7.2", type="analysis", difficulty=1, diag=0,
        stimulus=T("""
Grade 5 ELL, Bengali, Transitioning
Running record on a grade-level text: accuracy 98%; 112 words per minute; retelling: 2 of 6 key ideas
Student comment: I can read all the words, but I don't know what some of them mean, like migrate and temporary.
"""),
        stem="Based on this evidence, which need should the teacher prioritize?",
        options=[
            "Decoding multisyllabic words with greater accuracy",
            "Building academic vocabulary knowledge to support comprehension",
            "Increasing reading rate through repeated timed readings",
            "A special education evaluation, since comprehension lags behind decoding",
        ],
        answer=1,
        why="She decodes accurately and at a good rate, but her retelling captures only 2 of 6 key ideas, and she names unknown words (migrate, temporary). The need is academic (Tier 2) vocabulary, which limits comprehension. Accurate decoding with weak comprehension is a common ELL profile and calls for vocabulary instruction, not more decoding practice.",
        traps=[
            {"code": "LITERAL", "note": "98% accuracy shows decoding is a strength, not a need."},
            None,
            {"code": "LITERAL", "note": "112 words per minute shows that rate is not the problem. This fixates on a number instead of the key evidence."},
            {"code": "MISREFERRAL", "note": "A vocabulary gap in a Transitioning ELL is typical second-language development, not evidence of a disability."},
        ],
        key="Accurate decoding plus weak retelling usually points to a vocabulary and language need, not a decoding need.",
    ),
    dict(
        id="7.2-03", skill="7.2", type="analysis", difficulty=2, diag=1,
        stimulus=T("""
Student | Response to: Why did the author include the map?
Ana (Spanish) | The map is nice. It shows the river and the mountains and the city.
Dmitri (Russian) | Author put map. Map show where is river and mountains.
Farah (Urdu) | In the map there is river, mountain and city also. Is very colorful.
"""),
        stem="Which need do all three students share that is most significant for this task?",
        options=[
            "Explaining the author's purpose rather than describing what the map shows",
            "Using the articles 'a' and 'the' correctly before singular nouns",
            "Forming direct questions with correct English word order",
            "Adding more descriptive adjectives to their sentences about the map",
        ],
        answer=0,
        why="The question asks why the author included the map, but all three describe what the map shows. The shared, significant need is explaining the author's purpose, an academic language function (e.g., 'The author included the map to help readers see...'). Article errors are real for two students, but they are neither shared nor central to the task.",
        traps=[
            None,
            {"code": "PARTIAL", "note": "Dmitri and Farah omit articles (Russian and Urdu have no articles), but Ana uses them correctly, so this need isn't shared."},
            {"code": "LITERAL", "note": "No one is asking a question. 'Where is river' is an embedded clause, and it appears only in Dmitri's response."},
            {"code": "LITERAL", "note": "More description would move them further from the task. They need to explain purpose, not describe."},
        ],
        key="A shared need must appear in every student's evidence and matter for the task, not just be the most visible error.",
    ),
    dict(
        id="7.2-04", skill="7.2", type="scenario", difficulty=2, diag=0,
        stimulus=T("""
Grade 3 ELL, Pashto, 11 months in U.S. schools, Emerging
Home-language literacy: reads and writes Pashto at about grade level (confirmed with an interpreter)
English: knows 30 sight words; decodes consonant-vowel-consonant words slowly; retells read-alouds accurately in Pashto and in simple English
Classroom teacher: He's still not reading English after almost a year. Should we refer him for special education?
"""),
        stem="Which statement most accurately identifies this student's primary need?",
        options=[
            "A special education evaluation, because slow English decoding after a year suggests a reading disability",
            "Intensive oral English practice, with English reading postponed until he speaks English more fluently",
            "Explicit instruction in English decoding and print conventions that builds on his Pashto literacy",
            "More English reading at home in place of Pashto reading, so that he gets additional English practice",
        ],
        answer=2,
        why="He reads at grade level in Pashto, so he already understands how reading works. What is new is English letter–sound correspondences and left-to-right print (Pashto uses an Arabic-based script written right to left). His need is explicit English decoding instruction that builds on that foundation. Nothing in the evidence suggests a disability; his oral comprehension is strong in both languages.",
        traps=[
            {"code": "MISREFERRAL", "note": "Grade-level Pashto literacy and accurate retellings show strong underlying ability. Slow English decoding after 11 months is typical second-language development."},
            {"code": "EXCLUSION", "note": "Postponing reading until oral fluency develops withholds literacy instruction he is ready for, given his home-language literacy."},
            None,
            {"code": "DEFICIT", "note": "Replacing Pashto reading discards the literacy foundation that supports English through transfer."},
        ],
        key="Strong home-language literacy with slow early English decoding signals a second-language decoding need, not a disability.",
    ),
    dict(
        id="7.2-05", skill="7.2", type="analysis", difficulty=2, diag=2,
        stimulus=T("""
Grade 8 Integrated ENL science; Expanding ELL, Polish home language; oral explanation of photosynthesis:
So the plant, it takes the light from the sun and the air stuff, the CO2, and the water from the roots, and it makes, like, food for itself, sugar, and then it gives out the oxygen thing.
"""),
        stem="Which of the following best describes this student's most significant need?",
        options=[
            "Understanding the basic inputs and outputs of photosynthesis",
            "Using precise disciplinary vocabulary and structures to explain the process",
            "Pronouncing multisyllabic scientific terms such as 'photosynthesis' clearly",
            "Relying less on Polish when he discusses science content in class",
        ],
        answer=1,
        why="The science is right, but the language is everyday: 'the air stuff,' 'gives out the oxygen thing,' 'makes, like, food.' His need is academic language, meaning precise terms (absorbs, carbon dioxide, glucose, releases) and structures such as 'Plants use light energy to convert...'. This is a CALP need, not a content gap.",
        traps=[
            {"code": "LITERAL", "note": "He correctly names light, carbon dioxide, water, sugar, and oxygen. He understands the concept."},
            None,
            {"code": "LITERAL", "note": "Nothing in the evidence concerns pronunciation. This invents a problem the transcript doesn't show."},
            {"code": "DEFICIT", "note": "He doesn't use Polish here, and treating the home language as something to reduce is a deficit view."},
        ],
        key="When the concept is right but the wording is everyday, the need is academic (disciplinary) language, not content.",
    ),
    dict(
        id="7.2-06", skill="7.2", type="analysis", difficulty=1, diag=0,
        stimulus=T("""
Grade 11 ELL; Mixteco and Spanish; SIFE; 3 months in U.S. schools; Entering
Prior schooling: 2 years of primary school in Oaxaca, Mexico
Home-language literacy: recognizes some Spanish letters; does not yet read connected text
Observations: speaks Spanish fluently and some Mixteco; participates eagerly in oral activities; has worked in construction with his uncle
"""),
        stem="Which need is most significant for this student's literacy instruction?",
        options=[
            "Analyzing complex sentence structures in grade-level novels",
            "Learning U.S. holidays and customs before academic work begins",
            "Building his conversational Spanish so that it can support English learning",
            "Foundational literacy: print concepts, letter sounds, and decoding",
        ],
        answer=3,
        why="With two years of schooling and no connected reading in any language, his most significant need is foundational literacy, taught with age-respectful materials. His fluent oral Spanish and work experience are strengths to build on, for example through Language Experience Approach texts about construction. SIFE need foundational literacy alongside, not instead of, meaningful content.",
        traps=[
            {"code": "WRONG_LEVEL", "note": "Analyzing complex syntax in novels assumes reading skills he hasn't developed yet."},
            {"code": "PARTIAL", "note": "Cultural orientation can help newcomers, but it isn't a literacy need, and academic work shouldn't wait for it."},
            {"code": "LITERAL", "note": "He already speaks Spanish fluently. That is a strength, not a need."},
            None,
        ],
        key="For SIFE with limited literacy in any language, the priority need is foundational literacy taught with age-appropriate materials.",
    ),
    dict(
        id="7.2-07", skill="7.2", type="analysis", difficulty=3, diag=0,
        stimulus=T("""
Grade 3 Dual Language ELL, Spanish home language, Transitioning
Spanish narrative: Ayer fuimos a la playa. Mi hermano encontró un cangrejo y lo puso en un balde.
English narrative: Yesterday we go to the beach. My brother find a crab and he put it in a bucket.
Teacher note: Reads English past-tense verbs correctly; explains that she wrote 'fuimos' because it already happened.
"""),
        stem="Which statement most accurately identifies this student's need and its likely source?",
        options=[
            "English past-tense forms; a developmental pattern, since she controls the past in Spanish",
            "English past-tense forms; negative transfer, since Spanish does not mark past tense on verbs",
            "The concept of past time, which she has not yet developed in either of her languages",
            "English past-tense forms; a possible language disability, since the errors appear in every sentence",
        ],
        answer=0,
        why="She uses the Spanish preterite accurately and can explain why, so she understands past time. What she hasn't acquired is the English forms (went, found). Leaving verbs in the base form is a common developmental interlanguage pattern, not negative transfer, since Spanish marks past tense. Identifying the source correctly matters, because it points to a strategy that uses her Spanish as a resource (a cross-linguistic bridge) rather than suppressing it.",
        traps=[
            None,
            {"code": "MISAPPLIED_THEORY", "note": "Spanish marks past tense clearly (fuimos, encontró, puso), so Contrastive Analysis would not predict this error. It is developmental."},
            {"code": "LITERAL", "note": "She uses Spanish past forms accurately and explains that the events already happened, so she understands past time."},
            {"code": "MISREFERRAL", "note": "Unmarked past tense is a typical interlanguage stage for ELLs, not evidence of a disability."},
        ],
        key="Before blaming transfer, check whether the home language actually lacks the feature; many errors are developmental.",
    ),
    dict(
        id="7.2-08", skill="7.2", type="analysis", difficulty=3, diag=0,
        stimulus=T("""
Grade 8 ELL, Russian, Expanding; argument essay excerpt:
Schools should start later in the morning. Teenagers need more sleep. Article says that 70 percent of students sleep less than eight hours. Also, many students take bus at 6:30. In conclusion, schools should start later.
Rubric (1–4): Claim 3; Evidence 3; Reasoning (explains how evidence supports the claim) 1; Conventions 2
"""),
        stem="Which need is most significant to address first in this student's argument writing?",
        options=[
            "Using articles correctly, as in 'The article says' and 'take the bus'",
            "Adding more statistics so that the evidence is stronger and more varied",
            "Explaining how each piece of evidence supports the claim",
            "Acknowledging and responding to an opposing claim",
        ],
        answer=2,
        why="The essay lists facts after the claim but never explains how they support it (for example, 'Because 70 percent sleep less than eight hours, a later start would...'). The rubric confirms that reasoning (1) is the weakest criterion. Article errors are frequent but local, and they don't block meaning. Prioritize the need that most limits the purpose of the task.",
        traps=[
            {"code": "PARTIAL", "note": "Article errors are common for Russian speakers (Russian has no articles), but they don't block meaning, and reasoning is the weakest criterion."},
            {"code": "LITERAL", "note": "Evidence already scores 3. Adding more facts without explanation would repeat the real problem."},
            None,
            {"code": "PARTIAL", "note": "Addressing counterclaims is a grade 8 expectation, but reasoning is the weakest area, and a counterclaim also depends on reasoning."},
        ],
        key="Prioritize global needs that limit the task's purpose (e.g., reasoning) over frequent local errors that don't block meaning.",
    ),

    # ---------------- 7.3 Selecting a strategy ----------------
    dict(
        id="7.3-01", skill="7.3", type="scenario", difficulty=1, diag=0,
        stimulus="Grade 2 ELLs (Transitioning) tell detailed, well-sequenced stories about their weekends during morning meeting. Their written stories are only one or two sentences long.",
        stem="Which strategy would best build on the students' strength to address their need?",
        options=[
            "Having students copy a model story from the board to practice sentence structure",
            "Having partners tell their stories aloud, sketch each part, and then write from the sketches",
            "Assigning daily grammar worksheets on sentence structure before any story writing",
            "Reducing the writing requirement to a single sentence so that every student experiences success",
        ],
        answer=1,
        why="Telling the story aloud uses the students' oral strength, and sketching each part creates a plan that keeps the detail and sequence they already produce orally. Writing from the sketches bridges oral to written language. This talk-to-write sequence gives pushed output and a scaffold that can later be removed.",
        traps=[
            {"code": "PASSIVE", "note": "Copying is passive. Students produce none of their own language and don't use their storytelling strength."},
            None,
            {"code": "ISOLATED", "note": "Decontextualized worksheets separate grammar from meaningful writing and ignore the oral strength."},
            {"code": "LOWER_RIGOR", "note": "Shrinking the task lowers expectations instead of scaffolding students toward fuller writing."},
        ],
        key="Bridge an oral strength to a writing need with talk-to-write: rehearse aloud, plan visually, then write.",
    ),
    dict(
        id="7.3-02", skill="7.3", type="scenario", difficulty=2, diag=1,
        stimulus="Grade 6 Integrated ENL science. Three Spanish-speaking ELLs (Transitioning) had strong schooling in Spanish, read science texts in Spanish at grade level, and explain concepts well in Spanish. On English unit quizzes, they miss items containing words such as evaporation, transparent, and conclusion.",
        stem="Which instructional strategy would best build on the students' strength to address their need?",
        options=[
            "Requiring English-only discussion during science so the students stop translating everything in their heads",
            "Assigning lists of English science definitions to memorize for weekly vocabulary quizzes",
            "Teaching students to find Spanish–English cognates in science texts and record them on a bilingual chart",
            "Providing simplified English summaries of each unit that leave out technical vocabulary",
        ],
        answer=2,
        why="Academic English vocabulary in science is largely Latin-based, so many terms have Spanish cognates (evaporación, transparente, conclusión). Because these students already know the concepts and words in Spanish, cognate study turns their home-language literacy into immediate English vocabulary. This reflects Cummins' Common Underlying Proficiency and positive transfer.",
        traps=[
            {"code": "DEFICIT", "note": "Banning Spanish discards the strong literacy and content knowledge that are the students' greatest asset."},
            {"code": "ISOLATED", "note": "Memorizing definition lists is decontextualized and doesn't use the students' Spanish knowledge."},
            None,
            {"code": "LOWER_RIGOR", "note": "Removing technical vocabulary lowers rigor. The students need access to these words, not less exposure."},
        ],
        key="For students literate in a Romance language, cognate instruction turns home-language academic vocabulary into English vocabulary.",
    ),
    dict(
        id="7.3-03", skill="7.3", type="scenario", difficulty=2, diag=0,
        stimulus="Grade 7 Integrated ENL science. Two ELLs (Emerging) conduct investigations carefully, record accurate data, and correctly predict outcomes. Their written lab conclusions are single sentences such as: The ice melt fast in hot water.",
        stem="Which activity would best build on the students' strength to address their need?",
        options=[
            "Having students copy the teacher's model conclusion into their science notebooks after each lab",
            "Excusing the students from written lab conclusions until their English proficiency improves",
            "Teaching a separate grammar lesson on past-tense verbs before the next lab begins",
            "Using a claim–evidence–reasoning frame that cites their own data, rehearsed orally first",
        ],
        answer=3,
        why="The students' accurate data and predictions are the raw material for a strong conclusion. A claim–evidence–reasoning frame shows them how to turn that data into a scientific explanation, and oral rehearsal with a partner lets them try the language before writing. The strategy moves them from context-embedded lab work toward context-reduced academic writing, with scaffolds.",
        traps=[
            {"code": "PASSIVE", "note": "Copying the teacher's conclusion gives students no chance to explain their own data in their own words."},
            {"code": "EXCLUSION", "note": "Excusing them from writing removes them from the grade-level task instead of scaffolding it."},
            {"code": "ISOLATED", "note": "A stand-alone grammar lesson doesn't use their lab strength or teach the language of scientific explanation."},
            None,
        ],
        key="Use students' own data and hands-on knowledge as evidence in scaffolded claim–evidence–reasoning writing.",
    ),
    dict(
        id="7.3-04", skill="7.3", type="scenario", difficulty=2, diag=2,
        stimulus="Grade 9 SIFE newcomers (Entering) with two to three years of prior schooling. Both have extensive work experience (one repaired motorcycles, the other cooked in a family restaurant) and describe their work eagerly in their home languages and simple English. Both are just beginning to decode English.",
        stem="Which strategy would best build on the students' strength to address their literacy need?",
        options=[
            "Language Experience Approach texts the students dictate about their work, used for rereading and word study",
            "Kindergarten decodable books about family pets, read independently every day to build reading fluency",
            "Postponing reading instruction until the students have built more oral English vocabulary",
            "Daily phonics worksheets on letter sounds, completed silently at their desks during class",
        ],
        answer=0,
        why="In the Language Experience Approach, students' own oral accounts become their first reading texts. Because the texts come from their work experience (funds of knowledge), the content is familiar and comprehensible, so they can focus on decoding and word study. LEA also respects their age and expertise, which matters for adolescent SIFE.",
        traps=[
            None,
            {"code": "WRONG_LEVEL", "note": "Kindergarten books about pets are not age-appropriate for adolescents and ignore their experience."},
            {"code": "EXCLUSION", "note": "Delaying literacy instruction withholds what they most need. Oral and written English can develop together."},
            {"code": "ISOLATED", "note": "Silent worksheets drill sounds out of context and don't draw on the students' rich oral knowledge."},
        ],
        key="For SIFE with rich life experience, LEA turns their oral accounts into comprehensible, age-respectful reading texts.",
    ),
    dict(
        id="7.3-05", skill="7.3", type="scenario", difficulty=1, diag=0,
        stimulus="Grade 9 Long-Term ELLs (Expanding) argue persuasively during class discussions, giving reasons and rebutting peers. Their essays use conversational language such as gonna, like, and stuff, and they score 1 of 4 on formal style.",
        stem="Which activity would best build on the students' strength to address their need?",
        options=[
            "Circling every informal word in red on their drafts and returning the drafts to be recopied neatly",
            "Assigning more independent reading of novels at home so that students absorb a formal style",
            "Rewriting points from their own discussion transcripts in formal register, using a mentor text",
            "Moving the students into a beginning-level grammar class to review the basics of English",
        ],
        answer=2,
        why="Their oral arguments already contain claims, reasons, and rebuttals. Rewriting their own spoken points in formal register, guided by a mentor text, makes the gap between talk and academic writing visible (noticing) and gives them a model to aim for. This uses the strength directly to address the written-register need typical of Long-Term ELLs.",
        traps=[
            {"code": "OVERCORRECT", "note": "Marking every informal word focuses on errors without teaching the register shift, and it can raise anxiety."},
            {"code": "PARTIAL", "note": "Wide reading helps over time, but it doesn't use their oral strength or explicitly teach the register shift."},
            None,
            {"code": "WRONG_LEVEL", "note": "These are Expanding students. A beginning-level grammar class doesn't match their proficiency and is demotivating."},
        ],
        key="For Long-Term ELLs, turn strong oral argument into formal writing by explicitly shifting register with mentor texts.",
    ),
    dict(
        id="7.3-06", skill="7.3", type="scenario", difficulty=2, diag=0,
        stimulus="Grade 10 Integrated ENL global history. Two ELLs (Reading: Expanding; Speaking: Emerging) annotate and analyze primary sources accurately but rarely speak in discussions. One says: I know the answer, but I need time to say it.",
        stem="Which strategy would best build on the students' strength to address their need?",
        options=[
            "A structured discussion in which students prepare talk cards from their annotations and rehearse with a partner",
            "Cold-calling the students often during whole-class discussion so they practice speaking under real conditions",
            "Letting the students submit written responses instead of participating in class discussions",
            "Assigning pronunciation drills with minimal pairs to build the students' confidence in speaking",
        ],
        answer=0,
        why="Their document annotations give them something worth saying, and preparing talk cards and rehearsing with a partner gives them the time and language they say they need. The structure lowers the affective filter while still requiring academic speaking, and peer interaction creates negotiation of meaning. The frames and rehearsal can be faded as they gain confidence.",
        traps=[
            None,
            {"code": "WRONG_LEVEL", "note": "Unprepared, high-pressure speaking doesn't match an Emerging speaker's needs and raises anxiety."},
            {"code": "EXCLUSION", "note": "Replacing discussion with writing avoids the need instead of addressing it and removes the students from academic talk."},
            {"code": "ISOLATED", "note": "Minimal-pair drills are decontextualized and don't build the academic discussion language the students need."},
        ],
        key="Turn a reading strength into prepared talk: plan from texts, rehearse with frames, then discuss.",
    ),
    dict(
        id="7.3-07", skill="7.3", type="scenario", difficulty=3, diag=0,
        stimulus="Kindergarten Stand-alone ENL. Four ELLs (Emerging) love chants and rhyming songs. On a screener they identify rhymes (8–9 of 10) and clap syllables (9–10 of 10), but they segment three-sound words into phonemes at only 0–2 of 10.",
        stem="Which activity would best build on the students' strength to address their need?",
        options=[
            "Reading aloud more rhyming picture books each day to deepen the students' enjoyment of rhyme",
            "Reviewing alphabet flashcards daily, with students naming each letter and its sound in turn",
            "Assigning lists of decodable nonsense words for students to blend independently at their seats",
            "Taking rhyming words from a familiar chant and segmenting them into sounds with Elkonin boxes",
        ],
        answer=3,
        why="Phonological awareness develops from larger units (syllables, rhymes) to smaller ones (phonemes). Starting with rhyming words from a chant the children already love, then segmenting those words with Elkonin boxes, moves them along that continuum and keeps phoneme work in their zone of proximal development. Reading more rhyming books is enjoyable but stays at the level they have already mastered.",
        traps=[
            {"code": "PARTIAL", "note": "This builds on the strength but stays at the rhyme level. It doesn't move students to the phoneme-level need."},
            {"code": "ISOLATED", "note": "Flashcard drills are decontextualized and target letter knowledge, not the phoneme segmenting the screener shows is weak."},
            {"code": "WRONG_LEVEL", "note": "Independent nonsense-word blending assumes phonemic awareness and letter–sound skills these kindergartners don't yet have."},
            None,
        ],
        key="Move along the phonological-awareness continuum: use mastered rhyme and syllable skills as a springboard to phoneme segmenting.",
    ),
    dict(
        id="7.3-08", skill="7.3", type="scenario", difficulty=3, diag=0,
        stimulus="Grade 4 Stand-alone ENL. Three ELLs (Transitioning) whose home languages are Arabic, Bengali, and Haitian Creole read grade-level text with 96–98% accuracy and flag unknown words with sticky notes. When stuck, they only reread or skip, and they miss questions that depend on words like scarce and gather.",
        stem="Which strategy would best build on the students' strength to address their need?",
        options=[
            "Teaching all three to rely on English–home-language cognates as their main word-learning strategy",
            "Teaching fix-up strategies for the words they flag, along with explicit instruction in key Tier 2 words",
            "Pre-teaching every unfamiliar word in the text by having students copy the definitions from a dictionary",
            "Moving the students to texts at their independent level so that fewer words need to be flagged",
        ],
        answer=1,
        why="The students already monitor comprehension by flagging unknown words. Teaching fix-up strategies (context clues, word parts, home-language connections, asking a peer) turns that habit into a complete strategy (CALLA metacognitive strategies). Explicit instruction in high-utility Tier 2 words (Beck, McKeown & Kucan) addresses the vocabulary gap directly. Cognates help only some learners, and easier texts avoid the problem.",
        traps=[
            {"code": "ONE_SIZE", "note": "Haitian Creole shares many cognates with English through French, but Arabic and Bengali share few, so this won't work for all three."},
            None,
            {"code": "ISOLATED", "note": "Copying dictionary definitions is decontextualized, and pre-teaching every word is less effective than focusing on high-utility Tier 2 words."},
            {"code": "LOWER_RIGOR", "note": "Easier texts avoid the vocabulary students need for grade-level learning instead of scaffolding it."},
        ],
        key="Build on self-monitoring by adding fix-up strategies and explicit Tier 2 instruction, with supports matched to each home language.",
    ),

    # ---------------- 7.4 Explaining effectiveness ----------------
    dict(
        id="7.4-01", skill="7.4", type="application", difficulty=1, diag=0,
        stimulus="An ENL teacher lets grade 5 ELLs with strong Spanish literacy brainstorm and outline in Spanish before they write an English essay. Their English essays become more detailed and better organized.",
        stem="Which principle best explains why this strategy is effective?",
        options=[
            "Cummins' Common Underlying Proficiency: skills learned in one language support the other",
            "Lenneberg's Critical Period Hypothesis: language is acquired most easily before puberty",
            "Behaviorism: language is learned through habit formation and the reinforcement of responses",
            "Krashen's Natural Order Hypothesis: grammatical morphemes are acquired in a set order",
        ],
        answer=0,
        why="Cummins' Common Underlying Proficiency (the 'iceberg' model) holds that concepts and literacy skills developed in one language are available in another. Planning in Spanish lets students use their full reasoning and organizational skills, which then transfer to English writing. On the CR, CUP is the go-to rationale for any strategy that uses home-language literacy.",
        traps=[
            None,
            {"code": "MISAPPLIED_THEORY", "note": "The critical period concerns age and ultimate attainment. It doesn't explain why planning in Spanish improves English writing."},
            {"code": "MISAPPLIED_THEORY", "note": "Behaviorism explains learning through drill and reinforcement, not transfer of ideas and organization across languages."},
            {"code": "MISAPPLIED_THEORY", "note": "The Natural Order Hypothesis describes the sequence of grammar acquisition, not cross-language transfer of literacy skills."},
        ],
        key="Use Cummins' Common Underlying Proficiency to explain strategies that let students think, plan, or read in the home language.",
    ),
    dict(
        id="7.4-02", skill="7.4", type="analysis", difficulty=2, diag=0,
        stimulus="A candidate's CR identifies the shared strength as sequential oral retelling (all three students scored 5/5 on a sequencing listening check in Exhibit 2) and the shared need as explaining in writing why a character changes. The strategy is partner oral rehearsal with 'because' frames before writing.",
        stem="Which sentence from the candidate's explanation would best demonstrate Depth of Support?",
        options=[
            "This strategy will be effective because ELLs need scaffolding and comprehensible input in order to succeed in school.",
            "Research shows that oral rehearsal is a best practice that works well for all students in every grade and content area.",
            "Krashen, Cummins, Vygotsky, and Swain all support the use of oral language with English Language Learners in classrooms.",
            "Since all three already sequence events accurately (Exhibit 2), rehearsal frees them to focus on causal language, within their ZPD.",
        ],
        answer=3,
        why="Depth of Support means appropriate examples and details that show sound reasoning. The keyed sentence links an exhibit-based fact (5/5 sequencing) to a mechanism (attention is freed for new language) and to a named principle (ZPD). Generic or name-only explanations earn less credit because they don't show why the strategy fits these students.",
        traps=[
            {"code": "PARTIAL", "note": "True but generic. It could be pasted into any response and isn't tied to these students' evidence."},
            {"code": "ONE_SIZE", "note": "Claiming it works for all students ignores the specific profile. Scorers reward reasoning about these learners."},
            {"code": "PARTIAL", "note": "Naming four theorists without explaining any connection shows recall, not reasoning."},
            None,
        ],
        key="Explain effectiveness by linking exhibit evidence to a named principle and to how it works for these students.",
    ),
    dict(
        id="7.4-03", skill="7.4", type="application", difficulty=2, diag=1,
        stimulus="Before writing, each ELL explains her claim aloud to a partner. Partway through, one student stops: Wait, I said she feel sad, but I need to say why. She felt lonely because she had no friends. She then revises her written plan.",
        stem="Which theory best explains the benefit shown in this moment?",
        options=[
            "Krashen's Input Hypothesis, because she received comprehensible input from her partner",
            "Swain's Output Hypothesis, because producing language led her to notice a gap and revise",
            "Krashen's Affective Filter Hypothesis, because partner talk lowered her level of anxiety",
            "Schumann's Acculturation Model, because peer interaction reduced her social distance",
        ],
        answer=1,
        why="Swain's Output Hypothesis holds that producing language pushes learners to notice gaps between what they want to say and what they can say, to test hypotheses, and to reflect on form. The student noticed that 'she feel sad' didn't express her reasoning and reformulated it with the past tense and 'because.' That is the noticing function of output.",
        traps=[
            {"code": "TERM", "pair": "Input Hypothesis ↔ Output Hypothesis", "note": "The benefit came from her own speaking, not from input. This confuses input with output."},
            None,
            {"code": "PARTIAL", "note": "Partner talk may lower anxiety, but that doesn't explain the key moment: she noticed a gap in her own language and fixed it."},
            {"code": "MISAPPLIED_THEORY", "note": "Acculturation concerns social and psychological distance from the target-language group, not self-correction during a task."},
        ],
        key="When speaking or writing leads learners to notice and fix gaps, cite Swain's Output Hypothesis.",
    ),
    dict(
        id="7.4-04", skill="7.4", type="analysis", difficulty=2, diag=2,
        stimulus=T("""
Candidate's claim: All three students need to support their ideas with text evidence in writing.
Exhibit 2 (observation): All three students point to the correct page when asked where an event happened.
Exhibit 3 (rubric, 'Supports ideas with text evidence,' scale 1–4): Ana 1, Bao 1, Chidi 2.
Exhibit 4 (writing): Ana: Mia is brave. Bao: She was happy at the end. Chidi: Mia is nicer because she made a friend.
"""),
        stem="Which sentence would provide the strongest support for the candidate's claim?",
        options=[
            "In Exhibit 2, all three students point to the correct page when asked where an event happened.",
            "Chidi writes, 'Mia is nicer because she made a friend,' which shows that he does not use evidence.",
            "In Exhibit 3, all three score 1–2 on using text evidence, and in Exhibit 4 none quotes or cites the text.",
            "Their writing suggests that they were probably never taught how to find text evidence in the earlier grades.",
        ],
        answer=2,
        why="The keyed sentence names two exhibits, gives exact data for all three students, and shows the pattern in both scores and work samples (triangulation). That is what Depth of Support looks like when citing a need. Exhibit 2 is still useful, but as evidence of a strength the strategy can build on: they can locate information.",
        traps=[
            {"code": "LITERAL", "note": "This is evidence of a strength (locating information), not of the need. It could support the strategy, but it doesn't prove the claim."},
            {"code": "PARTIAL", "note": "It cites only one student, and Chidi does give a reason. A shared need requires evidence for all three."},
            None,
            {"code": "LITERAL", "note": "This is speculation about past instruction that appears nowhere in the exhibits. Scorers credit evidence, not guesses."},
        ],
        key="Support a shared need with exhibit-labeled evidence covering every student, ideally from more than one source.",
    ),
    dict(
        id="7.4-05", skill="7.4", type="application", difficulty=1, diag=0,
        stimulus="A grade 10 ELL with strong document-reading skills rarely speaks in discussions and says, I need time to say it. The teacher plans a Structured Academic Controversy: pairs prepare claims from documents, rehearse with sentence frames, and paraphrase each other before responding.",
        stem="Which explanation best supports the effectiveness of this strategy for this student?",
        options=[
            "It respects her silent period, so she will not have to speak until she feels completely ready.",
            "It replaces discussion with reading, which is the student's strongest language modality.",
            "It lets the teacher correct every grammatical error she makes while she is speaking.",
            "Preparation lowers her affective filter, and paraphrasing creates negotiation of meaning.",
        ],
        answer=3,
        why="Preparation and rehearsal give her the time she asks for, which lowers the affective filter (Krashen). Paraphrasing and responding to peers create negotiation of meaning, with clarification requests and confirmation checks, which Long's Interaction Hypothesis links to acquisition. Both explanations are tied directly to her profile.",
        traps=[
            {"code": "MISAPPLIED_THEORY", "note": "The silent period describes early beginners. This student needs structured speaking practice, and the activity requires her to speak."},
            {"code": "LITERAL", "note": "This misreads the strategy. Reading is the preparation, but the purpose of the activity is academic speaking."},
            {"code": "OVERCORRECT", "note": "Correcting every error during discussion raises anxiety and shifts the focus from meaning to form."},
            None,
        ],
        key="Justify structured discussion with the affective filter (preparation) and Long's Interaction Hypothesis (negotiation of meaning).",
    ),
    dict(
        id="7.4-06", skill="7.4", type="application", difficulty=2, diag=0,
        stimulus="A high school ENL teacher uses the Language Experience Approach with two SIFE newcomers. They dictate sentences about their work as a mechanic and a cook, the teacher writes the sentences on chart paper, and the group rereads them and does word study with words from the text.",
        stem="Which statement best explains why this approach supports the students' literacy development?",
        options=[
            "It teaches phonics in a fixed sequence that is independent of the students' own oral language.",
            "The text comes from the students' own words and experience, so they know the meaning and can focus on print.",
            "It prevents errors, because the teacher converts their dictation into polished standard written English.",
            "It uses simplified texts with fewer ideas, which lowers the expectations to match the students' level.",
        ],
        answer=1,
        why="In LEA, students read texts made from their own spoken language and experience, so the content is fully comprehensible (Krashen's i+1), and they can devote their attention to decoding and word recognition. Using their work experience also draws on funds of knowledge and respects their age, which lowers the affective filter for adolescent beginning readers.",
        traps=[
            {"code": "MISAPPLIED_THEORY", "note": "This misdescribes LEA, which is built on students' own oral language, not a fixed phonics sequence."},
            None,
            {"code": "OVERCORRECT", "note": "LEA's value comes from recording the students' own language closely. Polishing it into standard prose distances the text from what they can read."},
            {"code": "LOWER_RIGOR", "note": "LEA isn't about lowering expectations. It supplies comprehensible text drawn from rich experience."},
        ],
        key="LEA works because students read their own language and experiences, so the text is comprehensible and they can focus on print.",
    ),
    dict(
        id="7.4-07", skill="7.4", type="application", difficulty=3, diag=0,
        stimulus="A first-grade ENL teacher builds on students' strong rhyming and syllable skills (in English, Spanish, and Wolof) by moving from chant rhymes to onset–rime splitting and then to segmenting words into phonemes with Elkonin boxes.",
        stem="Which rationale most accurately explains why this sequence is effective?",
        options=[
            "Rhyming skill guarantees phoneme awareness, so the boxes mainly add some variety to the lesson.",
            "Children must master all letter names before they can benefit from phonological awareness work.",
            "Phonological awareness moves from larger to smaller units and transfers across languages.",
            "Songs and chants lower the affective filter, which is the main reason children learn to segment.",
        ],
        answer=2,
        why="Phonological awareness generally develops from larger units (words, syllables, rhymes) to smaller ones (onsets and rimes, then phonemes), so each step builds on the last within the children's ZPD. Phonological awareness also transfers across languages, so rhyming skill developed in Spanish or Wolof counts as a foundation. Both facts explain why starting from their strength works.",
        traps=[
            {"code": "PARTIAL", "note": "Rhyme awareness is a real foundation, but it doesn't guarantee phoneme awareness. The boxes are the core instruction, not variety."},
            {"code": "MISAPPLIED_THEORY", "note": "Phonological awareness is oral and can develop alongside letter knowledge. It doesn't require mastery of letter names first."},
            None,
            {"code": "PARTIAL", "note": "A low affective filter helps, but it is a supporting condition, not the reason the sequence builds phoneme segmenting."},
        ],
        key="Explain phonological-awareness sequences with the larger-to-smaller continuum and cross-language transfer.",
    ),
    dict(
        id="7.4-08", skill="7.4", type="application", difficulty=3, diag=0,
        stimulus="A grade 3 Dual Language teacher works with a Spanish-dominant ELL who uses the past tense accurately in Spanish but writes 'Yesterday we go' in English. The student builds a side-by-side chart matching the past-tense verbs in her own Spanish story to their English equivalents.",
        stem="Which explanation most accurately grounds this strategy in theory?",
        options=[
            "Comparing the languages helps her notice how English marks the past, drawing on her Spanish knowledge.",
            "Contrastive analysis predicts that her errors come from Spanish, so the chart shows which habits to suppress.",
            "Strict separation of languages is essential in Dual Language, and the chart keeps Spanish out of English.",
            "Translanguaging means she may write English assignments in Spanish when the English forms are difficult.",
        ],
        answer=0,
        why="Side-by-side comparison draws her attention to the specific English forms she lacks (Schmidt's Noticing Hypothesis), while her accurate Spanish past tense provides the conceptual anchor (Cummins' Common Underlying Proficiency). This planned cross-linguistic bridge is an established Dual Language practice that leverages the home language, as the Blueprint recommends.",
        traps=[
            None,
            {"code": "MISAPPLIED_THEORY", "note": "Spanish marks past tense clearly, so her error isn't transfer, and the chart uses Spanish as a resource, not something to suppress."},
            {"code": "DEFICIT", "note": "The chart deliberately connects the languages. Treating Spanish as interference to keep out misreads both the strategy and the biliteracy goals of Dual Language."},
            {"code": "MISAPPLIED_THEORY", "note": "Translanguaging pedagogy uses all of a student's languages to build meaning and skills. It doesn't mean avoiding English output on English tasks."},
        ],
        key="Ground cross-linguistic comparison in noticing (Schmidt) and CUP; it uses the home language as a resource, not interference.",
    ),
]

# ===========================================================================
# Guide: How to Write the 116 Constructed Response (lesson schema, skill 7.1)
# ===========================================================================
GUIDE = dict(
    skill="7.1",
    title="How to Write the 116 Constructed Response",
    why="The single constructed response is 20% of your score: an analysis of about 400–600 words of exhibits about ELLs, scored on completeness, accuracy, and depth of support.",
    body=[
        dict(h="What the scorers are looking for", md=T("""
The constructed response is scored on a 4-point scale against three performance characteristics. Know them cold, because everything you put on the page should serve one of them.

- **Completeness:** Did you do every bulleted task? Usually that means one strength, one need, one strategy, and an explanation of why the strategy works. Skip one and a 4 is off the table. Watch the qualifiers: if the prompt says the strength and need must be ones "that the students share," one student's strength does not count.
- **Accuracy:** Is what you say true to the exhibits and to the field? Use correct terms (Transitioning, not "intermediate"; Integrated ENL, not "push-in"), describe theories correctly, and choose a strategy that fits the students' proficiency levels and ages.
- **Depth of Support:** Do you prove it? Name exhibits, quote short phrases, give scores, describe the strategy in concrete steps, and explain *why* it works for *these* students.

Think of the score points this way:

- **4 (thorough command):** a precise strength and need, evidence from several exhibits, a concrete strategy that clearly connects the strength to the need, and theory tied to the evidence.
- **3 (general command):** all parts present and mostly accurate, but the evidence or explanation is thinner or more general.
- **2 (partial command):** a part is vague, missing, or not shared, such as a personality "strength," a list of strategies, or theory names with no connection.
- **1 (little or no command):** off-task, inaccurate, or largely missing.

Scorers don't reward fancy prose. They reward a response that is easy to check: each task in its own paragraph, evidence labeled by exhibit, and reasoning spelled out.
""")),
        dict(h="A 60-minute time plan", md=T("""
Protect a full 60 minutes for the constructed response, and don't let the multiple-choice section eat into it.

- **Minutes 0–5: Read the prompt first.** Underline the task words: *one* strength, *one* need, *share*, and the domain (*writing*, *oral language*, *literacy*). Now you know what to hunt for.
- **Minutes 5–15: Read and annotate the exhibits.** On scratch paper, make a two-column chart labeled Strength and Need, with a row for each student. Jot evidence with its exhibit number ("Ex 2: 5/5 sequencing"). Look at the NYSESLAT modalities: the highest often suggests the strength, and the lowest the need.
- **Minutes 15–20: Decide and outline.** Choose the strength–need pair you can prove for every student, then pick ONE strategy that uses the strength to reach the need. Jot two or three theory links.
- **Minutes 20–50: Write.** Follow the five-paragraph structure below and aim for about 500 words.
- **Minutes 50–57: Check against the prompt.** Is every bullet answered? Is each claim tied to an exhibit? Does the explanation mention these students, not just ELLs in general?
- **Minutes 57–60: Proofread.** Fix names, proficiency levels, and typos.
""")),
        dict(h="Choosing a shared strength and need", md=T("""
This decision drives your whole score. Run each candidate through four tests:

- **Is it a language or literacy skill?** "Motivated," "hardworking," and "friendly" are dispositions, not strengths you can build instruction on. "Retells events in sequence," "reads grade-level text accurately," and "strong Spanish literacy" are.
- **Does every student show it?** Write each student's name next to the evidence. If one student has none, choose another strength or need. A need that only two of three students show (for example, article errors) is a classic trap.
- **Is it significant?** It should matter for grade-level learning. Handwriting, one misspelling, or a single tense error is not significant. A pattern that shows up across exhibits is.
- **Can one strategy connect them?** The best pairs connect naturally: an oral strength with a writing need, home-language literacy with English writing, hands-on knowledge with academic text, or a reading strength with a speaking need.

Be precise. "Writing" is too broad for a need. "Moving from retelling to explaining how and why, using causal language such as *because* and *as a result*" is precise, and it points straight to a strategy. Use asset-based phrasing: the need is what students are *ready to learn next*, not what is "wrong" with them.

Also say what the evidence rules out. If students retell well but can't explain, the need is not comprehension. Writing "the issue is not understanding the plot; it is the language of explanation" shows a scorer that you analyzed rather than skimmed.
""")),
        dict(h="Citing evidence", md=T("""
Every claim gets evidence, and every piece of evidence gets a label. The pattern is **exhibit + specific detail + what it shows.**

- "In Exhibit 2, all three students scored 5/5 on the sequencing check, which shows strong listening comprehension."
- "Bilal's answer in Exhibit 2, 'Because... I don't know how to say it,' shows that he has the idea but not the language to explain it."
- "Exhibit 1 shows that Writing is the lowest NYSESLAT modality for all three students."

Tips:

- Use at least two exhibits for the strength and two for the need. Triangulation (test data plus observation plus a work sample) is persuasive.
- Quote short phrases; don't copy whole samples.
- Give numbers exactly as shown ("3 of 10," "Transitioning").
- When you show a shared pattern, name each student: "Daniela..., Bilal..., and Yuxin..."
- Never invent data or assume facts the exhibits don't give.
""")),
        dict(h="A reusable five-paragraph structure", md=T("""
Use the same structure every time; it makes each performance characteristic easy to see. Word targets are approximate.

- **Paragraph 1 (about 50 words), thesis:** "These students share a significant strength in ___ and a significant need in ___."
- **Paragraph 2 (about 100 words), evidence for the strength:** "This strength is evident across the exhibits. In Exhibit 1,... In Exhibit 3,... Together, this shows that..."
- **Paragraph 3 (about 100 words), evidence for the need:** "However, the students share a need in ___. In Exhibit 2,... Exhibit 4 confirms this:... The problem is not ___; it is ___."
- **Paragraph 4 (about 150 words), the strategy:** "To build on ___ to address ___, I would use ___. First,... Next,... Then,... Finally,... For [student], I would adjust this by..."
- **Paragraph 5 (about 120 words), why it works:** "This strategy would be effective for several reasons. First, because it begins with ___,... (theory plus evidence). Second,... Finally,..."

Two upgrades separate a 4 from a 3: say what the scaffold is and how it will be faded, and tie each theory to something a student actually did in the exhibits.
""")),
        dict(h="Strategy bank: high-value strategies and the theory behind them", md=T("""
Know each of these well enough to describe it in four or five concrete steps.

- **Oral rehearsal (talk-to-write):** partners say it before they write it. Oral strength → writing need. Theory: Swain's Output Hypothesis; Vygotsky's ZPD.
- **Sentence frames and a graphic organizer with gradual release:** strong ideas, weak structure. Theory: scaffolding (Wood, Bruner & Ross); ZPD.
- **Shared or interactive writing:** emergent or developing writers. Theory: scaffolding; Vygotsky.
- **Language Experience Approach:** oral language or life experience → early reading (SIFE, young learners). Theory: comprehensible input (Krashen); funds of knowledge (Moll).
- **Cognate study with a bilingual glossary or concept chart:** literacy in a language that shares many cognates with English (e.g., Spanish, French) → academic vocabulary. Theory: Cummins' CUP; positive transfer.
- **The Bridge (cross-linguistic comparison):** strong home-language literacy → a specific English form. Theory: CUP; Schmidt's Noticing Hypothesis; translanguaging (García).
- **Home-language brainstorming and planning:** strong reasoning in the home language → English writing. Theory: CUP; Developmental Interdependence.
- **Claim–evidence–reasoning with students' own data:** hands-on content knowledge → academic writing. Theory: CALP; Cummins' quadrants (context-embedded to context-reduced).
- **Sentence unpacking ("juicy sentences"):** content knowledge → dense academic text. Theory: noticing; CALP.
- **Structured academic conversation or Structured Academic Controversy:** reading or content strength → speaking need. Theory: Long's Interaction Hypothesis; affective filter; output.
- **Mentor-text deconstruction and register shifting:** oral argument (often Long-Term ELLs) → formal writing. Theory: BICS vs. CALP; noticing the gap.
- **Explicit Tier 2 vocabulary routine:** decoding or self-monitoring strength → vocabulary need. Theory: Beck, McKeown & Kucan; i+1.
- **Fix-up strategies (click and clunk) or reciprocal teaching:** self-monitoring → comprehension need. Theory: CALLA metacognitive strategies.
- **Elkonin boxes along the phonological-awareness continuum:** rhyme and syllable strength → phoneme need. Theory: phonological awareness transfers across languages; ZPD.
- **Dialogue journals:** willingness to communicate → writing fluency. Theory: affective filter; meaning-focused output.

Pick the one that best connects your specific strength and need. One well-described strategy beats five listed ones.
""")),
        dict(h="Common mistakes that cost points", md=T("""
- **Personality as the strength:** "She is motivated" is not a language skill.
- **A need that isn't shared or significant:** article errors in one student, or a single spelling slip.
- **The laundry list:** "I would use visuals, frames, groups, and technology." Scorers want one strategy, fully developed.
- **A strategy that ignores the strength:** if paragraph 4 never mentions the strength, the bridge is missing.
- **Name-dropping theory:** "According to Vygotsky..." with no link to the students earns little. Say what the theory predicts *for these students*.
- **Lowering rigor:** easier texts or shorter assignments instead of scaffolds for grade-level work.
- **Deficit or English-only moves:** banning the home language, blaming it for every error, or telling families to speak English at home.
- **One size fits all:** ignoring that one student is Emerging and another Expanding, or recommending cognates for a language that shares few with English.
- **Misreferral:** suggesting a disability evaluation for typical second-language development.
- **No exhibit labels or invented facts:** if a scorer can't trace a claim to an exhibit, it doesn't count as support.
""")),
    ],
    traps=[
        "Exam trap: choosing a strength that only one or two students show when the prompt says \"that the students share.\"",
        "Exam trap: naming a disposition (\"motivated,\" \"hardworking\") instead of a language or literacy skill as the strength.",
        "Exam trap: listing several strategies instead of describing one, in concrete steps, that connects the strength to the need.",
        "Exam trap: citing theory names without connecting them to specific evidence in the exhibits.",
        "Exam trap: \"fixing\" the need by lowering rigor (a simpler text or shorter task) or by removing the home language.",
    ],
    terms=[
        {"t": "Completeness", "d": "Performance characteristic: the degree to which the response addresses every part of the assignment."},
        {"t": "Accuracy", "d": "Performance characteristic: the degree to which the response shows relevant knowledge and skills accurately and effectively."},
        {"t": "Depth of Support", "d": "Performance characteristic: the degree to which the response gives appropriate examples and details that show sound reasoning."},
        {"t": "Shared strength or need", "d": "A strength or need that every student in the scenario shows, with evidence for each student."},
        {"t": "Significant", "d": "Important for grade-level learning and visible as a pattern across exhibits, not a one-time surface error."},
        {"t": "Triangulation", "d": "Supporting a claim with more than one kind of evidence, such as test data, observation notes, and work samples."},
        {"t": "Asset-based framing", "d": "Describing students by what they can do and are ready to learn next, with home language and culture as resources."},
        {"t": "Talk-to-write", "d": "Oral rehearsal of ideas with a partner before writing, so spoken language becomes the bridge to written language."},
        {"t": "Gradual release", "d": "Moving from teacher modeling to guided practice to independent work as scaffolds are removed."},
        {"t": "Common Underlying Proficiency", "d": "Cummins: concepts and literacy skills learned in one language are available in another, which supports transfer."},
        {"t": "Pushed output", "d": "Swain: producing language makes learners notice gaps, test hypotheses, and reflect on form."},
        {"t": "Negotiation of meaning", "d": "Long: clarification requests, confirmation checks, and comprehension checks during interaction that make input comprehensible."},
        {"t": "Funds of knowledge", "d": "Moll: the knowledge and skills students gain from family, community, and work, used as instructional resources."},
        {"t": "Register", "d": "A variety of language suited to a context or audience, such as casual conversation versus formal academic writing."},
        {"t": "Context-embedded vs. context-reduced", "d": "Cummins: tasks with rich visual and situational support versus tasks that depend mainly on language itself."},
    ],
    tip="Before you write, test your pair: Is it a language skill? Does every student show it? Can I cite two exhibits? Does my ONE strategy connect them?",
)

pathlib.Path(__file__).with_name("cr.json").write_text(
    json.dumps({"scenarios": SCENARIOS, "questions": QUESTIONS, "guide": GUIDE, "lessons": []},
               ensure_ascii=False, indent=1),
    encoding="utf-8",
)

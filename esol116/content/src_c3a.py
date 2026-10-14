# Competency 3 (part A): skills 3.1-3.4 for the NYSTCE ESOL CST (116) simulator.
# Run: python3 src_c3a.py  -> writes c3a.json next to this file.


def T(code, note, pair=None):
    d = {"code": code}
    if pair:
        d["pair"] = pair
    d["note"] = note
    return d


def Q(id, type, difficulty, stem, options, answer, why, traps, key, stimulus=None, diag=0):
    assert len(options) == 4 and len(traps) == 4, id
    assert traps[answer] is None, id
    assert all(t is not None for i, t in enumerate(traps) if i != answer), id
    q = {"id": id, "skill": id.split("-")[0], "type": type, "difficulty": difficulty, "diag": diag}
    if stimulus:
        q["stimulus"] = stimulus
    q["stem"] = stem
    q["options"] = options
    q["answer"] = answer
    q["why"] = why
    q["traps"] = traps
    q["key"] = key
    return q


QUESTIONS = []

# ---------------------------------------------------------------------------
# 3.1 NYS program models & Part 154 service requirements
# ---------------------------------------------------------------------------
QUESTIONS += [
    Q("3.1-01", "application", 2,
      "A grade 3 student whose home language is Wolof enrolls in a New York State school district. Her parents choose an ENL program, and her NYSITELL results place her at the Entering level. Which weekly schedule meets the minimum CR Part 154 requirement for her ENL services?",
      ["180 minutes of Stand-alone ENL and 180 minutes of Integrated ENL/ELA",
       "360 minutes of Stand-alone ENL, delivered as daily pull-out sessions",
       "90 minutes of Stand-alone ENL, 180 of Integrated ENL/ELA, and 90 of Integrated ENL/science",
       "180 minutes of Integrated ENL in ELA or in another core content area"],
      0,
      "For grades K–8, CR Part 154 requires an Entering student to receive 360 minutes of ENL per week: 180 minutes of Stand-alone ENL plus 180 minutes of Integrated ENL/ELA. The Stand-alone time builds English with a certified ESOL teacher, and the Integrated ENL/ELA time develops English inside grade-level ELA. Required minutes then decrease as proficiency rises (360, 360, 180, 180, 90).",
      [None,
       T("EXCLUSION", "An all pull-out schedule leaves out the required 180 minutes of Integrated ENL/ELA. Part 154 deliberately keeps even Entering students in grade-level ELA with ESOL support instead of separating them full time."),
       T("TERM", "This 360-minute pattern has only 90 Stand-alone minutes, which is the Emerging configuration (with its flexible 90 used as Integrated). Entering students need a full 180 minutes of Stand-alone ENL.", "Entering ↔ Emerging units of study"),
       T("NYS_POLICY", "180 minutes of Integrated ENL in ELA or another content area is the Expanding requirement. An Entering student needs twice as many minutes, including Stand-alone ENL.")],
      "K–8 Entering = 360 min/week: 180 Stand-alone ENL + 180 Integrated ENL/ELA.",
      diag=1),

    Q("3.1-02", "application", 2,
      "The program described is best identified as which of the following?",
      ["Transitional Bilingual Education",
       "One-way Dual Language",
       "Two-way Dual Language",
       "Integrated ENL"],
      2,
      "A two-way Dual Language program enrolls both ELLs and English-proficient students and teaches grade-level content in both languages for several years, with bilingualism and biliteracy as goals for every student. A one-way program serves students who are mostly from one language group. TBE also uses two languages, but its goal is to transition ELLs to English-only instruction.",
      [T("TERM", "TBE also teaches in two languages, but it serves ELLs and aims to move them into English-only instruction. It does not enroll English-proficient students or aim for biliteracy for all.", "TBE ↔ Dual Language"),
       T("TERM", "One-way Dual Language serves students who are mostly from one language group. A program that deliberately mixes ELLs with English-proficient students is two-way.", "one-way ↔ two-way Dual Language"),
       None,
       T("TERM", "Integrated ENL is part of an ENL program: content and English development taught in English. It does not teach grade-level content in Spanish or aim for biliteracy.", "bilingual program ↔ ENL program")],
      "Two-way Dual Language = ELLs + English-proficient peers in two languages, biliteracy for all; one-way = mainly one language group.",
      stimulus="Excerpt from a district program guide:\n\"About half of the students in this program are ELLs whose home language is Spanish, and about half are English-proficient students. All students learn grade-level content in both Spanish and English, and they stay in the program for several years. Our goals are bilingualism, biliteracy, academic achievement, and cross-cultural understanding for every student.\"",
      diag=2),

    Q("3.1-03", "scenario", 2,
      "Which response to the principal's plan best reflects CR Part 154?",
      ["It works, provided that the paraprofessional speaks the students' home language and attends every ELA lesson.",
       "It works, if the classroom teacher has completed the required ELL-focused CTLE hours for the cycle.",
       "It falls short, because Entering students must receive all of their ENL minutes in Stand-alone classes.",
       "It falls short, because Integrated ENL must be taught by a dually certified teacher or co-taught with an ESOL teacher."],
      3,
      "Under Part 154, Integrated ENL is delivered either by one teacher certified in both the content area and ESOL, or by a certified content teacher and a certified ESOL teacher co-teaching. A bilingual paraprofessional can be a valuable home-language support, but paraprofessional time does not count toward the required units of study.",
      [T("NYS_POLICY", "A bilingual paraprofessional is a valuable support, but paraprofessional time does not count toward ENL units of study, which must be delivered by appropriately certified teachers."),
       T("TERM", "The CTLE rule (at least 15% of PD hours on language acquisition and ELL needs) is professional development for all teachers. It does not qualify a content teacher to deliver Integrated ENL alone.", "ELL-focused CTLE hours ↔ ESOL certification"),
       T("NYS_POLICY", "Right conclusion, wrong reason. K–8 Entering students need 180 Stand-alone minutes AND 180 Integrated ENL/ELA minutes, not all Stand-alone."),
       None],
      "Integrated ENL = a dually certified teacher, or a certified content teacher co-teaching with a certified ESOL teacher; paraprofessional time doesn't count.",
      stimulus="Principal's memo:\n\"To give our grade 1 Entering students their Integrated ENL/ELA minutes, our bilingual paraprofessional will sit with them during the ELA block, which is taught by the classroom teacher. The ESOL teacher will continue to provide their Stand-alone ENL.\""),

    Q("3.1-04", "analysis", 3,
      "Based on CR Part 154, for which group is the district required to provide a bilingual education program?",
      ["The kindergarten Spanish speakers, because all of them attend the same school",
       "The grade 2 Bengali speakers, even though they are spread across several schools",
       "The Arabic speakers in grades 3–5, because together they number more than 20",
       "The grade 4 ELLs who speak Urdu, Nepali, Polish, or Karen, because there are more than 20"],
      1,
      "Part 154 requires a bilingual education program when 20 or more ELLs in the same grade level share the same home language, counted districtwide. The 22 Bengali-speaking second graders meet that threshold even though no single school has 20. The kindergarten group has only 19, the Arabic speakers are spread across three grades, and the grade 4 group does not share one home language. Parents of the Bengali speakers may still choose ENL.",
      [T("LITERAL", "Attending one building is a surface detail. Nineteen is below the threshold of 20, so this group does not trigger a required bilingual program."),
       None,
       T("NYS_POLICY", "The count must be within the same grade level. Nine Arabic speakers in each of three grades does not reach 20 in any grade."),
       T("NYS_POLICY", "The 20 students must share the same home language. Twenty-four ELLs who speak four different languages do not trigger a bilingual program in any one language.")],
      "Bilingual trigger: 20+ ELLs with the same home language in the same grade, counted districtwide (not per school).",
      stimulus="District ELL enrollment, October\nGrade | Home language | ELLs districtwide | Most in any one school\nK | Spanish | 19 | 19\n2 | Bengali | 22 | 9\n3 | Arabic | 9 | 6\n4 | Arabic | 9 | 5\n5 | Arabic | 9 | 6\n4 | Urdu, Nepali, Polish, Karen (combined) | 24 | 10"),

    Q("3.1-05", "scenario", 2,
      "A grade 1 student whose home language is Spanish is identified as an ELL at the Entering level. The district has a two-way Dual Language program in his grade. At the parent orientation, his parents say they would prefer an ENL program. What should the district do?",
      ["Place him in Dual Language, since Part 154 requires bilingual placement for Entering students when a program exists",
       "Place him in a general education class without ENL, since his parents have declined the bilingual program",
       "Honor the parents' choice and place him in ENL with the required Stand-alone and Integrated ENL/ELA minutes",
       "Place him in ENL, but in Stand-alone classes only until he reaches the Transitioning level"],
      2,
      "At orientation, parents learn about TBE, Dual Language, and ENL in their preferred language and then choose. If they choose ENL, the student is placed in ENL and receives the units of study for his level. For an Entering student in grades K–8, that is 180 minutes of Stand-alone ENL and 180 minutes of Integrated ENL/ELA each week. Declining a bilingual program is not the same as declining ELL services.",
      [T("NYS_POLICY", "Parents choose among the program options. Part 154 does not require bilingual placement at any proficiency level when parents prefer ENL."),
       T("NYS_POLICY", "Declining a bilingual program is not declining ELL services. The child is still an ELL and must receive ENL at the units required for his level."),
       None,
       T("EXCLUSION", "A K–8 Entering student needs 180 minutes of Integrated ENL/ELA as well as Stand-alone ENL. Keeping him out of integrated grade-level ELA withholds required access to grade-level instruction.")],
      "Parents choose TBE, Dual Language, or ENL; if they decline bilingual, the student still gets full ENL services.",
      ),

    Q("3.1-06", "analysis", 3,
      "An ENL coordinator reviews the weekly schedules above. Which student's schedule falls short of the CR Part 154 minimum?",
      ["Amira", "Jean-Pierre", "Oksana", "Tenzin"],
      3,
      "A K–8 Emerging student needs 360 minutes a week: 90 minutes of Stand-alone ENL, 180 minutes of Integrated ENL/ELA, and 90 flexible minutes. Tenzin has 360 minutes, but none of his Integrated time is in ELA, so the 180-minute Integrated ENL/ELA requirement is unmet. Amira matches the Entering requirement, Jean-Pierre's flexible 90 may be Stand-alone, and an Expanding student's 180 Integrated minutes may be in ELA or another core content area.",
      [T("NYS_POLICY", "Amira's schedule is exactly the Entering requirement: 180 minutes of Stand-alone ENL plus 180 minutes of Integrated ENL/ELA."),
       T("NYS_POLICY", "A Transitioning student needs 90 minutes of Integrated ENL/ELA plus 90 flexible minutes, and the flexible minutes may be Stand-alone. Jean-Pierre's schedule complies."),
       T("TERM", "At the Expanding level, the 180 Integrated minutes may be in ELA or another core content area, so co-taught science is acceptable.", "Integrated ENL/ELA ↔ Integrated ENL in any content area"),
       None],
      "Check each component, not just the total: Entering and Emerging students need 180 Integrated ENL minutes specifically in ELA.",
      stimulus="Weekly ENL schedules (grades K–8)\nStudent | Grade | NYSESLAT level | Weekly ENL schedule\nAmira | 2 | Entering | 180 min Stand-alone ENL + 180 min Integrated ENL/ELA\nJean-Pierre | 6 | Transitioning | 90 min Integrated ENL/ELA + 90 min Stand-alone ENL\nOksana | 8 | Expanding | 180 min Integrated ENL/science (co-taught)\nTenzin | 3 | Emerging | 180 min Stand-alone ENL + 180 min Integrated ENL/math"),

    Q("3.1-07", "application", 2,
      "A grade 6 student scored at the Transitioning level on the spring NYSESLAT. Which weekly ENL schedule for the next school year meets the CR Part 154 minimum?",
      ["90 minutes of Integrated ENL/ELA and 90 minutes of Integrated ENL in social studies",
       "180 minutes of Stand-alone ENL, with no Integrated ENL in any of his classes",
       "90 minutes of Integrated ENL/ELA, with no other ENL services during the week",
       "90 minutes of Stand-alone ENL and 90 minutes of Integrated ENL in mathematics"],
      0,
      "In grades K–8, a Transitioning student receives 180 minutes a week: 90 minutes of Integrated ENL/ELA plus 90 flexible minutes that may be Stand-alone ENL or Integrated ENL in any content area. The first schedule meets both parts. Schedules without Integrated ENL/ELA, or with only 90 total minutes, fall short.",
      [None,
       T("NYS_POLICY", "The total is right, but 90 of a Transitioning student's minutes must be Integrated ENL/ELA. Only the flexible 90 may be Stand-alone."),
       T("TERM", "Ninety minutes a week is the former-ELL (Commanding) service level. A Transitioning student still needs 180 minutes.", "Transitioning ↔ former-ELL service minutes"),
       T("NYS_POLICY", "The flexible 90 can be Stand-alone, but the other 90 must be Integrated ENL in ELA specifically. Integrated ENL in math does not substitute for it.")],
      "K–8 Transitioning = 180 min: 90 Integrated ENL/ELA + 90 flexible (Stand-alone or Integrated)."),

    Q("3.1-08", "application", 2,
      "A grade 4 student scored Commanding on the spring NYSESLAT. Which description of his services for the following school year is consistent with NYS requirements?",
      ["He exits ELL status and no longer receives ENL support or testing accommodations of any kind.",
       "He continues to receive 180 minutes of ENL until he also scores Level 3 on the Grades 3–8 ELA test.",
       "He receives 90 minutes a week of Integrated ENL or other approved former-ELL services for two years.",
       "He receives former-ELL services for four years, because ESSA keeps former ELs in the subgroup that long."],
      2,
      "Scoring Commanding on the NYSESLAT exits a student from ELL status, but former ELLs in NYS continue to receive 90 minutes a week of Integrated ENL (or other approved former-ELL services) for two years. They also keep ELL testing accommodations for two years after exit. ESSA's four-year figure concerns accountability reporting, not services.",
      [T("NYS_POLICY", "Exiting ELL status doesn't end support. Former ELLs receive continued services and keep testing accommodations for two years after exit."),
       T("TERM", "The ELA-test condition applies only to students who score Expanding. A Commanding score exits a student on its own.", "Commanding exit ↔ Expanding + ELA exit route"),
       None,
       T("TERM", "ESSA lets states keep former ELs in the EL subgroup for up to four years for accountability reporting. NYS former-ELL services last two years.", "ESSA 4-year accountability ↔ NYS 2-year former-ELL services")],
      "Former ELL (Commanding) = 90 min/week of Integrated ENL or approved services, plus accommodations, for 2 years."),

    Q("3.1-09", "knowledge", 1,
      "Which of the following best describes the goal of a Transitional Bilingual Education (TBE) program in New York State?",
      ["Developing bilingualism and biliteracy for ELLs and English-proficient students who learn together in two languages",
       "Using the home language for literacy and content as English instruction increases, so students can move to English-only classes",
       "Providing English language development with a certified ESOL teacher while all content is taught in English",
       "Placing ELLs in English-only content classes and using the home language only as a last resort when students are lost"],
      1,
      "TBE combines home language arts, content instruction in the home language and English, and ENL. The share of English increases over time, and the goal is to transition students to English-only instruction. Dual Language, by contrast, aims for long-term bilingualism and biliteracy and does not phase out the home language.",
      [T("TERM", "This describes two-way Dual Language, which aims for biliteracy for all students. TBE serves ELLs and aims to transition them to English-only instruction.", "TBE ↔ two-way Dual Language"),
       None,
       T("TERM", "This describes an ENL program. TBE includes ENL, but it also provides home language arts and content instruction in the home language.", "TBE ↔ ENL program"),
       T("DEFICIT", "This treats the home language as an emergency crutch in an English-only setting. That is the opposite of TBE, which uses the home language systematically to build literacy and content knowledge.")],
      "TBE: home language + English, with English growing; goal = transition to English-only. Dual Language: goal = bilingualism and biliteracy."),

    Q("3.1-10", "analysis", 3,
      "Which program model does the principal's description best match?",
      ["Transitional Bilingual Education, since all of the students in the program share the same home language",
       "Two-way Dual Language, since grade-level content is taught in both English and Spanish",
       "Integrated ENL, since former ELLs continue to receive language support in the same classes",
       "One-way Dual Language, since it serves one language group and aims for biliteracy"],
      3,
      "A one-way Dual Language program serves students who are predominantly from one language group and keeps both languages for literacy and content over the long term, because its goal is bilingualism and biliteracy. TBE also serves one language group, but it phases out the home language as English grows. Two-way programs deliberately combine ELLs with English-proficient students.",
      [T("TERM", "TBE also serves one language group, but it phases out the home language as English grows. Continuing Spanish after students test Commanding, with a biliteracy goal, signals Dual Language.", "TBE ↔ one-way Dual Language"),
       T("TERM", "Both Dual Language models teach in two languages. Two-way programs deliberately include English-proficient students, but this program serves only Spanish-speaking ELLs and former ELLs.", "one-way ↔ two-way Dual Language"),
       T("LITERAL", "Including former ELLs is a surface detail. Integrated ENL teaches content in English with language support; it does not provide Spanish literacy or aim for biliteracy."),
       None],
      "One language group + home language kept for biliteracy = one-way Dual Language; home language phased out = TBE.",
      stimulus="Principal's description at a family open house:\n\"Our program serves only Spanish-speaking ELLs and former ELLs. Students learn to read and write in both Spanish and English, and science and social studies are taught in both languages. Spanish instruction continues through grade 5 even after students test Commanding, because our goal is for every student to become bilingual and biliterate.\""),

    Q("3.1-11", "scenario", 1,
      "An ESOL teacher is planning Stand-alone ENL for grade 5 Entering students whose class is starting a science unit on ecosystems. Which plan best reflects the purpose of Stand-alone ENL in New York State?",
      ["Follow a separate grammar workbook so students master basic structures before they work with science content",
       "Use the period to help the students finish homework assigned in their general education science class",
       "Replace the ecosystems unit with simpler picture books about animals until the students reach Emerging",
       "Teach the English the students need for the unit, such as key vocabulary and patterns for describing food chains"],
      3,
      "In Stand-alone ENL, a certified ESOL teacher provides English language development so that students acquire the English they need to succeed in core content. The strongest Stand-alone lessons are anchored in the content students are studying. Here that means building the vocabulary, sentence structures, and language functions they will use in the ecosystems unit.",
      [T("ISOLATED", "A grammar sequence detached from content delays access to grade-level learning. Stand-alone ENL should build the English students need for their content classes."),
       T("PARTIAL", "Homework help is useful but reactive. It is not the systematic English language development that Stand-alone ENL exists to provide."),
       T("LOWER_RIGOR", "Swapping grade-level science for easier, unrelated texts lowers expectations. NYS expects ELLs to work with grade-level content, with scaffolds."),
       None],
      "Stand-alone ENL builds the English students need for grade-level content; it is linked to content, not a separate grammar track."),

    Q("3.1-12", "scenario", 3,
      "A middle school plans to provide the required ENL minutes for its grade 7 Expanding students through a social studies class co-taught by a certified social studies teacher and a certified ESOL teacher. Which statement about this plan is accurate under CR Part 154?",
      ["It is acceptable, because an Expanding student's 180 minutes may be Integrated ENL in ELA or another core content area.",
       "It is not acceptable, because Integrated ENL minutes for students at every level must take place in the ELA class.",
       "It is not acceptable, because Expanding students must also receive at least 90 minutes of Stand-alone ENL.",
       "It is acceptable only if the social studies teacher also holds ESOL certification and teaches the class alone."],
      0,
      "For K–8 Expanding students, Part 154 requires 180 minutes a week of Integrated ENL, which may be delivered in ELA or another core content area such as social studies. Co-teaching by a certified content teacher and a certified ESOL teacher is one of the two approved ways to deliver Integrated ENL; a single teacher certified in both areas is the other.",
      [None,
       T("TERM", "Entering and Emerging students need Integrated ENL/ELA specifically, and Transitioning students need 90 minutes of it. Expanding students' Integrated ENL may be in any core content area.", "Expanding ↔ Entering/Emerging ENL/ELA requirement"),
       T("NYS_POLICY", "There is no Stand-alone minimum at the Expanding level; the required 180 minutes are Integrated ENL."),
       T("NYS_POLICY", "Co-teaching by a certified content teacher and a certified ESOL teacher is an approved way to deliver Integrated ENL. Dual certification is the other option, not a requirement.")],
      "K–8 Expanding = 180 min of Integrated ENL in ELA OR another core content area; no Stand-alone minimum."),

    Q("3.1-13", "knowledge", 1,
      "A grade 2 Entering student whose home language is Chinese is enrolled in a Transitional Bilingual Education (TBE) program. Which statement about her instruction is accurate?",
      ["She receives no ENL, because part of her content instruction is delivered in her home language.",
       "She receives home language arts, content instruction in both languages, and ENL for her level.",
       "She receives all of her instruction in Chinese until she reaches the Expanding level in English.",
       "She receives content instruction only in English, and Chinese is used mainly for parent meetings."],
      1,
      "NYS bilingual programs (TBE and Dual Language) combine three parts: home language arts, content instruction in both the home language and English, and ENL. Students in a bilingual program still receive ENL units of study for their proficiency level, so the program develops both languages from the start.",
      [T("NYS_POLICY", "Students in bilingual programs still receive ENL for their proficiency level. Home-language content instruction does not replace English language development."),
       None,
       T("NYS_POLICY", "TBE develops both languages from the start. It is not home-language-only instruction until the student reaches a set English level."),
       T("TERM", "English-only content instruction describes an ENL program, not TBE, which teaches content in the home language as well as English.", "TBE ↔ ENL program")],
      "Bilingual programs (TBE, Dual Language) = home language arts + content in both languages + ENL."),

    Q("3.1-14", "scenario", 1,
      "A district enrolls six Pashto-speaking ELLs in grade 5 and no other Pashto speakers in that grade. A parent asks the district to create a Pashto bilingual class. Which response is accurate under CR Part 154?",
      ["A bilingual program is required only when 20 or more same-grade ELLs share a home language districtwide, so the student receives ENL.",
       "The district must open a Pashto bilingual class, because a parent has formally requested one in writing.",
       "The student should attend general education without ENL until enough Pashto speakers enroll to form a program.",
       "The student should receive ENL, and teachers should avoid Pashto in class so she is not confused by two languages."],
      0,
      "A bilingual program is mandated when 20 or more ELLs in the same grade share a home language districtwide. Six students do not reach that threshold, so the student receives ENL at the units required for her level. ENL teachers can still use Pashto as an asset through bilingual glossaries, home-language texts, and translanguaging.",
      [None,
       T("NYS_POLICY", "A parent request alone doesn't trigger a required bilingual program. The trigger is 20 or more ELLs with the same home language in the same grade, districtwide."),
       T("EXCLUSION", "Every identified ELL must be served now. Withholding ENL while waiting for a bilingual program denies the student required instruction."),
       T("DEFICIT", "Two languages don't confuse learners; the home language is a resource. ENL teachers can use Pashto texts, glossaries, and translanguaging even without a bilingual program.")],
      "Fewer than 20 same-language, same-grade ELLs districtwide: provide ENL, and still use the home language as an asset."),
]

# @@NEXT@@

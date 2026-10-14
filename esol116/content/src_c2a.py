# Competency 2 (part A): skills 2.1-2.4. Writes c2a.json next to this file.


def T(code, note, pair=None):
    d = {"code": code, "note": note}
    if pair:
        d["pair"] = pair
    return d


QUESTIONS = []

# ---------------------------------------------------------------- 2.1 (batch 1)
QUESTIONS += [
 {
  "id": "2.1-01", "skill": "2.1", "type": "scenario", "difficulty": 2, "diag": 1,
  "stimulus": "Home Language Questionnaire (excerpt), grade 4 enrollee\nWhat language(s) are spoken in the child's home? Bengali, some English\nWhat language did the child first understand and speak? Bengali\nWhat language does the child use most often with family? Bengali",
  "stem": "A family enrolls their 9-year-old son in a Queens elementary school and completes the Home Language Questionnaire (HLQ) excerpted above. Under CR Part 154, what should happen next?",
  "options": [
   "The school places him in Stand-alone ENL right away, since the HLQ responses establish that he is an English language learner.",
   "Qualified staff conduct an individual interview with the student in English and in Bengali to determine whether he should take the NYSITELL.",
   "The ENL teacher gives him the NYSESLAT during the first weeks of school to establish his English proficiency level for placement.",
   "His classroom teacher observes him for the first 45 school days and then recommends whether formal ELL testing is needed.",
  ],
  "answer": 1,
  "why": "In NYS the HLQ is only the first screen. Part 154 requires an individual interview with the student in English and the home language, conducted by qualified personnel. If the HLQ and interview indicate a language other than English, the student takes the NYSITELL, and the whole identification process must be finished within 10 school days of initial enrollment.",
  "traps": [
   T("NYS_POLICY", "The HLQ only signals that a student MAY be an ELL. ELL status is determined after the interview and the NYSITELL, not from questionnaire answers alone."),
   None,
   T("TERM", "The NYSESLAT is the annual spring test used to measure progress and exit; the NYSITELL is the identification and initial placement test.", "NYSITELL ↔ NYSESLAT"),
   T("NYS_POLICY", "There is no observation period before testing; identification must be complete within 10 school days. The 45-school-day window belongs to re-identification requests."),
  ],
  "key": "HLQ, then an interview in English and the home language by qualified staff, then the NYSITELL if indicated; all within 10 school days.",
 },
 {
  "id": "2.1-02", "skill": "2.1", "type": "knowledge", "difficulty": 1, "diag": 0,
  "stem": "Under CR Part 154, a district must complete the ELL identification process for a newly enrolled student within which time frame?",
  "options": [
   "Within 5 school days of initial enrollment",
   "Within 30 school days of initial enrollment",
   "Within 10 school days of initial enrollment",
   "Within 45 school days of initial enrollment",
  ],
  "answer": 2,
  "why": "NYS requires that the HLQ, the individual interview, and (when indicated) the NYSITELL be completed within 10 school days of initial enrollment. The other numbers are real Part 154 timelines that apply to different steps, which is exactly why they make tempting distractors.",
  "traps": [
   T("NYS_POLICY", "Five school days is the deadline for notifying parents of ELL status after the determination is made, not for identification itself."),
   T("NYS_POLICY", "Thirty school days is the window for determining SIFE status, which happens after a student is identified as an ELL."),
   None,
   T("NYS_POLICY", "Forty-five school days is the window for requesting a re-identification review, not for completing initial identification."),
  ],
  "key": "Identification: 10 school days. Parent notice: 5 school days after. SIFE: 30 school days. Re-identification request: 45 school days.",
 },
 {
  "id": "2.1-03", "skill": "2.1", "type": "application", "difficulty": 2, "diag": 2,
  "stem": "A 2nd grader whose family speaks Haitian Creole has just scored at the Emerging level on the NYSITELL and is identified as an ELL. Which action by the school best meets NYS requirements for informing his family?",
  "options": [
   "Send an English letter home with the student and ask his older sister, a 6th grader in the same school, to explain the results to their parents.",
   "Wait to contact the family until the spring NYSESLAT results confirm his proficiency level, so that the program recommendation is based on complete data.",
   "Mail a letter in Haitian Creole informing the family that he has been placed in a bilingual program, since bilingual settings are recommended at the Emerging level.",
   "Notify his parents of his ELL status in Haitian Creole within 5 school days and invite them to an orientation explaining TBE, Dual Language, and ENL options.",
  ],
  "answer": 3,
  "why": "Part 154 requires parent notification of ELL status within 5 school days of the determination, in the parents' preferred language, and a parent orientation that explains the program options (Transitional Bilingual Education, Dual Language, and ENL). Parents then make an informed program choice; the school does not choose for them.",
  "traps": [
   T("FAMILY_BARRIER", "Children should never serve as interpreters for official school communication, and the notice must be in the parents' preferred language, not English."),
   T("NYS_POLICY", "Notification cannot wait for the NYSESLAT; it is due within 5 school days of the NYSITELL determination."),
   T("NYS_POLICY", "The language is right, but the school cannot assign a program before the parent orientation. Parents choose among TBE, Dual Language, and ENL options."),
   None,
  ],
  "key": "Parents are notified within 5 school days, in their preferred language, then attend an orientation and choose a program.",
 },
 {
  "id": "2.1-04", "skill": "2.1", "type": "scenario", "difficulty": 3, "diag": 0,
  "stimulus": "Teacher note, school day 25 after enrollment: \"Kasia was identified as an ELL (Transitioning) on the NYSITELL. In class she reads and writes on grade level in English and participates fully in discussions. Her family speaks Polish at home, but she has attended English-language child care and preschool since age 2. I think she may have been misidentified.\"",
  "stem": "Kasia's 1st-grade teacher wants her ELL status reviewed. Which of the following is accurate under NYS regulations?",
  "options": [
   "Only a parent or guardian may request a re-identification review, so the teacher must ask Kasia's family to start the process themselves.",
   "The teacher may request a re-identification review with the consent of Kasia's parent, because the request falls within 45 school days of enrollment.",
   "The teacher may start a re-identification review on her own authority, because teachers have the most direct evidence of classroom proficiency.",
   "Kasia's status cannot be reviewed this year; she can leave ELL status only by meeting the NYSESLAT exit criteria in the spring.",
  ],
  "answer": 1,
  "why": "NYS allows a re-identification review within 45 school days of enrollment. It may be requested by the parent/guardian, by the student, or by a teacher with the parent's consent. This safeguard exists because a single test score can misidentify a student, as may have happened here.",
  "traps": [
   T("NYS_POLICY", "Parents can request a review, but they are not the only ones: a teacher (with parent consent) or the student may also initiate it."),
   None,
   T("NYS_POLICY", "A teacher may initiate the request, but only with the parent's consent; the family's role cannot be bypassed."),
   T("NYS_POLICY", "Outside the 45-school-day window this would be true, but day 25 is within it, so re-identification is available."),
  ],
  "key": "Re-identification: requested within 45 school days by a parent, the student, or a teacher with parent consent.",
 },
 {
  "id": "2.1-05", "skill": "2.1", "type": "knowledge", "difficulty": 1, "diag": 0,
  "stem": "A 10th grader has received ELL services for seven years and has not yet met the NYSESLAT exit criteria. Under NYS subgroup definitions, this student is best classified as which of the following?",
  "options": [
   "A Long-Term ELL",
   "A Developing ELL",
   "A student with interrupted/inconsistent formal education (SIFE)",
   "A former ELL",
  ],
  "answer": 0,
  "why": "NYS defines ELL subgroups by years of service: Newcomers have received 0–3 years of ELL services, Developing ELLs 4–6 years, and Long-Term ELLs have completed 6 or more years. Seven years places this student in the Long-Term ELL subgroup, which typically needs targeted academic literacy support.",
  "traps": [
   None,
   T("TERM", "Developing ELLs have received 4–6 years of service; seven years is past that range.", "Developing ELL ↔ Long-Term ELL"),
   T("TERM", "SIFE status depends on less than 12 months in U.S. schools and being two or more years below grade level because of interrupted schooling, not on years of ELL service.", "SIFE ↔ Long-Term ELL"),
   T("TERM", "Former ELLs have already met exit criteria; this student has not.", "former ELL ↔ Long-Term ELL"),
  ],
  "key": "Newcomer 0–3 years; Developing 4–6 years; Long-Term 6+ years of ELL services.",
 },
 {
  "id": "2.1-06", "skill": "2.1", "type": "analysis", "difficulty": 2, "diag": 0,
  "stimulus": "Student | Grade | Years of ELL services | Current NYSESLAT level\nAmina (Arabic) | 3 | 2 | Emerging\nDiego (Spanish) | 8 | 7 | Expanding\nLiang (Mandarin) | 6 | 5 | Transitioning\nOksana (Ukrainian) | 5 | 1 | Entering",
  "stem": "An ENL coordinator is reviewing this roster to plan targeted support by NYS ELL subgroup. Which student is a Developing ELL?",
  "options": ["Amina", "Diego", "Liang", "Oksana"],
  "answer": 2,
  "why": "Subgroups are defined by years of ELL service, not by current proficiency level. Liang has received 5 years of services, which falls in the Developing ELL range (4–6 years). Amina and Oksana are Newcomers (0–3 years), and Diego, at 7 years, is a Long-Term ELL.",
  "traps": [
   T("TERM", "Two years of service makes Amina a Newcomer (0–3 years), not a Developing ELL.", "Newcomer ↔ Developing ELL"),
   T("TERM", "Seven years of service exceeds the Developing range; Diego is a Long-Term ELL even though he is at Expanding.", "Developing ELL ↔ Long-Term ELL"),
   None,
   T("LITERAL", "Oksana's low proficiency level is a surface detail. Subgroups depend on years of service, and one year makes her a Newcomer."),
  ],
  "key": "ELL subgroups are set by years of service, not by NYSESLAT level.",
 },
 {
  "id": "2.1-07", "skill": "2.1", "type": "application", "difficulty": 1, "diag": 0,
  "stem": "A 6th grader scored at the Commanding level on last spring's NYSESLAT. Which of the following best describes her status this school year?",
  "options": [
   "She has exited ELL status and is no longer entitled to any ENL services or testing accommodations.",
   "She is a former ELL who receives continued ENL support and testing accommodations for two years.",
   "She remains an ELL until she also scores Level 3 or higher on the Grades 3–8 ELA test this spring.",
   "She is a former ELL who keeps testing accommodations for one more year but no longer receives instructional support.",
  ],
  "answer": 1,
  "why": "A Commanding score on the NYSESLAT meets the exit criteria on its own. Exited students become former ELLs and, under Part 154, keep receiving support (for example, Integrated ENL time in K–8) and ELL testing accommodations for two years after exit.",
  "traps": [
   T("NYS_POLICY", "Exiting ELL status does not end support; former ELLs keep services and accommodations for two years."),
   None,
   T("NYS_POLICY", "The ELA-test requirement applies only to students who score Expanding. Commanding alone is sufficient to exit."),
   T("NYS_POLICY", "Former ELLs receive both continued instructional support and testing accommodations, and for two years, not one."),
  ],
  "key": "Former ELLs keep ENL support and testing accommodations for two years after exiting.",
 },
]

# ---------------------------------------------------------------- 2.1 (batch 2)
QUESTIONS += [
 {
  "id": "2.1-08", "skill": "2.1", "type": "scenario", "difficulty": 3, "diag": 0,
  "stem": "A 7th grader transferring from another state has an IEP for a significant cognitive disability, and his HLQ indicates that Urdu is spoken at home. Under CR Part 154, how is it decided whether he takes the NYSITELL?",
  "options": [
   "He takes the NYSITELL within 10 school days, exactly like every other student whose HLQ shows a language other than English.",
   "The Committee on Special Education decides, because the IEP process takes precedence over ELL identification procedures.",
   "He is exempt from ELL identification, because his disability rather than his home language explains his academic needs.",
   "A Language Proficiency Team reviews the evidence and recommends whether he takes the NYSITELL; its recommendation goes to the superintendent.",
  ],
  "answer": 3,
  "why": "For a student who has an IEP, Part 154 adds a safeguard: a Language Proficiency Team (LPT) considers evidence of the student's English language development and whether the disability, rather than limited English, is the determining factor. The LPT recommends whether the student should take the NYSITELL, and that recommendation goes to the superintendent.",
  "traps": [
   T("NYS_POLICY", "Students with IEPs do not automatically follow the standard path; the LPT first decides whether the NYSITELL is appropriate."),
   T("NYS_POLICY", "The CSE does not make this decision. Part 154 assigns it to the Language Proficiency Team, with the recommendation going to the superintendent."),
   T("MISREFERRAL", "A disability does not rule out ELL status; ELLs with disabilities are a recognized subgroup, and the LPT exists to sort out language versus disability."),
   None,
  ],
  "key": "Student with an IEP: the Language Proficiency Team decides whether to give the NYSITELL and sends its recommendation to the superintendent.",
 },
 {
  "id": "2.1-09", "skill": "2.1", "type": "application", "difficulty": 2, "diag": 0,
  "stem": "Which of the following students meets the NYS definition of a student with interrupted/inconsistent formal education (SIFE)?",
  "options": [
   "A 7th grader from Yemen, in U.S. schools for four months, whose schooling was disrupted by conflict and who is three years below grade level in home-language literacy and math",
   "A 9th grader who has attended NYC schools since grade 6, has not yet exited ELL status, and is currently reading two years below grade level in English",
   "A 3rd grader who arrived from Seoul last month after continuous schooling in Korea and who scored at the Entering level on the NYSITELL",
   "A 5th grader born in the Bronx who missed six weeks of school this year while visiting relatives in the Dominican Republic",
  ],
  "answer": 0,
  "why": "SIFE are ELLs who have attended U.S. schools for less than 12 months and who, on initial enrollment, are two or more years below grade level in home-language literacy and/or math because of interrupted or inadequate schooling. The Yemeni student meets every part: recent arrival, interrupted schooling, and a measured gap in home-language literacy and math.",
  "traps": [
   None,
   T("NYS_POLICY", "This student has been in U.S. schools for over three years, and the SIFE gap is measured in home-language literacy and math, not English reading."),
   T("TERM", "A recent arrival with continuous schooling is a Newcomer ELL. Low English proficiency alone does not make a student SIFE.", "SIFE ↔ Newcomer"),
   T("LITERAL", "The word 'interrupted' is a surface match. A short absence by a U.S.-born student is not interrupted formal education, and nothing suggests she is an ELL."),
  ],
  "key": "SIFE: an ELL under 12 months in U.S. schools, 2+ years below grade level in home-language literacy and/or math because of interrupted schooling.",
 },
 {
  "id": "2.1-10", "skill": "2.1", "type": "scenario", "difficulty": 2, "diag": 0,
  "stem": "A 15-year-old Spanish speaker from Honduras enrolls in a Bronx high school. Her intake responses suggest she attended school only sporadically, and the NYSITELL identifies her as an ELL. What is the school's most appropriate next step regarding possible SIFE status?",
  "options": [
   "Refer her to the Committee on Special Education, since large gaps in her academic skills may point to a learning disability.",
   "Decide her SIFE status by the 10-day identification deadline, using her NYSITELL score as the main evidence of her skills.",
   "Within 30 school days, give the SIFE oral interview questionnaire and, if available in her language, the MLS literacy screener.",
   "Place her in 9th grade by age and wait for her spring NYSESLAT results before considering whether she might be SIFE.",
  ],
  "answer": 2,
  "why": "After a student is identified as an ELL, NYS schools have 30 school days to determine SIFE status. They use an oral interview questionnaire and, for certain languages, the Multilingual Literacy SIFE Screener (MLS), which looks at home-language literacy and math. Gaps caused by missed schooling are an opportunity-to-learn issue, not evidence of a disability.",
  "traps": [
   T("MISREFERRAL", "Gaps caused by interrupted schooling reflect missed opportunity to learn, not a disability. A referral at this point would confuse the two."),
   T("NYS_POLICY", "SIFE status has a 30-school-day window, and the NYSITELL measures English proficiency, not home-language literacy or math."),
   None,
   T("NYS_POLICY", "SIFE determination happens shortly after identification, not after the spring NYSESLAT; waiting delays the supports she needs."),
  ],
  "key": "SIFE status is determined within 30 school days using the oral interview questionnaire and, where available, the MLS.",
 },
 {
  "id": "2.1-11", "skill": "2.1", "type": "analysis", "difficulty": 3, "diag": 0,
  "stimulus": "Enrollment log, grade 6 student\nSchool day 1: Family enrolls student; HLQ indicates Ukrainian.\nSchool day 2: Individual interview in English and Ukrainian by a certified ESOL teacher working with a qualified interpreter.\nSchool day 6: NYSITELL administered; student identified as an ELL at the Transitioning level.\nSchool day 14: Entitlement letter sent to the family in Ukrainian; parent orientation scheduled.",
  "stem": "Which part of this process failed to meet CR Part 154 requirements?",
  "options": [
   "The NYSITELL was given too late, since the identification process must be completed within 5 school days of enrollment.",
   "The parent notification was late, since it must be sent within 5 school days of the ELL determination.",
   "The interview should have been conducted in English only, since the NYSITELL measures English proficiency.",
   "The entitlement letter should have been written in English, the language of instruction, with a translation available on request.",
  ],
  "answer": 1,
  "why": "Identification was finished on school day 6, well within the 10-school-day limit. Parent notification, however, is due within 5 school days of the determination, so it should have gone out by about school day 11; day 14 is late. The bilingual interview and the Ukrainian-language letter were both correct.",
  "traps": [
   T("NYS_POLICY", "Identification must be completed within 10 school days, not 5; day 6 is compliant. Five days is the parent-notification window."),
   None,
   T("NYS_POLICY", "Part 154 requires the interview in both English and the home language; conducting it only in English would be the violation."),
   T("FAMILY_BARRIER", "Notification must be in the parents' preferred language. An English letter with translation 'on request' puts the burden on the family."),
  ],
  "key": "Check two clocks: identification within 10 school days of enrollment; parent notice within 5 school days of determination.",
 },
 {
  "id": "2.1-12", "skill": "2.1", "type": "scenario", "difficulty": 2, "diag": 0,
  "stem": "A family that speaks Wolof enrolls their 11-year-old daughter in a Bronx middle school. No one on staff speaks Wolof, and her 13-year-old brother offers to interpret during the intake interview. What should the school do?",
  "options": [
   "Accept the brother's offer, because he knows both the family's language and his sister's school history better than an outside interpreter would.",
   "Conduct the interview in English only and rely on the NYSITELL results to determine whether she needs ELL services.",
   "Skip the interview, since no Wolof-speaking staff member is available, and proceed directly to NYSITELL testing.",
   "Arrange for a qualified interpreter so that qualified staff can conduct the interview in both English and Wolof.",
  ],
  "answer": 3,
  "why": "The identification interview must be conducted by qualified personnel in English and the home language, using a qualified interpreter when staff do not speak the language. A sibling is not a qualified interpreter, and a child should never carry that responsibility. The interview is a required step, so it cannot be skipped or done in English only.",
  "traps": [
   T("FAMILY_BARRIER", "Children should not interpret for official school processes; it compromises accuracy and confidentiality and places an adult burden on a child."),
   T("NYS_POLICY", "The interview must be in both English and the home language; an English-only interview cannot capture her home-language background."),
   T("NYS_POLICY", "The interview is a required part of Part 154 identification; lack of bilingual staff is not a reason to omit it."),
   None,
  ],
  "key": "No staff speaker of the language? Use a qualified interpreter, never a child, and still interview in both languages.",
 },
 {
  "id": "2.1-13", "skill": "2.1", "type": "knowledge", "difficulty": 1, "diag": 0,
  "stem": "Which of the following best describes the purpose of the NYSITELL?",
  "options": [
   "It identifies which newly enrolled students are ELLs and establishes each one's initial English proficiency level for placement.",
   "It measures ELLs' annual growth in listening, speaking, reading, and writing and determines when they meet exit criteria.",
   "It screens newly enrolled multilingual students for possible learning disabilities before ENL or bilingual placement.",
   "It measures newcomers' home-language literacy and math skills to determine whether they have interrupted schooling.",
  ],
  "answer": 0,
  "why": "The NYSITELL (New York State Identification Test for English Language Learners) is the identification and placement test given during initial enrollment when the HLQ and interview indicate a language other than English. Its result determines ELL status and the starting proficiency level (Entering through Commanding), which drives required units of study.",
  "traps": [
   None,
   T("TERM", "This describes the NYSESLAT, the annual spring test used to measure progress and determine exit.", "NYSITELL ↔ NYSESLAT"),
   T("MISREFERRAL", "Neither ELL identification test screens for disabilities; treating language testing as disability screening confuses language difference with disability."),
   T("TERM", "This describes SIFE screening (the oral interview and the MLS), not the NYSITELL, which measures English proficiency.", "NYSITELL ↔ MLS SIFE screener"),
  ],
  "key": "NYSITELL identifies ELLs and sets the initial level; NYSESLAT measures yearly progress and exit.",
 },
 {
  "id": "2.1-14", "skill": "2.1", "type": "application", "difficulty": 3, "diag": 0,
  "stem": "An 8th grader is in her second year of ELL services and has an IEP for a speech or language impairment. Which statement best describes her subgroup membership under NYS definitions?",
  "options": [
   "She is classified only as a student with a disability, because an IEP takes precedence over ELL subgroup designations.",
   "She is a Developing ELL, because students in the middle grades are placed in that subgroup regardless of years of service.",
   "She is both a Newcomer and an ELL with a disability, because ELL subgroup categories can overlap.",
   "She should not be considered an ELL, because her speech or language impairment explains her difficulty with English.",
  ],
  "answer": 2,
  "why": "NYS ELL subgroups are not mutually exclusive. Years of service (two years, so 0–3, Newcomer) places her in one subgroup, while her IEP places her among ELLs with disabilities. She is entitled to both her ENL services and her special-education services, and planning should address both her language development and her disability.",
  "traps": [
   T("NYS_POLICY", "An IEP does not cancel ELL status or ENL services; the student is entitled to both sets of services."),
   T("LITERAL", "Grade level is a surface detail. The Newcomer/Developing/Long-Term subgroups are defined by years of ELL service."),
   None,
   T("MISREFERRAL", "A disability and second-language development can coexist. Attributing all of her English difficulty to the impairment erases her real language-acquisition needs."),
  ],
  "key": "Subgroups overlap: a student can be a Newcomer, SIFE, or Long-Term ELL and also an ELL with a disability.",
 },
]

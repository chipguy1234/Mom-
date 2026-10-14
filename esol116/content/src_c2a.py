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

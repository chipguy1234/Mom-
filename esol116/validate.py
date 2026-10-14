#!/usr/bin/env python3
"""Validate an ESOL 116 content file (questions + lessons [+ scenarios]).

Usage: python3 validate.py path/to/file.json [more.json ...]
Exit code 1 if any ERROR is found. WARN lines are quality nudges.
"""
import json, re, sys
from collections import Counter, defaultdict

SKILLS = {
    "1": 7, "2": 7, "3": 7, "4": 7, "5": 7, "6": 6, "7": 4,
}
VALID_SKILLS = {f"{c}.{i}" for c, n in SKILLS.items() for i in range(1, n + 1)}
TRAPS = {"TERM", "PARTIAL", "DEFICIT", "LOWER_RIGOR", "ISOLATED", "PASSIVE", "MISREFERRAL",
         "ONE_SIZE", "WRONG_LEVEL", "OVERCORRECT", "EXCLUSION", "ASSESS_INVALID", "LAW_FACT",
         "NYS_POLICY", "STEREOTYPE", "FAMILY_BARRIER", "MISAPPLIED_THEORY", "LITERAL"}
TYPES = {"knowledge", "application", "scenario", "analysis"}


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()


def check(path):
    errs, warns = [], []
    data = json.load(open(path, encoding="utf-8"))
    qs = data.get("questions", [])
    lessons = data.get("lessons", [])
    ids = Counter(q.get("id") for q in qs)
    for i, c in ids.items():
        if c > 1:
            errs.append(f"duplicate id {i}")
    by_skill = defaultdict(list)
    ans_pos = Counter()
    longest_key = 0
    stems = {}
    for q in qs:
        qid = q.get("id", "?")
        sk = q.get("skill")
        if sk not in VALID_SKILLS:
            errs.append(f"{qid}: bad skill {sk!r}")
        if not str(qid).startswith(f"{sk}-"):
            errs.append(f"{qid}: id must start with skill code '{sk}-'")
        by_skill[sk].append(q)
        if q.get("type") not in TYPES:
            errs.append(f"{qid}: bad type {q.get('type')!r}")
        if q.get("difficulty") not in (1, 2, 3):
            errs.append(f"{qid}: difficulty must be 1-3")
        if q.get("diag", 0) not in (0, 1, 2):
            errs.append(f"{qid}: diag must be 0/1/2")
        for f in ("stem", "why", "key"):
            if not isinstance(q.get(f), str) or len(q.get(f, "").strip()) < 10:
                errs.append(f"{qid}: missing/short {f}")
        opts = q.get("options")
        if not isinstance(opts, list) or len(opts) != 4 or not all(isinstance(o, str) and o.strip() for o in opts):
            errs.append(f"{qid}: needs exactly 4 non-empty string options")
            continue
        if len({norm(o) for o in opts}) != 4:
            errs.append(f"{qid}: duplicate options")
        for o in opts:
            if re.search(r"\b(all|none|both) of the (above|these)\b", o, re.I) or re.search(r"\bboth [A-D] and [A-D]\b", o):
                errs.append(f"{qid}: forbidden option form: {o[:40]}")
            if re.match(r"^\(?[A-D][\).:]\s", o):
                errs.append(f"{qid}: options must not carry their own letter labels: {o[:30]}")
        a = q.get("answer")
        if a not in (0, 1, 2, 3):
            errs.append(f"{qid}: answer must be 0-3")
            continue
        ans_pos[a] += 1
        lens = [len(o) for o in opts]
        if lens[a] == max(lens) and lens.count(max(lens)) == 1:
            longest_key += 1
        tr = q.get("traps")
        if not isinstance(tr, list) or len(tr) != 4:
            errs.append(f"{qid}: traps must be a list of 4 aligned with options")
        else:
            for k, t in enumerate(tr):
                if k == a:
                    if t is not None:
                        errs.append(f"{qid}: traps[{k}] must be null (it is the answer)")
                    continue
                if not isinstance(t, dict):
                    errs.append(f"{qid}: traps[{k}] must be an object")
                    continue
                if t.get("code") not in TRAPS:
                    errs.append(f"{qid}: traps[{k}] bad code {t.get('code')!r}")
                if not isinstance(t.get("note"), str) or len(t["note"].strip()) < 15:
                    errs.append(f"{qid}: traps[{k}] needs a real note")
                if t.get("code") == "TERM" and not t.get("pair"):
                    warns.append(f"{qid}: traps[{k}] TERM without 'pair'")
        st = norm(q.get("stem", ""))[:90] + "|" + norm(q.get("stimulus", "") or "")[:60]
        if st in stems:
            warns.append(f"{qid}: stem looks duplicated with {stems[st]}")
        stems[st] = qid
    n = len(qs)
    if n:
        for pos in range(4):
            share = ans_pos[pos] / n
            if share < 0.18 or share > 0.32:
                errs.append(f"answer position {'ABCD'[pos]} is the key {share:.0%} of the time (keep 20-30%)")
        if longest_key / n > 0.38:
            errs.append(f"keyed option is the uniquely longest in {longest_key / n:.0%} of items (max 35%)")
        neg = sum(1 for q in qs if re.search(r"\b(NOT|LEAST|EXCEPT)\b", q.get("stem", "")))
        if neg > max(1, n // 20):
            warns.append(f"{neg} negative stems; keep it rare")
    for sk, items in sorted(by_skill.items()):
        d1 = [q["id"] for q in items if q.get("diag") == 1]
        d2 = [q["id"] for q in items if q.get("diag") == 2]
        if len(d1) != 1 or len(d2) != 1:
            errs.append(f"skill {sk}: needs exactly one diag:1 and one diag:2 (have {d1} / {d2})")
        stim = sum(1 for q in items if (q.get("stimulus") or "").strip())
        if stim < 3:
            warns.append(f"skill {sk}: only {stim} items with a stimulus (want >= 3)")
        appl = sum(1 for q in items if q.get("type") != "knowledge")
        if appl / len(items) < 0.5:
            warns.append(f"skill {sk}: only {appl}/{len(items)} non-knowledge items")
        diffs = Counter(q.get("difficulty") for q in items)
        if diffs[3] == 0 or diffs[1] == 0:
            warns.append(f"skill {sk}: difficulty spread {dict(diffs)}")
    lesson_sk = Counter(l.get("skill") for l in lessons)
    for l in lessons:
        sk = l.get("skill")
        if sk not in VALID_SKILLS:
            errs.append(f"lesson: bad skill {sk!r}")
        body = l.get("body", [])
        words = sum(len((b.get("md") or "").split()) for b in body)
        if not (3 <= len(body) <= 8):
            warns.append(f"lesson {sk}: {len(body)} sections")
        if words < 550:
            warns.append(f"lesson {sk}: only {words} words")
        if not (3 <= len(l.get("traps", [])) <= 6):
            warns.append(f"lesson {sk}: traps count {len(l.get('traps', []))}")
        terms = l.get("terms", [])
        if len(terms) < 8:
            warns.append(f"lesson {sk}: only {len(terms)} terms")
        for t in terms:
            if not t.get("t") or not t.get("d"):
                errs.append(f"lesson {sk}: bad term entry {t}")
        for f in ("title", "why", "tip"):
            if not l.get(f):
                errs.append(f"lesson {sk}: missing {f}")
    for sk in by_skill:
        if sk and not sk.startswith("7") and lesson_sk[sk] != 1:
            errs.append(f"skill {sk}: expected exactly 1 lesson, found {lesson_sk[sk]}")
    for s in data.get("scenarios", []):
        sid = s.get("id", "?")
        for f in ("title", "setting", "prompt", "model", "weak"):
            if not s.get(f):
                errs.append(f"scenario {sid}: missing {f}")
        if not s.get("exhibits"):
            errs.append(f"scenario {sid}: no exhibits")
        if len(s.get("tasks", [])) < 3:
            errs.append(f"scenario {sid}: needs >= 3 tasks")
        mw = len(s.get("model", "").split())
        if not (380 <= mw <= 700):
            warns.append(f"scenario {sid}: model response {mw} words (aim 450-600)")
        if len(s.get("checklist", [])) < 5:
            warns.append(f"scenario {sid}: checklist has {len(s.get('checklist', []))} items")

    print(f"== {path}: {n} questions, {len(lessons)} lessons, {len(data.get('scenarios', []))} scenarios")
    print("   per skill:", {k: len(v) for k, v in sorted(by_skill.items())})
    print("   answer positions:", {"ABCD"[k]: v for k, v in sorted(ans_pos.items())}, f"| key uniquely longest: {longest_key}/{n}")
    for w in warns:
        print("   WARN ", w)
    for e in errs:
        print("   ERROR", e)
    if not errs:
        print("   OK (no errors)")
    return not errs


if __name__ == "__main__":
    ok = all([check(p) for p in sys.argv[1:]])
    sys.exit(0 if ok else 1)

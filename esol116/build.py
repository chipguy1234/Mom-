#!/usr/bin/env python3
"""Merge content/*.json into the app template.

Outputs:
  dist/tesol116.artifact.html  - page body for the claude.ai Artifact (no html/head/body skeleton)
  ../tesol116.html             - standalone full HTML document (open in any browser / GitHub Pages)
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
CONTENT = ROOT / "content"
ORDER = ["c1a", "c1b", "c2a", "c2b", "c3a", "c3b", "c4a", "c4b", "c5a", "c5b", "c6a", "c6b", "cr"]


def main():
    questions, lessons, scenarios, guide = [], [], [], None
    missing = []
    for name in ORDER:
        p = CONTENT / f"{name}.json"
        if not p.exists():
            missing.append(name)
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        questions += d.get("questions", [])
        lessons += d.get("lessons", [])
        scenarios += d.get("scenarios", [])
        if d.get("guide"):
            guide = d["guide"]
    ids = [q["id"] for q in questions]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        sys.exit(f"duplicate ids across files: {sorted(dup)[:10]}")
    # keep only fields the app uses (smaller payload)
    keep = ("id", "skill", "type", "difficulty", "diag", "stimulus", "stem", "options", "answer", "why", "traps", "key")
    qs = [{k: q[k] for k in keep if k in q and q[k] not in (None, "")} for q in questions]
    for q in qs:
        q.setdefault("diag", 0)
    questions.sort(key=lambda q: (tuple(int(x) for x in q["skill"].split(".")), q["id"]))
    bank = {"questions": qs, "lessons": lessons, "scenarios": scenarios, "guide": guide}
    blob = json.dumps(bank, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (ROOT / "app.html").read_text(encoding="utf-8")
    assert "/*__BANK__*/" in tpl
    page = tpl.replace("/*__BANK__*/", blob)
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "tesol116.artifact.html").write_text(page, encoding="utf-8")
    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            + page.split("<style>", 1)[0] + "<style>" + page.split("<style>", 1)[1].split("</style>", 1)[0] + "</style>\n</head>\n<body>\n"
            + page.split("</style>", 1)[1] + "\n</body>\n</html>\n")
    (ROOT.parent / "tesol116.html").write_text(full, encoding="utf-8")
    per = {}
    for q in qs:
        per[q["skill"]] = per.get(q["skill"], 0) + 1
    print(f"questions={len(qs)} lessons={len(lessons)} scenarios={len(scenarios)} guide={'yes' if guide else 'no'} "
          f"size={len(page)/1024:.0f}KB missing={missing}")
    print("per competency:", {c: sum(v for k, v in per.items() if k.startswith(c + ".")) for c in "1234567"})


if __name__ == "__main__":
    main()

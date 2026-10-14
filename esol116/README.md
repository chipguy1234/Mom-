# TESOL 116 Studio

Study simulator for the NYSTCE ESOL CST (Field 116).

- `app.html`: the app (HTML/CSS/JS template). The question bank is injected at build time.
- `content/src_*.py` → `content/*.json`: questions, lessons and written-response tasks (schema in `SPEC.md`).
- `validate.py`: checks every content file (`python3 validate.py content/*.json`).
- `build.py`: merges the content into `../tesol116.html` (standalone page) and `dist/tesol116.artifact.html` (published version).

Published at https://claude.ai/artifact/NrLUPmfAjWYERVS7GEDvjy

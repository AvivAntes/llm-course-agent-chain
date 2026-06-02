# TODO — Broken Phone Project

## ✅ Done

- [x] `main.py` scaffold with 3 translation agents
- [x] `calculate_distance()` vector metric function
- [x] `run_gemini_skill()` Gemini CLI integration
- [x] Basic pipeline: EN → FR → HE → EN

---

## 🔲 Required (Basic Completion)

- [ ] Create `.claude/skills/en_to_fr/Skill.md` — English to French agent prompt
- [ ] Create `.claude/skills/fr_to_he/Skill.md` — French to Hebrew agent prompt
- [ ] Create `.claude/skills/he_to_en/Skill.md` — Hebrew to English agent prompt
- [ ] Verify Gemini CLI is installed and authenticated (`gemini --version`)
- [ ] Run `main.py` end-to-end and confirm output prints without errors
- [ ] Confirm the vector distance is printed at the end

---

## 🔲 Improvements (Bonus / Level 4)

- [ ] **Error handling** — wrap `subprocess.run()` in try/except; surface Gemini CLI errors clearly
- [ ] **Timeout protection** — add a timeout to `subprocess.run()` to prevent hangs
- [ ] **Empty output guard** — detect if an agent returns an empty string and raise a descriptive error
- [ ] **Multiple test sentences** — run the pipeline on 3–5 different phrases and compare distances
- [ ] **Distance histogram** — visualize distances across multiple sentences
- [ ] **Alternate language chains** — try EN → Spanish → Japanese → EN for comparison
- [ ] **Logging** — add a log file (`pipeline.log`) capturing each step's input/output and timestamp
- [ ] **CLI arguments** — accept `--text`, `--chain`, `--verbose` via `argparse`

---

## 🔲 Level 4 — Orchestrator Agent

- [ ] Build an **orchestrator agent** that:
  - Runs all three translation agents
  - Collects distances
  - Automatically selects the best Skill for each step
- [ ] Move agent dispatch logic into a dedicated `orchestrator.py` module
- [ ] Define a `SkillSelector` that scores each Skill and picks the best fit per translation step

---

## 📝 Notes

- Dr. Segal's tip: **don't stop at the minimum** — creativity is graded.
- The distance tool measures translation chain quality; try to get it as close to `0` as possible.
- Each Skill.md should be clear and specific — vague prompts lead to creative but inaccurate translations, which increases drift.

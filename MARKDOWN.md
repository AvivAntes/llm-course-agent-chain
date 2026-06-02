# Architecture & Design Notes — Broken Phone Pipeline

## System Design

### Pipeline Flow

```
[Original Text]
      │
      ▼
 ┌─────────────┐
 │   Agent 1   │  Gemini CLI + en_to_fr/Skill.md
 │  EN → FR    │
 └──────┬──────┘
        │
        ▼
 ┌─────────────┐
 │   Agent 2   │  Gemini CLI + fr_to_he/Skill.md
 │  FR → HE    │
 └──────┬──────┘
        │
        ▼
 ┌─────────────┐
 │   Agent 3   │  Gemini CLI + he_to_en/Skill.md
 │  HE → EN    │
 └──────┬──────┘
        │
        ▼
 [Final Text]
        │
        ▼
 ┌─────────────┐
 │ Distance    │  Vector metric: original vs. final
 │  Tool       │
 └─────────────┘
```

---

## Agent Architecture

Each agent is invoked via the Gemini CLI using a `--prompt` flag that points to a Skill profile. The Skill profile is a Markdown file containing the agent's persona and instructions.

### `run_gemini_skill(skill_path, input_text)`

- Builds a shell command: `gemini --prompt "Using skill in <path>, translate: <text>"`
- Runs via `subprocess.run()` with `capture_output=True`
- Returns `stdout` as the translated string

### Skill File Structure (`.claude/skills/<name>/Skill.md`)

Each Skill.md should define:
- The agent's role (e.g., "You are a professional French translator")
- Input language and output language
- Any style or formality constraints

---

## Distance Metric

### `calculate_distance(text1, text2) → float`

Uses a **cosine-like set similarity** on bag-of-words:

| Value | Meaning |
|-------|---------|
| `0.0` | Identical word sets — perfect preservation |
| `0.5` | Moderate drift — some words changed |
| `1.0` | No overlap — completely different text |

**Formula:**

```
similarity = |A ∩ B| / √(|A| × |B|)
distance   = 1 − similarity
```

**Limitations:**
- Case-insensitive, but does not stem or lemmatize words
- Word-order independent (bag-of-words)
- Does not handle synonyms (e.g., "all" vs "everyone" = distance > 0)

---

## The Four Implementation Levels (from the mission)

| Level | Description |
|-------|-------------|
| **Level 1 – Basic** | 3 separate projects + a 4th comparison project. Each reads a file, translates, saves output. |
| **Level 2 – One project per agent** | 3 agents in one project, each in a separate file. Agents pass data via files; translation chain terminates one after another. |
| **Level 3 – With Skills** | 3 different Skills, each agent translates using a different one. A 4th "find best" Skill = the vector distance comparison tool. |
| **Level 4 – Auto-orchestrator** | An orchestrator agent manages the three translations and distance metrics automatically, selects the best-fit Skill at each step. |

The current implementation (`main.py`) targets **Level 3**.

---

## Design Decisions

- **Shell via `subprocess`** — chosen over a Python SDK to leverage the Gemini CLI's built-in Skill loading mechanism.
- **UTF-8 encoding** — explicitly set to handle Hebrew and French characters correctly.
- **Jaccard-variant distance** — simple and deterministic, avoids embedding dependencies.

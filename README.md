[README.md](https://github.com/user-attachments/files/28516074/README.md)
# 🌐 Broken Phone — Multi-Agent Translation Chain

**Exercise 11 | Multi-Agent Translation Pipeline**

A Python experiment that simulates the classic "Broken Phone" (telephone) game using a chain of three AI translation agents. A sentence passes through English → French → Hebrew → English, and a vector distance metric measures how much meaning was lost (or preserved) along the way.

---

## 🎯 Mission Overview

The goal is to build a **multi-agent translation pipeline** with a comparison tool:

| Agent | Direction |
|-------|-----------|
| Agent 1 | English → French |
| Agent 2 | French → Hebrew |
| Agent 3 | Hebrew → English |
| Tool | Vector distance: original vs. final |

**Example sentence:** `"One for all and all for one"`

The ideal outcome is a vector distance of **0** — meaning the sentence survived the trip perfectly.

---

## 🚀 Quick Start

```bash
python main.py
```

Expected output:

```
--- Original Text: One for all and all for one ---

Running Agent 1 (English to French)...
Result: Un pour tous et tous pour un

Running Agent 2 (French to Hebrew)...
Result: אחד בשביל כולם וכולם בשביל אחד

Running Agent 3 (Hebrew back to English)...
Final Result: One for all and all for one

--- Broken Phone Vector Metric ---
Measured Vector Distance: 0.0
(Note: A distance of 0 means the meaning/text was perfectly preserved!)
```

---

## 🧠 How It Works

Each agent is powered by the **Gemini CLI** and uses a dedicated **Skill profile** stored in `.claude/skills/`. The Skill file contains the agent's system prompt, which instructs it to translate in one specific direction.

The **distance tool** uses a Jaccard-like metric on word sets:

```
distance = 1 - (|intersection| / sqrt(|words1| × |words2|))
```

A distance of `0` = perfect preservation. A distance of `1` = completely different text.

---

## 📁 Project Structure

```
.
├── main.py                        # Main pipeline script
├── README.md                      # This file
├── MARKDOWN.md                    # Architecture & design notes
├── TODO.md                        # Task list & improvement ideas
└── .claude/
    └── skills/
        ├── en_to_fr/
        │   └── Skill.md           # English → French agent prompt
        ├── fr_to_he/
        │   └── Skill.md           # French → Hebrew agent prompt
        └── he_to_en/
            └── Skill.md           # Hebrew → English agent prompt
```

---

## 📦 Requirements

- Python 3.8+
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) installed and authenticated
- Skill files configured in `.claude/skills/`

---

## 👨‍🏫 Assignment Notes

- **Dr. Segal's personal recommendation:** Don't stop at the minimum. Read the code, experiment, be creative — bonus points are awarded for creativity, not just execution.
- The grade reflects the **quality of your work**, not just whether it runs.

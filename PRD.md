**PRODUCT REQUIREMENTS DOCUMENT**

Multi-Agent Translation Chain System

*Course: AI Agents | Dr. Yoram Segal | Bar-Ilan University*

Version 1.0  |  June 2026

| Field | Details |
| :---- | :---- |
| Project Name | Broken Phone \- Multi-Agent Translation Chain |
| Assignment | Mission 2 – Home Exercise |
| Course | AI Agents (AI Agent Infrastructure, L05) |
| Instructor | Dr. Yoram Segal, Bar-Ilan University |
| Source File | main.py |
| Target Skill Level | Level 3 (with Skills) – bonus level: Level 4 (Orchestrator Agent) |
| Status | Draft – For Implementation |

# **1\. Project Overview**

This project implements a multi-agent pipeline that demonstrates the 'Broken Phone' (Telephone Game) effect in AI translation chains. The system routes a phrase through three sequential translation agents, then measures how much the semantic meaning drifted from the original using a vector distance metric.

The exercise is assigned as part of the AI Agents course at Bar-Ilan University, taught by Dr. Yoram Segal. It demonstrates core concepts of agent infrastructure: Skills, multi-agent orchestration, and the Context Window.

| Original Phrase (Required) "One for all and all for one" — Languages are not critical. Preference is for ancient Circassian, Arabic, Russian — but the core principle must be preserved. |
| :---- |

# **2\. Goals & Objectives**

* Build a 3-agent translation chain: English → French → Hebrew → English

* Measure semantic drift using a vector distance tool (Jaccard-based similarity)

* Implement each translation agent using Gemini CLI with a Skill.md profile

* Demonstrate the 'Broken Phone' effect — the more rounds, the further from origin

* Achieve bonus credit by maximizing creativity (Level 3 or Level 4 implementation)

# **3\. System Architecture**

## **3.1 Agent Pipeline**

The system follows a sequential pipeline architecture with four components:

| Component | Role | Input / Output |
| :---- | :---- | :---- |
| Agent 1 | English → French translator | English string → French string |
| Agent 2 | French → Hebrew translator | French string → Hebrew string |
| Agent 3 | Hebrew → English translator | Hebrew string → English string |
| Distance Tool | Vector similarity metric | Original \+ Final → distance score (0.0–1.0) |

## **3.2 Skill File Structure**

Each agent is driven by a Skill.md file located under .claude/skills/\<skill-name\>/. The Skill acts as a 'costume' for the agent, instructing it to behave as a specialized translator for a specific language pair.

| Skill Directory Layout .claude/skills/en\_to\_fr/Skill.md   → English to French.claude/skills/fr\_to\_he/Skill.md   → French to Hebrew.claude/skills/he\_to\_en/Skill.md   → Hebrew to English |
| :---- |

## **3.3 Distance Measurement Tool**

The calculate\_distance() function implements a Jaccard-based vector distance metric comparing the original English phrase to the back-translated English result:

| Distance Formula 1\. Tokenize both strings into word sets (lowercase)2. Compute intersection size3. Similarity \= |intersection| / sqrt(|set1| x |set2|)4. Distance \= 1 \- SimilarityDistance \= 0.0 → Perfect preservationDistance \= 1.0 → Complete semantic drift |
| :---- |

# **4\. Functional Requirements**

## **4.1 Agent Execution**

1. **FR-1:** Each agent must invoke the Gemini CLI with its designated Skill.md path and the input text.

2. **FR-2:** Agents must execute sequentially: Agent 1 output feeds Agent 2, Agent 2 output feeds Agent 3\.

3. **FR-3:** Agent output must be captured from stdout and passed to the next agent.

4. **FR-4:** The system must print each agent's output to the console for visibility.

## **4.2 Skill Files**

5. **FR-5:** Each Skill.md must specify the source and target language.

6. **FR-6:** Skills must be stored under .claude/skills/\<skill-name\>/Skill.md.

7. **FR-7:** Skills must be invocable from the terminal via the Gemini CLI \--prompt flag.

## **4.3 Distance Tool**

8. **FR-8:** The tool must accept two string inputs: original (English) and final (back-translated English).

9. **FR-9:** Output must be a float between 0.0 and 1.0, rounded to 4 decimal places.

10. **FR-10:** A distance of 0.0 must indicate perfect text preservation.

# **5\. Implementation Levels (Quality Tiers)**

The assignment defines four quality tiers. Higher tiers earn bonus credit. The submitted main.py implements Level 1 baseline; students are encouraged to reach Levels 3–4.

| Level | Name | Description |
| :---- | :---- | :---- |
| 1 – Basic | 3 Separate Projects | Three independent projects \+ one comparison project. Each reads a file, translates, saves output. Distance measured in fourth project. |
| 2 – Project/Agent | One Project per Agent | Three separate agents, one per project. Manual sequential terminal execution between agents. |
| **3 – Skills** | **Skills-based (BONUS)** | 3 Skills with different translation directions in a single agent. Agent 'disguises' itself per Skill. 4th Skill \= vector comparison tool. |
| **4 – Auto-Orchestrator** | **Orchestrator Agent (TOP BONUS)** | Orchestrator agent manages all 3 translations and distance comparisons automatically, end-to-end. Auto-selects the appropriate Skill at each step. |

# **6\. Current Implementation Analysis (main.py)**

## **6.1 What the Current Code Does**

The submitted main.py implements Level 1 (Basic) of the assignment. It contains two functions:

* **run\_gemini\_skill:** run\_gemini\_skill(skill\_path, input\_text) — Invokes the Gemini CLI via subprocess, passing a skill path and input text as a prompt.

* **calculate\_distance:** calculate\_distance(text1, text2) — Computes Jaccard-based vector distance between original and final English strings.

The main() function orchestrates three sequential calls and prints results, finishing with the distance metric.

## **6.2 Missing Components**

* Skill.md files are referenced (.claude/skills/en\_to\_fr/Skill.md etc.) but not created.

* No error handling for failed Gemini CLI calls or empty outputs.

* No file I/O — results are only printed to stdout, not persisted.

* Does not implement Level 3 (Skills disguise) or Level 4 (Orchestrator) for bonus credit.

# **7\. Skill.md File Specifications**

Each Skill.md file must instruct the agent to act as a specialized expert translator. The file should be written in Markdown format. Below are the required specifications per Skill:

| en\_to\_fr/Skill.md — English to French Expert You are an expert translator specializing in English to French translation.Your ONLY task is to translate the provided English text into natural, fluent French.Return ONLY the translated French text. No explanations, no notes, no alternatives. |
| :---- |

| fr\_to\_he/Skill.md — French to Hebrew Expert You are an expert translator specializing in French to Hebrew translation.Your ONLY task is to translate the provided French text into natural, fluent Hebrew.Return ONLY the translated Hebrew text. No explanations, no notes, no alternatives. |
| :---- |

| he\_to\_en/Skill.md — Hebrew to English Expert You are an expert translator specializing in Hebrew to English translation.Your ONLY task is to translate the provided Hebrew text into natural, fluent English.Return ONLY the translated English text. No explanations, no notes, no alternatives. |
| :---- |

# **8\. Non-Functional Requirements**

* Language: Python 3.x (the existing main.py must remain the entry point).

* CLI Dependency: Gemini CLI must be installed and accessible in PATH.

* Encoding: All subprocess calls must use UTF-8 encoding to handle Hebrew characters.

* Output Format: Console output must clearly label each agent stage and the final metric.

* Portability: Skill paths must be relative to the project root (.claude/skills/).

# **9\. Acceptance Criteria**

11. Running python main.py produces French, Hebrew, and back-translated English outputs.

12. The vector distance is printed as a float in \[0.0, 1.0\] with 4 decimal places.

13. All three Skill.md files exist under .claude/skills/\<name\>/Skill.md.

14. Each agent correctly invokes its designated Skill during execution.

15. The phrase 'One for all and all for one' is used as the original input.

16. (Bonus) Level 3: Each agent uses a different Skill, selected via 'disguise' mechanism.

17. (Bonus) Level 4: An orchestrator agent manages the full pipeline automatically.

# **10\. Theoretical Background (Course Context)**

This exercise directly demonstrates the following concepts from the L05 – Agent Infrastructure lecture by Dr. Yoram Segal:

* Skills — Skill.md files act as agent 'costumes', enabling the same LLM to behave as different specialized experts.

* Agent Architecture — The pipeline follows the 4-component model: LLM \+ Memory (Context Window) \+ Tools (subprocess) \+ RAG (Skill.md files).

* Context Window Management — Each agent call is stateless; the full input must be passed per call.

* Vector Distance & Semantic Search — The distance tool simulates semantic drift measurement, as taught in the Vectors and Tokens section.

* Lost in the Middle Effect — Long translation chains risk losing meaning, analogous to the U-shaped attention problem.

* Prompt Engineering — Each Skill.md is a prompt engineering artifact: role assignment (Act As), specific instructions, and clear output format.

*End of PRD – Multi-Agent Translation Chain*

Bar-Ilan University | AI Agents Course | Dr. Yoram Segal | 2026
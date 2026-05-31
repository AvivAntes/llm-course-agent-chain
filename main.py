import subprocess
import math

def run_gemini_skill(skill_path, input_text):
    """Executes the Gemini CLI using a specific Skill profile and prompt flag."""
    command = f'gemini --prompt "Using skill in {skill_path}, translate this text: {input_text}"'
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
    return result.stdout.strip()

def calculate_distance(text1, text2):
    """Vector distance tool comparing original vs final text to measure 'Broken Phone' effect."""
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    intersection = words1.intersection(words2)
    if not words1 or not words2:
        return 1.0
    similarity = len(intersection) / math.sqrt(len(words1) * len(words2))
    return round(1 - similarity, 4)

def main():
    # The original exercise text required by Dr. Segal
    original_text = "One for all and all for one"
    print(f"--- Original Text: {original_text} ---\n")
    
    # Agent 1: English -> French
    print("Running Agent 1 (English to French)...")
    french_text = run_gemini_skill(".claude/skills/en_to_fr/Skill.md", original_text)
    print(f"Result: {french_text}\n")
    
    # Agent 2: French -> Hebrew
    print("Running Agent 2 (French to Hebrew)...")
    hebrew_text = run_gemini_skill(".claude/skills/fr_to_he/Skill.md", french_text)
    print(f"Result: {hebrew_text}\n")
    
    # Agent 3: Hebrew -> English
    print("Running Agent 3 (Hebrew back to English)...")
    final_text = run_gemini_skill(".claude/skills/he_to_en/Skill.md", hebrew_text)
    print(f"Final Result: {final_text}\n")
    
    # Distance Tool Measurement
    distance = calculate_distance(original_text, final_text)
    print(f"--- Broken Phone Vector Metric ---")
    print(f"Measured Vector Distance: {distance}")
    print(f"(Note: A distance of 0 means the meaning/text was perfectly preserved!)")

if __name__ == "__main__":
    main()
	
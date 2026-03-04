import sys
import re

def validate_plan(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    issues = []
    for i, line in enumerate(content):
        if re.match(r'^\s*-\s*\[[ xX]\].+', line):
            text = re.sub(r'^\s*-\s*\[[ xX]\]\s*', '', line).strip()
            word_count = len(text.split())
            if word_count > 20:
                issues.append(f"Line {i+1}: Task too long ({word_count} words). Must be < 20 words. Text: '{text[:30]}...'")

    if issues:
        print("Validation Failed. The following tasks are not atomic:")
        for issue in issues:
            print(issue)
        sys.exit(1)
    else:
        print("Validation Passed. All tasks are atomic.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_plan.py <plan_markdown_file>")
        sys.exit(1)
    validate_plan(sys.argv[1])

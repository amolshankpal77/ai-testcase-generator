from prompt_template import build_prompt
from ai_client import generate_test_cases
from parser import parse_ai_output
from export_excel import export_to_excel

def main():

    requirement = input("Enter software requirement:\n")

    prompt = build_prompt(requirement)

    ai_output = generate_test_cases(prompt)

    print("AI Output:\n")
    print(ai_output)

    df = parse_ai_output(ai_output)

    export_to_excel(df)


if __name__ == "__main__":
    main()
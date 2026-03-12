import pandas as pd

def parse_ai_output(ai_text):

    rows = []
    lines = ai_text.split("\n")

    for line in lines:
        if "|" in line:
            columns = [col.strip() for col in line.split("|")]
            rows.append(columns)

    df = pd.DataFrame(rows)

    return df
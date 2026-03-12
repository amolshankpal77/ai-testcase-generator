import pandas as pd

def export_to_excel(df):

    file_name = "generated_test_cases.xlsx"

    df.to_excel(file_name, index=False)

    print("✅ Test cases exported to:", file_name)
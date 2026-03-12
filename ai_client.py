from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_test_cases(prompt):

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
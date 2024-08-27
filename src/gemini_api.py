import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging


load_dotenv()


genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')

logging.basicConfig(filename='app.log', level=logging.INFO)


def generate_text(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logging.error(f"Error generating text: {str(e)}")
        return f"Error: {e}"

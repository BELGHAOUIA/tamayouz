from decouple import config
from google import genai


gemini_api_key = config("GEMINI_API_KEY")

gemini_client = genai.Client(api_key=gemini_api_key)

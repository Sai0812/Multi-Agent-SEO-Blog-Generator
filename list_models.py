import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key configured: {api_key[:10]}...")

# Configure Gemini
genai.configure(api_key=api_key)

# List available models
print("\nListing available models:")
for m in genai.list_models():
    print(f"- {m.name}")
    print(f"  Supported generation methods: {m.supported_generation_methods}")

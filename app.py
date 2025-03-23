from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv
import traceback
import json
import re

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

print(f"API Key configured: {GOOGLE_API_KEY[:10]}...")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.8,
    "top_k": 40,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

try:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    print("Gemini model initialized successfully")
except Exception as e:
    print(f"Error initializing Gemini model: {str(e)}")
    traceback.print_exc()

app = Flask(__name__)

def generate_blog_content(topic):
    prompt = f"""Generate a comprehensive blog post about: {topic if topic else 'current HR and workplace management trends'}

You are a team of specialized agents working together:

1. Research Agent:
- Research current trends
- Identify key points
- Structure findings

2. Content Planning Agent:
- Create detailed outline
- Structure sections
- Plan flow

3. Content Generation Agent:
- Write comprehensive content
- Use engaging style
- Maintain professionalism

4. SEO Agent:
- Use relevant keywords naturally
- Optimize headings
- Enhance readability

5. Review Agent:
- Ensure perfect grammar
- Maintain consistent tone
- Polish final content

Format your response in clean HTML using:
- <h2> for main sections
- <h3> for subsections
- <p> for paragraphs
- <ul> and <li> for lists
- <strong> for emphasis

Important: Do not include any markdown code block markers (like ```html or ```) in your response.
Keep HTML formatting clean with no extra line breaks between tags."""

    try:
        response = model.generate_content(prompt)
        if response and hasattr(response, 'text'):
            # Remove any markdown code block markers if present
            content = response.text
            content = re.sub(r'```html\s*', '', content)
            content = re.sub(r'```\s*$', '', content)
            return content
        else:
            raise Exception("No content generated")
    except Exception as e:
        print(f"Generation error: {str(e)}")
        raise

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        topic = data.get('prompt', '')
        
        try:
            content = generate_blog_content(topic)
            return jsonify({'text': content})
            
        except Exception as api_error:
            error_details = traceback.format_exc()
            print(f"API Error: {str(api_error)}")
            print(f"Error details:\n{error_details}")
            return jsonify({
                'error': f'Gemini API error: {str(api_error)}',
                'details': error_details
            }), 500

    except Exception as e:
        error_details = traceback.format_exc()
        print(f"Server Error: {str(e)}")
        print(f"Error details:\n{error_details}")
        return jsonify({
            'error': str(e),
            'details': error_details
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

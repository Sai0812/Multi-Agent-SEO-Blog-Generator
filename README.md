# Multi-Agent SEO Blog Generator

A sophisticated web application that generates high-quality, SEO-optimized blog posts using a multi-agent system powered by Google's Gemini AI.

## Features

- **Research Agent**: Discovers trending HR topics and gathers relevant information
- **Content Planning Agent**: Creates structured blog post outlines
- **Content Generation Agent**: Writes comprehensive content
- **SEO Optimization Agent**: Ensures content follows SEO best practices
- **Review Agent**: Proofreads and improves content quality

## System Architecture

The application uses a client-server architecture:

- **Frontend**: HTML/CSS/JavaScript with a modern, responsive UI
- **Backend**: Python Flask server
- **AI Model**: Google Gemini Pro
- **API Integration**: RESTful API endpoints

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Copy `sample.env` to `.env`
   - Add your Gemini API key to `.env`

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Usage

1. (Optional) Enter a specific HR topic in the input field
2. Click "Generate Blog Post"
3. Watch the agents work in real-time:
   - Research trending topics
   - Create content outline
   - Generate comprehensive content
   - Optimize for SEO
   - Review and improve quality

## Tools and Frameworks

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **AI Model**: Google Gemini Pro
- **Development**: Visual Studio Code
- **Version Control**: Git

## Project Structure

```
.
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
├── templates/         # HTML templates
│   └── index.html    # Main application page
└── README.md         # Project documentation
```

## Notes

- The application uses Google's Gemini Pro model for AI content generation
- All agents work sequentially to ensure content quality
- The UI provides real-time feedback on the generation process
- Content is automatically optimized for SEO

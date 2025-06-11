
# AI-Powered QA Assistant

A Flask web app that uses OpenAI's GPT-4 to generate test cases and edge cases from a feature description.

## Features

- Input a product/feature description
- Automatically generate detailed test cases using GPT-4
- Lightweight Flask backend and browser-based UI

## Setup Instructions

### Prerequisites

- Python 3.8+
- OpenAI API key (set as environment variable)

### Installation

```bash
git clone https://github.com/your-username/ai-qa-assistant.git
cd ai-qa-assistant
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
export OPENAI_API_KEY=your_api_key_here
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to use the tool.

## File Structure

```
ai_qa_assistant/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

## License

MIT


---

## 🧠 Portfolio Case Study

### Project Summary
AI-Powered QA Assistant is a Flask web application that integrates OpenAI’s GPT-4 to generate detailed QA test cases from feature descriptions. Built to demonstrate how LLMs can assist software testers in reducing manual effort and improving test coverage.

### Skills Demonstrated
- Python (Flask)
- REST API design
- OpenAI API integration
- LLM prompt engineering
- Test automation design
- Frontend (HTML/JS)
- CI-ready with `pytest`
- Deployed to Heroku

### Resume Bullet (STAR Format)
- **Situation**: QA Engineers often spend hours writing test cases manually.
- **Task**: Build a faster, smarter solution using modern tools.
- **Action**: Designed and built a Flask app that uses GPT-4 to generate test cases from natural language.
- **Result**: Streamlined test planning workflow, and published project to GitHub + Heroku.

### LinkedIn Post Template
🚀 Just launched my personal project: **AI-Powered QA Assistant**!  
This Flask app uses OpenAI's GPT-4 to turn feature descriptions into test cases—instantly.  
Great for QA Engineers looking to level up with AI.  
🔗 [GitHub Repo]  
🔗 [Live on Heroku]  
#QA #AI #LLM #Python #Flask #Automation #Portfolio

---

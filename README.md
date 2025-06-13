
# 🤖 AI-Powered Test Case Generator

This is a Python Flask-based web application that uses OpenAI's GPT model to generate detailed and structured test cases from plain-language feature descriptions. Designed to help QA Engineers quickly brainstorm test coverage ideas, including edge cases, the app also supports exporting results as a CSV file.

---

## 🚀 Features

- ✅ Enter any feature description to generate test cases
- 📋 Results include ID, Title, and Expected Result for each test case
- 📥 Export test cases as a downloadable CSV file
- 🌐 Live deployment on Heroku
- 🧪 Flask-based backend with OpenAI integration
- 🐍 Built with Python 3, HTML/CSS, and JavaScript

---

## 🖥️ Demo

Try the live app: [Your Heroku App URL](https://ai-test-case-generator-demo-2679b905385f.herokuapp.com)

---

## 📦 Project Structure

```
ai_qa_assistant/
├── app.py               # Flask application logic
├── requirements.txt     # Dependencies
├── Procfile             # Heroku deployment config
├── runtime.txt          # Python version for Heroku
└── templates/
    └── index.html       # Frontend interface
```

---

## 📄 Requirements

- Python 3.10+
- Flask
- OpenAI Python SDK (`openai>=1.0.0`)
- Gunicorn (for deployment)
- A valid OpenAI API Key

---

## 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone git@github.com:YOUR_USERNAME/ai-test-case-generator.git
cd ai-test-case-generator
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your API key**

```bash
export OPENAI_API_KEY=your-key-here
```

(Or create a `.env` file and load with `python-dotenv` if preferred.)

5. **Run the app**

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ☁️ Deployment to Heroku (CI/CD)

- Push updates to your GitHub repo
- Link your repo to Heroku
- Set config var: `OPENAI_API_KEY`
- Select **Hobby Dyno** or higher for production
- Heroku will auto-deploy on `git push`

---

## 📤 Exporting to CSV

Click **Download as CSV** after test case generation to save a structured `.csv` file including:
- Test Case ID
- Title
- Expected Result

---

## 🔍 Example Feature Input

> A user should be able to log in with email and password.

🧠 Generates structured test cases like:

| ID  | Title                     | Expected Result                        |
|-----|---------------------------|----------------------------------------|
| TC1 | Login with valid creds    | User is redirected to dashboard        |
| TC2 | Invalid password          | User sees error message                |
| TC3 | Email not registered      | User prompted to create an account     |

---

## 🤝 Contributing

Want to improve the UI, add support for login/auth, or plug in test management tools like TestRail? PRs are welcome!

---

## 🛡️ License

MIT License © 2025 Patricia Bautista

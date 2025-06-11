# ai_qa_assistant/app.py

from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_test_cases():
    data = request.get_json()
    feature = data.get("feature")

    if not feature:
        return jsonify({"error": "Feature description is required."}), 400

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a QA expert."},
                {"role": "user", "content": f"Generate detailed test cases and edge cases for this feature: {feature}"}
            ]
        )
        result = response.choices[0].message.content
        return jsonify({"test_cases": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


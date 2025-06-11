# ai_qa_assistant/app.py

from flask import Flask, request, jsonify, render_template, Response
import openai
import os
import logging
import csv
import io

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a QA expert. Respond only in CSV format with columns: ID, Title, Expected Result."},
                {"role": "user", "content": f"Generate detailed test cases and edge cases for this feature: {feature}"}
            ]
        )
        result = response.choices[0].message.content
        return jsonify({"test_cases": result})

    except Exception as e:
        logger.error("OpenAI API error: %s", str(e))
        user_message = "An error occurred while generating test cases. Please try again later or check your OpenAI API usage."
        return jsonify({"error": user_message}), 500

@app.route("/download", methods=["POST"])
def download_csv():
    data = request.get_json()
    feature = data.get("feature")

    if not feature:
        return jsonify({"error": "Feature description is required."}), 400

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a QA expert. Respond only in CSV format with columns: ID, Title, Expected Result."},
                {"role": "user", "content": f"Generate detailed test cases and edge cases for this feature: {feature}"}
            ]
        )
        csv_data = response.choices[0].message.content

        # Create a Flask response with CSV content
        return Response(
            csv_data,
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment;filename=test_cases.csv"}
        )

    except Exception as e:
        logger.error("OpenAI CSV generation error: %s", str(e))
        return jsonify({"error": "Failed to generate CSV export."}), 500

if __name__ == "__main__":
    app.run(debug=True)

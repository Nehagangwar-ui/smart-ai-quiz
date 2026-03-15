from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__)
CORS(app)

# API KEY

client = Groq(api_key=os.environ.get("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"))

@app.route('/quiz', methods=['POST'])
def generate_quiz():

    data = request.json

    ques = data['questions']
    topic = data['topic']

    prompt = f"Generate {ques} MCQ question on {topic} with answer."

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile"
    )

    result = chat_completion.choices[0].message.content

    return jsonify({"quiz": result})


if __name__ == "__main__":
    app.run(debug=True)
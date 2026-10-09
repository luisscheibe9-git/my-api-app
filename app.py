import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from google import genai
from google.genai import types

load_dotenv()
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
app = Flask(__name__)

SYSTEM = (
    "You are a friendly programming tutor for complete beginners. "
    "Use short sentences, plain words, and everyday analogies. "
    "Keep answers under 200 words plus code. Code examples must be short (under 15 lines), "
    "runnable, and commented. Use fenced code blocks tagged with the language. "
    "Always answer in the language the student selected."
)

MODES = {
    "explain": "Explain this concept to a beginner, with one tiny example: {text}",
    "code": "Write short, simple code that does this, then explain it in 2-3 bullets: {text}",
    "example": "Explain what this code does, line by line, in simple terms:\n{text}",
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.json or {}
    mode = data.get("mode", "explain")
    lang = str(data.get("lang", "Python"))[:20]
    text = str(data.get("text", "")).strip()[:1000]
    if mode not in MODES or not text:
        return jsonify(error="Type a question first."), 400
    prompt = f"Language: {lang}\n" + MODES[mode].format(text=text)
    try:
        resp = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(system_instruction=SYSTEM),
        )
        return jsonify(text=resp.text)
    except Exception as e:
        return jsonify(error=f"Request failed (try again in a few seconds): {e}"), 500


if __name__ == "__main__":
    app.run(port=5050, debug=True)

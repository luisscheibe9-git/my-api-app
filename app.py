import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from google import genai

load_dotenv()
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
app = Flask(__name__)

PROMPT = (
    "You are a Pokedex entry writer. Write a fun, short Pokedex entry for: {thing}.\n"
    "Include: a Pokemon-style name, Type, Height/Weight, a 2-sentence description, "
    "and 2 signature moves. Keep it under 120 words."
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/entry", methods=["POST"])
def entry():
    thing = (request.json or {}).get("thing", "").strip()
    if not thing:
        return jsonify(error="Type something first."), 400
    try:
        resp = client.models.generate_content(
            model=MODEL, contents=PROMPT.format(thing=thing[:200])
        )
        return jsonify(text=resp.text)
    except Exception as e:
        return jsonify(error=f"Request failed: {e}"), 500


if __name__ == "__main__":
    app.run(port=5050, debug=True)

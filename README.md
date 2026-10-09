# my-api-app: Pokédex for Anything (Gemini)

Small Flask app that calls Google's Gemini API (free tier).

- `app.py` is the server and the only place the key is used
- `templates/index.html` is the page
- `.env` holds `GEMINI_API_KEY` (git-ignored, never commit)

## Run
1. Get a key at https://aistudio.google.com/apikey and paste it into `.env` after `GEMINI_API_KEY=`
2. `pip install -r requirements.txt`
3. `python app.py`, then open http://localhost:5050

If the model name errors, set `GEMINI_MODEL` in `.env` to a current one.

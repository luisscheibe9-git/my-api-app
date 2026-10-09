# my-api-app: Code Buddy (Gemini)

Beginner programming tutor. Flask server calls Google's Gemini API (free tier).

- `app.py`: server, the only place the key is used. `/api/ask` handles explain / code / example modes
- `templates/index.html`: page with quick examples, concept chips, and an ask box
- `.env`: holds `GEMINI_API_KEY` (git-ignored, never commit)

## Run
1. Get a key at https://aistudio.google.com/apikey and put it in `.env` as `GEMINI_API_KEY=...`
2. `pip install -r requirements.txt`
3. `python app.py`, then open http://localhost:5050

If the model name errors, set `GEMINI_MODEL` in `.env` to a current one.

## Note
This repo does not include an API key. To try it, get your own free Gemini key at https://aistudio.google.com/apikey and put it in a `.env` file as `GEMINI_API_KEY=...`. Never commit `.env`.

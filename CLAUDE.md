# Rules for this project
- The API key lives only in `.env`. Never read, print, or open `.env`. The user edits it themselves.
- `.env` must stay in `.gitignore`. Never commit it.
- The key is used only on the server (`app.py`), never in browser code.
- Stack: Python, Flask, `google-genai` SDK (Gemini free tier), port 5050.
- Model name comes from `GEMINI_MODEL` env var, default `gemini-3.8-flash`. Verify against ai.google.dev/gemini-api/docs if it errors.
- Keep things small; run with `python app.py`.
- Never paste an API key into an AI chat. Exception: free-tier keys (e.g. the free Gemini key) may be shared, since nothing of value is lost. Paid keys never.

# OpenHealing

A compassionate app that helps people experiencing grief discover trusted resources, connect with community support, and access professional care; onboarding for licensed clinicians is planned.

## Why OpenHealing
- Grief & mental health gap: **~137M Americans** live in shortage areas.
- Discovery problem: only **46%** know where to turn; resources often exist but go unfound.
- Persistent need: **54%** struggle to find resources; **57%** see support fade after months.


## Key features
- Search curated articles by keyword
- Find local resources on a map
- Community forum for ongoing peer support
- LLM-backed recommendations for tailored guidance


## Tech stack
- Python 3.11+, Flask 3.x
- SQLAlchemy 2.x, SQLite (dev), Postgres recommended for prod
- `requests`, `pgeocode`, `google-genai`

## Quick start
1. Create venv and install:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Set environment variables used by `backend/config.py`:

```powershell
setx FLASK_ENV development
setx GEMINI_API_KEY "<your-key>"
setx SERPAPI_KEY "<your-key>"
```

3. Run locally:

```powershell
python backend/app.py
```

Open http://localhost:5001/

## Tests
- Run unit tests:

```powershell
pip install pytest
pytest -q
```

## Next steps
- Add DB migrations (Alembic) and Postgres support
- Add CI to run tests and linting
- Containerize with Docker for reproducible deployments

For API details and schema, see `/docs`.
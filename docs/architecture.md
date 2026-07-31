## Architecture Overview

This document provides a concise, production-ready overview of OpenHealing's architecture and key components to help engineers onboard quickly.

Core components

- Backend (Flask): single-process Flask app located in `backend/` with blueprint-based routing. The application entrypoint is `backend/app.py`, which initializes the app, registers blueprints, and creates the database schema on startup.
- Service clients: `backend/services/` contains thin, well-scoped clients for third-party integrations:
   - `articles_client` — curated article search and helpers
   - `google_maps_client` — place search via SerpApi
   - `location_client` — IP-based geolocation fallback
   - `gemini_client` — LLM orchestration (prompt templates and safety framing)
- Persistence layer: SQLAlchemy models in `backend/db/models.py`. Database engine, session factory, and `session_scope()` transaction helper are in `backend/db/connection.py`.
- Frontend: server-rendered Jinja2 templates under `frontend/templates/` with static assets in `frontend/static/`. JSON endpoints exist to support progressive enhancement and potential SPA migration.

Data model (summary)

- `User` (users table)
   - `id` (PK, integer)
   - `username` (string, unique)
   - `password_hash` (string)
   - `created_at` (datetime)

- `Post` (forum posts)
   - `id` (PK, integer)
   - `user_id` (FK → users.id)
   - `title` (string)
   - `body` (text)
   - `category` (string)
   - `created_at` (datetime)

Integration patterns and design choices

- Pluggable clients: external integrations are encapsulated so providers can be replaced and network calls mocked in tests.
- Synchronous request handling keeps the codebase minimal. For production-scale LLM calls or long external requests, use background workers (Celery/RQ) and a job queue.
- Security: password hashing via Werkzeug; secrets injected from environment variables; avoid committing keys to the repository.

Request flows (high level)

1. Resource search (`GET /api/resources`) — the server:
    - Validates `query` parameter.
    - Resolves location via ZIP (`pgeocode`) if provided, otherwise falls back to IP geolocation.
    - Queries place API through `google_maps_client` and merges community-sourced results.
    - Optionally requests LLM recommendations via `gemini_client` and returns an aggregated JSON response.

2. Forum post creation (`POST /forum/new`) — the server:
    - Requires an authenticated session (`session["username"]`).
    - Persists the post via `post_queries.create_post` and redirects to the post view.

Testing and scalability roadmap

- Current tests cover route validation and client helper logic. External network calls are structured to be mocked for deterministic tests.
- Recommended improvements for production:
   - Replace SQLite with Postgres and add Alembic migrations.
   - Add CI (GitHub Actions) that runs tests, linting, and static analysis.
   - Containerize the application with a `Dockerfile` and provide a `docker-compose.yml` for local dev.
   - Offload LLM and long-running network calls to background workers and use caching for common queries.

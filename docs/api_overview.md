# API Reference

This file documents the primary HTTP endpoints in OpenHealing and intended request/response shapes. The backend serves both HTML pages (Jinja templates) and JSON endpoints for client consumption.

Authentication

- `GET /auth/signup` — render signup form
- `POST /auth/signup` — create a new user
  - Body form fields: `username`, `password`
  - Success: redirect to login or return 200 depending on route handling

- `GET /auth/login` — render login form
- `POST /auth/login` — authenticate user
  - Body form fields: `username`, `password`
  - Success: sets session and redirects

- `GET /auth/logout` — clear session and redirect

Articles

- `GET /api/articles?query=<q>` — search curated articles
  - Query params: `query` (required)
  - Response: JSON array of article objects, example element:

```json
{
  "title": "Article title",
  "url": "https://...",
  "summary": "Short summary",
  "source": "organization"
}
```

Resources

- `GET /api/resources?query=<q>&zip_code=<zip>&include_community=1` — search for local resources
  - Query params:
    - `query` (required)
    - `zip_code` (optional) — preferred location; if omitted, IP geolocation is used
    - `include_community` (optional) — include community-sourced entries
  - Response: JSON object with keys like `results`, `recommendations`, `location`.

Forum

- `GET /forum/` — render forum index (lists posts)
- `POST /forum/new` — create a new post (requires session)
  - Form fields: `title`, `body`, `category`
  - Success: redirect to `GET /forum/post/<id>`
- `GET /forum/post/<int:post_id>` — render a single post view

Misc

- `GET /` — homepage (index) renders via template

HTTP status codes and errors

- 200 — success
- 302 — redirect after form POSTs (auth, forum)
- 400 — bad request or missing required parameter (routes validate `query` for API endpoints)
- 401/403 — not currently used extensively; unauthenticated users are redirected to login for protected flows

Implementation notes

- JSON endpoints are implemented in `backend/routes/*_routes.py` and call service clients in `backend/services/` for external APIs.
- External network calls are designed to be mocked in unit tests. Unit tests live in `backend/tests/`.

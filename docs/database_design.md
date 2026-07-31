# Database Schema

This document describes the primary database schema used by OpenHealing. The project currently uses SQLite for development; the schema maps directly to SQLAlchemy models in `backend/db/models.py`.

Primary tables

- users
  - `id` INTEGER PRIMARY KEY AUTOINCREMENT
  - `username` TEXT NOT NULL UNIQUE
  - `password_hash` TEXT NOT NULL
  - `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP

- posts
  - `id` INTEGER PRIMARY KEY AUTOINCREMENT
  - `user_id` INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
  - `title` TEXT NOT NULL
  - `body` TEXT NOT NULL
  - `category` TEXT
  - `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP

Indexes and constraints

- `users.username` has a unique constraint to prevent duplicate accounts.
- `posts.user_id` is a foreign key referencing `users.id` with cascading delete semantics.

Repository mapping

- SQLAlchemy model definitions live in `backend/db/models.py` and mirror the fields above.
- Database engine, session factory, and transaction helper (`session_scope`) are defined in `backend/db/connection.py`.

Migration guidance

- For production, replace SQLite with Postgres and add Alembic for schema migrations. Suggested steps:
  1. Add `alembic` to project dependencies.
  2. Initialize Alembic with the SQLAlchemy URL from environment variables.
  3. Create an initial migration from current models and review the generated SQL.

Notes

- The current schema is intentionally small for an MVP. When adding features like comments, likes, or attachments, follow the same pattern: add a dedicated table, foreign keys, and tests.

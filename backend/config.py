import os


class Config:
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), "familyhelp.db")
    SECRET_KEY = "dev-key-change-later"
    # later: API keys pulled from .env

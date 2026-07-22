import os

class Config:
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), "familyhelp.db")
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///studentwise.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE", "false").lower() in ("1", "true", "yes")
    WTF_CSRF_ENABLED = True
    MAX_CONTENT_LENGTH = 1_000_000  # 1 MB upload limit
    WTF_CSRF_TIME_LIMIT = None      # form tokens last for the whole browser session

    # Optional alert channels. Leave blank to use in-app notifications only.
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", "587"))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")
    MAIL_FROM = os.environ.get("MAIL_FROM", "")
    SEMAPHORE_API_KEY = os.environ.get("SEMAPHORE_API_KEY", "")
    SEMAPHORE_SENDER_NAME = os.environ.get("SEMAPHORE_SENDER_NAME", "")

    @classmethod
    def validate(cls):
        if not cls.SECRET_KEY:
            raise RuntimeError("SECRET_KEY is missing. Copy .env.example to .env and set it.")


class TestConfig(Config):
    SECRET_KEY = "test-key"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    MAIL_SERVER = ""
    SEMAPHORE_API_KEY = ""

    @classmethod
    def validate(cls):
        pass

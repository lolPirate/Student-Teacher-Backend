import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "thisismyveryveryverysecretkey"
    DATABASE_URL = os.environ.get("DATABASE_URI") or r"sqlite:///db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") or True


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DeBUG = False

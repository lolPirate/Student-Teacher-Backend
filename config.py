import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "thisismyveryveryverysecretkey"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or r"sqlite:///db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") or True
    API_KEY = os.environ.get("API_KEY") or "myapikey"


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DeBUG = False

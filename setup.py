from app.app import *
from config import DevConfig
db.create_all(app=create_app(DevConfig))
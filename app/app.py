from flask import Flask
from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)

    # home
    from .home.view import view as home_view
    app.register_blueprint(home_view)

    return app
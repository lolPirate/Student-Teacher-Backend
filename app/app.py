from flask import Flask
from .models.models import db


def create_app(config):
    app = Flask("Teacher-Student-Backend")
    app.config.from_object(config)
    db.init_app(app)
    db.app = app

    # home
    from .home.view import view as home_view
    app.register_blueprint(home_view)

    return app

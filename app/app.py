from flask import Flask
from .models.models import db
from flask_cors import CORS


def create_app(config):
    app = Flask("Teacher-Student-Backend")
    app.config.from_object(config)
    db.init_app(app)
    db.app = app
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    # home
    from .home.view import view as home_view
    app.register_blueprint(home_view)

    # users
    from .users.views import view as user_view
    app.register_blueprint(user_view)

    return app

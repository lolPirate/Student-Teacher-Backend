from flask import Flask
from .models.models import db
from flask_cors import CORS
from flask_migrate import Migrate



def create_app(config):
    app = Flask("Teacher-Student-Backend")
    app.config.from_object(config)
    db.init_app(app)
    db.app = app
    migrate = Migrate(app, db)
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    # home
    from .home.view import view as home_view
    app.register_blueprint(home_view)

    # users
    from .users.views import view as user_view
    app.register_blueprint(user_view)

    return app

import flask_login
from flask import Flask
from flask_alembic import Alembic
from flask_cors import CORS
from resume_api.models import db, User
from resume_api.apis import api_v1, api_v1_w_auth

def create_app():

    app = Flask(__name__)
    app.config.from_object('resume_api.config.settings')

    db.init_app(app)

    api_v1.init_app(app)
    api_v1_w_auth.init_app(app)

    Alembic(app)
    CORS(app)

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)

    # This seems stupid wrong
    @login_manager.user_loader
    def load_user(user_id):
        user_entry = User.get(user_id)
        return User(*user_entry)

    return app


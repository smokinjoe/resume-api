from flask import Flask
from flask_alembic import Alembic
from flask_cors import CORS
from resume_api.models import db
from resume_api.apis import api_v1, api_v1_w_auth

def create_app():

    app = Flask(__name__)
    app.config.from_object('resume_api.config.settings')

    db.init_app(app)

    api_v1.init_app(app)
    api_v1_w_auth.init_app(app)

    Alembic(app)
    CORS(app)

    return app

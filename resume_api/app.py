from flask import Flask
from flask_alembic import Alembic
from flask_cors import CORS
from resume_api.models import db, User
from resume_api.apis import api_v1, api_v1_w_auth
import os

def create_app():

    app = Flask(__name__)
    app.config.from_object('resume_api.config.settings')

    db.init_app(app)

    api_v1.init_app(app)
    api_v1_w_auth.init_app(app)

    Alembic(app)
    CORS(app)

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    return app





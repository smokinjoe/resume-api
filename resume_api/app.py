from flask import Flask, jsonify, g, make_response
from flask_alembic import Alembic
from flask_cors import CORS
from resume_api.models import db, User
from resume_api.apis import api_v1, api_v1_w_auth

from flask_httpauth import HTTPBasicAuth

def create_app():

    app = Flask(__name__)
    app.config.from_object('resume_api.config.settings')

    db.init_app(app)

    api_v1.init_app(app)
    api_v1_w_auth.init_app(app)

    Alembic(app)
    CORS(app)

    auth = HTTPBasicAuth()

    @auth.error_handler
    def unauthorized():
        # return 403 instead of 401 to prevent browsers from displaying the default
        # auth dialog
        return make_response(jsonify({'message': 'Unauthorized access'}), 403)


    @app.route('/api/token')
    @auth.login_required
    def get_auth_token():
        token = g.user.generate_auth_token()
        return jsonify({ 'token': token.decode('ascii') })


    # JOE: NOTE: This gets called when @auth.login_required is performed
    @auth.verify_password
    def verify_password(username_or_token, password):
        # first try to authenticate by token
        user = User.verify_auth_token(username_or_token)
        if not user:
            # try to authenticate with username/password
            user = User.query.filter_by(username = username_or_token).first()
            if not user or not user.verify_password(password):
                return False
        g.user = user
        return True

    return app
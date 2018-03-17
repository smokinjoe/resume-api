from flask import current_app, request, g
from werkzeug.wrappers import Response
from werkzeug.exceptions import HTTPException
from resume_api.models import User

def verify_password(endpoint):
    auth = request.authorization

    if auth is None:
        payload = { 'message': 'Unauthorized.' }
        endpoint.return_error(403, payload=payload)

    username_or_token = auth.username
    password = auth.password

    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
from arrested import ArrestedAPI
from flask import jsonify, g, make_response, request
from flask_httpauth import HTTPBasicAuth
from resume_api.models import User
from .users import users_resource
from .projects import projects_resource
from .schools import schools_resource
from .weapons_of_choice import weapons_of_choice_resource
from .employment_experiences import employment_experiences_resource
from .technical_experiences import technical_experiences_resource
from .resume import resume_resource
from .token import token_resource
# from .middleware import get_api_client_from_request, get_client_token


# auth = HTTPBasicAuth()
#
# @auth.error_handler
# def unauthorized():
#     # return 403 instead of 401 to prevent browsers from displaying the default
#     # auth dialog
#     return make_response(jsonify({'message': 'Unauthorized access'}), 403)
#
# # JOE: NOTE: This gets called when @auth.login_required is performed
# @auth.verify_password
# def verify_password(username_or_token, password):
#     # print('JOE:', flush=True)
#     # print(username_or_token, flush=True)
#     # first try to authenticate by token
#     user = User.verify_auth_token(username_or_token)
#     if not user:
#         # try to authenticate with username/password
#         user = User.query.filter_by(username = username_or_token).first()
#         if not user or not user.verify_password(password):
#             return False
#     g.user = user
#     return True

# @app.route('/api/token')
# @auth.login_required
# def get_auth_token():
#     token = g.user.generate_auth_token()
#     return jsonify({ 'token': token.decode('ascii') })

def verify_password(endpoint):
    auth = request.authorization
    print(auth, flush=True)

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


api_v1 = ArrestedAPI(url_prefix='/v1')

api_v1_w_auth = ArrestedAPI(
    url_prefix='/v1',
    before_all_hooks=[
        # get_api_client_from_request,
        # get_client_token
        # auth.login_required
        verify_password
    ]
)

api_v1_w_auth.register_resource(users_resource, defer=True)
api_v1_w_auth.register_resource(projects_resource, defer=True)
api_v1_w_auth.register_resource(schools_resource, defer=True)
api_v1_w_auth.register_resource(weapons_of_choice_resource, defer=True)
api_v1_w_auth.register_resource(employment_experiences_resource, defer=True)
api_v1_w_auth.register_resource(technical_experiences_resource, defer=True)
api_v1_w_auth.register_resource(token_resource, defer=True)

api_v1.register_resource(resume_resource, defer=True)
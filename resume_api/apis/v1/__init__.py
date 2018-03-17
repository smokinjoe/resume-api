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
from .middleware import verify_password


api_v1 = ArrestedAPI(url_prefix='/v1')

api_v1_w_auth = ArrestedAPI(
    url_prefix='/v1',
    before_all_hooks=[
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
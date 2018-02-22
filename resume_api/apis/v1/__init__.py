from arrested import ArrestedAPI
from .users import users_resource
from .projects import projects_resource
from .schools import schools_resource
from .weapons_of_choice import weapons_of_choice_resource
from .middleware import get_api_client_from_request, get_client_token

api_v1 = ArrestedAPI(
    url_prefix='/v1',
    before_all_hooks=[
        get_api_client_from_request,
        get_client_token
    ]
)

api_v1.register_resource(users_resource, defer=True)
api_v1.register_resource(projects_resource, defer=True)
api_v1.register_resource(schools_resource, defer=True)
api_v1.register_resource(weapons_of_choice_resource, defer=True)

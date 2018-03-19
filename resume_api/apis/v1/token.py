from arrested import Resource, Endpoint, GetObjectMixin
from flask import g


token_resource = Resource('token', __name__, url_prefix='/token')


class TokenIndexEndpoint(Endpoint, GetObjectMixin):
    name = 'object'

    def get_object(self):
        token = g.user.generate_auth_token()
        return { 'token': token.decode('ascii') }

token_resource.add_endpoint(TokenIndexEndpoint)
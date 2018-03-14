# source: https://blog.openshift.com/use-flask-login-to-add-user-authentication-to-your-python-application/
from arrested import Resource, Endpoint, GetObjectMixin
from resume_api.models import db, User
from flask import request, jsonify, Blueprint
from flask_login import login_required, login_user, current_user, logout_user

login_resource = Resource('login', __name__, url_prefix='/login')


class LoginEndpoint(Endpoint, GetObjectMixin):
    name = 'object'

    def handle_post_request(self):
        json_payload = request.get_json()
        user_entry = User.query.filter_by(username=json_payload['username']).first().__dict__
        if (user_entry):
            user = User(user_entry['username'], user_entry['password'])
            print(user.password, flush=True)
            print(json_payload['password'], flush=True)
            if (user.password == json_payload['password']):  # not for prod
                login_user(user)
                return jsonify(isLoggedIn=current_user.is_authenticated), 200

        return jsonify(authorization=False), 403


# @bp.route("/logout", methods=["GET"])
# def logout():
#     logout_user()
#     return jsonify(isLoggedIn=current_user.is_authenticated)

login_resource.add_endpoint(LoginEndpoint)
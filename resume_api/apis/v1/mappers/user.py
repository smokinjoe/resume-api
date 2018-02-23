from kim import field, role

from .base import BaseMapper

from resume_api.models import User


class UserMapper(BaseMapper):

    __type__ = User

    name = field.String()
    email = field.String()
    website = field.String()
    street_address = field.String()
    city = field.String()
    state = field.String()
    zip = field.String()
    phone = field.String()

    __roles__ = {
        '__default__': role.blacklist('password')
    }

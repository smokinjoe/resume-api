from sqlalchemy_utils import EmailType, PasswordType, force_auto_coercion
from .base import db, BaseMixin, DictSerializable
from flask_login import UserMixin
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from resume_api.config import THE_SECRET_KEY

force_auto_coercion()


__all__ = ['User']


class User(BaseMixin, db.Model, DictSerializable, UserMixin):

    __tablename__ = 'resume_api_user'

    name = db.Column(db.Unicode(255))
    email = db.Column(EmailType, nullable=False)
    username = db.Column(db.Unicode(255), nullable=False)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
        ],
    ))
    website = db.Column(db.Unicode(127))
    street_address = db.Column(db.Unicode(127))
    city = db.Column(db.Unicode(127))
    state = db.Column(db.Unicode(127))
    zip = db.Column(db.Unicode(127))
    phone = db.Column(db.Unicode(127))

    def __init__(self, email, password):
        self.email = email
        self.username = email
        self.password = password

    @property
    def serialize(self):
        result = super(User, self).serialize
        extra = {
            'name'          : self.name,
            'email'         : self.email,
            'website'       : self.website,
            'street_address': self.street_address,
            'city'          : self.city,
            'state'         : self.state,
            'zip'           : self.zip,
            'phone'         : self.phone
        }
        return dict(result, **extra)

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(THE_SECRET_KEY, expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(THE_SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid but expired token
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user
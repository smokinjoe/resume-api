from sqlalchemy_utils import EmailType, PasswordType, force_auto_coercion
from .base import db, BaseMixin, DictSerializable
from flask_login import UserMixin


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

    def set_password(self, password):
        #self.password = bcrypt.generate_password_hash(password)
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

    # @classmethod
    # def get(cls, id):
    #     print(id, flush=True)
    #     # return User.query.filter_by(username=id)
    #     return cls.get(id)
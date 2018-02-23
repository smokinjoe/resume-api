from sqlalchemy_utils import EmailType, PasswordType
from .base import db, BaseMixin


__all__ = ['User']


class User(BaseMixin, db.Model):

    __tablename__ = 'resume_api_user'

    name = db.Column(db.Unicode(255), nullable=False)
    email = db.Column(EmailType, nullable=False)
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

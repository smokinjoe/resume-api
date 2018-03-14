import os


class Config(object):

    ALEMBIC_CONTEXT = {
        'render_as_batch': True
    }


class Dev(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////opt/code/resume_api.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = 'admin'
    BASIC_AUTH_PASSWORD = 'secret'
    SECRET_KEY = 'secret_xxx'


settings = globals()[os.environ.get('FLASK_CONFIG', 'Dev')]

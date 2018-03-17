import os


THE_SECRET_KEY = os.environ.get('REACT_APP_JOE_RESUME_API_SECRET')


class Config(object):

    ALEMBIC_CONTEXT = {
        'render_as_batch': True
    }


class Dev(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////opt/code/resume_api.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = THE_SECRET_KEY

settings = globals()[os.environ.get('FLASK_CONFIG', 'Dev')]

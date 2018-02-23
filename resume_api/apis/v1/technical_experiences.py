from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin, DBCreateMixin, DBObjectMixin

from resume_api.models import db, TechnicalExperience
from .mappers import TechnicalExperienceMapper

technical_experiences_resource = Resource('technical_experience', __name__, url_prefix='/technical_experiences')

class TechnicalExperiencesIndexEndpoint(KimEndpoint, DBListMixin, DBCreateMixin):
    name = 'list'
    many = True
    mapper_class = TechnicalExperienceMapper
    model = TechnicalExperience

    def get_query(self):
        stmt = db.session.query(TechnicalExperience)
        return stmt

class TechnicalExperienceObjectEndpoint(KimEndpoint, DBObjectMixin):
    name = 'object'
    url = '/<string:obj_id>'
    mapper_class = TechnicalExperienceMapper
    model = TechnicalExperience

    def get_query(self):
        stmt = db.session.query(TechnicalExperience)
        return stmt

technical_experiences_resource.add_endpoint(TechnicalExperiencesIndexEndpoint)
technical_experiences_resource.add_endpoint(TechnicalExperienceObjectEndpoint)
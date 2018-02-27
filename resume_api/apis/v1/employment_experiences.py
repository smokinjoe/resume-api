from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin, DBCreateMixin, DBObjectMixin

from resume_api.models import db, EmploymentExperience
from .mappers import EmploymentExperienceMapper

employment_experiences_resource = Resource('employment_experiences', __name__, url_prefix='/employment_experiences')

class EmploymentExperiencesIndexEndpoint(KimEndpoint, DBListMixin):
    name = 'list'
    many = True
    mapper_class = EmploymentExperienceMapper
    model = EmploymentExperience

    def get_query(self):
        stmt = db.session.query(EmploymentExperience)
        return stmt

# JOE: NOTE: Disconnected until I have the auth figured out
class EmploymentExperiencesCreateEndpoint(KimEndpoint, DBCreateMixin):
    name = 'list'
    many = True
    mapper_class = EmploymentExperienceMapper
    model = EmploymentExperience

    def get_query(self):
        stmt = db.session.query(EmploymentExperience)
        return stmt

# JOE: NOTE: Disconnected until I have the auth figured out
class EmploymentExperienceObjectEndpoint(KimEndpoint, DBObjectMixin):
    name = 'object'
    url = '/<string:obj_id>'
    mapper_class = EmploymentExperienceMapper
    model = EmploymentExperience

    def get_query(self):
        stmt = db.session.query(EmploymentExperience)
        return stmt

employment_experiences_resource.add_endpoint(EmploymentExperiencesIndexEndpoint)
# employment_experiences_resource.add_endpoint(EmploymentExperienceObjectEndpoint)

from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin, DBCreateMixin, DBObjectMixin

from resume_api.models import db, School
from .mappers import SchoolMapper

schools_resource = Resource('schools', __name__, url_prefix='/schools')


class SchoolsIndexEndpoint(KimEndpoint, DBListMixin, DBCreateMixin):
    name = 'list'
    many = True
    mapper_class = SchoolMapper
    model = School

    def get_query(self):
        stmt = db.session.query(School)
        return stmt


class SchoolObjectEndpoint(KimEndpoint, DBObjectMixin):
    name = 'object'
    url = '/<string:obj_id>'
    mapper_class = SchoolMapper
    model = School

    def get_query(self):
        stmt = db.session.query(School)
        return stmt

schools_resource.add_endpoint(SchoolsIndexEndpoint)
schools_resource.add_endpoint(SchoolObjectEndpoint)
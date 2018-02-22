from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin, DBCreateMixin, DBObjectMixin

from resume_api.models import db, WeaponOfChoice
from .mappers import WeaponOfChoiceMapper

weapons_of_choice_resource = Resource('weapons_of_choice', __name__, url_prefix='/weapons_of_choice')

class ProjectsIndexEndpoint(KimEndpoint, DBListMixin, DBCreateMixin):
    name = 'list'
    many = True
    mapper_class = WeaponOfChoiceMapper
    model = WeaponOfChoice

    def get_query(self):
        stmt = db.session.query(WeaponOfChoice)
        return stmt

class ProjectObjectEndpoint(KimEndpoint, DBObjectMixin):
    name = 'object'
    url = '/<string:obj_id>'
    mapper_class = WeaponOfChoiceMapper
    model = WeaponOfChoice

    def get_query(self):
        stmt = db.session.query(WeaponOfChoice)
        return stmt

weapons_of_choice_resource.add_endpoint(ProjectsIndexEndpoint)
weapons_of_choice_resource.add_endpoint(ProjectObjectEndpoint)
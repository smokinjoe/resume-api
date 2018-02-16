from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin

from resume_api.models import db, Project
from .mappers import ProjectMapper

projects_resource = Resource('projects', __name__, url_prefix='/projects')

class ProjectsIndexEndpoint(KimEndpoint, DBListMixin):
    name = 'list'
    many = True
    mapper_class = ProjectMapper
    model = Project

    def get_query(self):
        stmt = db.session.query(Project)
        return stmt

projects_resource.add_endpoint(ProjectsIndexEndpoint)
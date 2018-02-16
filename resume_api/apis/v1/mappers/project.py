from kim import field
from .base import BaseMapper
from resume_api.models import Project

class ProjectMapper(BaseMapper):
    __type__ = Project
    title = field.String()
    link_title = field.String()
    link_url = field.String()
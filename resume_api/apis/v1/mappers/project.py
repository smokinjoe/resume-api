from kim import field
from .base import BaseMapper
from resume_api.models import Project

class ProjectMapper(BaseMapper):
    __type__ = Project
    name = field.String()
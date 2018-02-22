from kim import field
from .base import BaseMapper
from resume_api.models import School

class SchoolMapper(BaseMapper):
    __type__ = School
    school_name = field.String()
    wut = field.String()
    date_of_graduation = field.String()
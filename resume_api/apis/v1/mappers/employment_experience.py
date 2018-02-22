from kim import field
from .base import BaseMapper
from resume_api.models import EmploymentExperience

class ResponsibilityMapper(BaseMapper):
    __type__ = dict
    title = field.String()
    order = field.Integer()
    description = field.String()

class EmploymentExperienceMapper(BaseMapper):
    __type__ = EmploymentExperience
    company_name = field.String()
    company_role = field.String()
    date_start = field.String()
    date_end = field.String()
    responsibilities = field.Collection(field.Nested(ResponsibilityMapper, source='__self__'))
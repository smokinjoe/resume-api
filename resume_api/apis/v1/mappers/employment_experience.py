from kim import field
from .base import BaseMapper
from resume_api.models import EmploymentExperience

# WIP: JOE: NOTE: Implement this later
# class ResponsibilityMapper(BaseMapper):
#     __type__ = dict
#     title = field.String()
#     order = field.Integer()
#     description = field.String()

class EmploymentExperienceMapper(BaseMapper):
    __type__ = EmploymentExperience
    company_name = field.String()
    company_role = field.String()
    date_start = field.String()
    date_end = field.String()
    items = field.Collection(field.String())
from kim import field
from .base import BaseMapper
from resume_api.models import TechnicalExperience

class TechnicalExperienceMapper(BaseMapper):
    __type__ = TechnicalExperience
    title = field.String()
    items = field.Collection(field.String())
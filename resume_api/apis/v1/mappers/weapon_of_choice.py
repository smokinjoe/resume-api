from kim import field
from .base import BaseMapper
from resume_api.models import WeaponOfChoice

class WeaponOfChoiceMapper(BaseMapper):
    __type__ = WeaponOfChoice
    title = field.String()
    items = field.Collection(field.String())
from .base import db, BaseMixin, DictSerializable

__all__ = ['EmploymentExperience']

class EmploymentExperience(BaseMixin, db.Model, DictSerializable):
    __tablename__ = 'employment_experience'
    company_name = db.Column(db.Unicode(127), nullable=False)
    company_role = db.Column(db.Unicode(255), nullable=False)
    date_start = db.Column(db.Unicode(127), nullable=False)
    date_end = db.Column(db.Unicode(127), nullable=False)
    items = db.Column(db.PickleType(), nullable=False)

    @property
    def serialize(self):
        result = super(EmploymentExperience, self).serialize
        extra = {
            'company_name'  : self.company_name,
            'company_role'  : self.company_role,
            'date_start'    : self.date_start,
            'date_end'      : self.date_end,
            'items'         : self.items
        }
        return dict(result, **extra)
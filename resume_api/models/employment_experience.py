from .base import db, BaseMixin

__all__ = ['EmploymentExperience']

class EmploymentExperience(BaseMixin, db.Model):
    __tablename__ = 'employment_experience'
    company_name = db.Column(db.Unicode(127), nullable=False)
    company_role = db.Column(db.Unicode(255), nullable=False)
    date_start = db.Column(db.Unicode(127), nullable=False)
    date_end = db.Column(db.Unicode(127), nullable=False)
    items = db.Column(db.PickleType(), nullable=False)
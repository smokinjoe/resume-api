from .base import db, BaseMixin

__all__ = ['TechnicalExperience']

class TechnicalExperience(BaseMixin, db.Model):
    __tablename__ = 'technical_experience'
    title = db.Column(db.Unicode(255), nullable=False)
    items = db.Column(db.PickleType(), nullable=False)
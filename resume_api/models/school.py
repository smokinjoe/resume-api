from .base import db, BaseMixin

__all__ = ['School']

class School(BaseMixin, db.Model):
    __tablename__ = 'school'
    school_name = db.Column(db.Unicode(255), nullable=False)
    wut = db.Column(db.Unicode(255), nullable=False)
    date_of_graduation = db.Column(db.Unicode(255), nullable=False)
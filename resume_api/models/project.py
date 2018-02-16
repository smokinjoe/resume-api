from .base import db, BaseMixin

__all__ = ['Project']

class Project(BaseMixin, db.Model):
    __tablename__ = 'project'
    name = db.Column(db.Unicode(255), nullable=False)
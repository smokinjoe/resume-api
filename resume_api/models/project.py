from .base import db, BaseMixin

__all__ = ['Project']

class Project(BaseMixin, db.Model):
    __tablename__ = 'project'
    title = db.Column(db.Unicode(255), nullable=False)
    link_title = db.Column(db.Unicode(255), nullable=False)
    link_url = db.Column(db.Unicode(255), nullable=False)
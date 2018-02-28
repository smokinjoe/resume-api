from .base import db, BaseMixin, DictSerializable
__all__ = ['Project']

class Project(BaseMixin, db.Model, DictSerializable):
    __tablename__ = 'project'
    title = db.Column(db.Unicode(255), nullable=False)
    link_title = db.Column(db.Unicode(255), nullable=False)
    link_url = db.Column(db.Unicode(255), nullable=False)

    @property
    def serialize(self):
        result = super(Project, self).serialize
        extra = {
            'title'     : self.title,
            'link_title': self.link_title,
            'link_url'  : self.link_url
        }
        return dict(result, **extra)

from .base import db, BaseMixin, DictSerializable

__all__ = ['TechnicalExperience']

class TechnicalExperience(BaseMixin, db.Model, DictSerializable):
    __tablename__ = 'technical_experience'
    title = db.Column(db.Unicode(255), nullable=False)
    items = db.Column(db.PickleType(), nullable=False)

    @property
    def serialize(self):
        result = super(TechnicalExperience, self).serialize
        extra = {
            'title' : self.title,
            'items' : self.items
        }
        return dict(result, **extra)
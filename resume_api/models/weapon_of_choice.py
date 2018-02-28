from .base import db, BaseMixin, DictSerializable

__all__ = ['WeaponOfChoice']

class WeaponOfChoice(BaseMixin, db.Model, DictSerializable):
    __tablename__ = 'weapon_of_choice'
    title = db.Column(db.Unicode(255), nullable=False)
    items = db.Column(db.PickleType(), nullable=False)

    @property
    def serialize(self):
        result = super(WeaponOfChoice, self).serialize
        extra = {
            'title': self.title,
            'items': self.items
        }
        return dict(result, **extra)
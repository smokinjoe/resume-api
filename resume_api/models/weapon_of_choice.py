from .base import db, BaseMixin

__all__ = ['WeaponOfChoice']

class WeaponOfChoice(BaseMixin, db.Model):
    __tablename__ = 'weapon_of_choice'
    title = db.Column(db.Unicode(255), nullable=False)
    items = db.Column(db.PickleType(), nullable=False)
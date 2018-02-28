from .base import db, BaseMixin, DictSerializable

__all__ = ['School']

class School(BaseMixin, db.Model, DictSerializable):
    __tablename__ = 'school'
    school_name = db.Column(db.Unicode(255), nullable=False)
    wut = db.Column(db.Unicode(255), nullable=False)
    date_of_graduation = db.Column(db.Unicode(255), nullable=False)

    @property
    def serialize(self):
        result = super(School, self).serialize
        extra = {
            'school_name'           : self.school_name,
            'wut'                   : self.wut,
            'date_of_graduation'    : self.date_of_graduation
        }
        return dict(result, **extra)
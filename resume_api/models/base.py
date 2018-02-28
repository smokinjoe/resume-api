import datetime
from collections import OrderedDict
from sqlalchemy.ext.declarative import declared_attr

from . import db

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


# Source: http://piotr.banaszkiewicz.org/blog/2012/06/30/serialize-sqlalchemy-results-into-json/
class DictSerializable(object):
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'created_at': dump_datetime(self.created_at),
           'updated_at': dump_datetime(self.updated_at)
       }

class BaseMixin(object):

    @declared_attr
    def id(cls):

        return db.Column(db.Integer, primary_key=True)

    @declared_attr
    def created_at(cls):

        return db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @declared_attr
    def updated_at(cls):

        return db.Column(db.DateTime, default=datetime.datetime.utcnow)
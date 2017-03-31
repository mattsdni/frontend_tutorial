import json

from frontend_tutorial import db


class BaseModel(db.Model):
    __abstract__ = True
    json_attrs = []

    def to_json(self):
        return json.dumps(dict((k, getattr(self, k)) for k in self.json_attrs))

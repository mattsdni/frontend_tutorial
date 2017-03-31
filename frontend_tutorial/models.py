import json

from frontend_tutorial import db


class BaseModel(db.Model):
    __abstract__ = True
    json_attrs = []

    def to_json(self):
        return json.dumps(dict((k, getattr(self, k)) for k in self.json_attrs))


class Applicant(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True)
    json_attrs = ['id', 'fname', 'lname', 'email']

    @property
    def full_name(self):
        return self.fname + " " + self.lname

    @staticmethod
    def get_by_email(email):
        return Applicant.query.filter_by(email=email).first()

    def from_json(self, source):
        if 'fname' in source:
            setattr(self, 'fname', source['fname'])
        if 'lname' in source:
            setattr(self, 'lname', source['lname'])
        if 'email' in source:
            setattr(self, 'email', source['email'])
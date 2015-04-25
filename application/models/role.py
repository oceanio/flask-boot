# -*- coding:utf-8 -*-
from flask_security import RoleMixin

from application import db


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __unicode__(self):
        if self.description:
            return self.name + '(' + self.description + ')'
        return self.name
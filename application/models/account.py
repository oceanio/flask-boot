# -*- coding:utf-8 -*-
import datetime

from flask_security import UserMixin

from .role import *


roles_users = db.Table('roles_accounts',
                       db.Column('account_id', db.Integer(), db.ForeignKey('account.id', ondelete="CASCADE")),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id', ondelete="CASCADE")))


class Account(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))
    nickname = db.Column(db.String(250))

    abbrev = db.Column(db.String(45))

    create_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    update_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    confirmed_at = db.Column(db.DateTime())

    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)

    def __unicode__(self):
        return self.email
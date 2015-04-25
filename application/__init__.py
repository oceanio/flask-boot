# -*- coding:utf-8 -*-
from app import *
from admin import *
from services import services

db.create_all()

app.register_blueprint(services)
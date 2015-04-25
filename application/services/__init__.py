# -*- coding:utf-8 -*-
from flask import Blueprint


services = Blueprint('services', __name__, template_folder='templates', static_folder='static', url_prefix='/api')

from .search import *

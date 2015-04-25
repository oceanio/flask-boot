# -*- coding:utf-8 -*-
from flask_admin import Admin
from flask_security import SQLAlchemyUserDatastore, Security
from redis import Redis

from ..app import db, app
from ..models import Account, Role
from views import *


user_datastore = SQLAlchemyUserDatastore(db, Account, Role)
security = Security(app, user_datastore)

admin = Admin(app, u'管理后台',
              index_view=MyAdminIndexView(name=u'主页'),
              base_template='admin/main.html',
              template_mode='bootstrap3')

admin.add_view(MyModelView(Role, db.session, name=u'角色', endpoint=u'role', category=u'用户信息'))
admin.add_view(UserView(Account, db.session, name=u'用户', endpoint=u'user', category=u'用户信息'))
admin.add_view(MyRedisCli(Redis(host='localhost', port=6379, db=3), name=u'Redis控制台'))
from tasks import *
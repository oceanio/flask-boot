# -*- coding:utf-8 -*-
from flask import redirect
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.rediscli import RedisCli
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_security.utils import encrypt_password
from wtforms import fields, validators


# Create admin
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect('/auth/login')

        return self.render('admin/index.html')


class MyModelView(ModelView):
    @staticmethod
    def is_accessible():
        return current_user.has_role('admin')


class UserView(MyModelView):
    column_list = ('email', 'roles')
    form_columns = ('email', 'roles', 'password', 'confirm')

    form_extra_fields = {
        'password': fields.PasswordField(u'密码', [validators.EqualTo('confirm', message=u'密码不匹配')]),
        'confirm': fields.PasswordField(u'确认密码')
    }

    def on_model_change(self, form, model, is_created):
        password = form.password.data
        if password != '':
            model.password = encrypt_password(password)
        else:
            user = self.model.query.filter_by(email=form.email.data).first()
            if user:
                model.password = user.password


class MyRedisCli(RedisCli):
    @staticmethod
    def is_accessible():
        return current_user.has_role('admin')
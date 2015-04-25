# -*- coding:utf-8 -*-
from logging.handlers import RotatingFileHandler
import logging

from celery import Celery
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# TODO: 解决logging的配置问题
file_handler = RotatingFileHandler('/tmp/starlinks.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
app.logger.addHandler(file_handler)

db = SQLAlchemy(app, session_options=dict(autoflush=False))

mail = Mail(app)


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(celery.Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)
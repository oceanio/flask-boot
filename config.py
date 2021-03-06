# -*- coding:utf-8 -*-

SECURITY_URL_PREFIX = '/auth'
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True
SECURITY_CHANGEABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECURITY_CONFIRMABLE = True
SECURITY_POST_LOGOUT_VIEW = '/auth/login'
SECURITY_POST_RESET_VIEW = '/auth/login'
SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False

CELERY_BROKER_URL = 'redis://localhost:6379/3'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'
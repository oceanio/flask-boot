# -*- coding:utf-8 -*-
from application import celery, mail
from . import security


@celery.task
def send_security_email(msg):
    mail.send(msg)


@security.send_mail_task
def delay_security_email(msg):
    send_security_email.delay(msg)
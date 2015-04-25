# -*- coding:utf-8 -*- 
import sys

from application import celery


if __name__ == '__main__':
    celery.worker_main(sys.argv)
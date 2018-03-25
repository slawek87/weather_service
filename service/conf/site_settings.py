import pymysql
from conf.defaults import *  # noqa
import dj_database_url
pymysql.install_as_MySQLdb()

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weather_service',
        'USER': 'root',
        'PORT': '3306',
        'PASSWORD': 'k1k2k3k4',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'use_unicode': True,
            'charset': 'utf8mb4',
            'autocommit': True,
            'init_command': 'SET foreign_key_checks = 0;',
        },
    }
}


# ######### Q_CLUSTER CONFIGURATION
Q_CLUSTER = {
    'name': 'Weather Service',
    'workers': 8,
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Weather Service',
    'redis': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 3,
        'password': None,
        'socket_timeout': None,
        'charset': 'utf-8',
        'errors': 'strict',
        'unix_socket_path': None
    }
}

ALLOWED_HOSTS = ['*']
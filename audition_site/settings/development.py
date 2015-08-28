# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'afx_db',
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASS'),
        'HOST': '',
        'PORT': '',
    }
}
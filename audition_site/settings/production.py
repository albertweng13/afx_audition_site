# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

DATABASES = { 'default': dj_database_url.config()}

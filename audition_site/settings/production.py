# -*- coding: utf-8 -*-
from .base import *

DEBUG = False

DATABASES = { 'default': dj_database_url.config()}

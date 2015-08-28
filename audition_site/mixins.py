# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.timezone import now
import datetime
from audition_site.apps.org import forms
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from .apps.org import models
from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
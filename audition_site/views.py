# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.timezone import now
import datetime
from audition_site.apps.org.forms import DancerForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

def home(request):
    today = datetime.date.today()
    return render(request, "audition_site/index.html", {'today': today, 'now': now(), 'show_login': True})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

class DancerSignUpView(FormView):
    template_name = 'audition_site/signup.html'
    form_class = DancerForm
    success_url = '/'
    def form_valid(self, form):
        m = form.save()
        #return super(DancerSignUpView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url() + "dancer/" + str(m.id))

def dancerId(request, id):
    return render(request, "audition_site/success.html", {'id': id, 'show_login': False})
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.timezone import now
import datetime
from audition_site.apps.org import forms
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from .apps.org import models

def home(request):
    today = datetime.date.today()
    return render(request, "audition_site/index.html", {'today': today, 'now': now(), 'show_login': True})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

class DancerSignUpView(FormView):
    template_name = 'audition_site/signup.html'
    form_class = forms.DancerForm
    success_url = '/successsignup/'
    def form_valid(self, form):
        m = form.save()
        #return super(DancerSignUpView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url() + str(m.id))

def dancerId(request, id):
    return render(request, "audition_site/successdancer.html", {'id': id, 'show_login': False})

def castingGroupId(request, id):
    return render(request, "audition_site/successgroup.html", {'id': id, 'show_login': False})

class CastingGroupFormView(FormView):
    template_name='audition_site/castinggroupform.html'
    form_class = forms.CastingGroupForm
    success_url = '/'
    def form_valid(self, form):
        m = form.save()
        ids = [int(dancer_id) for dancer_id in m.dancer_ids.split(',')]
        for dancer in ids:
            d = models.Dancer.objects.filter(id=dancer).first()
            if d is not None:
                d.casting_group = m
                d.save()
        return HttpResponseRedirect(self.get_success_url() + "successcastinggroup/" + str(m.id))

def dancerProfile(request, dancerId):
    d = models.Dancer.objects.filter(id=dancerId).first()
    return render(request, "audition_site/dancer.html", {'d': d})

def castingGroupProfile(request, groupId):
    g = models.CastingGroup.objects.filter(id=groupId).first()
    d = g.dancers.all()
    return render(request, "audition_site/group.html", {'g': g, 'dancers': d, 'yt_link': embedYouTubeLink(g.video_link)})

def embedYouTubeLink(link):
    return link.replace("youtube.com/watch?v=", "youtube.com/embed/")

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
from . import mixins
from django.shortcuts import redirect
import os
import sys
@login_required
def home(request):
    if hasattr(request.user, 'director'):
        isD = True
        org = request.user.director.team.semester
    else:
        isD = False
        org = request.user.owned_org
    teams = org.teams.all()
    tteams = filter(lambda x: x.level=='T', teams)
    pteams = filter(lambda x: x.level=='P', teams)
    return render(request, "audition_site/index.html", {'isD': isD, 'tteams': tteams, 'pteams': pteams, 'org': org})

@login_required
def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

@login_required
def conflicts(request):
    if hasattr(request.user, 'director'):
        isD = True
        org = request.user.director.team.semester
        tId = request.user.director.team.id
    else:
        isD = False
        org = request.user.owned_org
        tId = 0
    conflicts = sorted(org.conflictedDancers, key=lambda x: x.id)
    if isD:
        your_conflicts = filter(lambda x: request.user.director.team in x.team_offers, conflicts)
    else:
        your_conflicts = []
    empty = len(conflicts) == 0
    return render(request, "audition_site/conflicts.html", {'empty': empty, 'yourConflicts': your_conflicts, 'yourTId': tId, 'dancers': conflicts, 'isD': isD})


def fail(request):
    return render(request, "audition_site/fail.html")

@login_required
def team(request):
    if hasattr(request.user, 'director'):
        team = request.user.director.team
        dancers = team.dancers.all()
        size = team.team_size
        org = team.semester
        if team.level == 'T':
            level = "Training Team"
            if org.trainingFinalized == True:
                finalized="Yes, your roster is finalized."
            else:
                finalized="No, your roster has not been finalized. This may be because you have not indicated that you've chosen all your dancers, or this may be dependent on conflicts or holdouts within other teams."
        else:
            level = "Project Team"
            if org.projectsFinalized == True:
                finalized="Yes, your roster is finalized."
            else:
                finalized="No, your roster has not been finalized. This may be because you have not indicated that you've chosen all your dancers, or this may be dependent on conflicts or holdouts within other teams."
        if team.reached_limit:
            full = "Yes, you cannot choose any more dancers for your team."
        else:
            full = "No, you can choose more dancers for your team if you wish."
        (f, m) = team.gender_ratio
        return render(request, "audition_site/team.html", {'myTeam': True, 'team': team, 'level': level, 'dancers': dancers, 'size': size, 'full': full, 'female': f, 'male': m, 'finalized': finalized})
    else:
        return render(request, "audition_site/team.html")

def searchById(request):
    query = request.GET.get('dancerId')
    return HttpResponseRedirect('/dancer/' + query)

def searchByName(request):
    query = request.GET.get('dancerName').lower()
    if hasattr(request.user, 'owned_org'):
        org = request.user.owned_org
        dancers = org.dancers.all()
    elif hasattr(request.user, 'director'):
        org = request.user.director.team.semester
        dancers = org.dancers.all()
    else:
        dancers = []
    dancersWithName = sorted(filter(lambda x: query in ((x.name).lower()), dancers), key=lambda x: x.id)

    return render(request, 'audition_site/search_dancers.html', {'query': query, 'dancers': dancersWithName})







class DancerSignUpView(FormView):
    template_name = 'audition_site/signup.html'
    form_class = forms.DancerForm
    success_url = '/successsignup/'
    def form_valid(self, form):
        m = form.save()
        dancerlist="Current Dancer List:\n"
        dancers = models.Dancer.objects.all()
        for d in dancers:
            dancerlist+="Number: " + str(d.id) + "|"
            dancerlist+="Name: " + d.name + "|"
            dancerlist+="Gender: " + d.gender + "|"
            dancerlist+="Phone: " + d.phone + "|"
            dancerlist+="Email: " + d.email + "|"
            if(d.casting_group is not None):
                dancerlist+="CastingGroup: " + str(d.casting_group.id) +"\n"
            else:
                dancerlist+="CastingGroup:\n"
        sys.stdout.write(dancerlist)
            
        #return super(DancerSignUpView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url() + str(m.id))

@login_required
def allDancers(request):
    if hasattr(request.user, 'owned_org'):
        org = request.user.owned_org
        d = org.dancers.all()
    elif hasattr(request.user, 'director'):
        org = request.user.director.team.semester
        d = org.dancers.all()
    else:
        d = []
    return render(request, "audition_site/all_dancers.html", {'dancers': sorted(d, key=lambda x: x.id)})

def dancerId(request, id):
    return render(request, "audition_site/successdancer.html", {'id': id, 'show_login': False})

class DancerProfileView(TemplateView):
    template_name = "audition_site/dancer.html"

    def get_context_data(self, **kwargs):
        request = self.request
        dancerId = kwargs['dancerId']
        d = models.Dancer.objects.filter(id=dancerId).first()
        if hasattr(request.user, 'director'):
            team = request.user.director.team
            org = team.semester
            onTeam = team in d.teams.all()
            canbechosen = team.choosingDancers and (not team.reached_limit) and (d.eligible == True)
            if team.level == 'T':
                canbechosen = canbechosen and (d.eligibleTraining == True)
            unchecked = canbechosen and not onTeam
            return {'hidden_remove_form': forms.RemoveDancerForm({'teamId': team.id, 'dancerId': dancerId}), 'hidden_add_form': forms.AddDancerForm({'teamId': team.id, 'dancerId': dancerId}),'addOrRemove': team.choosingDancers, 'director_view': True, 'canRemove': onTeam, 'canChoose': unchecked, 'onTeam': onTeam, 'd': d}
        else:
            org = request.user.owned_org
            return {'d': d, 'director_view': False}

def hidden_add_form_handler(request, dancerId):
    add_dancer_form = forms.AddDancerForm(request.POST)

    if add_dancer_form.is_valid():
        team = request.user.director.team
        dancer = models.Dancer.objects.filter(id = dancerId).first()
        team.dancers.add(dancer)
        team.save()
        return HttpResponseRedirect("/team/")
    else:
        return HttpResponseRedirect("/")

def hidden_remove_form_handler(request, dancerId):
    remove_dancer_form = forms.RemoveDancerForm(request.POST)

    if remove_dancer_form.is_valid():
        team = request.user.director.team
        dancer = models.Dancer.objects.filter(id = dancerId).first()
        team.dancers.remove(dancer)
        team.save()
        return HttpResponseRedirect("/team/")
    else:
        return HttpResponseRedirect("/")






class RandomizeView(TemplateView):
    template_name = "audition_site/conflicts.html"

    def get_context_data(self, **kwargs):
        request = self.request
        if hasattr(request.user, 'director'):
            isD = True
            org = request.user.director.team.semester
            tId = request.user.director.team.id
        else:
            isD = False
            org = request.user.owned_org
            tId = 0
        if hasattr(request.user, 'owned_org'):
            isE = True
        else:
            isE = False
        conflicts = org.conflictedDancers
        if len(conflicts) == 0:
            readyToRandomize = True
            for t in org.teams.all():
                if not t.allSet:
                    readyToRandomize = False
        else:
            readyToRandomize = False
        if isD:
            your_conflicts = filter(lambda x: request.user.director.team in x.team_offers, conflicts)
        else:
            your_conflicts = []
        return {'readyToRandomize': readyToRandomize, 'hidden_randomize_form': forms.RandomizeForm(''), 'isE': isE, 'yourConflicts': your_conflicts, 'yourTId': tId, 'dancers': conflicts, 'isD': isD}

def hidden_randomize_form_handler(request):
    randomize_form = forms.RandomizeForm(request.POST)

    if randomize_form.is_valid():
        org = request.user.owned_org
        org.randomizeDancersIntoTeams()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/?fail=FAIL")






@login_required
def teamProfile(request, teamId):
    team = models.Team.objects.filter(id=teamId).first()
    if hasattr(request.user, 'director') and (team == request.user.director.team):
        return redirect("/team/")
    else:
        dancers = team.dancers.all()
        size = team.team_size
        org = team.semester
        if team.level == 'T':
            level = "Training Team"
            if org.trainingFinalized == True:
                finalized="Yes, this roster is finalized."
            else:
                finalized="No, this roster has not been finalized. This may be because directors have not indicated that they've chosen all your dancers, or this may be dependent on conflicts or holdouts within other teams."
        else:
            level = "Project Team"
            if org.projectsFinalized == True:
                finalized="Yes, this roster is finalized."
            else:
                finalized="No, this roster has not been finalized. This may be because directors have not indicated that they've chosen all your dancers, or this may be dependent on conflicts or holdouts within other teams."
        if team.reached_limit:
            full = "Yes, this team cannot choose any more dancers."
        else:
            full = "No, this team can choose more dancers if the directors wish."
        (f, m) = team.gender_ratio
        return render(request, "audition_site/team.html", {'myTeam': False, 'team': team, 'level': level, 'dancers': sorted(dancers, key=lambda x: x.id), 'size': size, 'full': full, 'female': f, 'male': m, 'finalized': finalized})




@login_required
def castingGroupId(request, id):
    return render(request, "audition_site/successgroup.html", {'id': id, 'show_login': False})

class CastingGroupFormView(mixins.LoginRequiredMixin, FormView):
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

@login_required
def castingGroupProfile(request, groupId):
    g = models.CastingGroup.objects.filter(id=groupId).first()
    d = g.dancers.all()
    return render(request, "audition_site/group.html", {'g': g, 'dancers': d, 'yt_link': embedYouTubeLink(g.video_link)})

def embedYouTubeLink(link):
    return link.replace("youtube.com/watch?v=", "youtube.com/embed/")

@login_required
def all(request):
    isExec = hasattr(request.user, 'owned_org')
    isDir = hasattr(request.user, 'director')
    if hasattr(request.user, 'owned_org'):
        org = request.user.owned_org
        cg = org.castingGroups.all()
    elif hasattr(request.user, 'director'):
        org = request.user.director.team.semester
        cg = org.castingGroups.all()
    else:
        cg = []
    # cg.reverse()
    
    return render(request, "audition_site/all.html", {'cg': sorted(cg, key=lambda x: x.id), 'u': request.user, 'isE': isExec, 'isD': isDir})







# class AddDancerView(TemplateView):
#     template_name = 




class AllSetTeamView(TemplateView):
    template_name = "audition_site/team.html"

    def get_context_data(self, **kwargs):
        request = self.request
        if hasattr(request.user, 'director'):
            team = request.user.director.team
            dancers = team.dancers.all()
            size = team.team_size
            org = team.semester
            if team.level == 'T':
                level = "Training Team"
                if org.trainingFinalized == True:
                    finalized="Yes, your roster is finalized."
                else:
                    finalized="No, your roster has not been finalized. This may be because you have not indicated that you've chosen all your dancers, or this may be dependent on conflicts or holdouts within other teams."
            else:
                level = "Project Team"
                if org.projectsFinalized == True:
                    finalized="Yes, your roster is finalized."
                else:
                    finalized="No, your roster has not been finalized. This may be because you have not indicated that you've chosen all your dancers, or this may be dependent on conflicts or holdouts within other teams."
            if team.reached_limit:
                full = "Yes, you cannot choose any more dancers for your team."
            else:
                full = "No, you can choose more dancers for your team if you wish."
            (f, m) = team.gender_ratio
            allSet = team.allSet
            showForm = not team.hasConflicts
            showUndo = team.hasConflicts and team.allSet
            showSorry = org.choosingProjects and team.level=='T'
            return {'showSorry': showSorry, 'allSet': allSet, 'showForm': showForm, 'un_all_set_form': forms.UnAllSetForm({'org': ''}), 'all_set_form': forms.AllSetForm({'org': ''}), 'myTeam': True, 'team': team, 'level': level, 'dancers': dancers, 'size': size, 'full': full, 'female': f, 'male': m, 'finalized': finalized}
        else:
            return {}

def hidden_all_set_form_handler(request):
    randomize_form = forms.AllSetForm(request.POST)

    if randomize_form.is_valid():
        team = request.user.director.team
        team.allSet = True
        team.save()
        return HttpResponseRedirect("/team")
    else:
        return HttpResponseRedirect("/?fail=FAIL")

def hidden_un_all_set_form_handler(request):
    randomize_form = forms.UnAllSetForm(request.POST)

    if randomize_form.is_valid():
        team = request.user.director.team
        team.allSet = False
        team.save()
        return HttpResponseRedirect("/team")
    else:
        return HttpResponseRedirect("/?fail=FAIL")



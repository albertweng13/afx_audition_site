# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
    return render(request, "audition_site/index.html", {})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings

def index(request):
    return render(request, 'index.html',{'aba':'inicio','settings':settings})
def inicio(request):
    return render(request, 'index.html',{'aba':'inicio'})

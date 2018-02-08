# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime


def addnum(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def addnum2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


def first(request):
    return HttpResponse("<H1>Hello,World!</H1>")


def welcome(request):
    context = {}
    context['title'] = 'Hello World!'
    context['content'] = 'Welcome to Django!'
    context['TutorialList'] = ['1', '2', '3', '4']
    return render(request, 'welcome.html', context)


def time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)



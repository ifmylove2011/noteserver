"""noteserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import *

from . import views, note_op, search, search2

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^add$', views.addnum),
    path('add2/<int:a>/<int:b>/', views.old_add2_redirect),
    path('addnew/<int:a>/<int:b>/', views.addnum2, name='add2'),
    path('admin/', admin.site.urls),
    path('first/', views.first),
    path('time/', views.time),
    url(r'^noteservice$', note_op.noteservice),
    path('download/<str:file_name>', note_op.file_download),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^upload', note_op.upload),
]

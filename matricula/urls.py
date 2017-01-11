# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin,auth
from django.contrib.auth.views import login,logout_then_login
from django.conf.urls.static import static
from .views import index,inicio
import sistema
import rest_framework
from rest_framework.authtoken import views

import rest_framework_jwt.views

from sistema.views import altera_senha,login as login_json
    

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^situacao/$', situacao,name="situacao"),
    url(r'^inicio/$', inicio,name="inicio"),
    url(r'^$', index,name="index"),
    url(r'^matricula/', include('sistema.urls'),name='matricula-space'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', login_view, name='login-ok'),
    url(r'^auth/', include('djoser.urls')),
    #url(r'^auth/login', rest_framework_jwt.views.obtain_jwt_token),
    url(r'^auth/login', login_json),
    url(r'^auth/altera_senha', altera_senha),
    url(r'^entrar/$', login, {'template_name':'login.html'}, name='login'),
    url(r'^sair/$', logout_then_login, {'login_url':'%s/#!login/'%settings.BASE_URL_SITE}, name='logout'),
]








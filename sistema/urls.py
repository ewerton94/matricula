# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from django.views.i18n import javascript_catalog
from django.contrib.auth import login

help(login)

from .views import *

js_info_dict = {
    'packages': ('sistema',),
}




urlpatterns = (
    #url(r'^$', inicio, name='index'),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict),
    url(r'^cadastro', cadastro,name="cadastro"),
    url(r'^disciplinas$', disciplinas,name="disciplinas"),
    url(r'^disciplinas_matriculadas$', disciplinas_matriculadas,name="disciplinas_matriculadas"),
    url(r'^horarios', horarios,name="horarios"),
    url(r'^nova', nova_matricula,name="nova_matricula"),
    url(r'^disciplinas_matriculadas/delete/(?P<disciplina_id>\d+)', deletar_disciplinas,name="deletar_disciplinas"),
    url(r'^get_usuario_logado', get_usuario_logado,name="get_usuario_logado"),
    url(r'^get_usuario_deslogado', get_usuario_deslogado,name="get_usuario_deslogado"),

)



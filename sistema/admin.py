# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Curso, Disciplina, Aluno, Matricula, Oferta, Reajuste

admin.site.site_header = "Administracao de Matriculas - CTEC"
admin.site.index_title = "Administracao de Matriculas - CTEC"
admin.site.site_title = "Site de Administracao de Matriculas - CTEC"

# Register your models here.
class Matricula_Admin(admin.ModelAdmin):
    #list_display = ['alun','pagamento','minicurso','aceite','ativa']
    search_fields = ['aluno__nome',]
    #list_filter=('pagamento','minicurso','aceite','ativa')
    
admin.site.register(Matricula,Matricula_Admin)
admin.site.register(Reajuste,Matricula_Admin)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Aluno)
admin.site.register(Oferta)

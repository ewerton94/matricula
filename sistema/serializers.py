# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import Disciplina, Curso, Aluno,Oferta
from drf_braces.serializers.form_serializer import FormSerializer
from .forms import Form_Cadastro


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ('id', 'nome')
        
        
class OfertaSerializer(serializers.ModelSerializer):
    disciplinas=DisciplinaSerializer(many=True, read_only=True)
    class Meta:
        model = Oferta
        fields = ('disciplinas',)
        

        
class CadastroFormSerializer(FormSerializer):
    class Meta:
        form = Form_Cadastro
        
        
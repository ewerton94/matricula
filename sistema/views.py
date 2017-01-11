# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .forms import Form_Cadastro, Form_Matricula
from .models import Curso, Disciplina, Aluno, Matricula,Oferta
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import os, sys
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.conf import settings
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import os
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser


from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from drf_braces.serializers.form_serializer import FormSerializer
from .serializers import CadastroFormSerializer,DisciplinaSerializer,OfertaSerializer




#from .serializers import FilmeSerializer,GeneroSerializer

from django.core.files.storage import default_storage

import time


import json
import sys

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.views.generic import TemplateView

from .forms import Form_Cadastro
from rest_framework.exceptions import APIException

'''Mensagens de Erro'''


class EmailExistente(APIException):
    status_code = 503
    default_detail = 'Email já cadastrado no sistema.'
    default_code = 'email_cadastrado'


class DisciplinaExistente(APIException):
    status_code = 503
    default_detail = 'Você já se inscreveu na disciplina '
    default_code = 'disciplina_existente'


class VagasEsgotadas(APIException):
    status_code = 503
    default_detail = 'Lamentamos, mas as vagas estão esgotadas para a disciplina '
    default_code = 'vagas_esgotadas'


class HorariosCoincidentes(APIException):
    status_code = 503
    default_detail = 'Verifique os horários da oferta acadêmica! Você está tentando se matricular em disciplinas cujos horários coincidem.'
    default_code = 'horarios_coincidentes'

class UsuarioDeslogado(APIException):
    status_code = 401
    default_detail = 'Você não está conectado, entre no sistema para continuar.'
    default_code = 'usuario_deslogado'
    

class EmailInexistente(APIException):
    status_code = 401
    default_detail = 'E-mail não cadastrado no sistema.'
    default_code = 'email_invalido'
    

class SenhaInvalida(APIException):
    status_code = 401
    default_detail = 'Senha inválida!'
    default_code = 'email_invalido'
    

    
"""UTILS"""

def email_existente(email):
    i = User.objects.filter(username=email)
    if i:
        return True
    else:
        return False
    
def confere_horarios(disciplinas_inscritas,solicitacao):
    if solicitacao:
        disciplinas_a_se_inscrever = [get_object_or_404(Disciplina, pk=pk) for pk in solicitacao]
        l1=[]
        for a in disciplinas_a_se_inscrever:
            l1.extend(Oferta.objects.filter(disciplinas=a))

        l2=[]
        for a in disciplinas_inscritas:
            l2.extend(Oferta.objects.filter(disciplinas=a))
        print("Horarios A se matricular")
        print(l1)
        print("Horarios matriculados")
        print(l2)
        
        if len(set(l1)) != len(l1):
            raise HorariosCoincidentes()
        if l1 and l2:
            for e in l1:
                if e in l2:
                    raise HorariosCoincidentes()
    return True
                





    


    
'''Views'''    
 

    
    
@api_view(['GET','POST'])  
def cadastro(request):
    if request.method == 'POST':
        solicitacao = request.data['dado']            
        mat = solicitacao['matricula']
        email=solicitacao['email']
            
        if email_existente(email):
            raise EmailExistente()


        user = User.objects.create_user(email, email, solicitacao['senha1'])
        new_user = authenticate(
            username=solicitacao['email'],
            password=solicitacao['senha1'],
        )

        if new_user is not None:
            auth_login(request, new_user)
        curso=get_object_or_404(Curso,pk=int(solicitacao['curso']))
        usuario = Aluno.objects.create(nome = solicitacao['nome'],
                                             n_matricula = mat,
                                             email=solicitacao['email'],
                                             curso = curso,
                                             usuario=request.user)
        usuario.save()

        return Response('ok')
        
    else:        
        lista=[]  
        return Response(lista)




@login_required 
@api_view(['GET'])
def disciplinas(request):
    if request.method == 'GET':
        ds = Disciplina.objects.all()
        serializer = DisciplinaSerializer(ds, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def login(request):
    username=request.data['username']
    password=request.data['password']
    try:
        usuario=User.objects.get(username=username)
    except:
        raise EmailInexistente()
    new_user=authenticate(username=username, password=password)
    if new_user is not None:
        auth_login(request, new_user)
        return Response("OK")
    else:
        raise SenhaInvalida()
        
        
@api_view(['POST'])       
def altera_senha(request):
    username=request.user.username
    current_password=request.data['current_password']
    new_user=authenticate(username=username, password=current_password)
    if new_user is not None:
        auth_login(request, new_user)
        usuario=User.objects.get(username=username)
        usuario.set_password(request.data['new_password'])
        usuario.save()
        return Response("OK")
    else:
        raise SenhaInvalida()
        
        
    
    
@api_view(['GET'])
def get_usuario_logado(request):
    if request.method == 'GET':
        try:
            user=request.user
            user=User.objects.get(pk=user.pk)
            if user.is_authenticated():
                return Response({'username':user.username})
        except:
            raise UsuarioDeslogado()
          
        
from  rest_framework.permissions import AllowAny


@api_view(['GET'])
def get_usuario_deslogado(request):
    if request.method == 'GET':
        user=request.user
        user=User.objects.filter(id=user.pk)
        if not user:
            return Response("OK")
        if user[0].is_authenticated():
            raise EmailInexistente() 
            
        return Response("OK") 
            

            
    


    

@login_required 
@api_view(['GET'])
def disciplinas_matriculadas(request):
    if request.method == 'GET':
        aluno = Aluno.objects.get(usuario=request.user)
        matricula=Matricula.objects.filter(aluno=aluno)
        if matricula:
            ds = matricula[0].disciplinas.all()
            print(ds)
        else:
            ds=[]
        serializer = DisciplinaSerializer(ds, many=True)
        return Response(serializer.data)
    
@login_required 
@api_view(['GET'])
def horarios(request):
    if request.method == 'GET':
        if not request.user.is_authenticated():
            return Response([])
        ds = Oferta.objects.all()
        lista=[]
        aluno = Aluno.objects.get(usuario=request.user)
        matricula=Matricula.objects.filter(aluno=aluno)
        if matricula:
            disciplinas_matriculadas = matricula[0].disciplinas.all()
        else:
            disciplinas_matriculadas=[]
        for o in ds:
            disciplinas = [e for e in o.disciplinas.all() if e in disciplinas_matriculadas]
            serializer = DisciplinaSerializer(disciplinas, many=True)
            lista.append({"disciplinas":serializer.data})
        return Response(lista)

    
@api_view(['DELETE'])
def deletar_disciplinas(request,disciplina_id):
    if request.method == 'DELETE':
        aluno = Aluno.objects.get(usuario=request.user)
        matricula=Matricula.objects.filter(aluno=aluno)
        disciplina=get_object_or_404(Disciplina,pk=int(disciplina_id))
        if matricula:
            ds = matricula[0]
        else:
            ds=[]
        if ds:
            ds.disciplinas.remove(disciplina)
            ds.data=datetime.now()
            ds.save()
        return Response("ok")
    
    
@api_view(['POST'])
@login_required 
def nova_matricula(request):
    if request.method == 'POST':
        solicitacao = request.data['disciplinas']
        aluno = Aluno.objects.get(usuario=request.user)
        nome = aluno.nome.split()[0]
        matricula_realizada=Matricula.objects.filter(aluno=aluno)
        if matricula_realizada:
            disciplinas_inscritas=matricula_realizada[0].disciplinas.all()
        else:
            disciplinas_inscritas=[]
        disciplinas=[]
        print(nome)
        
    
    
        for d_id in solicitacao:
            disciplina = get_object_or_404(Disciplina, pk=d_id)
            if disciplina in disciplinas_inscritas:
                ex=DisciplinaExistente()
                ex.detail=ex.default_detail + " "+disciplina.nome + "!"
                raise ex
            elif disciplina.vagas<=len([1 for matricula in Matricula.objects.all() if disciplina in matricula.disciplinas.all()]):
                ex=VagasEsgotadas()
                ex.detail=ex.default_detail + " "+disciplina.nome + "!"
                raise ex

        if confere_horarios(disciplinas_inscritas,solicitacao):
            disciplinas_a_se_matricular=[]
            if matricula_realizada:
                matricula=matricula_realizada[0]
                matricula.data=datetime.now()
            else:
                matricula=Matricula()
                matricula.aluno=aluno
                matricula.save()
            for disciplina_id in solicitacao:
                disciplina_a_se_matricular=get_object_or_404(Disciplina, pk=disciplina_id)
                matricula.disciplinas.add(disciplina_a_se_matricular)
                
            print(disciplinas_a_se_matricular)
            #matricula = Matricula.objects.create(aluno=aluno,disciplinas=disciplinas_a_se_matricular)
            matricula.save()
            return Response("ok")
        

def situacao(request,**kwargs):
    pass
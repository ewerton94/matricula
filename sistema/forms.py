
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


from .models import Curso,Disciplina
from django.contrib import messages
from django.utils import six
from djng.forms import NgDeclarativeFieldsMetaclass, NgModelFormMixin


class Form_Cadastro(forms.Form):
    error_messages = {
        'password_mismatch': "As senhas fornecidas não são iguais.",
    }
    nome = forms.CharField(label="Nome Completo:", error_messages={'required':'Por favor, Insira o seu nome!'}, 
                           widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Nome Completo',}))
    
    matricula = forms.CharField(label="Número de Matrícula:", error_messages={'required':'Por favor, Insira o seu número de matrícula!'},
                          widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':''}))
    email = forms.EmailField(label="E-mail para contato:",
                             error_messages={'invalid': 'Por favor, Insira um e-mail válido!', 'required':'Por favor, Insira um e-mail!'}, 
                             widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'example@example.com'}))
    
    senha1 = forms.CharField(label="Senha para acesso ao sistema:", error_messages={'required':'Por favor, Insira a senha!'},
                                  widget=forms.PasswordInput(
            attrs={'class':'form-control'}))
    senha2 = forms.CharField(label="Digite a senha novamente:", error_messages={'required':'Por favor, Insira a senha!'},
                                  widget=forms.PasswordInput(
            attrs={'class':'form-control'}))
    
    curso = forms.ChoiceField(label="Curso:", choices=((c.id,c.nome) for c in Curso.objects.all()),error_messages={'required':'Por favor, Insira o seu curso de Origem!'},
                                  widget=forms.Select(
            attrs={'class':'form-control','placeholder':'Curso de Origem'}))
    
    def verifica_senhas(self): # check if password 1 and password2 match each other
        if 'senha1' in self.data and 'senha2' in self.data:#check if both pass first validation
            if self.data['senha1'] != self.data['senha2']: # check if they match each other
                
                return "As senhas não cambinam!"
            
class Form_Matricula(forms.Form):

    
    disciplinas = forms.MultipleChoiceField(label = "Disciplinas que deseja se inscrever:",
                                           choices = ((m.id,m.nome) for m in Disciplina.objects.all()),
                                           widget=forms.CheckboxSelectMultiple(
            attrs={'class':''}))
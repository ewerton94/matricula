# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso)
    eletiva = models.BooleanField()
    periodo = models.IntegerField()
    vagas = models.IntegerField()
    
    def __str__(self):
        return self.nome
    

class Aluno(models.Model):
    class Meta:
        verbose_name='Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']
    id = models.AutoField(primary_key=True)
    usuario= models.OneToOneField(User, related_name='profile')
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length = 50)
    n_matricula = models.CharField(max_length = 15)
    email = models.EmailField()
    curso = models.ForeignKey(Curso)
    def __str__(self):
        return '%s'%self.nome
    
class Matricula(models.Model):
    class Meta:
        ordering = ['data']
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno)
    data = models.DateTimeField(auto_now_add=True,verbose_name = 'Data da Matrícula')
    disciplinas =models.ManyToManyField(Disciplina,related_name="disciplinas",blank=True)
    def __str__(self): 
        l = ["%s | %s |"%(self.aluno.nome,self.aluno.n_matricula)]
        ds = [" - %s"%d.codigo for d in self.disciplinas.all()]
        l.extend(ds)
        return "".join(l)
    
    
class Reajuste(models.Model):
    class Meta:
        ordering = ['data']
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno)
    data = models.DateTimeField(auto_now_add=True,verbose_name = 'Data da Matrícula')
    disciplinas_a_retirar =models.ManyToManyField(Disciplina,related_name="disciplinas_a_retirar",blank=True)
    disciplinas_a_adicionar =models.ManyToManyField(Disciplina,related_name="disciplinas_a_adicionar",blank=True)
    def __str__(self): 
        l = ["%s | %s | RETIRAR:"%(self.aluno.nome,self.aluno.n_matricula)]
        ds = [" - %s"%d.codigo for d in self.disciplinas_a_retirar.all()]
        l.extend(ds)
        l.append(" || ADICIONAR:")
        ds = [" - %s"%d.codigo for d in self.disciplinas_a_adicionar.all()]
        l.extend(ds)
        return "".join(l)
    
class Oferta(models.Model):
    horario = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField(Disciplina)
    def __str__(self):
        return self.horario
    

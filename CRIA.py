arq = open("DISCIPLINAS_ambiental.txt",'rt',encoding="utf-8")
linhas=[]
for linha in arq.readlines():
    linha=linha.strip()
    linha=linha.split(';')
    linhas.append(linha)
from sistema.models import Disciplina, Curso
curso=Curso.objects.all()[0]
Disciplina.objects.bulk_create([
        Disciplina(nome=linha[0],codigo=linha[1],curso=curso,eletiva=False,vagas=linha[2],periodo=linha[3]) for linha in linhas
])

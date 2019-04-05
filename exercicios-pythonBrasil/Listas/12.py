#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 

from random import *
idades = []
alturas = []
media = 0
for i in range(1,30 + 1):
    x = randint(6,25)
    y = uniform(1.3,2)
    alturas.append(f'{y:.2f}')
    idades.append(x)
map(float,alturas)
# print(idades)
# print(alturas)
# aluno = []
for x in zip(idades,alturas):
    if x[0] > 13:
        print(x)
    
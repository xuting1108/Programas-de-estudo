#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor. 

a = [1, 6, 3, 5, 9, 8, 4, 2, 7, 10]
eleva = []
soma = 0
for i in a:
    eleva.append(i**2)
    soma = sum(eleva)
print(f'os quadrados de {a} são: {eleva}, e a soma dos quadrados é: {soma}')
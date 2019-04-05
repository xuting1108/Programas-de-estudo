#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range(1,5 + 1):
    print(f'************ {i}ª informaçao *************')
    idade.append(int(input('informe a idade: ')))
    altura.append(float(input('informe a altura em (m): ')))

print(f'Ordem normal das idades: {idade} ordem inversa: {idade[::-1]}')
print(f'Ordem normal das alturas: {altura} ordem inversa: {altura[::-1]}')

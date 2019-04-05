#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 

l1 = ['fernanda', 'roberta', 'lucas', 'elzi', 'filipe', 'igor', 'katia', 'pedro', 'thiago', 'bia']

l2 = [1,6, 9, 15, 16, 12, 18, 25, 62, 84]

l3 = []
# l3.append(zip(l1,l2))
# print(l3)

for x in zip(l1,l2):
    l3.append(x[0])
    l3.append(x[1])
print(l3)
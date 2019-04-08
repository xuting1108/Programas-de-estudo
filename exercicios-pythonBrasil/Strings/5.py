# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

#     FULANO
#     FULAN
#     FULA
#     FUL
#     FU
#     F

def nome_vertical_escada(nome):
    x = ''
    for i in nome:
        i += x 
        print(x.upper())

nome = input('informe seu nome: ')
nome_vertical_escada(nome)
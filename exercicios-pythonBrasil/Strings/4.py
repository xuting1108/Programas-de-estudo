# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

#     F
#     FU
#     FUL
#     FULA
#     FULAN
#     FULANO
def nome_vertical_escada(nome):
    x = ''
    for i in nome:
        x += i
        print(x.upper())

nome = input('informe seu nome: ')
nome_vertical_escada(nome)

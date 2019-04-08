#Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas. 
def nome_contrario(nome):
    inverso = nome[::-1]
    maius = inverso.upper()
    print(f'olá {nome} seu nome de tras pra frente é: {maius}')

nome  = input('informe seu nome: ')
nome_contrario(nome)
#  Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

#     Data de Nascimento: 29/10/1973
#     Você nasceu em  29 de Outubro de 1973.



# def mes_por_extenso(data):

# data = [i.split('/') for i in aniversarios]
data = '11/01/1992'
mes = data.split('/')

print(mes[1])

if mes[1] == 01:
    print('janeiro')
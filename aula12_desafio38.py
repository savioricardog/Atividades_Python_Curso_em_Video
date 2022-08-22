# prog que leia dois numeros int e mostre as mensagens
# 1°  valor é maior ou 2° valor é maior ou não existe maior.

n1 = int(input('Diga um valor '))
n2 = int(input('Diga outro valor '))
if n1 > n2:
    print('O primeiro valor {} é maior'.format(n1))
elif n2 > n1:
    print('O segundo valor {} é maior'.format(n2))
else:
    print('Não existe número maior, os dois são iguais.')
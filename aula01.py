# 1-script que leia o nome e digite as boas vindas

nome = input('Diga seu nome, por gentileza. ')
print('Seja bem vindo {}, é um prazer te conhecer.'.format(nome))

# 2- script que leia a data de nascimento

dia = input('Qual o dia que você nasceu? ')
mes = input('Qual o mês que você nasceu? ')
ano = input('Qual o ano que você nasceu? ')
print('Você nasceu em {}/{}/{}. Correto!?'.format(dia,mes,ano))

# 3- script que leia dois numeros e tente mostrar a soma entre eles.

n1 = int(input('Diga um número '))
n2 = int (input('Diga outro número '))
soma = n1 + n2
print('A soma dos números é {}'.format(soma))

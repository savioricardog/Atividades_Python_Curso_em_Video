#prog que pergunte o salario, e calcule aumento
#salario>1250=10% / salario<1250=15%

salario = float(input('Qual o seu salario? '))
if salario>1250:
    print('O seu salario de {}, aumentado de 10% fica {}'.format(salario,(salario * 10/100)+salario))
else:
    print('O seu salario de {}, aumentado de 15% fica {}'.format(salario, (salario * 15/100)+salario))
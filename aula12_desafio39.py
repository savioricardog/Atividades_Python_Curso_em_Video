# prog que leia data de nascimento e de acordo com a idade:
# 1° se ele ainda vai se alistar | 2° se é hora de se alistar
# 3° se já passou do tempo de se alistar | mostrar o tempo que falta/passou do prazo.
from datetime import date as dt
ano = int(input('Em que ano você nasceu? '))
atual = dt.today().year
data = atual - ano
if data < 18:
    print('Você ainda irá se alistar, Você nasceu em {} e tem{} anos.\n'
          'E seu alistamento ocorrerá em {}'.format(ano, data, ano + 18))
elif data == 18:
    print('Está na epóca de você se alistar.\n'
          'Você nasceu em {} e já tem {} anos completos'.format(ano, data))
elif data > 18:
    print('Você nasceu em {} já tem {} anos.\n'
          'Fazem {} anos que você deveria ter se alistado.'.format(ano, data, (data - 18)))
    alistamento = str(input('Você se alistou? ').title())
    if alistamento == 'Sim':
        print('Que bom, é isso ai!')
    elif alistamento == 'Não':
        print('E ta esperando o que porra?!')

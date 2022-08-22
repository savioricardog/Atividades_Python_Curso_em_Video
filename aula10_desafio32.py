#faça um programa que leia um ano qualquer e diga se é ano bissexto
from datetime import date as dt
ano = int(input('Diga um ano . Coloque 0 para analisar o ana atual. '))
if ano == 0:
    ano = dt.today().year #se colocar "0" ele vai usar a data atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {}, não é bissexto'.format(ano))
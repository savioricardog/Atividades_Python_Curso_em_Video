# ler ano de nasc e dizer a categoria do atleta de natação

from datetime import date as dt
anoNasc = int(input('Em que ano você nasceu? '))
atual = dt.today().year
categoria = atual - anoNasc
if categoria <= 9:
    print('O atleta tem {} anos e é da categoria MIRIM.'.format(categoria))
elif categoria <= 14:
    print('O atleta tem {} anos e é da categoria INFANTIL.'.format(categoria))
elif categoria <= 19:
    print('O atleta tem {} anos e é da categoria JUNIOR.'.format(categoria))
elif categoria <= 20:
    print('O atleta tem {} anos e é da categoria SÊNIOR.'.format(categoria))
elif categoria > 20:
    print('O atleta tem {} anos e é da categoria MASTER.'.format(categoria))
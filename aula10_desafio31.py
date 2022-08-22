#desenvolva uum programa que pergunte a distancia de uma viagem e calcule o preço da passagem

distancia = float(input('Qual é o distancia da sua viagem em km? '))
if distancia <= 200:
    print('O valor da passagem é {:.2f}'.format(distancia * 0.50))
else:
    print('O valor da passagem é {:.2f}'.format(distancia * 0.45))
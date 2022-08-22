# prog que le a velocidade do carro

velo = int(input('A velocidade do carro é '))
multa = (velo - 80) * 7
if velo > 80:
    print('Você ultrapassou o limite de velocidade de 80km/h\n'
          'você está multado em R$ {} reais!'.format(multa))
else:
    print('Você está andando dentro do limite de velocidade!')
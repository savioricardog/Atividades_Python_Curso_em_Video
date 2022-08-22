n1 = float(input('Quantos reais você tem na carteira? R$ '))
dolar = 4.99
euro = 5.24
convDolar = n1 / dolar
convEuro = n1 / euro
print('O valor do dolár está R$ {}, e do Euro está {},\n'
      'então com R$ {} reais você consegue comprar R$ {:.2f} dólares.\n'
      'Ou {:.2f} euros.'.format(dolar,euro, n1, convDolar,convEuro))
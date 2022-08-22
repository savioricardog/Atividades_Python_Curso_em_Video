precBruto = float(input('O preço bruto do produto é R$ '))
print('Mas na liquidação sairá com 5% de desconto.')
desc = precBruto - (precBruto * 5 / 100)
print('Então de R$ {:.2f} reais, com desconto de 5%,\n'
      'O produto sairá por R$ {:.2f} reais.'.format(precBruto, desc))

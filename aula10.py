#condições simples e compostas

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2
print('A sua média é {:.2f}'.format(n))
if n >= 6.00:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')
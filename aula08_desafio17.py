from math import hypot
# testandooooo
ca = float(input('Valor do cateto adjacente: '))
co = float(input('Valor do cateto oposto: '))
h = hypot(ca, co)
print('A hipotenusa é {:.2f}'.format(h))
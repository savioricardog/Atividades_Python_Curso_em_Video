#diga a multiplica por 2,3 e a raiz de um numero
n = int(input('Diga um numero '))
multi2 = n * 2
multi3 = n * 3
raiz = n ** (1/2)
print('O número {} multiplicado por x2 é {},\npor x3 é {}'
      ' e a sua raiz quadrada é {:.3f}'.format(n,multi2,multi3,raiz))
# prog que leia um número e diga o seu fatorial.
n = int(input('Digite um numero '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))

'''from math import factorial
from time import sleep
numero = int(input('Diga um valor '))
fatorial = factorial(numero)
print(fatorial)
sleep(0.5)
while numero != 0:
    numero = int(input('Diga um valor '))
    fatorial = factorial(numero)
    sleep(0.5)
    print(fatorial)'''



#escreva um programa que faça o pc pensar em um numero de 0 a 5
import random

num = str(input('Qual número o pc pensou? '))
lista = ('1','2','3','4','5')
r = random.choice(lista)
print('O número pensado é {}'.format(r))
if num == r:
    print('Você acertou, congrats bro!')
elif num > '5' :
    print('É de 0 a 5, burro!')
else:
    print('Errado, tente outra vez!')
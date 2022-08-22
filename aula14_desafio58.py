# refaça desafio 28 em que o pc vai pensar em um numero de 0a10 e o usuario vai tentar adivinhar.

import random  # from random import randint

cont = 1
num = str(input('Qual número que o pc pensou? '))
lista = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')  # or randint(0, 10)
r = random.choice(lista)
while num != r:
    num = str(input('TCHUUFAVOR, de novo anda anda '))
    cont += 1
print('O pc pensou no n° {} e você precisou de {} tentativas para acertar.'.format(r, cont))

# -----------------------------------------------------------

'''from random import randint
computador = randint(0, 10)
print('Sou seu computador e pensei em número entre 0 e 10.')
print('Séra que consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente novamente! ')
        elif jogador > computador:
            print('Menos.. Tente novamente! ')
print('Você acertou o n° {} com {} palpites'.format(computador, palpites))'''

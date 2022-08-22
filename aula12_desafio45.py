# jokenpo
print('{:=^50}'.format(' Jokenpozin maroto '))

import random
from time import sleep

jogador = str(input('''Escolha no jokenpo:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura.
Qual sua jogada? ''')).capitalize()
pc = ['Pedra', 'Papel', 'Tesoura']
choice = random.choice(pc)
print('-='* 30)
print('\033[7:34:50mJÓ\033[m')
sleep(0.5)
print('\033[7:34:50mKEN\033[m')
sleep(0.5)
print('\033[7:34:50mPÔ!!!\033[m')
sleep(0.5)
print('-= '*30)
if choice == 'Pedra':
    if jogador == '0':
        print('EMPATE, ambos escolheram {}'.format('Pedra'))
    elif jogador == '1':
        print('O jogador com {} GANHOU do pc que escolheu {}'.format('Papel', 'Pedra'))
    elif jogador == '2':
        print('O jogador com {} PERDEU para o pc que escolheu {}'.format('Tesoura', 'Pedra'))
    else:
        print('Jogada invalida, tente novamente!')
elif choice == 'Papel':
    if jogador == '0':
        print('O jogador com {} PERDEU para o pc que escolher {}'.format('Pedra', 'Papel'))
    elif jogador == '1':
        print('EMPATE, ambos escolheram {}'.format('Papel'))
    elif jogador == '2':
        print('O jogador com {} GANHOU do pc que escolheu {}'.format('Tesoura', 'Papel'))
    else:
        print('Jogada invalida, tente novamente!')
elif choice == 'Tesoura':
    if jogador == '0':
        print('O jogador com {} GANHOU do pc que escolheu {}'.format('Pedra', 'Tesoura'))
    elif jogador == '1':
        print('O jogador com {} PERDEU para o pc que escolheu'.format('Papel', 'Tesoura'))
    elif jogador == '2':
        print('EMPATE, o ambos escolheram {}'.format('Tesoura'))
    else:
        print('Jogada invalida, tente novamente!')
#crie um porgrama que leia um numero int e diga se é par ou impar

num = int(input('Diga-me um número '))
identNum = num % 2
if identNum  == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))

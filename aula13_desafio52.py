# prog que leia um número e diga se é um número primo

np = int(input('Diga um número '))
tot = 0
for c in range(1, np + 1):
    if np % c == 0:
        print('\033[33m'.format(c), end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m\nO número {}, foi divisivel {}x'.format(np, tot), end=' ')
if tot == 2:
    print('\nE por isso ele é primo')
else:
    print('\nE por isso ele não é primo')


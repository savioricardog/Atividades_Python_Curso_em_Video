# prog que leia os n's pares de 0 a 50.
#for c in range(2, 51, 2):
#    print('.', end='')
#    print(c, end=' ')
#print('Feito!')

cont = 0
for c in range(1, 51):
    if c % 2 == 0:
        cont += c
        print(c,end=' ')
print('.')
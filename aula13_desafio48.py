# prog que leia todos os numeros impares multiplos de 3 entre 1 e 500
soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('O somatorio dos {} número é {}'.format(cont,soma))

# prog que calcule a soma de todos os números impares que são * 3
# e que estão entres 1 e 500
#soma = 0
#cont = 0
#for m in range(1, 501, 2):
#    if m % 3 == 0:
#        soma = soma + m
#        cont = cont + 1
#print('A soma de todos os {} valores é {}.'.format(cont,  soma))
# prog que leia 6 numeros int e mostre a soma de todos os impares
soma = 0
cont = 0
for s in range(1,7):
    numeros = int(input('Digite um número inteiro '))
    if numeros % 2 == 0:
        soma += numeros
        cont += 1
print('A soma de todos os números {} pares é {}'.format(cont,soma))

# prog que leia 6 numeros e considere apenas a soma dos pares.
#cont = 0
#soma = 0
#for c in range(0, 7):
#    n = int(input('Digite um valor '))
#    if n % 2 == 0:
#        soma += n
#        cont += 1
#print('A soma de todos os {} valores PARES é {}.'.format(cont, soma))
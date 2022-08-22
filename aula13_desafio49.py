# refaça o exercicio 9 da tabuada

tabuada = int(input('Diga qual o número que você quer a tabuada '))
for t in range(1, 11):
    conta = tabuada * t
    print('A tabuada de {} é: {} x {} = {}'.format(tabuada, tabuada, t, conta))

#----------------------------------------------------

# refazer o desafio 9
#valor = int(input('Escolha um número para ver a tabuada: '))
#for t in range(1, 11):
#    n = valor * t
#    print('A tabuada de {} é: {} x {} = {}'.format(valor, valor, t, n ))

#-----------------------------------------------------

# jeito diferente
#valor = int(input('Escolha um número para ver a tabuada: '))
#for t in range(1, 11):
#    print('A tabuada de {} é: {} x {} = {}'.format(valor, valor, t, valor*t))

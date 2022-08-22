#prog que leia o maior e o menor peso
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso {} '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso é {}, e o menor é {}'.format(maior, menor))



# prog que leia o peso de 5 pessoas e diga o maior e o menor
#smaller = None
#biggest = None
#for i in range(5):
#    while True:
#        try:
    #            weight = float(input('Entre com o peso da pessoa n° {} '.format(i+1)))
            #        except ValueError:
    #            print('Ops, vocÊ digitou errado')
            #            continue
        #        break
    #    smaller = weight if smaller is None else min(smaller, weight)
    #    biggest = weight if biggest is None else max(biggest, weight)

#print('Menor peso {}'.format(smaller))
#print('Maior peso {}'.format(biggest))

#maior = 0
#menor = 0
#for p in range(1,6):
#    peso = float(input('Peso {} '.format(p)))
#    if p == 1:
#        maior = peso
#        menor = peso
#    else:
#        if peso > maior:
#            maior = peso
#        if peso < menor:
#            menor = peso
#print('O maior peso lido foi de {}kg '.format(maior))
#print('O menor peso lido foi de {}kg '.format(menor))
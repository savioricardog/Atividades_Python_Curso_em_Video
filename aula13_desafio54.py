# prog que leia a idade de 7 pessoas e diga quais são maiores de idade.
from datetime import date as dt
data_atual = dt.today().year
maior = 0
menor = 0
for n in range(1,8):
    ano_nasci = int(input('Qual sua data de nascimento '))
    idade = data_atual - ano_nasci
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Das {} pessoas ouvidas, {} são menores de idade'.format(n, menor))
print('E {} são maiores de idade'.format(maior))

#prog que leia a data de nascimento de 7 sete pessoas e diga quantas
#ainda nao são maiores de idade
#from datetime import date  as dt
#soma = 0
#some = 0
#ano = dt.today().year
#for maioridade in range(0, 7):
    #anoNasc = int(input('Diga sua data de nascimento: '))
    #cont = (ano - anoNasc)
    #if cont < 18:
        #soma += 1
        #    else:
#        some += 1
#print('Ao todo tivemos {} menores de idade'.format(soma))
#print('E {} de maior'.format(some))

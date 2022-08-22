# pro que leia a razao e primeiro termo de uma pa e mostre os 10 proximos termos
from time import sleep
prim_Termo = int(input('Diga o 1° termo dessa P.A '))
razao = int(input('Diga o valor da razão dessa P.A '))
deci_Termo = prim_Termo + (10-1) * razao
for pa in range(prim_Termo, deci_Termo + razao, razao):
    sleep(0.5)
    print('{}'.format(pa), end= ' → ')
print('Acabou')
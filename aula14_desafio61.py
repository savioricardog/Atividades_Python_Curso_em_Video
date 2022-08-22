# refazer desafio 51 utilizando while

prim_Termo = int(input('Diga o primeiro termo dessa P.A: '))
razao = int(input('Diga a razão dessa P.A: '))
deci_Termo = prim_Termo + (10-1) * razao
pa = prim_Termo
cont = 1
while cont <= 10:
    print('{} → '.format(pa),end='')
    pa = pa + razao
    cont += 1
print('FIM')
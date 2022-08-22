# melhorar o desafio 61

prim_Termo = int(input('Qual o primeiro termo da PA '))
razao = int(input('Qual a razao da PA '))
pa = prim_Termo
cont = 1
while cont <= 10:
    print('{} → '.format(pa))
    pa = pa + razao
    cont += 1
    pergunta = int(input('Gostaria de ver mais quantos termos? '))
    while cont <= (pergunta + 10):
        print('{} → '.format(pa), end='')
        pa = pa + razao
        cont +=1
    while pergunta != 0:
        pergunta = int(input('Gostaria de ver mais quantos termos? '))
        print('{} → '.format(pa), end='')
        pa = pa + razao
        cont += 1
print('fim')
#prog que leia nome, idade e sexo de 4 pessoas
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher20 = 0
for p in range(1, 5):
    print('------ {}° pessoa ------0'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é {}'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('Ao todo {} mulheres tem 20 anos ou menos'.format(tot_mulher20))


#soma = 0
#novo = 0
#velho = 0
#for m in range(1,5):
#    nome = str(input('Diga o nome da {}° pessoa '.format(m)))
#   idade = int(input('Diga a idade da {}° pessoa '.format(m)))
#    #sexo = str(input('Diga o sexo da {}° pessoa '.format(m)))
#   soma += idade
#   if m == 1:
#       velho = idade
##       novo = idade
  #  else:
##     if idade > velho:
#          velho = idade
#print('A média de idade do grupo é {}'.format(soma / m))
#print('O mais velho tem {} e é {}'.format(velho,))
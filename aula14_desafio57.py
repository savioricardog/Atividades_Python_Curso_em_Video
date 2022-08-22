#prog que leia o sexo do usuario
sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()
while sexo not in 'MASCULINO/FEMININO':
        sexo = str(input('Dados invalidos, tente novamente ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))

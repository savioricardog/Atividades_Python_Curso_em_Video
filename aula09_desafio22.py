#Ler nome com todas as letras maisculas
#Ler nome com todas as letra minusculas
#Contar a quantidade de letras (sem os espaços)
#Contar letras só do primeiro nome


nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em MAIUSCULO fica {}'.format(nome.upper()))
print('Seu nome em minusculo fica {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))

#print('O primeirio nome tem {} letra'.format(nome.find(' ')))
separa = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])))
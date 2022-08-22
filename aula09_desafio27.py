#programa que leia o nome completo e mostre o primeiro e ultimo nome da pessoa./////////////////////////////////////

nome = str(input("Diga seu nome: ")).title().strip().split()
print('O seu primeiro nome é: {}.'.format(nome[0]))
print('O seu ultimo nome é {}'.format(nome[len(nome)-1]))

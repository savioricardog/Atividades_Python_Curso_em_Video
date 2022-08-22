#leia o nome de uma pessoa e diga se tem "silva" no nome

nome = str(input('Diga seu nome ')).strip().title()
print('O teu nome tem "Silva"? {}'.format('Silva' in nome))
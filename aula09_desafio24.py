# crie um programa que leia um nome de uma cidade e diga se começa com "santo"

cidade = str(input('Nome da cidade: ')).title().strip()
priNome = 'Santo' in cidade.split()[0]
print('O nome da cidade começa com "Santo"?'
      '\n{}'.format(priNome))

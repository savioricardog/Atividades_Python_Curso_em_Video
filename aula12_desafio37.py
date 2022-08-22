# prog que leia um numero inteiro e diga a base de conversão
# 1° binario | 2° octal | 3° hexadecimal

num = int(input('Digite um número inteiro '))
print('''Escolha uma das bases para conversão:
[ 0 ] converter para BINARIO
[ 1 ] converter para OCTAL
[ 2 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 0:
    print('{} convertido para BINARIO é igual a {}'.format(num,bin(num)[2:]))
elif opcao == 1:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 2:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num )[2:]))
else:
    print('Comando invalido, tente novamente!')
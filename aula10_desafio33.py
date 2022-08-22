# fazer um prog que leia tres numeros e diga qual é o maior e qual é o menor

a = int(input('diga o primeiro numero '))
b = int(input('diga o segundo numero '))
c = int(input('diga o terceiro numero '))
menor = a
if b < a and c < a:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado é: {}'.format(maior))
print('O menor valor digitado foi: {} '.format(menor))

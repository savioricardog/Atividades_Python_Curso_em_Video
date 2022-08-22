#faça um programa que mostre um numero de 0 a 9999 e mostre cada numero separado na tela.
#unidade, dezena, centena e milhar.

numero = int(input('Digite um valor até 9999: '))
milhar = numero // 1 % 10
centena = numero // 10 % 10
dezena = numero // 100 % 10
unidade = numero // 1000 % 10
print('Milhar: {}'.format(milhar))
print('Centena: {}'.format(centena))
print('Dezena: {}'.format(dezena))
print('Unidade: {}'.format(unidade))

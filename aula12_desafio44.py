# prog que calcule valor a ser pago conforme a condição de pagamento.
print('{:=^40}'.format(' LOJAS GARCIA '))
subTotal = float(input('Qual o valor da sua compra? R$ '))
condPagto = str(input('''Formas de pagamento:
[ 0 ] à vista dinheiro/cheque
[ 1 ] á vista cartão
[ 2 ] 2x no cartão
[ 3 ] 3x ou mais no cartão.
Qual você prefere? '''))
if condPagto == '0':
    total = ((subTotal * (10/100)) - subTotal) * -1
    print('Sua compra de R${}, terá 10% de desconto saindo por R${}'.format(subTotal, total))
elif condPagto == '1':
    total = ((subTotal * (5/100)) - subTotal) * -1
    print('Sua compra de R$, terá 5% de desconto, saindo por R${}'.format(subTotal, total))
elif condPagto == '2':
    parcela = subTotal / 2
    print('Sua compra de {}, por ser em 2x no cartão, vai ter 2 parcela de {}.\n'
          'Não terá desconto.'.format(subTotal, parcela))
elif condPagto == '3':
    total = ((subTotal * (20 / 100)) + subTotal)
    nParcelas = int(input('Em quantas parcelas? '))
    parcela = total / nParcelas
    print('''Sua compra de {}, por ser em {} vezes no cartão, terá um acréscimo de 20% de juros.
saindo então por um total de {}, tendo parcelas de {} reais'''.format(subTotal, nParcelas, total, parcela))
else:
    print('Opção invalidade de pagamento, tente novamente!')

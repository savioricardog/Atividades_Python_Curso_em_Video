# program. que aprove emprestimo bancario de casa.
# 1° quest - valor da casa | 2° - salario comprador | 3° cond. pagto.
from typing import Tuple

valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu sálario? '))
condPagto = float(input('Qual a condição de pagamento? '))
prestacao = valorCasa / condPagto
if prestacao < (salario * (30/100)):
    print('Empréstimo Aceito. Sua parcela será de {}, por {} meses'
    .format(prestacao, condPagto))
elif prestacao > (salario * (30/100)):
    print('Empréstimo negado, o valor da parcela de {} '
          'excede 30% do seu salario'.format(prestacao))
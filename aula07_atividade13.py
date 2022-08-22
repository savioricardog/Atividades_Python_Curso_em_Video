salario = float(input('O salario de josevaldo antes do aumento era '))
print('E então ele recebeu um aumento de 15%')
novoSalario = (salario * (15 / 100)) + salario
print('O salario de josevaldo saiu de {:.2f}, e após um aumento de 15%,\n'
      'foi para {:.2f}'.format(salario, novoSalario))

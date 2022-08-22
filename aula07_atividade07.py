#some duas notas de um aluno e de a média
n1 = float(input('Primeira nota '))
n2 = float(input('Segunda nota '))
media = (n1 + n2) / 2
print('A primeira nota {}, somada a segunda {},\n'
      'da uma média de {:.2f}.'.format(n1,n2,media))
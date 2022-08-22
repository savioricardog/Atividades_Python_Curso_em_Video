base = float(input('Tamanho da base do objeto: '))
altura = float(input('Altura do objeto: '))
area = base * altura
qLts = area / 2
print('A base da parede tem {}m², e a altura dela é de {}m²,\n'
      'logo a area da casa é {}m². Então a quantidade\n'
      'de tinta para pintar essa  parede é {}'.format(base, altura, area, qLts))

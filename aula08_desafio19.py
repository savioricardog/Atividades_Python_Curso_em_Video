import random
a1 = str(input('1° aluno '))
a2 = str(input('2° aluno '))
a3 = str(input('3° aluno '))
a4 = str(input('4° aluno '))
lista = [a1, a2, a3, a4]
choice = random.choice(lista)
print('O aluno escolhido foi {}' .format(choice))

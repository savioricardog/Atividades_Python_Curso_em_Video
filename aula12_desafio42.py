# repetir desafio 35 dos triangulos e dizer qual triangulo os valores formariam
from time import sleep
t1 = int(input('Diga o 1° número '))
t2 = int(input('Diga o 2° número '))
t3 = int(input('Diga o 3° número '))
if t1 <= t2 + t3 and t2 <= t1 + t3 and t3 <= t1 + t3:
    print('Pode ser um triangulo.')
    sleep(0.5)
    if t1 == t2 == t3:
        print('Este é um traiangulo EQUILATERO')
    elif t1 != t2 == t3 or t1 == t2 != t3 or t3 == t1 != t2 or t3 != t1 == t2:
        print('Este é um triangulo ISÓSCELES.')
    elif t1 != t2 != t3:
        print("Este é um triangulo ESCALENO.")
else:
    print('Não pode formar um triangulo.')

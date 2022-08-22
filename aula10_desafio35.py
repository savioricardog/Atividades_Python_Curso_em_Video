# prog que leia comprimento de 3 retas e diga se pode formar um triangulo

r1 = float(input('Diga um valor '))
r2 = float(input('Diga outro valor '))
r3 = float(input('Diga mais um valor '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Pode formar um triangulo")
else:
    print('Não pode formar um triangulo!')

d = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
valor = (km * 0.15) + (d * 60)
print("O valor a ser pago é de R$ {:.2f} reais".format(valor))

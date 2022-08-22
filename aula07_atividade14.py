temp = float(input('Informe a temperatura em °C: '))
cf = float (temp * 9 / 5) + 32
print('A temperatura de {} °C corresponde a {} °F'.format(temp, cf))
fc = (temp - 32) * 5 / 9
temp1 = float(input('Informe a temperatura em °F '))
print('Já de fahrenheit para celsius fica: {} °C -> {:.2f} °F'.format(temp1, fc))
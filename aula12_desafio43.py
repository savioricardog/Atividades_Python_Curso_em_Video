# logica que leia altura e massa de uma pessoa, calcule IMC
# E CALCULE CONFORME A FAIXA .

peso = float(input('Qual seu peso? '))
altura = float(input('Qual é a sua altura (em M)? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.2f} e você está abaixo do seu peso ideial.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.2f} e você está no seu peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('O seu IMC é de {:.2f} e você está com sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print("O seu imc é de {:.2f} e você está com obesidade.".format(imc))
elif imc >= 40:
    print('O seu IMC é de {:.2f} e você tem obesidade morbida.'.format(imc))

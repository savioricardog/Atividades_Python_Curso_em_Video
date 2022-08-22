# prog que leia 2 notas e calcule a media. Dizendo se passou ou não

nota1 = float(input('Qual a sua 1° nota? '))
nota2 = float(input('Qual a sua 2° nota? '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('A sua média é {} e você foi reprovado.'.format(media))
elif 7.0 > media <= 5.0:
    print('Sua média foi {} e você ficou de recuperação'.format(media))
elif media > 6.9:
    print('Você foi aprovado com média {}, parabéns!'.format(media))

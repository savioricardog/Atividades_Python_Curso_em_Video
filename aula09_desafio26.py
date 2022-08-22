#programa que leia uma frase e mostre:
#quantas vezes aparece "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez.

frase = str(input('Diga uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes.'.format(frase.count("A")))
print('O "A" aparece a primeira vez em: {}.'.format(frase.find("A")+1))
print('O "A" aparece a ultima vez em: {}.'.format(frase.rfind("A")+1))
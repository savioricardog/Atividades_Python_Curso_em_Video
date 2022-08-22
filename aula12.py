nome = str(input('Diga seu nome ')).title()
if nome == "Savio":
    print('Que belo nome você tem!')
elif nome == 'Gustavo':
    print('Então é de você que ouvi falar.')
elif nome in 'Clark Bruce Barry' \
             '':
    print('Baita nome hein, bro')
else:
    print('Muito prazer em te conhecer!')
print('Tenha um bom dia, {}'.format(nome))

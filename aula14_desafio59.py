# prog que leia dos valores e mostre um menu na tela: [1] somar, [2] multiplicar, [3] maior,
# [4] novos números, [5] sair do programa.

n1 = int(input('Primeiro valor '))
n2 = int(input('Segundo valor '))
opcao = 0
while opcao != 5:
    print('que você gostaria de fazer?\n'
          '[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Números\n[ 5 ] Sair do programa.\n')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos valores {} + {} = {}.'.format(n1, n2, soma))
        print('---' * 20)
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação dos valores {} x {} = {}.'.format(n1, n2, multiplicacao))
        print('---' * 20)
    elif opcao == 3:
        if n1 > n2:
            print('O valor 1 que é {}, é maior que o valor 2.'.format(n1))
            print('---' * 20)
        else:
            print('O valor 2 que é {}, é maior que o valor 1.'.format(n2))
            print('---' * 20)
    elif opcao == 4:
        print('Escolha novos números.')
        n1 = float(input('digite um valor: '))
        n2 = float(input('digite outro valor: '))
        print('---' * 20)
    elif opcao > 5:
        print('Opção invalida. tente novamente.')
        print('---' * 20)

"""valor_1 = int(input('digite um valor: '))
valor_2 = int(input('digite outro valor: '))
escolha = input('Podemos prosseguir para as opções? ').upper()
if escolha == 'SIM':
    sleep(0.5)
    while escolha != '5':
        sleep(0.5)
        escolha = input('que você gostaria de fazer?\n'
                        '[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Números\n[ 5 ] Sair do programa.\n')
        if escolha == '1':
            sleep(0.5)
            soma = valor_1 + valor_2
            print('A soma dos valores {} + {} = {}.'.format(valor_1, valor_2, soma))
            print('---' * 20)
        elif escolha == '2':
            sleep(0.5)
            multiplicacao = valor_1 * valor_2
            print('A multiplicação dos valores {} x {} = {}.'.format(valor_1, valor_2, multiplicacao))
            print('---' * 20)
        elif escolha == '3':
            sleep(0.5)
            if valor_1 > valor_2:
                sleep(0.5)
                print('O valor 1 que é {}, é maior que o valor 2.'.format(valor_1))
                print('---' * 20)
            else:
                sleep(0.5)
                print('O valor 2 que é {}, é maior que o valor 1.'.format(valor_2))
                print('---' * 20)
        elif escolha == '4':
            sleep(0.5)
            print('Escolha novos números.')
            valor_1 = int(input('digite um valor: '))
            valor_2 = int(input('digite outro valor: '))
            print('---' * 20)
        elif escolha > '5':
            sleep(0.5)
            print('Opção invalida. tente novamente.')
            print('---' * 20)
else:
    print('Ok. Acabou!')"""



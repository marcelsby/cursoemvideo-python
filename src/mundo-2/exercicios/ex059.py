print('{1} {0} {1}'.format('DESAFIO #059', '=' * 5))

try:
    while True:
        n1 = float(input('\nDigite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

        print('\nOpções:')
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos números')
        print('[5] Sair')
        opt = int(input('Digite a opção desejada: '))

        if opt == 1:
            print('\nResultado da soma dos dois números: {}'.format(n1 + n2))
        elif opt == 2:
            print('\nResultado da multiplicação dos dois números: {}'.format(n1 * n2))
        elif opt == 3:
            maior = n1 if n1 > n2 else n2
            print('\nDos dois números inseridos o maior é: {}'.format(maior))
        elif opt == 4:
            continue
        elif opt == 5:
            break

    print('\nAté mais! ;)')
except (Exception, ValueError):
    if ValueError:
        print('\n\033[31mO valor inserido é inválido! Saindo...\033[m')
    else:
        print(Exception)

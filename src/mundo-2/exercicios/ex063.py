print('{1} {0} {1}'.format('DESAFIO #063', '=' * 5))

contador = 0

try:
    qtd_termos = int(input('Digite a quantidade de termos da sequência de Fibonacci desejada: '))

    f_menos_um = 1
    f_menos_dois = 0

    print('\n===== SEQUÊNCIA DE FIBONACCI =====')
    while contador < qtd_termos:
        if contador == 0:
            print('{} '.format(f_menos_dois), end='')
            contador += 1
        elif contador == 1:
            print(' {} '.format(f_menos_um), end='')
            contador += 1
        else:
            f_atual = f_menos_um + f_menos_dois
            f_menos_dois = f_menos_um
            f_menos_um = f_atual
            print(' {} '.format(f_atual), end='')
            contador += 1

except ValueError:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

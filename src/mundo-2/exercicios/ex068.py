from random import randint
print('{1} {0} {1}'.format('DESAFIO #068', '=' * 10))

try:
    print('=x=x=x=x= JOGO DO PAR OU ÍMPAR =x=x=x=x=')

    win_counter = 0

    while True:
        num_player = int(input('\nDigite seu número: '))
        evenOrOdd = input('Escolha entre par ou ímpar [P/I]: ').upper().strip()

        if evenOrOdd != 'P' and evenOrOdd != 'I':
            raise ValueError

        num_cpu = randint(0, 10)
        sum_inputs = num_player + num_cpu

        if evenOrOdd == 'P' and sum_inputs % 2 == 0:
            print('\033[32mVENCEU A RODADA!\033[m')
            win_counter += 1
        elif evenOrOdd == 'I' and sum_inputs % 2 != 0:
            print('\033[32mVENCEU A RODADA!\033[m')
            win_counter += 1
        else:
            print('\033[31mPERDEU A RODADA!\033[m')
            break

    if win_counter == 0:
        print('\033[31m\nAcabou!\nVocê não venceu nenhuma vez contra o Computador.\033[m')
    elif win_counter == 1:
        print('\033[31m\nAcabou!\033[m\nVocê venceu \033[32m1\033[m vez contra o Computador.')
    else:
        print(f'\033[31m\nAcabou!\033[m\nVocê venceu \033[32m{win_counter}\033[m vezes contra o Computador.')

except ValueError:
    print('\033[31m\nEntrada inválida detectada!\nSaindo...')
    exit(1)

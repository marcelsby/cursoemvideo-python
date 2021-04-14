print('{1} {0} {1}'.format('DESAFIO #067', '=' * 10))

try:
    num = 0
    print('-= Para parar digite um número negativo! =-')

    while True:
        num = int(input('\nDigite o número que deseja mostrar a tabuada: '))

        if num < 0:
            print('\nFim!')
            break

        print(f'\nTabuada do número {num}: ')
        for i in range(1, 11):
            print(f'{i} * {num} = {i * num}')

except ValueError:
    print('\033[31m\nNúmero inválido detectado!\nSaindo...')
    exit(1)

print('{1} {0} {1}'.format('DESAFIO #060', '=' * 5))

try:
    num = int(input('Digite um número inteiro para que seu fatorial seja calculado: '))

    if num < 0:
        raise ValueError
    elif num == 1 or num == 0:
        print('O fatorial de {} é: {}'.format(num, 1))
    else:
        fat = num
        contador = num - 1

        while contador > 0:
            fat *= contador
            contador -= 1

        print('O fatorial de {} é: {}'.format(num, fat))

except (ValueError, Exception):
    if ValueError:
        print('\n\033[31mValor inválido detectado! Saindo...\033[m')
        exit(1)
    else:
        print(Exception)
        exit(1)

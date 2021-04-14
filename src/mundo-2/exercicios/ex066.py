print('{1} {0} {1}'.format('DESAFIO #066', '=' * 10))

try:
    print('- Digite "999" para parar o loop -')
    contador = soma = num = 0

    while True:
        num = int(input('Digite um número inteiro: '))

        if num == 999:
            break

        soma += num
        contador += 1

    if contador == 1:
        print(f'\n\033[32mO número inserido foi: {soma}')
        print(f'\033[33mFoi inserido apenas 1 número')
    else:
        print(f'\n\033[32mA soma dos números inseridos é: {soma}')
        print(f'\033[33mForam inseridos {contador} números')

except ValueError:
    print('\033[31m\nNúmero inválido detectado!\nSaindo...')
    exit(1)

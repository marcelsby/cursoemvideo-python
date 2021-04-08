print('{1} {0} {1}'.format('DESAFIO #064', '=' * 5))

total = 0
inseridos = 0

try:
    while True:
        print('Insira "999" para parar!')
        num = int(input('Digite um valor: '))

        if num == 999:
            break
        else:
            inseridos += 1
            total += num
except ValueError:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

print('Soma total: {}'.format(total))
print('Quantidade de números inseridos: {}'.format(inseridos))
print('Fim.')

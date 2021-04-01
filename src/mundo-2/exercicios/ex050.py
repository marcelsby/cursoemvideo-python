print('{1} {0} {1}'.format('DESAFIO #050', '=' * 5))

total = int()

try:
    for i in range(6):
        temp = int(input('Digite um número inteiro: '))
        total += temp
except Exception:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

print(total)


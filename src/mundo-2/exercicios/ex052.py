print('{1} {0} {1}'.format('DESAFIO #052', '=' * 5))

try:
    num = int(input('Digite um número inteiro: '))
except Exception:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

is_primo = True

for i in range(2, num):
    if num <= 1:
        is_primo = False
        break
    elif num % i == 0:
        is_primo = False
        break

if is_primo:
    print('\n\033[32m{} é primo!'.format(num))
else:
    print('\n\033[31m{} não é primo!'.format(num))

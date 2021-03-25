print('{1} {0} {1}'.format('DESAFIO #038', '=' * 5))

try:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
except:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

if n1 > n2:
    print('O primeiro valor é maior que o segundo.')
elif n2 > n1:
    print('O segundo valor é maior que o primeiro.')
elif n1 == n2:
    print('Os dois valores são iguais.')

print('{1} {0} {1}'.format('DESAFIO #049', '=' * 5))

num = input('Digite um número inteiro: ')

if num.isdecimal():
    num = int(num)
else:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

print('\nTabuada:')
for multiplicador in range (1, 11):
    resultado = num * multiplicador
    print('{} x {} = {}'.format(num, multiplicador, resultado))

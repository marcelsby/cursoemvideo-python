print('{1} {0} {1}'.format('DESAFIO #023', '=' * 5))

try:
    num = int(input('Digite um número entre 0 e 9999: '))
    if num < 0 or num > 9999:
        exit(1)
except:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

num_digitos = []

for digit in str(num):
    num_digitos.append(digit)

if len(num_digitos) == 1:
    print('Unidade: {}'.format(num_digitos[0]))
elif len(num_digitos) == 2:
    print('Unidade: {}'.format(num_digitos[1]))
    print('Dezena: {}'.format(num_digitos[0]))
elif len(num_digitos) == 3:
    print('Unidade: {}'.format(num_digitos[2]))
    print('Dezena: {}'.format(num_digitos[1]))
    print('Centena: {}'.format(num_digitos[0]))
elif len(num_digitos) == 4:
    print('Unidade: {}'.format(num_digitos[3]))
    print('Dezena: {}'.format(num_digitos[2]))
    print('Centena: {}'.format(num_digitos[1]))
    print('Milhar: {}'.format(num_digitos[0]))









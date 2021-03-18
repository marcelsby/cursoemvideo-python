from mycolors import colorthis
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
    print('Unidade: {}'.format(colorthis(num_digitos[0], background='green')))
elif len(num_digitos) == 2:
    print('Unidade: {}'.format(colorthis(num_digitos[1], background='green')))
    print('Dezena: {}'.format(colorthis(num_digitos[0], background='blue')))
elif len(num_digitos) == 3:
    print('Unidade: {}'.format(colorthis(num_digitos[2], background='green')))
    print('Dezena: {}'.format(colorthis(num_digitos[1], background='blue')))
    print('Centena: {}'.format(colorthis(num_digitos[0], background='yellow')))
elif len(num_digitos) == 4:
    print('Unidade: {}'.format(colorthis(num_digitos[3], background='green')))
    print('Dezena: {}'.format(colorthis(num_digitos[2], background='blue')))
    print('Centena: {}'.format(colorthis(num_digitos[1], background='yellow')))
    print('Milhar: {}'.format(colorthis(num_digitos[0], background='purple')))

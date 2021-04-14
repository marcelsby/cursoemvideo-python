print('{1} {0} {1}'.format('DESAFIO #071', '=' * 10))

valor_a_sacar = 0

cedulas_um_real = 0
cedulas_dez_reais = 0
cedulas_vinte_reais = 0
cedulas_cinquenta_reais = 0

print('=-=-=-=-=-= Caixa eletrônico =-=-=-=-=-=')

try:
    valor_a_sacar = int(input('\nDigite o valor a ser sacado: '))

    if valor_a_sacar <= 0:
        raise ValueError

except ValueError:
    print('\n\033[33mO valor a ser sacado deve ser maior ou igual a R$ 1.00!\033[m\nSaindo...')
    exit(1)

if valor_a_sacar // 50 >= 1:
    cedulas_cinquenta_reais = valor_a_sacar // 50
    valor_a_sacar -= cedulas_cinquenta_reais * 50

if valor_a_sacar // 20 >= 1:
    cedulas_vinte_reais = valor_a_sacar // 20
    valor_a_sacar -= cedulas_vinte_reais * 20

if valor_a_sacar // 10 >= 1:
    cedulas_dez_reais = valor_a_sacar // 10
    valor_a_sacar -= cedulas_dez_reais * 10

if valor_a_sacar // 1 >= 1:
    cedulas_um_real = valor_a_sacar // 1
    valor_a_sacar -= cedulas_um_real * 1

print('\nImprimindo cédulas, preste atenção na boca do caixa:')
print(f'Quantidade de cédulas de R$ 1: {cedulas_um_real}')
print(f'Quantidade de cédulas de R$ 10: {cedulas_dez_reais}')
print(f'Quantidade de cédulas de R$ 20: {cedulas_vinte_reais}')
print(f'Quantidade de cédulas de R$ 50: {cedulas_cinquenta_reais}')

print('{1} {0} {1}'.format('DESAFIO #033', '=' * 5))
try:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))

    if n1 == int(n1):
        n1 = int(n1)

    if n2 == int(n2):
        n2 = int(n2)

    if n3 == int(n3):
        n3 = int(n3)

except:
    print('\nInsira números reais!\nSaindo...')
    exit(1)

menor = 0
maior = 0

# Lógica para encontrar o menor
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3

# Lógica para encontrar o maior
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3

print('\n', '-' * 41)
print('O menor valor dos três inseridos é: {}'.format(menor))
print('O maior valor dos três inseridos é: {}'.format(maior))
print('-' * 41)

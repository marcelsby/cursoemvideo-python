print('{1} {0} {1}'.format('DESAFIO #061', '=' * 5))

try:
    primeiro_termo = int(input('Digite o primeiro termo da sua PA: '))
    razao = int(input('Digite a razão da sua PA: '))
except ValueError:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

ultimo_termo = primeiro_termo * 10

print('Resultado da PA:')
i = 0
while i < 10:
    if i == 0:
        print(primeiro_termo)
    else:
        print(primeiro_termo + razao * i)
    i += 1

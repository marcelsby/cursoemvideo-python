valores = []

try:
    for i in range(4):
        num = int(input(f'Digite o {i + 1}o número: '))
        valores.append(num)

    valores = tuple(valores)

except ValueError:
    print('\nValor incorreto inserido!\nSaindo...')
    exit(1)

ocorr_nove = valores.count(9)
if ocorr_nove > 0:
    print(f'Quantidade de aparições do número nove: {ocorr_nove}')

primeiro_tres = valores.index(3)
if primeiro_tres > 0:
    print(f'O três apareceu pela primeira vez na posição: {primeiro_tres}')

pares = []

print(valores)
for j in valores:
    if valores[j] % 2 == 0:
        pares.append(valores[j])

if len(pares) > 0:
    print('Números pares inseridos:', end=' ')
    for n in pares:
        print(n, end=' ')

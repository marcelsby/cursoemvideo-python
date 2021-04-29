valores = []

try:
    for i in range(4):
        num = int(input(f'Digite o {i + 1}º número: '))
        valores.append(num)

    valores = tuple(valores)

except ValueError:
    print('\nValor incorreto inserido!\nSaindo...')
    exit(1)

ocorr_nove = valores.count(9)
if ocorr_nove > 0:
    print(f'\nQuantidade de aparições do número nove: {ocorr_nove}')
else:
    print('O número 9 não faz parte da tupla inserida!')

try:
    primeiro_tres = valores.index(3)
except:
    primeiro_tres = -1

if primeiro_tres > 0:
    print(f'O três apareceu pela primeira vez na posição: {primeiro_tres}')
else:
    print('O número 3 não existe na tupla inserida!')

pares = []

pares = valores.find()

for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        pares.append(valores[i])

tam_pares = len(pares)
if tam_pares > 0:
    print('Números pares inseridos:', end=' ')
    for n in pares:
        if n == tam_pares - 1:
            print(n)
        else:
            print(n, end=' ')

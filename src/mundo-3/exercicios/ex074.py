from random import randint

sorteados = []

for i in range(5):
    rand_num = randint(1, 100)
    sorteados.append(rand_num)

sorteados = tuple(sorteados)

print('Números sorteados: ', end='')
for n in sorteados:
    print(n, end=' ')

print(f'\nO menor número sorteado foi {min(sorteados)}')
print(f'O maior número sorteado foi {max(sorteados)}')



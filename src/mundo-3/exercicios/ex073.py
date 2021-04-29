times = ('Flamengo', 'Internacional', 'Atlético-MG',
         'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
         'Santos', 'Athletico-PR', 'Bragantino', 'Ceará SC',
         'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife',
         'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

print('Brasileirão Série A\n')

print('Os 5 primeiros colocados:')
for pos, time in enumerate(times):
    if pos == 5:
        break

    print(f'{pos + 1}. {time}')

print('\nOs 4 últimos colocados:')
for pos in range(-1, -5, -1):
    print(f'{abs(pos)}. {times[pos]}')

print('\nTimes em ordem alfabética:')
ordenado = sorted(times)

for time in ordenado:
    print(time)

corinthians_pos = times.index('Corinthians')
print(f'\nO {times[corinthians_pos]} está na {corinthians_pos}ª posição da tabela')


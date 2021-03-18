print('{1} {0} {1}'.format('DESAFIO #031', '=' * 5))

distancia = input('Digite em quilômetros a distância da sua viagem: ')

if distancia.isdecimal():
    distancia = int(distancia)
else:
    print('\nDistância inválida!\nSaindo...')
    exit(1)

preco_passagem = 0

if distancia < 200:
    preco_passagem = distancia * 0.50
else:
    preco_passagem = distancia * 0.45

print('Sua passagem custará: R${:.2f}'.format(preco_passagem))

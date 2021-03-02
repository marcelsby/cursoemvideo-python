print('{1} {0} {1}'.format('DESAFIO #015', '=' * 5))

try:
    dias_alugados = int(input('Por quantos dias o carro foi alugado? '))
    km_percorridos = float(input('Quantos KMs foram percorridos com o carro? '))
except:
    print('\nValor inválido inserido!\nSaindo...')
    exit(1)

v_aluguel = (dias_alugados * 60) + (km_percorridos * 0.15)

print('\nValor do aluguel: R${:.2f}'.format(v_aluguel))

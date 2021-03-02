print('{1} {0} {1}'.format('DESAFIO #008', '=' * 5))

t_metros = input('Digite um tamanho em metros: ')

if not t_metros.isdecimal():
    print('\nValor inválido!\nSaindo...')
    exit(1)
else:
    t_metros = int(t_metros)

t_cm = t_metros * 100
t_mm = t_metros * 1000

print('Tamanho em centímetros: {} cm\nTamanho em milímetros: {} mm'.format(t_cm, t_mm))

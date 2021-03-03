print('{1} {0} {1}'.format('DESAFIO #027', '=' * 5))

nome = input('Digite seu nome completo: ')

try:
    if not nome.replace(' ', '').isalpha():
        exit(1)
except:
    print('\nNome inválido inserido\nSaindo...')
    exit(1)

separado = nome.split()
primeiro = separado[0]
ultimo = separado[len(separado) - 1]

print('Nome completo: {}'.format(nome))
print('Primeiro nome: {}'.format(primeiro))
print('Último nome: {}'.format(ultimo))

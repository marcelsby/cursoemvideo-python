print('{1} {0} {1}'.format('DESAFIO #025', '=' * 5))

nome = input('Digite um nome: ')

try:
    if not nome.replace(' ', '').isalpha():
        exit(1)
except:
    print('\nNome inválido inserido\nSaindo...')
    exit(1)

tem_silva = 'SILVA' in nome.upper()

if tem_silva:
    print('\nEste nome possui "SILVA"!')
else:
    print('\nEste nome não possui "SILVA"!')
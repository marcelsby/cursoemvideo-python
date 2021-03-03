print('{1} {0} {1}'.format('DESAFIO #024', '=' * 5))

cidade = input('Digite o nome de uma cidade: ')

try:
    if not cidade.replace(' ', '').isalpha():
        exit(1)
except:
    print('\nNome inválido inserido\nSaindo...')
    exit(1)

if not cidade.upper().find('SANTO') == 0:
    print('\nO nome da cidade inserida não se inicia com "SANTO"!')
else:
    print('\nO nome da cidade inserida se inicia com "SANTO"!')
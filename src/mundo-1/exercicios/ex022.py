from mycolors import colorthis
print('{1} {0} {1}'.format('DESAFIO #022', '=' * 5))

nome = input('Digite seu nome completo: ')

if not nome.replace(' ', '').isalpha():
    print('\nNome inválido inserido!\nSaindo...')
    exit(1)

print('\nSeu nome em caixa alta fica assim: {}'.format(colorthis(nome.upper(), background='green')))
print('Seu nome em caixa baixa fica assim: {}'.format(colorthis(nome.lower(), background='red')))
print('Seu nome é composto de {} letras.'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome é composto de {} letras.'.format(len(nome.split()[1])))

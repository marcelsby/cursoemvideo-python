from mycolors import colorthis

print('{1} {0} {1}'.format('DESAFIO #030', '=' * 5))
n = input('Digite um número inteiro: ')

if n.isdecimal():
    n = int(n)
else:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

if n % 2 == 0:
    print('\nO NÚMERO INSERIDO É {}!'
          .format(colorthis('PAR', background='blue')))
else:
    print('\nO NÚMERO INSERIDO É {}!'
          .format(colorthis('ÍMPAR', background='purple')))

from mycolors import colorthis
from math import sqrt, pow
print('{1} {0} {1}'.format('DESAFIO #017', '=' * 5))

try:
    cat_op = float(input('Insira o comprimento do cateto oposto (em centímetros): '))
    cat_adj = float(input('Insira o comprimento do cateto adjacente (em centímetros): '))
except:
    print('\nValor inválido inserido!\nSaindo...')
    exit(1)

hip = sqrt(pow(cat_op, 2) + pow(cat_adj, 2))

print('\nMedidas dos catetos:'
      '\nCateto oposto: {}cm'
      '\nCateto adjacente: {}cm'
      .format(colorthis(cat_op, background='purple'), colorthis(cat_adj, background='purple')))
print('\nO comprimento da hipotenusa formada por esses catetos é igual a {}cm'
      .format(colorthis(hip, background='green')))

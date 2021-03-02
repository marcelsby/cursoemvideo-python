print('{1} {0} {1}'.format('DESAFIO #016', '=' * 5))
from math import trunc

try:
    num = float(input('Insira um número real qualquer: '))
except:
    print('\nValor inválido inserido!\nSaindo...')
    exit(1)

print('\nA parte inteira do número {} é {}'.format(num, trunc(num)))

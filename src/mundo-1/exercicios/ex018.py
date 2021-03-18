print('{1} {0} {1}'.format('DESAFIO #018', '=' * 5))
from math import sin, cos, tan, radians

try:
    ang_graus = int(input('Insira um ângulo em graus (Ex: 45º = 45): '))
except:
    print('\nValor inválido inserido!\nSaindo...')
    exit(1)

ang_rad = radians(ang_graus)

print('\nÂngulo inserido: {}º'
      '\nSeno: {:.2f}'
      '\nCosseno: {:.2f}'
      '\nTangente: {:.2f}'
      .format(ang_graus, sin(ang_rad), cos(ang_rad), tan(ang_rad)))
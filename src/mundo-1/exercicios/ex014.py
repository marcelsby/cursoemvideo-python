print('{1} {0} {1}'.format('DESAFIO #014', '=' * 5))

try:
    t_celsius = float(input('Insira uma temperatura em graus Celsius: '))
except:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

t_fahrenheit = (t_celsius * (9 / 5)) + 32

print('\nTemperatura em Celsius = ºC {:.1f}'
      '\nTemperatura em Fahrenheit = ºF {:.1f}'
      .format(t_celsius, t_fahrenheit))

exit(0)

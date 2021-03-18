from mycolors import colorthis
print('{1} {0} {1}'.format('DESAFIO #011', '=' * 5))

print('Insira os seguintes valores em metros:')

try:
    altura = float(input('Altura da parede: '))
    largura = float(input('Largura da parede: '))
except:
    print('\nValor inválido inserido!\nSaindo...')
    exit(1)

area = altura * largura

qtd_tinta = (area / 2)

print('Para pintar uma parede de {} m2 serão necessários {} litros de tinta.'.format(colorthis(area, background='green'),
                                                                                     colorthis(str(qtd_tinta), background='blue')
                                                                                     .replace('.', ',')))

exit(0)
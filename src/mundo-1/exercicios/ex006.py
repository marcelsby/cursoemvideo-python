from mycolors import colorthis
import re

print('{1} {0} {1}'.format('DESAFIO #006', '=' * 5))

num = input('Digite um número: ')

if not re.search("\d*\.\d*", num) == None:
    num = float(num)
elif num.isdecimal():
    num = int(num)
else:
    print('\nInsira um valor válido!\nSaindo...')
    exit(1)

dobro = num * 2
triplo = num * 3
raizQuadrada = num ** (1 / 2)

print('Número inserido: {}'.format(colorthis(num, 'underlined', 'cyan')))
print('Seu dobro é: {}\nSeu triplo é: {}'.format(colorthis(dobro, 'bold', 'blue'),
                                                 colorthis(triplo, 'bold', 'red')))
print('A raiz quadrada desse número é: {}'.format(colorthis(raizQuadrada, font='green')))

from mycolors import colorthis
from random import randint
print('{1} {0} {1}'.format('DESAFIO #028', '=' * 5))
entrada = input('Digite um número de 0 a 5: ')

if entrada.isdecimal():
    entrada = int(entrada)
else:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

sorteado = randint(0, 5)

print(colorthis('\nVENCEU!', background='green') if entrada == sorteado else colorthis('\nPERDEU!', background='red'))

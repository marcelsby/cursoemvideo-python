print('{1} {0} {1}'.format('DESAFIO #09', '=' * 5))

num = input('Insira um número inteiro: ')

if num.isdecimal():
    num = int(num)
else:
    print('\nInsira um valor inválido!\nSaindo...')
    exit(1)

print('\nTabuada do número {}:'.format(num))
print('{} x 1 = {}'.format(num, num * 1))
print('{} x 2 = {}'.format(num, num * 2))
print('{} x 3 = {}'.format(num, num * 3))
print('{} x 4 = {}'.format(num, num * 4))
print('{} x 5 = {}'.format(num, num * 5))
print('{} x 6 = {}'.format(num, num * 6))
print('{} x 7 = {}'.format(num, num * 7))
print('{} x 8 = {}'.format(num, num * 8))
print('{} x 9 = {}'.format(num, num * 9))
print('{} x 10 = {}'.format(num, num * 10))

print('{1} {0} {1}'.format('DESAFIO #005', '=' * 5))

num = input('Insira um número inteiro: ')

if not num.isdecimal():
    print('Insira um valor válido!\nSaindo...')
    exit(1)

num = int(num)

suc = num + 1
ant = num - 1

print('\n\nO sucessor do número {2} é: {0}\nO antecessor do número {2} é: {1}'.format(suc, ant, num))

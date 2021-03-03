print('{1} {0} {1}'.format('DESAFIO #026', '=' * 5))


def get_ultimo_a(string):
    ultimo = 0
    i = 0

    for char in string:
        if char == 'a':
            ultimo = i
        i += 1

    return ultimo


frase = input('Digite uma frase: ')

try:
    if not frase.replace(' ', '').isalnum():
        exit(1)
except:
    print('\nNome inválido inserido\nSaindo...')
    exit(1)

frase_min = frase.lower()
cont_a = frase_min.count('a')
primeira = frase_min.find('a')
ultima = get_ultimo_a(frase_min)

print('\nFrase inserida:\n{}\n'.format(frase))

if cont_a == 1:
    print('A letra "a" aparece {} vez na frase.'.format(cont_a))
elif cont_a > 1:
    print('A letra "a" aparece {} vezes na frase.'.format(cont_a))
else:
    print('A letra "a" não aparece na frase.'.format(cont_a))

if primeira > -1:
    print('A letra "a" aparece pela primeira vez na {}a posição da frase.'.format(primeira + 1))

if primeira > -1:
    print('A letra "a" aparece pela primeira vez na {}a posição da frase.'.format(ultima + 1))



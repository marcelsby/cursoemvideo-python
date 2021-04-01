print('{1} {0} {1}'.format('DESAFIO #048', '=' * 5))

print('Números ímpares e múltiplos de 3 entre 1 e 500:')
for num in range(1, 500):
    if num % 2 != 0 and num % 3 == 0:
        print(num)

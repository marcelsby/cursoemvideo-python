print('{1} {0} {1}'.format('DESAFIO #037', '=' * 5))

try:
    num = int(input('Digite um número inteiro qualquer: '))
except:
    print('\nSua entrada não é um número inteiro!\nSaindo...')
    exit(1)

print('\nBases:\n1. Binária\n2. Octal\n3. Hexadecimal')
base = int(input('Digite a base que você deseja que seu número seja convertido: '))

if base == 1:
    print('\nO número {} convertido para binário é: {}'.format(num, format(num, 'b')))
elif base == 2:
    print('\nO número {} convertido para octal é: {}'.format(num, format(num, 'o')))
elif base == 3:
    print('\nO número {} convertido para hexadecimal é: {}'.format(num, format(num, 'X')))
else:
    print('\nNenhuma base detectada, saindo...')
    exit(1)

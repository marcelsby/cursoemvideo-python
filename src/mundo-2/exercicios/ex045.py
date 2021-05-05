from random import randint

print('{1} {0} {1}'.format('DESAFIO #045', '=' * 10))
print('{:^34}'.format('PEDRA x PAPEL x TESOURA'))

try:
    print('Opções:' '\n1. Pedra'
          '\n2. Papel'
          '\n3. Tesoura\n')

    jogador = int(input('Escolha uma das opções para jogar: '))

    if jogador > 3 or jogador < 1:
        raise Exception()

except:
    Exception('\nA opção deve ser um número de 1 a 3.\nSaindo...')
    exit(1)

cpu = randint(1, 3)

if cpu == jogador:
    print('\033[33mEMPATE!')
elif cpu == 1 and jogador == 3 or cpu == 2 and jogador == 1 or cpu == 3 and jogador == 2:
    print('\033[31mDERROTA!')
else:
    print('\033[32mVITÓRIA!')

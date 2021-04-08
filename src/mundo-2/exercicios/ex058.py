from random import randint
print('{1} {0} {1}'.format('DESAFIO #058', '=' * 5))

tentativas = 0

while True:
    entrada = input('Digite um número de 0 a 10: ')
    tentativas += 1

    if entrada.isdecimal():
        entrada = int(entrada)
    else:
        print('\nEntrada inválida!\nSaindo...')
        exit(1)

    sorteado = randint(0, 10)

    if entrada == sorteado:
        if tentativas == 1:
            print('\n\033[32mParabéns, você acertou!\033[m\nVocê levou \033[33m{}\033[m rodada para adivinhar.'
                  .format(tentativas))
        else:
            print('\n\033[32mParabéns, você acertou!\033[m\nVocê levou \033[33m{}\033[m rodadas para adivinhar.'
                  .format(tentativas))
        break
    else:
        print('\033[31mNão é esse número, tenta de novo! HAHAHA ^U^\033[m')

from mycolors import colorthis
print('{1} {0} {1}'.format('DESAFIO #029', '=' * 5))

velocidade_atual = input('Digite sua velocidade atual: ')

if velocidade_atual.isdecimal():
    velocidade_atual = int(velocidade_atual)
else:
    print('Entrada inválida!\n Saindo...\n')
    exit(1)

if velocidade_atual > 80:
    excedente = velocidade_atual - 80
    multa = excedente * 7

    print(colorthis('\nMULTADO!', background='red'))
    print('Sua multa irá custar: R${:.2f}'.format(multa))

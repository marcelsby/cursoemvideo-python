print('{1} {0} {1}'.format('DESAFIO #032', '=' * 5))
ano = input('Digite um ano: ')

if ano.isdecimal():
    ano = int(ano)
else:
    print('\nAno inválido!\nSaindo...')
    exit(1)

divisivel_por_quatro = ano % 4 == 0
divisivel_por_cem = ano % 100 == 0
divisivel_por_quatrocentos = ano % 400 == 0

bissexto = (divisivel_por_quatro and not divisivel_por_cem) or divisivel_por_quatrocentos

if bissexto:
    print('\n{} é um ano bissexto!'.format(ano))
else:
    print('\n{} não é um ano bissexto!'.format(ano))

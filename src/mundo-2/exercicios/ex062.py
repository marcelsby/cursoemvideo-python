print('{1} {0} {1}'.format('DESAFIO #062', '=' * 5))

try:
    primeiro_termo = int(input('Digite o primeiro termo da sua PA: '))
    razao = int(input('Digite a razão da sua PA: '))

    ultimo_termo = primeiro_termo * 10

    print('Resultado da PA:')
    i = 0
    while i < 10:
        if i == 0:
            print(primeiro_termo)
        else:
            print(primeiro_termo + razao * i)
        i += 1

    ultimo_termo += 1

    while True:
        resposta = input('\nVocê deseja exibir mais termos [S/N]? ').upper()
        if resposta != 'S':
            break

        print('\nPara sair do programa digite \"0\"')
        qtd_termos = int(input('\nDigite quantos termos você deseja exibir: '))
        if qtd_termos == 0:
            break

        i = 0
        while i < qtd_termos:
            if i == 0:
                print(ultimo_termo)
            else:
                print(ultimo_termo + razao * i)
            i += 1

        ultimo_termo = ultimo_termo + razao * qtd_termos
except ValueError:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

print('Até logo! B)')

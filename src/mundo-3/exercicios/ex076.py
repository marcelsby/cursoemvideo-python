estoque = ()
cont = 1

try:
    while True:
        print(f'\nCadastrando o {cont}º produto:')
        nome = input(f'Nome: ').strip()
        preco = float(input(f'Preço: ').replace(',', '.'))
        continuar = input('Deseja continuar [S/N]? ').upper()

        produto = (nome, preco),
        estoque += produto

        if continuar != 'S':
            break

        cont += 1

except ValueError:
    print('\nValor incorreto inserido!\nSaindo...')
    exit(1)


print('-' * 50)
print(f'{"NOTA FISCAL":^50}')
print('-' * 50)

for produto in estoque:
    print('{:.<43}R${:>0}'.format(produto[0], produto[1]))

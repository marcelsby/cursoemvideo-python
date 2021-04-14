print('{1} {0} {1}'.format('DESAFIO #070', '=' * 10))

total_gasto = float()
qtd_produtos_custam_mais_de_mil = int()
nome_produto_mais_barato = str()
preco_produto_mais_barato = float()
contador = 1

try:
    while True:
        print(f'\nInserindo os dados do {contador}o produto:')

        nome = input('Nome: ').strip()
        preco = float(input('Preço: ').replace(',', '.').strip())

        total_gasto += preco

        if preco > 1000:
            qtd_produtos_custam_mais_de_mil += 1

        if contador == 1:
            nome_produto_mais_barato = nome
            preco_produto_mais_barato = preco
        elif preco < preco_produto_mais_barato:
            nome_produto_mais_barato = nome
            preco_produto_mais_barato = preco

        continuar = input('\nDeseja continuar [S/N]? ').upper().strip()

        if continuar != 'S':
            break

        contador += 1

except ValueError:
    print('\033[31m\nEntrada inválida detectada!\nSaindo...')
    exit(1)

print('\nTotal gasto na compra: \033[32mR$ {:.2f}\033[m'.format(total_gasto))
print(f'Quantidade de produtos que custam mais de R$ 1000.00: \033[32m{qtd_produtos_custam_mais_de_mil}\033[m')
print(f'Nome do produto mais barato: \033[32m{nome_produto_mais_barato}\033[m')

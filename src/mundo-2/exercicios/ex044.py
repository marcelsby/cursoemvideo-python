print('{1} {0} {1}'.format('DESAFIO #044', '=' * 5))

try:
    print('Formas de pagamento:'
          '\n1. À vista no dinheiro/cheque: 10% desconto'
          '\n2. À vista no cartão: 5% desconto'
          '\n3. Até 2x no cartão: preço normal'
          '\n4. 3x ou mais no cartão: 20% de juros\n')

    preco_base = float(input('Digite o valor do produto: '))
    forma_pagamento = int(input('Selecione a forma de pagamento: '))
except:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)

preco_final = float()

if forma_pagamento == 1:
    preco_final = preco_base * 0.9
elif forma_pagamento == 2:
    preco_final = preco_base * 0.95
elif forma_pagamento == 3:
    preco_final = preco_base
elif forma_pagamento == 4:
    preco_final = preco_base * 1.20
else:
    print('\nForma de pagamento inválida!\nSaindo...')

print('De acordo com a forma de pagamento o preço final do produto será: \033[32mR${:.2f}'.format(preco_final))

print('{1} {0} {1}'.format('DESAFIO #012', '=' * 5))

try:
    preco = float(input('Insira o valor do produto: '))
except:
    print('\nValor inválido inserido!\nSaindo...')
    exit(1)

preco_liquidacao = preco * 0.95

print('Preço antes da liquidação: R${:.2f}\nPreço na liquidação: R${:.2f}\nVocê economiza: R${:.2f}'.format(preco, preco_liquidacao, preco - preco_liquidacao).replace('.', ','))
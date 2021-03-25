print('{1} {0} {1}'.format('DESAFIO #036', '=' * 5))

try:
    salario = float(input('Quanto é o seu salário? '))
    preco_imovel = float(input('Qual é o valor do imóvel que você deseja comprar? '))
    pagamento_anos = float(input('Em quantos anos você irá pagar? '))
except:
    print('\nValor de entrada inválido detectado!\nSaindo...')
    exit(1)

qtd_parcelas = pagamento_anos * 12
valor_parcela = preco_imovel / qtd_parcelas
porcentagem_parcela_sobre_salario = valor_parcela / salario

if porcentagem_parcela_sobre_salario > 0.3:
    print('\nSeu empréstimo foi negado por exceder o limite de 30% do seu salário.')
else:
    print('\nParabéns! Seu empréstimo foi aprovado.')

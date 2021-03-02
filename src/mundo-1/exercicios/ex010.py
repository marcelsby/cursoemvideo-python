print('{1} {0} {1}'.format('DESAFIO #010', '=' * 5))

reais = input('Quanto reais você tem disponível para comprar dólares? ')

try:
    reais = float(reais)
except:
    print('\nValor inválido inserido!\nFormato correto: "19.31"\nSaindo...')
    exit(1)

dolar_hoje = 5.68
qtd_dolares = reais // dolar_hoje

print('Cotação do dólar hoje: USD 1,00 = R$ {}'.format(dolar_hoje).replace('.', ','))
print('Com R${:.2f} você compra {:.0f} dólares no dia de hoje.'.format(reais, qtd_dolares).replace('.', ',', 1))

exit(0)

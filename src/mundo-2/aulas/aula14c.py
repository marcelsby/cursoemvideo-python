# Situação: o usuário irá inserir valores até que o valor inserido seja 0
# Ou seja, eu não sei quantos valores o usuário irá inserir
total = 0
qtd_par = 0
qtd_impar = 0

# Simulação de DO WHILE em Python
while True:
    n = int(input('Digite um valor: '))

    if n == 0:
        break
    else:
        total += n

        if n % 2 == 0:
            qtd_par += 1
        else:
            qtd_impar += 1

print('Soma total: {}'.format(total))
print('Quantidade de números pares inseridos: {}'.format(qtd_par))
print('Quantidade de números ímpares inseridos: {}'.format(qtd_impar))
print('Fim')

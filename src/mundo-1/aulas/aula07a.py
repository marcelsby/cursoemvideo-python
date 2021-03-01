# Operadores Aritméticos
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
potenciacao = n1 ** n2

print('A soma dos valores inseridos é igual a {}'.format(soma))
print('A multiplicação dos valores inseridos é igual a {}'.format(multiplicacao))
print('A divisão dos valores inseridos é igual a {:.2f}'.format(divisao), end=' | ')
print('A divisão inteira é igual a {}'.format(divisao_inteira))
print('A potenciação dos valores inseridos é igual a {}'.format(potenciacao))

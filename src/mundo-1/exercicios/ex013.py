print('{1} {0} {1}'.format('DESAFIO #013', '=' * 5))

try:
    salario = float(input('Insira seu salário: '))
except:
    print('\nValor inválido inserido!\nSaindo...')
    exit(1)

salario_aumentado = salario * 1.15

print('\nSalário antes do aumento: R${:.2f}\nSalário depois do aumento: R${:.2f}'.format(salario, salario_aumentado))
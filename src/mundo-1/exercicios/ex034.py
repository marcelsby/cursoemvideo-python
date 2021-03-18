print('{1} {0} {1}'.format('DESAFIO #034', '=' * 5))
try:
    salario = float(input('Digite seu salário: '))
except:
    print('\nSalário inválido inserido!\nSaindo...')
    exit(1)

salario_com_aumento = float()

if salario > 1250:
    salario_com_aumento = salario * 1.10
else:
    salario_com_aumento = salario * 1.15

print('\nSeu novo salário é: R${:.2f}'.format(salario_com_aumento))

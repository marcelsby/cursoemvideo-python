print('{1} {0} {1}'.format('DESAFIO #040', '=' * 5))

try:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
except:
    print('\nNota inválida!\nSaindo...')
    exit(1)

media = (nota1 + nota2) / 2

if media >= 7:
    print('\033[0;32mAPROVADO!')
elif 5 <= media <= 6.9:
    print('\033[0;33mRECUPERAÇÃO!')
elif media < 5:
    print('\033[0;31mREPROVADO!')

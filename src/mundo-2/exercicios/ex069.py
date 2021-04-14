print('{1} {0} {1}'.format('DESAFIO #069', '=' * 10))

try:
    qtd_maiores_de_idade = 0
    mulheres_sub_vinte = 0
    qtd_homens = 0
    contador = 1

    while True:
        print(f'\nInserindo os dados da {contador}a pessoa:')

        idade = int(input('Idade: '))
        sexo = input('Sexo [M/F]: ').upper().strip()

        if sexo != 'M' and sexo != 'F':
            raise ValueError

        if idade > 18:
            qtd_maiores_de_idade += 1

        if idade < 20 and sexo == 'F':
            mulheres_sub_vinte += 1

        if sexo == 'M':
            qtd_homens += 1

        continuar = input('\nDeseja continuar [S/N]? ').upper().strip()

        if continuar != 'S':
            break

        contador += 1

    print(f'\nPessoas maiores de 18 anos: {qtd_maiores_de_idade}')
    print(f'Homens cadastrados: {qtd_homens}')
    print(f'Mulheres sub 20: {mulheres_sub_vinte}')

except ValueError:
    print('\033[31m\nEntrada inválida detectada!\nSaindo...')
    exit(1)

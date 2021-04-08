print('{1} {0} {1}'.format('DESAFIO #057', '=' * 15))

while True:
    sexo = input('Digite um sexo [M/F]: ').upper()

    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Sexo inválido, tente novamente...')
print('Fim')

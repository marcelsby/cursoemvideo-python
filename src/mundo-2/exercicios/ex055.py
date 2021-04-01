print('{1} {0} {1}'.format('DESAFIO #055', '=' * 5))

maior_peso = float()
menor_peso = float()

try:
    for i in range(5):
        peso_atual = float(input('Digite o {}o peso: '.format(i + 1)))

        if i == 0:
            maior_peso = peso_atual
            menor_peso = peso_atual
        else:
            if peso_atual > maior_peso:
                maior_peso = peso_atual
            elif peso_atual < menor_peso:
                menor_peso = peso_atual
except Exception:
    print('\n\033[31mPeso inválido!\nSaindo...')
    exit(1)

print('O maior peso registrado foi \033[32m{} Kg\033[m\n'
      'O menor peso registrado foi \033[34m{} Kg\033[m'
      .format(maior_peso, menor_peso))
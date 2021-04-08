print('{1} {0} {1}'.format('DESAFIO #064', '=' * 5))

total = 0
contador = 0
maior = 0
menor = 0

try:
    while True:
        num = int(input('Digite um valor inteiro: '))

        # Cálculos simples
        contador += 1
        total += num
        media = total / contador

        # Maior e menor
        if contador == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            elif num < menor:
                menor = num

        resposta = input('Deseja inserir mais números [S/N]? ').upper()
        if resposta != 'S':
            break

    print('\nA média dos valores inseridos é: {}'.format(media))
    print('O maior número inserido foi: {}'.format(maior))
    print('O menor número inserido foi: {}'.format(menor))
    print('Foi inserido apenas 1 valor') if contador == 1 else print('Foram inseridos {} valores'.format(contador))

except ValueError:
    print('\nEntrada inválida!\nSaindo...')
    exit(1)


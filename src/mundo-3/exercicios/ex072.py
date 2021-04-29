while True:
    num = int(input('Digite um número inteiro de 0 a 20: '))

    if num >= 0 and num <= 20:
        break

    print('Você digitou um número inválido, tente novamente')

extenso = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE',  'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

print(f'O número que você digitou por extenso é: {EXTENSO[num]}')

print('{1} {0} {1}'.format('DESAFIO #043', '=' * 5))

try:
    peso = float(input('Digite seu peso (Kg): '))
    altura = float(input('Digite sua altura (m): '))
except:
    print('\nValor inválido detectado!\nSaindo...')
    exit(1)

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= IMC < 25:
    print('Você está no peso ideal.')
elif 25 <= IMC < 30:
    print('Você está com sobrepeso.')
elif 30 <= IMC < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')

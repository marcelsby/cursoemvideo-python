print('{1} {0} {1}'.format('DESAFIO #053', '=' * 5))

try:
    frase = input('Digite uma frase: ').replace(' ', '').lower()
    if len(frase) == 0:
        raise Exception
except Exception:
    print('\nFrase vazia!\nSaindo...')
    exit(1)

ultimo_indice_frase = len(frase) - 1
frase_invertida = str()

for letra in range(ultimo_indice_frase, -1, -1):
    frase_invertida += frase[letra]

if frase == frase_invertida:
    print('\n\033[32mA frase inserida é um palíndromo!')
else:
    print('\n\033[31mA frase inserida não é um palíndromo!')

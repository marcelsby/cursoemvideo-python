# Manipulando Texto
frase = 'Curso em Vídeo Python'
frase2 = '             Curso em Vídeo Python        '
print(frase)

# Fatiamento
print('\nFatiamento de string:')
print(frase[7])

print(frase[3:])
print(frase[9:])
print(frase[9:14])

## Intervalo de todos os elementos mas exibindo apenas de dois em dois
## (quando os dois primeiros argumentos são omitidos o Python considera o final e o início da string)
print(frase[::2])
print(frase[0:14:3])

# Aspas triplas para printar strings com quebra de linha
print("""\nLorem ipsum dolor sit amet, consectetur adipiscing elit.
Aliquam id ex tincidunt dui eleifend vulputate.
Nunc tortor turpis, vehicula ac varius condimentum, rhoncus vel libero.
Suspendisse a sagittis nulla, vel gravida tellus.
Sed sagittis lorem ut felis mollis, in ullamcorper risus lacinia.
Proin consectetur porttitor auctor.\n""")

# Análise
print('\nFunção len():')
print(len(frase))
print(len(frase2))

print('\nMétodo .count():')
print(frase.count('o'))
print(frase.count('O'))

print('\nMétodo .upper() aninhado com o .count():')
print(frase.upper().count('O'))

print('\nOperador "in" retorna True se a string inserida existe na string operada e caso contrário retorna False:')
print('Python' in frase)
print('Python' in frase2)

print('\nMétodo .find():')
print(frase.find('Python'))
print(frase.find('píton'))

# Transformação
print('\nMétodo .upper():')
print(frase.upper())

print('\nMétodo .lower():')
print(frase.lower())

print('\nMétodo .strip():')
print(frase2)
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

print('\nMétodo .replace():')
print(frase.replace('Python', 'Banco de Dados MySQL'))

print('\nStrings são imutáveis, logo não é possível alterá-las diretamente por meio de atribuição, apenas por meio dos métodos de transformação:')
print(frase2)
frase2 = frase2.replace('Python', 'Banco de Dados Redis').upper().strip()
print(frase2)

print('\nMétodo .split():')
print(frase.split())
print(frase2.split())

print('\nMétodo .join():')
print('_'.join(frase2.split()))



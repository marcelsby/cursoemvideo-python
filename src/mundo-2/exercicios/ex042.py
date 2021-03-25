print('{1} {0} {1}'.format('DESAFIO #042', '=' * 5))

try:
    a = float(input('Insira o comprimento da primeira reta: '))
    b = float(input('Insira o comprimento da segunda reta: '))
    c = float(input('Insira o comprimento da terceira reta: '))

    if a == int(a):
        a = int(a)

    if b == int(b):
        b = int(b)

    if c == int(c):
        c = int(c)

except:
    print('\nComprimento de reta inválido detectado!\nSaindo...')
    exit(1)

existe_triangulo = bool()

if a > b + c or b > a + c or c > a + b:
    existe_triangulo = False
else:
    existe_triangulo = True

if existe_triangulo:
    print('\nÉ possível formar um triângulo com as retas inseridas!')

    if a == b == c:
        print('O triângulo formado será triângulo equilátero.')
    elif a != b != c:
        print('O triângulo formado será triângulo escaleno.')
    else:
        print('O triângulo formado será triângulo isóceles.')

else:
    print('\nNão O triângulo formado será triângulo com as retas inseridas!')

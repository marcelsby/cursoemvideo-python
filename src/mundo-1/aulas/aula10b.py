# Exemplo clássico de condição
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('A sua média do bimestre é: {:.2f}'.format(media))

if media >= 6:
    print('Parabéns! Você foi aprovado no bimestre!')
else:
    print('Reprovado! Se aplique mais!')

# Operador 'ternário'
print('APROVADO!' if media >= 6 else 'REPROVADO!')

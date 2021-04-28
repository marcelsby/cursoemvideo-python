# Tuplas

# Antes
lanche = 'Hambúrguer'
lanche = 'Suco'

# Agora com variáveis compostas
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-1])
print(lanche[-3:])

# Tuplas são imutáveis
# lanche[1] = 'Refrigerante'

# Iterando sobre tuplas
print(f'\nVocê tem {len(lanche)} lanches!')
print('Seus lanches são:')
for comida in lanche:
    print(f'{comida}')

# Utilizando a função len()
for contador in range(0, len(lanche)):
    if contador == 0:
        print()
    print(f'Eu vou comer {lanche[contador]}')

# Utilizando a função enumerate()
for pos, comida in enumerate(lanche):
    if pos == 0:
        print()
    print(f'Eu vou comer {comida} na posição {pos}')

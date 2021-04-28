# Tuplas podem ser concatenadas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(f'Tupla B ordenada: {sorted(b)}')
print(f'Tupla C: {c}')
print(f'A tupla C têm {len(c)} elementos')
print(f'O número 5 aparece {c.count(5)} vezes na tupla C')
print(f'O número 8 aparece pela primeira vez na posição {c.index(8)} na tupla C')

# Tuplas podem armazenar valores de diferentes tipos
pessoa = ('Marcel', 19, 'M', 74.80)
print(pessoa)

# Apagar uma variável
del(pessoa)

# Com o comando Break e utilizando 'f' strings
soma = num = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num

print(f'A soma dos números inseridos é: {soma}')

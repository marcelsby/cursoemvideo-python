from random import randint
print('{1} {0} {1}'.format('DESAFIO #019', '=' * 5))

alunos = []

i = 0
while i < 4:
    nome = input('Digite o nome do {}o aluno: '.format(i+1))
    if nome.isalpha():
        alunos.append(nome)
        i += 1
    else:
        print('\nNome inválido!\nSaindo...')
        exit(1)

ordem_apresentacao = []
i = 0
tam_alunos = len(alunos)
while i < tam_alunos:
    escolhido = randint(0, len(alunos) - 1)
    ordem_apresentacao.append(alunos[escolhido])
    alunos.pop(escolhido)
    i += 1

print('\nOrdem de apresentação do trabalho:')
i = 1
for aluno in ordem_apresentacao:
    print('{}. {}'.format(i, aluno))
    i += 1

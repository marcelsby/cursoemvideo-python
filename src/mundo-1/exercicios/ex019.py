from mycolors import colorthis
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

escolhido = alunos[randint(0, len(alunos))]
print('\nO aluno escolhido para apagar o quadro foi {}'.format(colorthis(escolhido, background='cyan')))

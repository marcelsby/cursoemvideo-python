from mycolors import colorthis
import re

print('{1} {0} {1}'.format('DESAFIO #007', '=' * 5))


def testar_tipo(input_nota):
    if input_nota.isdigit():
        return float(input_nota)
    elif not re.search("\d*\.\d*", input_nota) is None:
        return float(input_nota)
    else:
        print('\nInsira uma nota válida!\nSaindo...')
        exit(1)


def calc_media_final(notas):
    media = 0
    for nota_individual in notas:
        media += nota_individual

    media_final = media / len(notas)

    return media_final


notas = []

notas.append(input('Insira a primeira nota: '))
notas.append(input('Insira a segunda nota: '))

i = 0
for elemento in notas:
    notas.pop(i)
    notas.insert(i, testar_tipo(elemento))
    if i < len(notas):
        i += 1
    else:
        break

media_final = calc_media_final(notas)

print('A média final do aluno foi: {}'.format(colorthis(media_final, font='blue')))

exit(0)

from datetime import date

print('{1} {0} {1}'.format('DESAFIO #041', '=' * 5))

try:
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
except:
    print('\nAno inválido!\nSaindo...')
    exit(1)

ano_atual = date.today().year
idade_atleta = ano_atual - ano_nascimento
categoria = str()

if idade_atleta <= 9:
    categoria = 'Mirim'
elif idade_atleta <= 14:
    categoria = 'Infantil'
elif idade_atleta <= 19:
    categoria = 'Junior'
elif idade_atleta <= 20:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print('Sua categoria é: {}'.format(categoria))

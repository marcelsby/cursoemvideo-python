from datetime import date

print('{1} {0} {1}'.format('DESAFIO #039', '=' * 5))

try:
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
except:
    print('\nAno inválido!\nSaindo...')
    exit(1)

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print('\nVocê precisa se alistar IMEDIATAMENTE!')
elif idade > 18:
    tempo_passado = idade - 18
    print('\nVocê já passou da idade de se alistar.')
    if tempo_passado == 1:
        print('Já se passou 1 ano do seu ano de alistamento.')
    else:
        print('Já se passaram {} anos do seu ano de alistamento.'.format(tempo_passado))
elif idade < 18:
    tempo_para_alistar = 18 - idade
    print('\nVocê ainda não está na idade de se alistar.')
    if tempo_para_alistar == 1:
        print('Falta 1 ano para você se alistar.')
    else:
        print('Faltam {} anos para você se alistar.'.format(tempo_para_alistar))

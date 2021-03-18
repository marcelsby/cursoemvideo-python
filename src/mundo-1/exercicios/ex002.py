from mycolors import colorthis
print('===== DESAFIO #002 =====')
print('Insira os seguintes dados da sua data de nascimento:')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
print('Você nasceu em: {}/{}/{}. Correto?'.format(colorthis(dia, font='green'),
                                                  colorthis(mes, font='purple'),
                                                  colorthis(ano, font='blue')))

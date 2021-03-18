# Trabalhando com cores no terminal
# Padrão ANSI = \033[ESTILO;COR_DA_FONTE;COR_DO_FUNDOmTEXTO_AQUI\033[m
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

print('Estilos:')
print('\033[0mPADRÃO\033[m')
print('\033[1mNEGRITO\033[m')
print('\033[4mSUBLINHADO\033[m')
print('\033[7mINVERTIDO\033[m\n')

print('Cores para o texto (29-37):')
print('\033[0;29mBRANCO\033[m')
print('\033[0;30;47mPRETO\033[m')
print('\033[0;31mVERMELHO\033[m')
print('\033[0;32mVERDE\033[m')
print('\033[0;33mAMARELO\033[m')
print('\033[0;34mAZUL\033[m')
print('\033[0;35mROXO\033[m')
print('\033[0;36mCIANO\033[m')
print('\033[0;37mCINZA\033[m\n')

print('Cores para o fundo (40-47):')
print('\033[7;29mBRANCO\033[m')
print('\033[0;29;40mPRETO\033[m')
print('\033[0;29;41mVERMELHO\033[m')
print('\033[0;29;42mVERDE\033[m')
print('\033[0;29;43mAMARELO\033[m')
print('\033[0;29;44mAZUL\033[m')
print('\033[0;29;45mROXO\033[m')
print('\033[0;29;46mCIANO\033[m')
print('\033[0;30;47mCINZA\033[m\n')

print('\033[0;29;41mHello, it\'s me Mario!\033[m')
print('\033[35;43mLakers\033[m')

# Utilizando o format para separar as coisas
print('{}{}{}'.format('\033[1;29;41m', ' Coca-Cola ', '\033[m'))

# Utilizando um dicionário para armazenar cores
cor = {
    'fecha': '\033[m',
    'amarelo_e_vermelho': '\033[4;33;41m',
}

print('{}{}{}'.format(cor['amarelo_e_vermelho'], ' Flash ', cor['fecha']))

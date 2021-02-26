entrada = input('Digite algo: ')

# Método .isnumber() / .isalpha() / .isalnum() / .is___()
# Realiza um teste lógico que retorna True / False dependendo do que foi inserido no input
print('Tipo do dado inserido: {}'.format(type(entrada)))
print('É uma string formada por caracteres numerais? {}'.format(entrada.isnumeric()))
print('É uma string composta por dígitos decimais? {}'.format(entrada.isdecimal()))
print('É uma string alfabética? {}'.format(entrada.isalpha()))
print('É uma string alfanumérica? {}'.format(entrada.isalnum()))
print('É uma string uppercase? {}'.format(entrada.isupper()))
print('É uma string que seus caracteres pertencem a tabela ASCII?'.format(entrada.isascii()))
print('A string é um identificador de variável válido em Python?'.format(entrada.isidentifier()))



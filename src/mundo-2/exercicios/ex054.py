from datetime import date
print('{1} {0} {1}'.format('DESAFIO #054', '=' * 5))

ano_atual = date.today().year

maiores = 0
menores = 0

try:
    for i in range(7):
        ano_nascimento = int(input('Digite o {}o ano de nascimento: '.format(i + 1)))
        if len(str(ano_nascimento)) == 4 and ano_nascimento <= ano_atual:
            if ano_nascimento == ano_atual:
                idade = 1
            else:
                idade = ano_atual - ano_nascimento

            if idade >= 21:
                maiores += 1
            else:
                menores += 1
        else:
            raise Exception

except Exception:
    print('\n\033[31mAno inválido!\nSaindo...')
    exit(1)

print('\n\033[33mPESSOAS QUE:\n'
      '\033[32mAtingiram a maioridade: {}\n'
      '\033[31mNão atingiram a maioridade: {}'
      .format(maiores, menores))

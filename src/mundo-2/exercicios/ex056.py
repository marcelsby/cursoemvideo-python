print('{1} {0} {1}'.format('DESAFIO #056', '=' * 15))


class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


def filtrar_sexo(pessoas, sexo):
    res = []
    for p in pessoas:
        if p.sexo == sexo:
            res.append(p)

    return res


def filtrar_pessoa_mais_velha(pessoas):
    p_maior_idade = Pessoa('', 0, '')
    for p in pessoas:
        if p.idade > p_maior_idade.idade:
            p_maior_idade = p

    return p_maior_idade


def filtrar_mulheres_sub_vinte(mulheres):
    sub_vinte = []
    for m in mulheres:
        if m.idade < 20:
            sub_vinte.append(m)

    return sub_vinte


def get_media_idades(pessoas):
    total_idade = int()
    for p in pessoas:
        total_idade += p.idade

    media_idade = int(total_idade / len(pessoas))

    return media_idade


pessoas = []

try:
    for i in range(4):
        print('\n{}'.format('=' * 44))
        print('{1} INSERINDO OS DADOS DA {0}a PESSOA: {1}'.format(i + 1, '=' * 5))

        # Input e validação
        nome = input('Nome: ')
        if not nome.replace(' ', '').isalpha():
            raise Exception

        idade = int(input('Idade: '))
        if idade < 1:
            raise Exception

        sexo = input('Sexo (M, F): ')
        if sexo.upper() != 'M' and sexo.upper() != 'F':
            raise Exception

        # Instanciação da pessoa inserida
        pessoa_inserida = Pessoa(nome, idade, sexo)
        pessoas.append(pessoa_inserida)
except Exception:
    print('\033[31m\nDado inválido inserido!\nSaindo...')
    exit(1)

# Cálculo da média da idade das pessoas inseridas
media_idade = get_media_idades(pessoas)

# Qual é o nome do homem mais velho?
homem_mais_velho = filtrar_pessoa_mais_velha(filtrar_sexo(pessoas, 'M'))

# Quantas mulheres tem menos de 20 anos?
qtd_mulheres_jovens = len(filtrar_mulheres_sub_vinte(filtrar_sexo(pessoas, 'F')))


# Output das informações solicitadas
print('\nA média de idade do grupo é: {}'.format(media_idade))
print('O nome do homem mais velho é: {}'.format(homem_mais_velho.nome))
print('A quantidade de mulheres abaixo dos 20 anos no grupo é: {}'.format(qtd_mulheres_jovens))

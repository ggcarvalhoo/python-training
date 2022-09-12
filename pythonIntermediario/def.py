def saudacao(msg='ola', nome='giovanna'):
    nome = nome.replace('a', '4')
    msg = msg.replace('a', '4')
    return f'{msg}, {nome}'

variavel = saudacao()

print(variavel)
"""
Operador ternário em Python
"""

login_user = True
msg = 'Usuário logado. ' if (login_user == True) else 'Você precisa logar'
print(msg)

# -----------------------------------------------

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Digite apenas números')

else:
    idade = int(idade)
    maioridade = (idade >= 18)
    msg = 'Pode acessar' if maioridade else 'Não pode acessar. '
    print(msg)

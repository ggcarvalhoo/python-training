#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite se você é do sexo F ou M: ')
sexo = sexo.upper()

if sexo == 'F':
    print('Você é do sexo feminino')

elif sexo == 'M':
    print('Você é do sexo masculino')

else:
    print('Não entendi, digite F ou M')


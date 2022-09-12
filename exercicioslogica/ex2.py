# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    print(f'O número informado foi {numero}')
else:
    print('Você não digitou um número')
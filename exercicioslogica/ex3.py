# Faça um Programa que peça dois números e imprima a soma.

num1 = input('Digite um número inteiro: ')
num2 = input('Digite outro número inteiro: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    soma = num1 + num2
    print(soma)

else:
    print('Digite números inteiros válidos')
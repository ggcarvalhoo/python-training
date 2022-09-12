# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

lista = list(range(num1 + 1, num2))

for i in lista:
    print(i)

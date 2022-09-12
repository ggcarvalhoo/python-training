#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input('Digite qual o valor que você ganha por hora em R$: '))
horas = int(input('Digite quantas horas você trabalhou no mês: '))
salario = (valorHora * horas)
print(f'O seu salário mensal é de R$ {salario}')
"""
1- crie uma função que exibe uma saudação com os parâmetros saudação
e nome

2- crie uma função que recebe 3 números como parâmetros e exiba a soma
entre eles.

3- crie uma função que receba 2 números. o primeiro é um valor e o
segundo é um percentual (ex 10%).
Retorne (return) o valor do primeiro número somado do aumento do
percentual do mesmo. (Não esquecer do print)

4- fizz buzz - se o parametro da função for divisível por 3
retorne fizz, se o parametro da função for divisivel por 5 retorne
buzz. se o parametro da função for divisivel por 5 e por 3, retorne
fizzbuzz, caso contrário, retorne o número enviado.

"""

# 1

def saudacao(saudar='Olá', nome='giovanna'):
    return f'{saudar} {nome}'

print(saudacao())

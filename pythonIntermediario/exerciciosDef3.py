"""
3- crie uma função que receba 2 números. o primeiro é um valor e o
segundo é um percentual (ex 10%).
Retorne (return) o valor do primeiro número somado do aumento do
percentual do mesmo. (Não esquecer do print)
"""

def function(v1, v2):
    return v1 + (v1 * v2 / 100)

print(function(100, 50))

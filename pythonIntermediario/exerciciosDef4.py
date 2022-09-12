"""
4- fizz buzz - se o parametro da função for divisível por 3
retorne fizz, se o parametro da função for divisivel por 5 retorne
buzz. se o parametro da função for divisivel por 5 e por 3, retorne
fizzbuzz, caso contrário, retorne o número enviado.

"""

def fizzbuzz(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return 'FizzBuzz'
    if n1 % 3 == 0:
        return 'Fizz'
    if n1 % 5 == 0:
        return 'Buzz'
    return n1
print(fizzbuzz(15))
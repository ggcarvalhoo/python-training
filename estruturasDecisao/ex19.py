num1 = float(input('digite um número: '))
num2 = float(input('digite outro número: '))

if num1 > num2:
    print(f'o número {num1} é maior que o número {num2}')

elif num2>num1:
    print(f'o número {num2} é maior que o número {num1}')

elif num1 == num2:
    print(f'os números {num1} e {num2} são iguais')

else:
    print('nada aconteceu')
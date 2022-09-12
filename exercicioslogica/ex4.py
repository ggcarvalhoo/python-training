# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = input('Digite a sua primeira nota: ')
nota2 = input('Digite sua segunda nota: ')
nota3 = input('Digite sua terceira nota: ')
nota4 = input('Digite sua quarta nota: ')

if nota1.isdigit() and nota2.isdigit() and nota3.isdigit() and nota4.isdigit():
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    nota4 = float(nota4)
    media = (nota1 + nota2 + nota3 + nota4)/4
    print(f' Sua média bimestral é: {media}')

else:
    print('Digite números válidos')
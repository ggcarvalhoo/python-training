# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

l = float(input('Digite a medida do lado do quadrado: '))
area = l**2
dobro = area*2

print(f'O valor da área desse quadrado é {area:.2f}m² e o dobro da área é {dobro:.2f}m²')
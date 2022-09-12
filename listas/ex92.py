# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []
for i in range(5):
    lista.append(int(input(f'Digite o {i+1}° número: ')))

print(f'Os números digitados foram {lista}')

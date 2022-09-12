"""
Desempacotamento de listas em python
"""

lista = ['A', 'B', 'C', 1, 2, 3, 4, 5, 6, 7]

n1, n2, n3, *resto = lista

print(n1)
print(n2)
print(n3)
print(*resto)
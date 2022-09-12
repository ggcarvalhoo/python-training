"""
contadores
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

for v1, v2 in enumerate(range(10, 1, -1)):
    print(v1, v2)


print('----------')

cont = range(20, 31, +1)

for v1, v2 in enumerate(cont, 40):
    print(v1, v2)
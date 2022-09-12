# Objeto que enumera elementos dentro da lista
# Objeto que enumera cada iteração do for

lista = [
    # 0    1    3
    ['1', '2', '3'], # 0
    ['A', 'B', 'C'], # 1
    ['!', '@', '#']  # 2
]
#   enumerate do elemento | elemento
for v1, v2 in enumerate(lista, 10):
    print(v1)
    print(v2)
    print('---------------')

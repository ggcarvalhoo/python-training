lista = ['maria', 'jose', 'carlos', 'cadu']

letra_digitada = input('Digite uma letra: ')
letra_digitada = letra_digitada.lower()

for elemento in lista:
    if elemento.startswith(letra_digitada):
        print(f'Essa palavra começa com a letra: {letra_digitada}')
        if letra_digitada in elemento:
            print(f'A palavra é {elemento}')
            continue
    else:
        print(f'Essa palavra não começa com a letra: {letra_digitada}')



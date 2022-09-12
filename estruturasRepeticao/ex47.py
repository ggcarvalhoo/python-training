"""
Faça um programa que leia um nome de usuário e a sua senha e
não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

usuario = input('Digite seu usuário: ')
senha = input('Digite a sua senha: ')

while usuario == senha:
    print("ERRO! \nVocê não pode ter usuario e senha iguais")
    usuario = input('Digite seu usuário: ')
    senha = input('Digite a sua senha: ')

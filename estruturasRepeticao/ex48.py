"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário em R$: '))
sexo = input('Digite seu sexo(F ou M): ')
estadoCivil = input('Digite seu estado civil(S, C, V ou D): ')


while len(nome) < 3:
    nome = input('ERRO! Seu nome precisa ter mais de 3 caracteres. \n'
          'Digite seu nome: ')

while idade < 0 and idade > 150:
    idade = int(input('ERRO! Sua idade precisa estar entre 0 e 150. \n'
          'Digite sua idade: '))

while salario < 0:
    salario = float(input('ERRO! Seu salário precisa ser maior que 0. \n'
                          'Digite seu salário: '))

while sexo != 'f' or sexo != 'm':
    sexo = sexo.lower()
    sexo = input('ERRO! Seu sexo precisa ser F ou M. \n'
                 'Digite seu sexo: ')
    sexo = sexo.lower()

while (
    estadoCivil != "s"
    and estadoCivil != "c"
    and estadoCivil != "v"
    and estadoCivil != "d"
   ):
    estadoCivil = input('ERRO! Seu estado civil precisa ser -> (S, C, V ou D \n'
                        'Digite seu estado civil(S, C, V ou D): ')



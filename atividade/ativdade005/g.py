# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 03/06/2024
# atividade005
# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('NÚMEROS PRIMOS')
print('.'*79)

# Entrada de dados.

inicio = int(input('insira um valor para iniciar: '))
final = int(input('insira um valor para finalizar: '))

for c in range(inicio,(final + 1)):
    for a in range(inicio,c):
        if c % a == 0:
            break
    else:
        print(c)
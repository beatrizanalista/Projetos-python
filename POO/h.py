# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que imprima os valores no
#  # intervalo definidos pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os

os.system('cls')

comeco = int(input('digite o valor do primeiro intervalo:'))
fim = int(input('digite o valor do segundo intervalo:'))
print('3 valores irão ser ignorados')
ignorado_1= int(input('entre com o 1 valor: '))
ignorado_2 = int(input('entre com o 2 valor: '))
ignorado_3 = int(input('entre com o 3 valor: '))

for i in range(comeco, fim):
    if i ==  ignorado_1 or i == ignorado_2 or i == ignorado_3:
        continue
print('')
print({i})

print('-'*70)
print('fim do programa!')
print()
# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que imprima os números primos entre 0 e 100.

import os

os.system('cls')


for c in range(0, 100):
    for b in range(5,c):
        if c % b ==0:
            break
    else:
        print('')
        print({c})

print('-'*70)
print('fim do progrma! ')
print()
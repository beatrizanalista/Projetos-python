# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.

import os

os.system('cls')


class Contagem:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
impar = 0
soma = 0

for b in range(1, 100):
    if not b % 2 ==0:
    impar  += 1
    soma  += b 
print({b}  and= '-')

print('')
print('impar')
print()
print(soma)

print('-'*70)
print('fim do progrma! ')
print()
# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 14/06/2024
# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

import os


os.system('cls')

entrada = ()
nomes = []
indice = 0
nome = " "

print('-'*70)
while True:
    entrada = input('Digite 5 nomes separados por espaços: ')
    nomes = entrada.split()
    if (len(nomes) > 5):
        print('Digite apenas cinco nomes')
        continue
    else:
        break
print('-'*70)

print('='*79)
print('Nomes e seus índices')
for indice, nome in enumerate(nomes):
    print(f'Índice: {indice} Nome: {nome}')
print('-'*70)

print('-'*70)
print('Fim do programa')
print('='*70)
# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 11/07/2024
# Crie uma função que receba uma lista de números. Depois retorne duas listas com os números pares, os números ímpares, a quantidade de números pares e a quantidade de números ímpares.

import os

from aula18.packing_unpackinng import empacotar

os.system('cls')


def numeros(*lista_numeros):
  print(f'numeros: {lista_numeros}')
  for i in lista_numeros:
      print(numeros)
      
empacotar(2, 4, 6, 8, 10, 12) 
print(f'2 = {2}')
print(f'4 = {4}')
print(f'6 = {6}')
print(f'8 = {8}')
print(f'10 = {10}')
print(f'12 = {12}')

lista_numeros = [2, 4, 6, 8, 10, 12]
empacotar(*lista_numeros)
print()

print('-'*70)
print('fim do programa!')
print()
# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 14/06/2024
# Faça um programa que leia as vogais, depois mostre-as em ordem inversa.

import os



os.system('cls')

vogais = ['a', 'e', 'i', 'o', 'u']
vogais_inversa = []

print('.'*79)
print(f'Invetendo a ordem das vogais: {vogais}')
print('.'*79)

vogais.sort()
vogais_inversa = vogais.copy()
vogais_inversa.sort(reverse = True)

print('-'*70)
print(f'Vogais: {vogais}')
print(f'Vogais em ordem inversa: {vogais_inversa}')
print('-'*70)

print('-'*70)
print('Fim do programa')
print('='*70)
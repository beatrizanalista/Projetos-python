# Utilizando o exercício anterior,  adicione mais 2 elementos ao dicionário.

import os


os.system('cls')

dicionario = {}

print('-'*70)
print('Dicionario com 4 elementos')
print('='*70)

ifood = {}

ifood [1] = 'mclanche'
ifood [2] = 'burgurking'
ifood [3] = 'Garotão'
ifood [4] = 'Digão'

ifood[5] = int(input('Digite o lugar do seu lanche'))
ifood[6] = int(input('Digite o lugar do lange a ser adicionado '))

print(f'fast food{ifood}')
print('-'*70)
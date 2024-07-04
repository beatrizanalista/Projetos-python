# Utilizando o exercício anterior , retire um elemento do dicionário.

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

print('removendo um item usando pop().')
if ifood:
    ifood = int('Digite o ifood que deseja excluir:')
    lugar_removido = ifood.pop(ifood,'ifood não encontrado')
    print('item removido:{ifood}:{lugar_removido}')
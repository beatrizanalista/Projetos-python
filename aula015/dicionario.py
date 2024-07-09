import os


os.system('cls')

print('-'*70)
print('estrutura de dados: Dicionario ')
print('='*70)

compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# Atribuindo valores
compras['id'] = 1
compras['item'] = 'caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'Sherlock holmes'
pessoas['endereco'] = 'Baker street'
pessoas['numero'] = '221B'
pessoas['cidade'] = 'Londres'
pessoas['pais'] = 'inglaterra'

cores['red'] = 'vermelho'
cores['green'] = 'verde'
cores['blue'] = 'azul'

elementos['pb'] = 'chumbo'
elementos['Au'] = 'ouro'
elementos['N'] = 'nitrogenio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

# saida simples
print(f'minhas compras: {compras}')
print(f'Detetives: {pessoas}')
print(f'cor RGB {cores}')
print(f'Tabela periodica: {elementos}')
print(f'listagem de numeros: {numeros}')
print()
print('-'*100)

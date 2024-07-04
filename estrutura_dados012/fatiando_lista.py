import os


os.system('cls')

print('-' * 70)
print('estrutura de dados: listas [ ]')
print('=' * 70)

lista_mista = ['a', 'b', 3, 'john', 'e', 500, 'g', 'h']

# fatiamento 0 1º elemento
lista_fatiada1 = lista_mista[0]
# fatia todos os elementos
lista_fatiada2 = lista_mista[0:]
# fatia os elementos do indice 0 ate o indice 6
lista_fatiada3 = lista_mista[0:6]
# fatia os elementos do indice 0 ate o indice 6 de 2 em 2
lista_fatiada4 = lista_mista[0:6:2]
# fatia os elementos da direita para esquerda
lista_fatiada5 = lista_mista[::-1]

print(f'fatiando uma lista: {lista_fatiada1}\n')
print(f'fatiando uma lista: {lista_fatiada2}\n')
print(f'fatiando uma lista: {lista_fatiada3}\n')
print(f'fatiando uma lista: {lista_fatiada4}\n')
print(f'fatiando uma lista: {lista_fatiada5}\n')

print('-'*70)
print('fim do programa!')
print('-'*70)
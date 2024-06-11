import os


os.system('cls')

print('-'*70)
print('estrutura de dados: listas [ ]')
print('=' * 70)

lista_numeros_interos = [1, 2, 3, 4]
lista_vogais = ['a', 'e', 'i', 'o', 'u']  
lista_nomes = ['john', 'jane', 'carol']
lista_heterogenea = ['john', 80, 1.90, 'AB']
lista_dentro_lista = [[1, 2, 3, 4], ['a', 'e', 'i', 'o', 'u']]

print(f'lista de numeros: {lista_numeros_interos}')
print(f'lista de vogais: {lista_vogais}')
print(f'lista de nomes: {lista_nomes}')
print(f'lista misturada: {lista_heterogenea}')
print(f'lista de lista: {lista_dentro_lista}')

# varrendo os indices manualmente
lista_num_indice_0 = lista_numeros_interos[0]
lista_vogais_indice_1 = lista_vogais[1]
lista_nomes_indice_2 = lista_nomes[2]
lista_heterogenea_indice_3 = lista_heterogenea[3]
lista_num_indice_1 = lista_dentro_lista[1]

print('-'*70)
print('acessando os elementos de uma lista')
print('='*70)
print(f'lista de numeros: {lista_num_indice_0}')
print(f'lista de vogais: {lista_vogais_indice_1}')
print(f'lista de nomes: {lista_nomes_indice_2}')
print(f'lista de heterogenea: {lista_heterogenea_indice_3}')
print(f'lista de lista: {lista_num_indice_1}')

print('-'*70)
print('fim do programa!')
print('-'*70)
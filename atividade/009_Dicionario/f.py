# Faça um programa que cadastra 5 tipos de vinho.
# Para os campos deste cadastro tome como referência
# nome do vinho, tipo, teor alcoólico e safra.

import os


os.system('cls')

print('-' * 70)
print('CATÁLOGO DE VINHOS')
print('=' * 70)

catalogo = {}
lista = []
opcao = ''

while opcao != 's':
    catalogo['Nome'] = input('Digite o nome do vinho: ')
    catalogo['Tipo'] = input('Digite o tipo do vinho: ')
    catalogo['Teor'] = input('Digite o teor do vinho: ')
    catalogo['safra'] = input('Digite a safra do vinho: ')
    catalogo['vinhos'] = input('Digite o códico para os vinhos: ')
    lista.append(catalogo.copy())
    opcao = input('Deseja sair? (s/n)').lower().strip()

print('='*70)

for elemento in lista:
    for chave, valor in elemento.items():
        print(f'{chave}:{valor}', end='\n')
    print('='*70)
    
print('-'*70)
print('fim do programa!')
print()
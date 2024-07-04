import os


os.system('cls')

print('-'*70)
print('saida com in e not in')
print('='*70)

# exemplo com in
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if (3 in lista_numeros):
    print(lista_numeros)
    posicao = lista_numeros.index(3)
    print(f'o numero 3 esta na posicao {posicao}')
else:
    print('o elemento nao consta na listagem')
    
print()

# exemplo com not in
lista_nomes = ['jonh', 'jane', 'carol']

if ('maria' not in lista_nomes):
    # antes
    print(lista_nomes)
    
    # nao esta na lista, acrescentar
    lista_nomes.append('maria')
    
    print('\no nome maria foi acrescentado')
    print(lista_nomes)
    
print()
print('-'*70)
print('fim do programa!')
print('-'*70)
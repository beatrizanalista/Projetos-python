import os


os.system('cls')

print('-'*70)
print('saida com for...enumerate()')
print('='*70)

soma = 0 

# criando uma lista
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,  10]

# percorrendo a lista com o enumerate()
# o comando enumerate adiciona um indice
# para cada valor de nossa lista
# start opcional, para nao comecar no indice 0
# enumerate(listaNumeros, start = 1)

# para cada numero dentro da lista de numeros, enumere com u indice
for indice, numero in enumerate(lista_numeros):
    soma += numero # soma dos numeros
    print(f'indice: {indice} = numero: {numero}')
    
print('-'*70)
print(f'a soma de todos os numeros e: {soma}')
print('fim do programa!')
print('-'*70)
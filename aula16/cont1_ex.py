import os


os.system('cls')

#  Inicialização do dicionario e da lista
elementos = {} # Dicionario
periodica = [] # lista

# Entrada de dados
for c in range(2): # considerando a entrada de 2 elementos
    print(f"Entrada de dados {c + 1}:")
    simbolo = str(input('Simbolo do elemento: '))
    nome = str(input('Nome do elemento: '))
    
    # Adiciona os dados ao dicionario
    elementos['simbolo'] = simbolo
    elementos['nome'] = nome
    
    # Usa append() com copy() para adicionar uma cópia do dicionariio á lista
    periodica.append(elementos.copy())

print()
print('-'*70)
print("elementos na tabela periódica:")
print(periodica)
print('-'*70)
print()

# for aninhado para percorrer a lista e o dicionario
print("Detalhes dos elementos:")
for elemento in periodica: # para cada elemento na lista
    for chave, valor in elemento.items(): # para cada chave e valor do dicionario
        print(f'{chave.capitalize()}: {valor}') # Imprime a chave e o valor de maneira legível
    print('-'*70) # linha separada entre elementos
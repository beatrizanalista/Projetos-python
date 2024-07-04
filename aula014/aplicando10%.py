import os


os.system('cls')

print('-'*70)
print('estrutura de dados: list comprehensins[]')
print('='*70)

lista_numeros = [100, 200, 300, 500, 600]

# triplicar os valores
lista_com_juros = []

for item in lista_numeros:
    
    lista_com_juros.append(item + (item * .10))
    
print('aplicar 10% de juros: forma normal')
print(f'lista triplicada: {lista_com_juros}')
print()

# list comprehension
lista_com_juros_2 = [item + (item * .10) for item in lista_numeros]
print('aplicar 10% de juros: list comprehension')
print(f'lista triplicada: {lista_com_juros_2}\n')
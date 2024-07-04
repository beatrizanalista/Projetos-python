import os


os.system('cls')

print('-'*70)
print('estrutura de dados: list comprehensions []')
print('='*70)

lista_numeros = [1, 2, 3, 4, 5,]

# triplicando os valores
lista_nova_triplicada = []

for item in lista_numeros:
    lista_nova_triplicada.append(item * 3)
    
print('triplicando os valores: forma normal')
print(f'lista triplicada: {lista_nova_triplicada}')
print()

# lista comprehensions
lista_nova_triplicada_2 = [item * 3 for item in lista_numeros]
print('triplicar os valores: list comprehensions')
print(f'lista triplicada: {lista_nova_triplicada_2}\n')
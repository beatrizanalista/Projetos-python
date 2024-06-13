import os


os.system('cls')

print('-'*70)
print('estrutura de dados: list comprehensions [ ]')
print('='*70)

lista_precos = [100, 200, 300, 500, 600]

# triplicar os valores
lista_com_juros = []

for valor in lista_precos:
    if valor < 300:
        lista_com_juros.append(valor + (valor * .10))

print('aplicar juros em conticional: forma normal')
print(f'lista triplicada: {lista_com_juros}')
print()

# list comprehensions
lista_com_juros_2 = [valor + (valor * .10)
                     for valor in lista_precos if valor < 300]
print('aplicar juros em condicional: list comprehensions')
print(f'lista triplica: {lista_com_juros_2}\n')
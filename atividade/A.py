# curso de desenvolvimento de sistema
# autor:beatriz victoria
# data:16/06/2024
# atividade006
#  C-Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa

import os


os.system('cls')

print('-'*70)
print(
    'no Programa que procure uma lista numeros:\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]')
print('='*70)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
produto = []
numeros_impares = 0 
numero_pares = 0  
multiplos_de_2 = 0
multiplos_de_3 = 0
multiplos_de_4 = 0
lista_reversa = lista_reversa

intervalo_1_9 = lista[0:9]
intervalo_8_13 = lista[8:13]

print('Numeros impares: ')  
while numeros_impares <= 15:
    numeros_impares += 1
    if (numeros_impares % 2 == 0):  
        continue
    print(f'{numeros_impares}', end=(' | '))
else:
    numeros_impares -= 1
    print('')
    print('.'*70)
print('Numeros pares: ')  

while numero_pares <= 15:
    numero_pares += 1
    if numero_pares % 2 != 0: 
        continue
    print(f'{numero_pares}', end=(' | '))
else:
    numero_pares -= 1
    print('')
    print('-'*70)

multiplos_de_2 = [num for num in lista if num % 2 == 0]
multiplos_de_3 = [num for num in lista if num % 3 == 0]
multiplos_de_4 = [num for num in lista if num % 4 == 0]

print("Múltiplos de 2:", multiplos_de_2)
print("Múltiplos de 3:", multiplos_de_3)
print("Múltiplos de 4:", multiplos_de_4)
print('.'*70)

for num in lista[4:6]:
    for num_b in lista[10:12]:
        num_c = num * num_b
        produto.append(num_c)
print(f'Produto dos intervalos 5:6 e 11:12: {produto}')
print('.'*70)

lista_reversa = lista.copy()
lista_reversa.reverse()
print(f'Lista revertida: {lista_reversa}')
print('-'*70)







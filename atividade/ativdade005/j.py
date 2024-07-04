# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares,
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.

import os


os.system('cls')
 
contagem = 0
impares = 0

for c in range(1,100):
    if c % 2 != 0:
        contagem += 1
        impares += c
    else:
        continue

print(f'contagem de impares {impares} ')
print(f'contagem de numeros {contagem} ')
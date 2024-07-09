# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 14/06/2024
# Ler uma lista com 10 números, depois apresente o maior e o menor número da lista

import os


os.system('cls')

entrada = ()
numeros_str = []
numeros_int = []
numero = 0
maior = int
menor = int

print('.'*79)
print('qual e o meior e o maior dos numeros')
print('.'*79)

print('-'*79)
while True:
    entrada = input('Digite 10 números separados por espaços: ')
    numeros_str = entrada.split()
    
   
    if (len(numeros_str) > 10):
        print('Digite no máximo 10 números!')
        continue

    for numero in numeros_str:
        if (numero.isnumeric()):
            numeros_int.append(int(numero))
        else:
            print('Digite apenas números!')
            break
    else:
        break
print('-'*79)

maior = numeros_int[0]
for numero in numeros_int:
    if numero > maior:
        maior = numero
    else:
        continue

menor = numeros_int[0]
for numero in numeros_int:
    if numero < menor:
        menor = numero
    else:
        continue

print('='*79)
print(f'intervalo: {numeros_int}')
print(f'no intervalo o maior número é {maior}')
print(f'E o menor número é {menor}')
print('='*70)

print('-'*70)
print('Fim do programa')
print('='*70)
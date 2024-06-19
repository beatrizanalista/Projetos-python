import os

os.system('cls')

lista = []
lista_par = []
lista_impar = []

numeros_entrada = input("numeros inteiros")
numeros = numeros_entrada.split()
lista.extend(numeros)

for num in lista:
    num = int(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
        
print(f'numeros pares: {lista_par} ')
print(f'numeros impares: {lista_impar} ')
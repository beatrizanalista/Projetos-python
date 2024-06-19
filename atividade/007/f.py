import os
import random


os.system('cls')

lista = []
ascendente = []
descendente = []

numero_aleatorio = [random.randint(0, 100) for _ in range(10)]

ascendente.extend(numero_aleatorio)
descendente.extend(numero_aleatorio)

ascendente.sort()
descendente.sort(reverse=True)

print(ascendente)
print(descendente)
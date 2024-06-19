import os
import random


os.system('cls')


print('-'*70)
print("sorteio dos numeros")
print('-'*70)

megasena = []
lotofacil = []

for i in range(1,60):
    i = int(i)
    megasena.append(i)
    
    if i <= 25:
        lotofacil.append(i)

sorteio_mega = random.sample(megasena,6)
sorteio_loto = random.sample(lotofacil,15)

print(f'numeros sortiados: {sorteio_mega}')
print(f'numeros sortiados loto: {sorteio_loto}')


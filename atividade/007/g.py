<<<<<<< HEAD
# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 14/06/2024
# Faça um programa que sorteia os números da Mega Sena e da Lotofácil

importar  sistema operacional
importar  aleatoriamente


os . sistema ( 'cls' )


imprimir ( '-' * 70 )
print ( "sorteio dos numeros" )
imprimir ( '-' * 70 )

megasena  = []
lotofácil  = []

para  i  no  intervalo ( 1 , 60 ):
    eu  =  int ( eu )
    Mega Sena . acrescentar ( eu )

    se  eu  <=  25 :
        lotofácil . acrescentar ( eu )

sorteio_mega  =  aleatório . amostra ( megasena , 6 )
sorteio_loto  =  aleatório . amostra ( lotofacil , 15 )

print ( f'números sorteados: { sorteio_mega } ' )
print ( f'numeros sorteados loto: { sorteio_loto } ' )
=======
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

>>>>>>> 4321d289fe0f4d0f537d779cb19cac7fd1e1415f

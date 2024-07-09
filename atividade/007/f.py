<<<<<<< HEAD
# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 14/06/2024
# Faça um programa que gere 10 números aleatórios. Após gerar esses números,
# crie duas listas novas com ordenação ascendente e descendente.
importar  sistema operacional
importar  aleatoriamente


os . sistema ( 'cls' )

lista  = []
ascendente  = []
descendente  = []

numero_aleatório  = [ aleatório . randint ( 0 , 100 ) para  _  no  intervalo ( 10 )]

ascendente . estender ( número_aleatório )
descendente . estender ( número_aleatório )

ascendente . organizar ()
descendente . ordenar ( reverso = Verdadeiro )

imprimir ( off )
imprimir ( descendente )
=======
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
>>>>>>> 4321d289fe0f4d0f537d779cb19cac7fd1e1415f

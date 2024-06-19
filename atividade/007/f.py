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
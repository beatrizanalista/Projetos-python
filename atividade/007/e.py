# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 14/06/2024
# Faça um programa que receba 7 números inteiros. Depois quebre essa lista em: 
# lista de pares e lista de ímpares.
import os  

os . sistema ( 'cls' )

lista  = []
lista_par  = []
lista_impar  = []

números_entrada  =  input ( "números inteiros" )
numeros  =  numeros_entrada. dividir ()
lista . estender ( números )

para  num  na  lista :
    num  =  int ( num )
    se  num  %  2  ==  0 :
        lista_par . acrescentar ( num )
    outro :
        lista_impar . acrescentar ( num )

print( f'números pares: { lista_par } ' )
print( f'numeros importa: { lista_impar } ' )
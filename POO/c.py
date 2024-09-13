# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


class Intervalo:
    def __init__(self, inicio, fim ):
        self.inicio = inicio
        self.fim = fim
    
    def imprimir(self, inicio, fim):
        pass
    
class Inverso:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def Imprimir_Intervalo(self):
        for i in range(self.inicio, self.fim -1, -1):
            print(i, end= ', ') 
        print()
    
        
os.system('cls')


Intervalo = Inverso(10, 0)

Intervalo.Imprimir_Intervalo()

print('-'*70)
print('fim do programa!')
print()
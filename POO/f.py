# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que imprima os números primos entre 0 e 100.

import os

os.system('cls')


class Imprima:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def imprimir_primos(self, inicio, fim):
        pass
    
    
class Primos(Imprima):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def imprimir_primos(self):
        for c in range(self.inicio, self.fim):
            for b in range(self.inicio,c):
                if c % b ==0:
                    break
            else:
                print(c, end=', ')

imprima = Primos(2, 101)

imprima.imprimir_primos()

print('-'*70)
print('fim do progrma! ')
print()
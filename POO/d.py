# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que imprima os números pares entre 0 e 100.

import os


class Impressao:
    def __init__(self, inicio, fim ):
        self.inicio = inicio
        self.fim = fim
        
    def imprimir_pares(self, inicio, fim):
        pass
    
    
class Imprima(Impressao):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def imprimir_pares(self):
        for i in range(0, 100):
            if i % 2 ==0:
                print(i, end= ', ')
        print()



os.system('cls')

Impressao = Imprima(inicio=0, fim=100 + 1)

print('-'*70)
print(f'inicio {Impressao.inicio} até {Impressao.fim} ')
print()

impressao = Imprima(0, 100)

impressao.imprimir_pares()

print('-'*70)
print('fim do programa! ')
print()
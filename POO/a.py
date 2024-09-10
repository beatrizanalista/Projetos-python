# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que imprima os números no intervalo entre 1 e 100. Os números devem ser apresentados na horizontal

import os


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def imprimir_intervalo(self, inicio, fim):
        pass


class ImpressaoIntervalos(Intervalo):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def imprimir_intervalo(self):
        for i in range(self.inicio, self.fim):
            print(i, end=',')


os.system('cls')

intervalo = ImpressaoIntervalos(inicio=1, fim=100 + 1)

print('-'*70)
print(f'inicio {intervalo.inicio} até o {intervalo.fim - 1}')
print()

intervalo = ImpressaoIntervalos(1, 101)

intervalo.imprimir_intervalo()
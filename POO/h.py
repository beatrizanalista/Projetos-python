# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que imprima os valores no
#  # intervalo definidos pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os

os.system('cls')


class intervalo:
    def __init__(self, ignorado_1, ignorado_2, ignorado_3, inicio, fim):
        self.ignorado_1 = ignorado_1
        self.ignorado_2 = ignorado_2
        self.ignorado_3 = ignorado_3
        self.inicio = inicio
        self.fim = fim
        
    def impressos_ignorado(self):
        pass
    
    
class Ignorado(intervalo):
    def __init__(self, inicio, fim, ignorado_1, ignorado_2, ignorado_3):
        self.ignorado_1 = ignorado_1
        self.ignorado_2 = ignorado_2
        self.ignorado_3 = ignorado_3
        self.inicio = inicio
        self.fim = fim
        
    def impressos_ignorado(self):
        for i in range(self.inicio, self.fim):
            if i == ignorado_1 or i == ignorado_2 or i == ignorado_3:
                continue
            else:
                print(i, end=', ')
        
ignorado_1= int(input('entre com o 1 valor: '))
ignorado_2 = int(input('entre com o 2 valor: '))
ignorado_3 = int(input('entre com o 3 valor: '))
inicio = int(input('o primeiro número para iniciar,onde será ignorado: '))
fim = int(input('o ultimo (fim) número para finalizar,onde será ignorado: '))
print('3 valores irão ser ignorados')

imprimir = Ignorado(inicio, fim, ignorado_1, ignorado_2, ignorado_3,)
imprimir.impressos_ignorado()
print()

print('-'*70)
print('fim do programa!')
print()
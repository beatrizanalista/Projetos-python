# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver  impresso.

import os


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def imprimir_intervalo(self, inicio, fim ):
        pass
    
class Imprimir(Intervalo):
    def __init__(self, inicio, fim):
        self.inicio= inicio
        self.fim= fim
        
    def imprimir_intervalo(self):
        for i in range(self.inicio, self.fim + 1):
            print( i, end=',')
        print()
        
os.system('cls')

inicio = int(input('qual o primeiro número que deseja ver: '))
fim = int(input('qual o ultimo número que deseja ver: '))

intervalo = Imprimir(inicio, fim)

intervalo.imprimir_intervalo()

print('-'*70)
print('fim do programa!')
print()
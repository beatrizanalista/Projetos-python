# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo,
# assim como a soma dos mesmos.

import os

os.system('cls')

class Contagem:
    def __init__(self, inicio, fim, impar, soma):
        self.inicio = inicio
        self.fim = fim
        self.impar = impar
        self.soma = soma
        
    def intervalo_impar(self):
        pass
    
    
class intervalo(Contagem):
    def __init__(self, inicio, fim, impar, soma ):
        self.inicio = inicio
        self.fim = fim
        self.impar = impar
        self.soma = soma
        
    def intervalo_impar(self,):
     for b in range(1, 100):
        if not b % 2 ==0:
            impar  += 1
            soma  += b 
        print(b, end=  '-')  


print('')
print('impar')
print('soma')
print()

contagem = intervalo(1, 100 )
contagem.intervalo_impar()

print('-'*70)
print('fim do progrma! ')
print()
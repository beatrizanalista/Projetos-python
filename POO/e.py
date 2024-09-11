# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


class Soma:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def quantidade_pares(self, inicio, fim):
        pass
    

class Intervalo(Soma):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def quantidade_pares(self):
        quantidade = 0
        for i in range(0, 100):
            if i % 2 ==0:
                print(i, end= ', ')  
                quantidade = quantidade + 1
        print()
        print(f'A quantidade de números pares foi: {quantidade}')
       

os.system('cls')

Soma = Intervalo(inicio=0, fim=100 + 1)

print('-'*70)
print(f'inicio {Soma.inicio} até {Soma.fim} ')
print()

soma = Intervalo(0, 100)

soma.quantidade_pares()

print('-'*70)
print('fim do programa! ')
print()



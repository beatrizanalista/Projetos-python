# curso de desenvolvimento de sistemas
# turma 0152
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

import os

os.system('cls')


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def imprimir_primos(self, inicio, fim):
        pass


class Primos(Intervalo):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def imprimir_primos(self):
        if self.inicio < 2:
            self.inicio = 2
            print('Não existe número primo menor')
        for i in range(self.inicio, self.fim + 1):
            for c in range(self.inicio, i):
                if i % c == 0:
                    break
            else:
                print(i, end=', ')


inicio = int(input('insira um numero para iniciar: '))
fim = int(input('insira um número para finalizar: '))

imprime = Primos(inicio, fim)

imprime.imprimir_primos()

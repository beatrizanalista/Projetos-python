# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 03/06/2024
# atividade005
# Faça um programa que imprima os valores no intervalo definidos pelo usuário.  
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os


os.system('cls')

inicio = int(input('insira um valor para iniciar: '))
final = int(input('insira um valor para finalizar: '))

ignora1 = int(input('insira o 1º valor a se ignorar: '))
ignora2 = int(input('insira o 2º valor a se ignorar: '))
ignora3 = int(input('insira o 3º valor a se ignorar: '))

for c in range(inicio,(final +1)):
    if ((c == ignora1) or (c == ignora2) or (c == ignora3)):
        continue
    print(c)

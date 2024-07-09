# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 21/05/2024
# atividade 004
# Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra 'o' aparece e em que posição ela aparece pela primeira e última vez

import os

os.system('cls')

print('-'*70)
print('digite o nome completo')
print('.'*70)

print('-'*70)
nome_completo = str(input('entre com o nome: ' )).strip()
print('.'*70)

lista_quebrado = nome_completo.split(' ')
primeiro_nome = lista_quebrado[0]
ultimo_nome = lista_quebrado[-1]

print(lista_quebrado)
print(f'seu primeiro nome é {primeiro_nome} ')
print(f'seu ultimo nome é {ultimo_nome} ') 

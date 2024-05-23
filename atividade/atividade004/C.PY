# curso de desenvolvimento de sistemas
# turma 0152 (braba)
# autor:Beatriz Victoria
# data: 21/05/2024
#Faça um programa que leia o nome de uma pessoa e verifique se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os

os.system('cls')


print('-'*70)
print('strings ')
print('='*70)

nome ="GABRIEL Braga"  

print(f'nome: {nome}')
if "braga" in nome: # verificando pra ver se esta no nome
    print('a palavra esta presente')
else:
    ('a palavra nao esta presente')
print('.'*70)

print('e(and) falso') # verdadeiro ou falso
if ('braga'):
    print('verdadeiro')
else:
    print('falso')

print('.'*70)

print('e (and) verdadeiro')
if ('braga'):
    print('falso')
else:
    print('falso')

    print('='*70)
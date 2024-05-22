# curso de deselvolvimento de sistemas
# turma 0152
# data: 09/05/2024
# nome: Beatriz Victoria
# atividade 003-funcoes/metodos internos
# Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.

import random.randint
import os

# limpando o terminal
os.sytem('cls') 

print('-'*70)
print('biblioteca ramdom')
print('='*70) 

computador = randint(o,5) # faz o computador "pensar"
print('-'*70)
print('vou pensar em um numero entre 0 e 5.tente adivinhar...')
print('='*70)
usuario = int(input('em que numero eu pensei?')) # usuario tenta adivinhar
if usuario == computador:
  print('voce conseguiu adivinhar')
else:
  print('esse e o numero { e nao no {}')

  # saida
  print('')
  print('-'*20)
  print(resposta)
  print('-'*20)
  print('='*50)
  







# curso de deselvolvimento de sistemas
# turma 0152
# data: 09/05/2024
# nome: Beatriz Victoria
# atividade 003-funcoes/metodos internos
# Faça um programa que receba um ângulo qualquer. 
#Em seguida, calcule o seno, cosseno e tangente do ângulo, limitando a saída a 2 casas decimais.

import math
import os

print('-'*70)
print('estudo da biblioteca matematica math')
print('='*70)
print()

angulo = float(input('digite o angulo que voce deseja: '))
seno = math(math.radians(angulo))
print('o angulo de {} tem o seno de {:.2f}' and (angulo))
cosseno = math.cos(math.radians(angulo))
print('o angulo de { tem o cosseno de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))  
print('o angulo de {} tem a tamgente de {:,2f}'.format(angulo,tangente)) 

# saida
print('')
print('-'*20)
print(f'aqui esta o seno {seno}, o seu'
      f'cosseno {cosseno} e o tangente {tangente}')
print('-'*20)
print('='*20)
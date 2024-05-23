# curso de desenvolvimento de sistemas
# turma 0152 (braba)
# autor:Beatriz Victoria
# data: 26/04/2024
# atividade002

# importando as bibliotecas
import os


# limpando o terminal
os.system('cls')

print('-'*70)
print('atividade002')
print('-'*70)
 
# conticional
a = input('insira o valor 1: ')
b = input('insira o valor 2: ') 
c = input('insira o valor 3: ')
 
 
if (a + b > c and b + c > a and c + a and c + a > b):
   
  print('pode ser um triangulo')
else:
    print('nao pode ser um triangulo')
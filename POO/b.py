# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver  impresso.

import os


os.system('cls')

inicio = int(input('qual o primeiro número que deseja ver: '))
fim = int(input('qual o ultimo número que deseja ver: '))

for i in range(inicio, fim):
    print('')
    print('{c}')

print('-'*70)
print('fim do programa!')
print()
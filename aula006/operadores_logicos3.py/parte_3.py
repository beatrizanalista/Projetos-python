# curso de desenvolvimento de sistemas
# turma 0152 (braba)
# autor: Beatriz victoria
# data: 25/04/2024
# estudo de condicionais: parte 4
# operadores logicos

# importando as bibliotecas
import os


# limpando o terminal
os.system('cls')

# declaracao
a = 10
b = 5
c = 'jonh'

print('-'*70)
print('condicionais: operadores logocos')
print('='*70)

# E (and) verdadeiro
print('E (and) verdadeiro ')
if (a > 5 and b != c):
    print('verdadeiro: bloco executado')
else: 
    print('falso: bloco execultado')
    
    print('.'*70)  
    
    # (and) falso 
    print('e (end) falso')
    if (a > 5 and b == c):
        print('verdadeiro: bloco execultado')
    else:
        print('falso: bloco executado')
         
 # print('.'*70)
   
   # ou (or) verdadeiro
print('ou (or) verdadeiro')  
if (a > 5 or b == c):
     print('verdadeiro: bloco executado')
else:
    print('falso: bloco executado')
    
    print('.'*70)
    
    # ou (or) falso
    print('ou (or) falso')
    if (a < 5 or c == 'jane'):
         print('verdadeiro: bloco executado')
    else:
        print('falso: bloco executado')
        print('-'*70)
        print()         
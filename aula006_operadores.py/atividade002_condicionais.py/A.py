# curso de desenvolvimento de sistemas
# turma 0152 (braba)
# autor: Beatriz Victoria
# data: 25/04/20224
# atividade002 de condicionais

# importando as bibliotecas
import os


# limpamdo o terminal
os.system('cls')

# declaracao
a = 10
b = 6
c = 'claudio'

print('-'*70)
print('condicionais: operadores logicos')
print('='*70)

# processamento
print(int)('entre com um numero inteiro')

# e (and) vrdadeiro
print('e (and) verdadeiro')
if (a > 6 and b !=c):
    print('verdadeiro: bloco executado')
else:
    print('falso:bloco execultado')
    
    print('.'*70)
    
    # e (and) falso
    print('e (and) falso')
    if (a > 6 and b == c):
        print('verdadeiro: bloco execultado')
    else:
        print('falso: bloco executado')
        
        print('.'*70)
        
        # ou (or) verdadeiro
        print('ou (or) verdadeiro')
        if (a > 6 or b == c):
            print('vrdadeiro: bloco execultado')  
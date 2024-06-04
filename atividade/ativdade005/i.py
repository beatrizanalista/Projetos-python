# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 03/06/2024
# atividade005
# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os


os.system('cls')

print('-'*70)
print('Algoritmo que imprime a frase "estou em looping"')
print('='*70)

while(True):
    print('ESTOU EM LOOPING')
    
    letra = str(input('Digite a letra "F" para parar o loop: ')).lower()
    
    if (letra != 'f'):
        print('letra "F" não foi digitada,o loop continua')
        print('.'*70)
    
    else:
        print('-'*70)
        print('A letra foi digitado,voce parou o loop!!')
        break

print('-'*70)
print()
            
            
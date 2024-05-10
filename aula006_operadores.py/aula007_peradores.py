# curso de desenvolvimento de sistemas
# turma 0152 (braba)
# autor:Beatriz Victoria
# data:25/04/2024
# estudo de condicionais:parte 2
# objeto: pratica com condicionais simples e anilhadas

import os


os.system('cls')

# declaracoes
a = 10
b = 5
resposta = ''

print('-'*70)
print('estudo de condicional (simples)')
print('='*70)

# condicionais
if a > b:
    resposta = f'{a} e maior que {b}'
else:
    resposta = f'{a} nao e maior que {b}'
    # saida
    print('-'*70)
    print(resposta)
    
    # declaracoes
    a = 5
    b = 5
    
    print('-'*70)
    print('estudo de condicional (anilhada)')
    print('='*70)
    
    if a > b:
        resposta = f'{a} e maior que {b}'
    elif a > b:

    else
        resposta = f'o valores sao iguais; {a} = {b}'
        #saida
        print('-'*70)
        print(resposta)
        print('-'*70)
        print()
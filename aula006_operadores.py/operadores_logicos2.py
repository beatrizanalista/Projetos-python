# curso de desenvolvimento de sistemas
# turma 0152 (braba)
# autor: Beatriz Victoria
# data:25/04/2024
# estudo de condicionais: parte 3
# operadores relacionais

import os


os.system('cls')

a = 10
b = 5
c = 'jose'
d = 'jose'

print('-'*70)
print('condicionais: operadores relacionais')
print('='*70)

# igualdade (==)
if c == d:
    print('-'*70)
    print(f'{c} e igual {d}')
    print('='*70)
else:
    print(f'{c} nao e igual a {d} ')
    
    # DIFERENCA (!=)
    if a != c:
        print('-'*70)
        print(f'{a} e diferente de {c}')
        print('='*70)
    else:
        print(f'{a} nao e diferente de {c}')
        
        # maior que (>)
        if a > b:
            print('-'*70)
            print(f'{a} e maior que {b}')
            print('='*70)
        else:
            print(f'{a} nao e maior que {b}')
                  
        # menor que (<)
        if b < a:
            print('-'*70)
            print(f'{b} e menor que {a}')
            print('='*70)
        else:
            print(f'{b} nao e menor que {a}')
             
        # maior ou igual a (>=)
        if a >=b:
            print('-'*70)
            print(f'{a} e maior ou igual a {b}')
            print ('')
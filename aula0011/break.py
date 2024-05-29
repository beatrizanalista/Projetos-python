import os 


os.system('cls')

print('-'*70)
print('estrutura de controle: break')
print('='*70)

print()

for c in range(0, 10):
    
    print(f'valor: {c}')
    
    # condicao para terminar a contagem
    if (c == 5):
        print(f'contagem interropida no {c}')
        break
    
print('-'*70)
print('fim do programa!')
print()
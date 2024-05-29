import os


os.system('cls')

print('-'*70)
print('estrutura de controle while else break')
print('='*70)

print()

while (True):
    
    # lower() garante o tratamento para entrada de 's' ou 'S' 
    nome = str(input('digite um nome [s - Sair]: ')).lower()
    
    if (nome != 's'):
        print('comtinue digitando...')
    else:
        print('-'*70)
        print('voce digitou "s" para sair!')
        
        # interrrompe o laco
        break
    
print('-'*70)
print()
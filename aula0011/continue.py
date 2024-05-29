import os


os.system('cls')

print('-'*70)
print('estrutura de controle: continue')
print('='*70)

print()

for c in range(1, 11):
    if c == 5:
        # 5 esta fora do loop, se retirar a linha abaixo,
        # ele nao aparecera na saida, deixei para verificacao!
        print(f'o numero {c} esta fora do loop')
        continue    # salta e o ciclo continua
    print(f'o numero e {c}')
    
    
print('-'*70)
print()
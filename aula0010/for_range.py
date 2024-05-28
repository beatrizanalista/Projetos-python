import os 


os.system('cls')

print('-'*70)
print('estrutura de controle for range')
print('='*70)

print()

for var_iteradora in range(1, 7):
    # end= coloca os numeros em uma mesma linha
    print(f'volor: {var_iteradora}', end=" | ")
    
print()
print()
    
  # ou
    
inicio = 1
fim = 7
passo = 2
    
for var_iteradora in range(inicio, fim, passo):
     # end= coloca os numeros em uma mesma linha
      print(f'valor: {var_iteradora}', end=" | ")
        
print()
print()
        
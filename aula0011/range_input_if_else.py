import os


os.system('cls')

print('-'*50)
print('estrutura de controle com input e if')
print('='*50)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'{var_iteradora + 1}º numero: '))
    
    if (numero % 2 == 0):
        print(f'o numero {numero} e par')
    else:
        print(f'o numero {numero} e impar')
        
        print('-'*50)
        print()
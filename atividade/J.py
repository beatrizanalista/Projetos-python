#
# inports
import os


os.system('cls')

print('-'*70)
print('operadores artmeticos: ordem de precedencia')
print('-'*70)

# entrada de dados
base = float(input('insira a base do retângulo '))
altura = float(input('insira a altura de retângulo '))

# processamento
perimetro = 2* (base + altura)

# saida 
print(f'o perimetro e = {perimetro}')

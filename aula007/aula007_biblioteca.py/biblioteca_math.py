import math
import os


os.system('cls')

print('-'*70)
print('estuda da biblioteca matematica math')
print('='*70)
print()

# entrada de dados
numero_decimal = float(input('entre com um numero decimal'))

# processamento
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal)

# saida
print('-'*50)
print(f'o numero {numero_decimal} arredonda para cima e: {
    arredondar_para_cima}')
print(f'o numero {numero_decimal} arredonda para baixo e:{
    arredondar_para_baixo}')
print('-'*70)
# imports
import os

# limpar o terminal 
os.system('cls')

print('-'*70)
print('operadores aritméticos')
print('='*70)

# entrada de dados
print('---soma')
print('-'*70)
parcela_1 = float(input('entre com 1ª parcela: '))
parcela_2 = float(input('entre com a 2ª parcela: '))

print()
print('--- subtracao')
print('-'*70)
minuendo = float(input('entre com o minuendo: '))
subtraendo = float(input('entre com o subtraendo: '))

print()
print('--- produto')
print('-'*70)
multiplicando = float(input('entre com o multiplicando: '))
multiplicador = float(input('entre com o multiplicador: '))

print()
print('--- divisao')
print('-'*70)
dividendo = float(input('entre como o dividendo: '))
divisor = float(input('entre com o divisor: '))

# prcessamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo 
produto = minuendo * multiplicador
quociente = dividendo / divisor

# saida
print('='*70)
print('resultados')
print('-'*70)
print(f'A soma de {parcela_1} + {parcel_2}')
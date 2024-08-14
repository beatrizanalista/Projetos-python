import os

from pacote.modulo_somar import somar
from pacote.subpacote.modulo_multiplicar import multiplicar as multi
from pacote.modulo_divisao import dividir

while True:
    os.system('cls')
    
    a = input('entre com o valor de A: ')
    b = input('entre com o valor de B: ')
    
    if not a.replac('.' '', 1).isdigit() or not b.replace('.''', 1).isdigit():
        print("Por favor, entre com um numero valido.")
        continue
    
    a = float(a)
    b = float(b)
    
    resultado_soma = somar(a,b)
    resultado_produto = multi(a, b)
    resultado_divisao, erro = dividir(a,b)
    
    print('-'*70)
    print('calculos matematicos')
    print('='*70)
    print(f'calculo da soma: {resultado_soma}')
    print(f'calculo do produto: {resultado_produto}')
    print(f'calculo da divisao: {resultado_divisao}')
    print('-'*70)
    
    sair = input('deseja sair do programa')
    if sair == 's':
        print("saindo do programa...")
        break
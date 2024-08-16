import os

from pacote.modulo_somar import somar # type: ignore
from pacote.subpacote.modulo_multiplicar import multiplicar as multi # type: ignore
from pacote.modulo_divisao import dividir # type: ignore

while True:
    os.system('cls')
    
    a = input('Entre com o valor de A: ')
    b = input('Entre com o valor de B: ')
    
    if not a.replace('.', '',1).isdigit() or not b.replace('.', '',1).isdigit():
        print("por favor,entre com um número válido.")
        continue
    
    a = float(a)
    b = float(b)
    
    resultado_soma = somar(a, b)
    resultado_produto = multi(a, b)
    resultado_divisao, erro = dividir(a, b)
    
    print('-'*70)
    print('Calculos Matematicos')
    print('='*70)
    print(f'cálculo da soma: {resultado_soma}')
    print(f'Calculo do produto: {resultado_produto}')
    print(f'Cálculo da divisão: {resultado_divisao}, {erro}')
    print('-'*70)
    
    sair = input("Deseja sair do programa? (s/n): ").strip().lower()
    if sair == 's':
        print("saindo do programa...")
        break
    
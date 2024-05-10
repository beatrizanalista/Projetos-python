# import as bibliotecas
import os
import math


# limpando o terminal
os.system('cls')

print('-'*70)
print('estudo da biblioteca matematica math')
print('='*70)
print()

# declaracoes
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5 # cateto oposto
ca = 10 # cateto adjacaente

# processamento
potencia = math.pow(base, expoente)
raizquadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)

#saida
print(f'{base} eleva a {expoente} e igual a: {potencia}')
print(f'a raiz quadrada de `{radicando} e: {raizquadrada}')
print(f'o seno de {angulo} e: {seno:.2f}')
print(f'o cosseno de {angulo} e: {cosseno:.2f}')
print(f'a tangente de {angulo} e: {tangente:.2f} ')
print(f'o valor da hipotenusa e: {hipotenusa:.2f}')
print('-'*70)

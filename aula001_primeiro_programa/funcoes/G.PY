# curso de deselvolvimento de sistemas
# turma 0152
# data: 09/05/2024
# nome: Beatriz Victoria
# Atividade.
# atividade 003-funcoes/metodos internos
# Faça um programa que peça os valores de a, b e c de uma equação do 2º grau. 
# Calcule as raízes da equação do 2º grau seguindo a fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

# biblioteca
import os
import math

# limpando o terminal
os.system('cls')

print('-'*50)
print('exercicio G')
print('-'*50)

# entrada
a = int(input('entre com o valor de A: '))
b = int(input('entre com o valor de c:'))
resposta = ''

# processamento 
discriminante = b**2 - 4*a*c
rd = math.sqrt(discriminante) # raiz descriminante
r1 = (-b + rd) / (2*a) # raiz 1
r2 = (-b - rd) / (2*a) # raiz 2

if rd > 0:
    resposta = (f'o resultado da equacao é:'
    f'raiz positiva = {r1} raiz negativa = {r2}')
else:
    resposta = f'essa equacao e incalculavel'

    # saida
    print('')
    print('-'*20)
    print(resposta)
    print('-'*20)
    print('='*20)

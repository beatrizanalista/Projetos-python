# curso de desenvolvimento de sistemas
# turma 0152 (braba)
# autor: Beatriz victoria
# data:26/04/2024
# atividade002

# import as bibliotecas
import os


# limpando o terminal
os.system('cls')

# entrada

a = float(input('entre com o valor de a:'))
b = float(input('entre com o valor de b:'))
c = float(input('entre com o valor de c:'))

delta = (b ** 2) - 4 * a * c

x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)
print(f'x1 = {x1}')
print(f'x2 = {x2}')  
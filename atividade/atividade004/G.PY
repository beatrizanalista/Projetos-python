# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 21/05/2024
# Faça um programa que receba um número inteiro e mostre na tela:
#• A quantidade de unidades, a quantidade de dezenas, a quantidade de centenas e a quantidade de milhares.

import os


os.system('cls')


print('entre com os numeros')
numero = int(input('informe um numero:'))
u = numero // 1 % 10
d = numero // 10 % 10 
c = numero // 100 % 10
m = numero // 1000 % 10

print('analisando o numero {}', format(numero))
print('unidade: {}'. format(u))
print('dezena: {}'. format (d))
print('centena: {}'. format(c))
print('milhar: {}'. format(m))


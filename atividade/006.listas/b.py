# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 14/06/2024
# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os


os.system('cls')

print('.'*79)
print('soma dos elemnetos da lista')
print('.'*79)

# Declarações de variáveis
numero_entrada = 0
num = 0
numeros = []
soma = 0 + 0

# Entrada de dados do usuário.
print('-'*79)

while True:
    numero_entrada = input('Digite um número: ')
    # Validação de dados.
    if (numero_entrada.isnumeric()):
        numero_entrada = int(numero_entrada)
        numeros.append(numero_entrada)
        if (len(numeros) == 5):
            break
    else:
        print('Entrada inválida!')
        continue

print('-'*79)

# Processamento de dados.
for numero in numeros:
    soma += numero

# Saída de dados.
print('-'*70)
print(f'sequência dos números: {numeros}')
print(f'soma de todos elementos da sequência é: {soma}')
print('='*70)

# Imprimindo título de fim.
print('-'*70)
print('Fim do programa!')
print('-'*70)
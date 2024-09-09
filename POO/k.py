# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Crie um programa que pede que o usuário digite um nome ou uma frase, 
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

import os


os.system('cls')

while True:
    frase = int(input('digite a frase que deseja verificar: '))
    print()

    if(frase.isnumeric()):
        print('frase está invalida')

    else:
        break

escrita_normal = frase.replace('', "").lower()
invertido = escrita_normal[::-1]
if (escrita_normal = invertido):
    verificado = f' {frase} é um palíndromo'
else:
    verificado = f'{frase} não é um palíndromo'

print('-'*70)
print('é um polindromo')
print()

print('-'*70)
print('fim do programa!')
print()
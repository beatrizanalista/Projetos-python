# Faça um programa para criar um dicionário com 5  cores. Depois,  imprima as chaves e os valores deste dicionário

import os 


os.system('cls')

dicionario = {}
lista = {}

def exibirOpcoes():
    print('-'*70) 
    print('1. Adicinar cor')
    print('2. Mostrar cores')
    print('3. Sair')
    print('-'*70)

opcao = input('O que você deseja fazer?\n')

if opcao == '1':
        for i in range(1, 6):
            chave = i
            valor = input('Informe a cor:')

        meu_dicionario['cor'] = chave
        meu_dicionario['valor'] = valor
            # meu_dicionario[chave] = cor

            # adicionando na lista
        lista.append(meu_dicionario.copy())
        print('-'*70)

elif opcao == '2':
        print('\nCores adicionadas')
        for elemento in lista:
            for chave, valor in elemento.items():
                print(f'{chave} - {valor}')
            print('-'*70)

elif opcao == '3':
        print('finalizando...')
break

else:
print('erro...')  
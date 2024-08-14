# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 11/07/2024
# Crie uma função que verifica se uma aluno está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados. O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

import os


os.system('cls')

aluno = []
nome = {}
matricula = ''
nascimento = ''

def cadastro(*lista_nomes):
    print(f'Empacoatados: {lista_nomes}')
    for i in lista_nomes: 
        print(f'Empacotado: {i}')
         
dicionario = ['Nome', 'Matricula', 'nascimento']
empacotar = cadastro 
cadastro.append('nome completo: {nome}')  # corrir o erro
nascimento.insert('insira sua data de nascimento: {nascimento}')
matricula.insert('insira o numero da matricula: {matricula}')

print('-*70')
print('Final do programa!...')
print()
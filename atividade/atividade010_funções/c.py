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
         
dicionario = ['nome', 'matricula', 'data de nascimento']
empacotar = dicionario_cadastro   # type: ignore
dicionario_cadastro.append('nome completo {nome} :') # type: ignore # nome completo para ajudar a preenger o cadastro
nascimento.insert('insira sua data de nascimento: ')



print('-'*70)
print('Fim do cadastro!Volte sempre!')
print()



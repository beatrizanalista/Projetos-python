import os


os.system('cls')

print('-'*70)
print('saida com for')
print('='*70)

# criando uma lista
lista_alunos = []

for c in range (0, 5):
    nome = str(input('entre com o nome do aluno: '))
    
    # guardando em uma lista
    lista_alunos.append(nome)
    
print()
print('impressao dos nomes de alunos:')

# utilizando o len() para saber  quantidade de alunos
for aluno in range(len(lista_alunos)):
    print(lista_alunos[aluno], )
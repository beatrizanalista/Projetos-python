import os


os.system('cls')

print('-'*70)
print('funcoes string')
print('='*70)

frase1 = "ola, mundo!"
quantidade_caracteres = len(frase1) # conta os caracteres
print(f'a frase {frase1} \ncontem {quantidade_caracteres} caracteres')
print('-'*70)

minusculas = frase1.lower() # frase em minusculo
print(f'frase original: {frase1}')
print(f'frase nova: {minusculas}')
print('.'*70)

minusculas = frase1.upper() #frase em maiusculo
print(f'frase original: {frase1}')
print(f'frase nova: {minusculas}')
print('.'*70)

capitalizada = frase1.capitalize() # frase capitalizada
print(f'frase origianal: {frase1}')
print(f'frase nova: {capitalizada}')
print('.'*70) 

frase2 = '   ola,mundo '
sem_espacos = frase2.strip() # retirar espacos,antes e depois
print(f'frase original: {frase2}')
print(f'frase nova: {sem_espacos}')
print('.'*70)

substituicao = frase1.replace("mundo","python") # troca palavra
print(f'frase original: {frase1}')
print(f'frase nova: {substituicao}')
print('.'*70)

lista = frase1.split(",") # separa as palavras de uma str em uma lista
print(f'frase original: {frase1}')
print(f'frase nova: {lista}')
print('.'*70)

lista = ['ola mundo']
juncao = "-".join(lista) # transforma uma lista em uma string com separador
print(f'frase original: {lista}')
print(f'frase nova: {juncao}')
print('.'*70)
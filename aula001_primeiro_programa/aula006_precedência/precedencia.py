# imports
import os


os.system('cls')

print('-'*70)
print('operadores artmeticos: ordem de procedencia')
print('-'*70)

# entrada
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

# processamento
soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 / 4
media_correta = (nota1 + nota2 + nota3 + nota4) / 4

# saida
print('----notas----------')
print(f'nota 1: {nota1} | nota 2: {nota2} | '
      f'nota 3: {nota3} | nota 4: {nota4}')
print('-'*70)
print(f'media errada: {media}')
print(f'media correta: {media_correta}')
print('-'*70)
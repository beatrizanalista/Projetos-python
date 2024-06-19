# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 14/06/2024
# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.
import os



os.system('cls')

entrada = ()
notas = []
soma =  + 0
media = 0

print('-'*70)
print('medias das notas dos alunos')
print('-'*70)


print('-'*70)
while True:
    entrada = input('Digite as notas de quatro alunos separadas por espaços: ')
    notas = entrada.split()
    
    if (len(notas) > 4):
        print(' insira apenas quatro notas')
        continue
    else:
        break
    
print('-'*70)

for nota in notas:
    soma += int(nota)
media = soma / len(notas)

print('-'*70)
print(f'A média das notas {notas} é: {media}')
print('='*70)

print('-'*70)
print('Fim do programa')
print('='*70)
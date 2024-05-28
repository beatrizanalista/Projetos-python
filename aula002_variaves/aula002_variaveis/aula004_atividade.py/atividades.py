# imports 
# biblioteca para interagir o OS
import os


# limpar terminal 
os.system('cls')

print('-'*70)
print('entrada de dados do usuario')
print('='*70)

# entrada com casting
nome = str(input('nome_do_primata:'))
idade = int(input('entre com a idade: '))
peso = float(input('entre com o peso: '))
raça = int(input('raça_do_primata: '))
doencas = True

# saida interpolada
print(f'nome do primata é {nome}' )
print(f'sua idade {idade} ano' )
print(f'qual o seu peso {peso} kg')  
print(f'qual a raça {raça}')
print(f'possui doencas {doencas}')
print('-')*70
print('')
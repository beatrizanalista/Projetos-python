import os

os.system('cls')


frase = str(input('digite uma frase: '))
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra aparece na pocicao {}'.informat(frase.find('A')+1))
print('A ultima palavra letra A aparece opocicao {}'.format(frase.rfind('A')+1))
# curso de desenvolvimento de sistemas
# turma 0152 (braba)
# autor: Beatriz Victoria
# data:26/04/2024
# atividade002

# importando as bibliotecas
import os 


# limpantando o terminal 
os.system('cls')

print('-'*70)
print('verificação de anos bissestos')
print('='*70)

# entrada de dados 
ano = int(input)('informe um ano')

# condicional
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    resposta = f'o ano {ano} e bissexto'
else:
    resposta = f'o ano {ano} nao e bissexto'
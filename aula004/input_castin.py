# imports
# biblioteca para interagir o SO
import os
# biblioteca para pegar data e hora do sistema
import datetime


# limpar o terminal
os.system('cls')

print('-'*70)
print('entrada de dados em python')
print('='*70)

# entrada
nome = input('entre com um nome: ')
peso = input('entre com o peso: ')
altura = input('entre com a altura: ')

# entrada com casting
nascimento = int(input('data de nascimento: '))
cep = int(input('entre com o seu cpf: '))
bairro = str(input('entre com o bairro: '))
rua = str(input('entre com a rua: '))
numero = int(input('entre com o numero: '))

# processamento: pegando o ano correte
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento 

# saida 
print('-'*70)
print('saida de dados')
print('='*70)
print('nome..........: ', nome)
print('data de nascimento: ', nome)
print('peso...........: ', peso)
print('altura........: ', altura)

# saida interpolada
print(f'{nome}, voce tem {idade} anos!')
print(f'cep..........:{cep}')
print(f'bairro.........: {bairro}')
print(f'rua..........: {rua}')
print(f'numero..........: {numero} ')
print('-'*70)
print('')


      
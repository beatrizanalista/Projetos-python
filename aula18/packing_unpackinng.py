import os


os.system('cls')

# definindo uma função para empacotar
def empacotar(*lista_numeros):
    print(f'Empacoatados: {lista_numeros}')
    for i in lista_numeros:
        print(f'Empacotado: {i}')
        
# invocando a função empacotar
empacotar(1, 2, 3, 4, 5)

# Desempacotando (lista)
def desempacotar(a, b, c, d, e):
    print('desempacotar:')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')
    print(f'e = {e}')
    
    # invocando a função desempacotar
    lista_numeros = [1, 2, 3, 4, 5,] # lista
    desempacotar(*lista_numeros) # * args
    
# Packing dicionario
def empacotar_dicionario(**dados_dicionario): # **kwargs
    print(f'dados do dicionario: {dados_dicionario}')
    for k, v in dados_dicionario.items():
        print(f'chave: {k}, valor: {v}')
        
print('-'*70)
print('---Dicionario')
empacotar_dicionario(nome = 'juquinha', idade = 70, peso = 70.5)

# unpacking dicionario
print('-'*70)
def desempacotar_dicionario(nome, idade, peso):
    print(f'nome = {nome}')
    print(f'idade = {idade}')
    print(peso = {peso})
    
dicionario = dict(nome = 'Maria', idade = 70,peso = 70.5)
desempacotar_dicionario(**dicionario)
print()
import csv
import os


# nome do arquivo cvs
arquivo = "arquivos_cvs/gravacao/alunas.csv"

# Lista para armazenar os dados
lista = []

# Abrindo o arquivo cvs para leitura
with open(arquivo, 'r') as arquivo_cvs:
    # criando um leitor de cvs que lê o arquivo como dicionario
    leitura = csv.DictReader(arquivo_cvs, delimiter=';')
    
    # iterado sobre cada linha (registrado) no arquivo cvs dicionario a lista
    for linha in leitura:
        lista.append(linha)
        
        os.system('cls')
print('-'*70)
print('nome\ttelefone\tcidade')
print('='*70)
# exibindo a lista resultante
for resgistro in lista:
    flag = 0
    for k, v in registro.items(): # type: ignore
        print(v, end='\t')
        flag += 1
        if flag == 3:
            print()
print('-'*70)
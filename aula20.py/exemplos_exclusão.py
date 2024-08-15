import csv
import os


os.system('cls')

arquivo = 'arquivos_csv/gravacao/alunas.csv'
nome_para_apagar = input("digite o nome que deseja apagar:")

# lemdo os dados do arquivo
with open(arquivo, 'r') as arquivo_csv: 
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)
    
# verificando se o nome existe e apagando o registro
apagado = False
novo_cadastro = [registro for registro in cadastro /]
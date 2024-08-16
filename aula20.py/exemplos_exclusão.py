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
novo_cadastro = [registro for registro in cadastro \
                 if registro['nome'] != nome_para_apagar]

if len(novo_cadastro) < len(cadastro):
    apagado = True
    
# Reescreva o arquivo com os dados atualizados
with open(arquivo, 'w', newline='') as arquivo_csv:
    campos = ['nome', 'telefone', 'cidade']
    escever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    escever.writeheader()
    escever.writerows(novo_cadastro)
print('-'*70)
if apagado:
    print(f"registro com nome {nome_para_apagar} apagado com sucesso")
else:
    print(f"registro com nome {nome_para_apagar} nao encontrado")
print('-'*70)
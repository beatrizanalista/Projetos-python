import csv
import os

os.system('cls')

arquivo = 'arquivos_csv/gravacao/alunas.csv'
nome_para_apagar = input("nome para excluir: ")

# lendo os dados do arquivo
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)
    
# flag
apagado = False

# varrendo os registros para remover o nome escolhido
i = 0
while i < len(cadastro):
    if cadastro[i]['nome'] == nome_para_apagar:
        del cadastro[i]
        apagado = True
    else:
        i += 1
        
# Reescreva o arquivo com os dados atualizados
with open(arquivo, 'w', newline='') as arquivo_csv:
    campos = ['nome', 'telefone', 'cidade']
    escrever = csv.DictWriter(arquivo_csv,
                              fieldnames=campos, delimiter=';')
    
    escrever.writeheader()
    escrever.writerows(cadastro)
    
print('-'*70)
if apagado:
    print(f"Registro com nome {nome_para_apagar} apagado com sucesso")
else:
    print(f"Registro com nome {nome_para_apagar} não encontrado")
print('-'*70)
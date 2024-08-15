# import a biblioteca csv
import csv
import os


# criando uma lista de dicionarios: cada dicionario é uma linha (registro)
lista = [
    {'nome':'Agata', 'telefone': '(32)99196-0000', 'cidade':'Juiz de fora'},
    {'nome':'Bia', 'telefone': '(32)99196-1111', 'cidade':'Juiz de fora'},
    {'nome':'Coly', 'telefone': '(32)99196-2222', 'cidade':'Juiz de fora'},
    {'nome':'isis', 'telefone': '(32)99196-3333', 'cidade':'Juiz de fora'},
]

# caminho para a pasta onde o arquivo csv será salvo
pasta = 'arquivos_csv/gravacao/'

# verificando se a pasta onde o arquivo csv será salvo
os.makedirs(pasta, exist_ok=True)

# nome para o arquivo cvs para gravar as informações
arquivo = 'arquivos_cvs/gravacao/alunos.csv'

# caminho completo do arquivo cvs
caminho_arquivo = os.path.jonh(pasta, arquivo)

# abre o arquivo 'arquivo' no modo de escrita('w')
# se o arquivo não existir,ele será criado; se existir, será trucado (esvaziado)
# newline='': evita a adicao de linhas em branco extras ao gravar o arquivo em algumas plataformas
# as arquivo_csv: atribui o objeto arquivo ao 'arquivo_csv' para ser usado dentro do bloco with
with open(arquivo, 'w', newline='') as arquivo_csv:
    
    # campos = ["name", "telefone", "cidade"]: define a lista de nomes de campos
    # (cabeçalhos das colunas do cvs)
    campos = ['nome', 'telefone', 'cidade']
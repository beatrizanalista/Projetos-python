# import as bibliotecas
import os
# podemos importar so as funcoes que queremos utilizar
from datetime import datetime
from datetime import date


# limpando o terminal
os.system('cls')

# declarando uma variavel para data
data = datetime.now()

# declarando uma variavel data formatada
data_formatada = data.strftime('%d/%m/%y')

# declaracao uma variavel data e hora formatada
data_hora_formatado = data.strftime('%d/%m/%Y %H:%M')

print(f'data formatada: {data_formatada}')
print(f'data e hora formatadas: {data_hora_formatado}')

# recebendo o ano 
data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

# imprimindo a data atual e o nascimento
print('-'*70)
print(f'data atual no sistema: {data_atual}')

import os


os.system('cls')

# inicializada uma lista vazia
lista_numeros = []

# pede ao usuario para inserir tres numeros
for i in range(3):
    numero = int(input("digite um numero: "))
    
    # adiciona o numero a lista
    lista_numeros.append(numero)
    
# verifica se o numero inserido esta na lista e
# exibe uma mensagem correspondente
numero_verificar = int(input("digite um numero: "))

if numero_verificar in lista_numeros:
    print(f"o numero {numero_verificar} esta na lista!")
else:
    print(f"o numero {numero_verificar} nao esta na lista.")
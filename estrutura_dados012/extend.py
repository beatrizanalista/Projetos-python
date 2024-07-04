import os


os.system('cls')

# inicializa a lista vazia
lista_numeros = []

# solicita ao usuario para inserir numeros separados por espaço
entrada = input("digite numeros separados por espaço: ")

# divide a string de entrada em uma lista de strings
numeros = entrada.split()

# cria uma lista para armazenar os numeros pares
pares = []

# itera sobre os numeros inseridos
for numero in numeros:
    # converte a string para inteiro
    numero_aux = int(numero)
    # verifica se o numero e par
    if numero_aux % 2 == 0:
        # adiciona o numero par a lista de pares
        pares.append(numero_aux)
        
# usa extend() para adicionar todos os numeros pares a lista principal
lista_numeros.extend(pares)

# exibe a lista resultante
print(f"numeros pares adicionados a lista:{lista_numeros}")
    
    
import os


os.system('cls')

# solicita ao usuario para inserir numeros separados por espaco
entrada = input("digite numeros separados por espaco:")

# divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
    
# solicita ao usuario para inserir o numero que deseja contar na lista
numero_para_contar = int(input("digite o numero que deseja contar: "))

# conta o numero de vezes que o numero fornecido aparece na lista
contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f"o numero {numero_para_contar} aparece {contagem} vezes na lista")
else: 
    print(f"o numero {numero_para_contar} nao aparece na lista.")
    
# exiba a lista fornecida para referencia
print(f"lista fornecida: {numeros}")
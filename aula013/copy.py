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
    
# solicita ao usuario para decidir se deseja
# criar uma copia da lista
escolha = input("deseja criar uma copia? (s/n): ").strip().lower()

# verifica a escolha do usuario e cria uma copia da
#  lista se a resposta for 's'
if escolha == 's':
    lista_copiada = numeros.copy()
    print(f"copia da lista: {lista_copiada}")
else:
    print("a lista nao foi copiada.")
    
# exibe a lista fornecida para referencia
print(f"lista fornecida: {numeros}")
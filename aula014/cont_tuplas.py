# solicitar ao usuário a quantidade de elementos da tupla
import os


os.system('cls')

# solicitar ao usuário a quantidade de elementos na tupla
numero_elementos = int(input("Quantos elementos na tupla?"))

# Iniciar uma lista vazia para armazenar os elementos
elementos = []

# Estrutura de repetição para obter os elementos do usuário
for i in range(numero_elementos):
    while True:
        valor = input(f"digite o valor {i + 1}: ")
        if valor.isdigit(): # verifica se a entrada é um número
            elementos.append(int(valor))
            break
        else:
            print("Entrada invalida. Digite um número")
            
# converter a lista para uma tupla
tupla = tuple(elementos)

print('-'*70)
# exibir a tupla criada
print(f"Tupla criada: {tupla}")
print('-'*70)

# Estrutura de repetição para permitir múltiplas
# operações até que o usuário deseje sair
while True:
    # conticional para verificar a presença de
    # um numero especifico
    valor = int(input("verificar se o número na tupla: "))
    
    if valor in tupla:
        print(f"O número {valor} está na tupla.")
        # contar quantas vezes o número aparece
        
        contagem = tupla.count(valor)
        print(f"O número {valor} aparece {contagem} vez(es).")
        # Encontrar o índice da primeira ocorrência
        
        indice = tupla.index(valor)
        print(f"A 1ª ocorrência de {valor} está no índice {indice}")
        
    else:
        print(f"O número {valor} não está na tupla.")
        
    # perguntar ao usuario se deseja realizar
    # outra operação ou sair
    continuar = input("deseja continuar? (s/n):").lower()
    if continuar != 's':
        print("Encerrando o programa. Ate mais!")
        break
print('-'*70)
print('fim do programa!')
print()
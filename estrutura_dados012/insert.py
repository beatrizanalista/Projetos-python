import os


os.system('cls')

# lista original
lista = [1, 2, 3, 4]

# pedindo ao usuario para fornecer a
# posição e o elemento a ser inserido
posicao = int(input("posicao onde deseja inserir o elemento: "))
elemento = input("elemento a ser inserido: ")

# verificando se a posicao fornecida pelo usuario e valida
if posicao >= 0 and posicao <= len(lista):
    # inserindo o elemento na lista na posicao especifica pelo usuario
    lista.insert(posicao,elemento)
    print("lista apos a insercao:", lista)
else:
    print(f"posicao fora do intervalo 0, {len(lista)}")
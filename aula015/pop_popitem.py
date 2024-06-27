import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print("\nMenu de opçaoes:")
    print("1. Adicionar um par chave-valor")
    print("2. Remover um item usando pop()")
    print("3. Remover o último item usando popitem()")
    print("4. Mostrar dicionario atual")
    print("5. sair")
    print('-'*70)
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        # Adicionar um par chave-valor ao dicionario
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        meu_dicionario[chave] = valor
        print(f"par {chave}: {valor} adicionado.")
        
    elif opcao == '2':
        # remover um item especifico usando pop()
        if meu_dicionario:
            chave = input("Digite a chave do item que deseja remover:")
            valor_removido = meu_dicionario.pop(chave, "chave não encontrada")
            print(f"item removido: {chave}: {valor_removido}")
        else:
            print("o dicionário está vazio. Adicione itens primeiro.")
            
    elif opcao == '3':
        # Remover o último item usando popitem()
        if meu_dicionario:
            chave, valor = meu_dicionario.popitem()
            print(f"ultimo item removido: {chave}: {valor}")
        else:
            print("o dicionario está vazio. Adicionario itens primeiro.")
            
    elif opcao == '4':
        # Mostrar o dicionario atual
        if meu_dicionario:
            print("Dicionario atual:", meu_dicionario)
        else:
            print("Dicionario está vazio.")
            
    elif opcao == '5':
        print("saindo do programa.")
        break
    
    else:
        print("opção invalida. Tente novamente.")
import os


os.system('cls')
# Criação do dicionario vazio
meu_diciorio = {}

while True:
    print('-'*70)
    # exibição do menu de opções
    print("\nMenu de opções:")
    print("1. Adicionar um par chave-valor")
    print("2. Mostrar o dicionario")
    print("3. Mostrar o tamanho do dicionario")
    print("4. Fazer uma cópia do dicionario")
    print("5. limpar o dicionario")
    print("6. Sair")
    print('-'*70)
    
    # solicitação da escolha do usuário
    opcao = input("Escolha uma opção (1-6): ")
    
    if opcao == '1':
        # Adiciona um novo par chave-valor ao dicionário
        chave = input("digite a chave: ")
        valor = input("Digite o valor: ")
        meu_diciorio[chave] = valor
        print(f"Par {chave}: {valor} adicionado.")
        
    elif opcao == '2':
        # Exibe o dicionario atual
        print("Dicionario atual:", meu_diciorio)
        
    elif opcao == '3':
        # Mostrar o tamanho do dicionario usando len()
        tamanho = len(meu_diciorio)
        print(f"O dicionario tem {tamanho} elementos.")
        
    elif opcao == '4':
        # Cria uma cópia do dicionário usando copy() e exibe a cópia
        copia_dicionario = meu_diciorio.copy()
        print("Copia do dicionario:", copia_dicionario)
        
    elif opcao == '5':
        # Limpa o dicionario usndo clear()
        meu_diciorio.clear()
        print("Dicionario limpo.")
        
    elif opcao == '6':
        # sai do programa
        print("Saida do programa.")
        break
    
    else:
        # Mensagem para opção invalida
        print("opção invalida. Tente novamente.")
import os


os.system('cls')

meu_dicionario = None

# loop principal do programa
while True:
    print('-'*70)
    print("\nMenu de opçãoes:")
    print("1. Criar dicionario com fromkeys()")
    print("2. Buscar valor de uma chave com get()")
    print("3. sair")
    print('-'*70)
    
    opcao = input("Escolha uma opção (1-3): ")
    
    if opcao == '1':
        # Criação de um dicionario usando fromkeys()
        chaves = input("Digite as chaves separadas por vircula: ").split(',')
        valor_padrao = input("Digite o valor padrão para as chaves:")
        meu_dicionario = dict.fromkeys(chaves, valor_padrao)
        print("Dicionario criado:", meu_dicionario)
        
    elif opcao == '2': 
        # Verifica se o dicionário foi criado antes de tentar acessá-lo
        if meu_dicionario is not None:
            chave = input("Digite a chave que deseja buscar: ")
            valor = meu_dicionario.get(chave, "chave nao encontrada")
            print(f"valor para a chave '{chave}': {valor}")
        else:
            print("Erro! crie um dicionario.")
            
    elif opcao == '3':
        print("saindo do programa.")
        break
    
    else:
        print("Opção invalida. Tente novamente.")  
            
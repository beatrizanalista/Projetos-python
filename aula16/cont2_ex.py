import os


os.system('cls')


print('-'*70)
print('-------- TABELA PERIIÓDICA -----')
print('='*70)

# Inicialização do dicionario e da lista
elementos = {} # Dicioanrio
periodica = [] # Lista

while True:
    os.system('cls')
    
    # cabeçalho do menu
    print('-'*70)
    print('Menu de opções:')
    print('='*70)
    print('1. Adicioanr um elemento')
    print('2. visualizar todos os elementos')
    print('3. Atualizar um elemento')
    print('4. Remover um elemento')
    print('5. sair')
    print('-'*70)
    
    # solicitação da escolha do usuário
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        # Adicionar um elemento
        simbolo = str(input('simbolo do elemento: '))
        nome = str(input('Nome do elemento: '))
        elementos['simbolo'] = simbolo
        elementos['nome'] = nome
        periodica.append(elementos.copy())
        input("\nElemento adicionado. Pressione enter para continuar...")
        
    elif opcao == '2':
        # visualizar todos os elementos
        print("\nElementos no tabela periódica:")
        print('-'*70)
        for elementos in periodica:
            for chave, valor in elemento.items():
                print(f'{chave.capitalize()}: {valor}')
            print('-'*70)
        input("\nPressione enter para continuar...")
        
    elif opcao == '3':
        # Atualizar um elemento 
        simbolo = str(input('Digite o simbolo do elemento para atualizar: '))
        # Inicializada a flag como False
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input(f'Digite o novo simbolo para'
                f' {simbolo} (ou deixe em branco para manter o atual): '))
                novo_nome = str(input(f'Digite o novo nome para'
                f' {nome} (ou deixe em branco para manter  o atual): '))
                
                # Atualiza o simbolo e o nome se fornecidos
                if novo_simbolo:
                    elemento['simbolo'] = novo_simbolo
                if novo_nome:
                    elemento['nome'] = novo_nome
                # Define a flag como True quando o elemento é encontrado
                encontrado = True
                break
            
        if encontrado:
            input("\nElemento atualizado. Enter para continuar...")
        else:
            input("\nElemento não encontrado. Enter para continuar...")
            
    elif opcao == '4':
        # Remover um elemento
        simbolo = str(
            input('Digite o simbolo do elemento que deseja remover: '))
        encontrado = False # Inicializa a flag como false   
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                periodica.remove(elemento)
                # Define a flag como True quando o elemento é encontrado
                encontrado = True
                break
            if encontrado:
                input("\nElemento removido. Enter para continuar...")  
            else:
                input("\nElemento não encontrado. Enter para continuar...")  
    
    elif opcao == '5':
        print("saindo do programa.")
        break
    
    else:
        input("opção invalida. Enter para tentar novamente...")            
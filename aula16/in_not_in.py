import os


# inicialização do dicionário de contatos
agenda = {
    'jojo': '99196-3030',
    'Dio': '99196-5050',
    'Jolyne': '99196-6060',
    'Lisa Lisa': '99196-7070',
    'Speedwagon': '99196-8080',
    'Zeppeli': '99196-9090',
    'Suzie Q': '99196-0000'
}

while True:
    os.system('cls')
    
    print('-'*70)
    print("\nAgenda de contatos:")
    for nome, telefone in agenda.items():
        print(f"{nome}: {telefone}")
    print('='*70)
    
    # Primeiro teste: verificar se 'Jojo' está no dicionario
    if 'jojo' in agenda:
        print('Primeiro teste: verificar se jojo está no dicionario')
        print('verdadeiro! jojo está no dicionario')
    else:
        print('Falso! jojo não está no dicionario')
        
    print()
    
    # Segundo teste: verificar se 'John' não está no dicionario
    if 'jonh' not in agenda:
        print('Segundo teste: verificando se Jonh não está no dicionario')
        print('verdadeiro! jonh não está no dicionario')
    else:
        print('Falso! Jonh não está no dicionario')
        
    print('-'*70)
    print()
    
    print('-'*70)
    print("Menu de opções:")
    print("1. Adicionar um contato")
    print("2. Remover um contato")
    print("3. Verificar contato especifico")
    print("4. Mostrar agenda")
    print("5. sair")
    print('-'*70)
    
    opcao = input("Escolha uma opção (1-5)")
    
    if opcao == '1':
        # Adicionar um contato
        nome = input("Digite o nome de contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print(f"contato {nome}: {telefone} adicionado.")
        
    elif opcao == '2':
        # remover um contato
        nome = input("Digite o nome do contato que deseja remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"contato {nome} removido.")
        else:
            print(f"contato {nome} não encontrado na agenda.")
            
    elif opcao == '3':
        # verificar contato especifico
        nome = input("Digite o nome do contato que deseja verificar: ")
        if nome in agenda:
            print(f"Contato encontrado - {nome}: {agenda[nome]}")
        else:
            print(f"contato {nome} não encontrado na agenda.")
            
    elif opcao == '4':
        # Mostrar agenda atual
        print("\nAgenda de contatos:")
        print(agenda)
        
    elif opcao == '5':
        print("saindo do programa.")
        break
    
    else:
        print("opção invalida. tente novamente.")
        
    # Pausa para o usuario ver as mensagens antes
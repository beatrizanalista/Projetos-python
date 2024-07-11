# Fenindo funções

def limpa_tela():
    """função para limpar o terminal
    """
    import os
    os.system('cls')
    
    
def soma(a,b):
    """Função para somar 2 números
    
    Args:
        a (int): valor de a
        b (int): valor de b
        
    Returns:
       Retorna a soma de 2 números
    """
    return a + b


def firula():
    print('-'*70)
    
# programa principal


# chamando a função
limpa_tela()
firula()
resposta = soma(1,2)
print(f'A soma dos 2 números é: {resposta}')
firula()
print()

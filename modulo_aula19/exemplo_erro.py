try:
    # código que pode gerar várias exceções
    resultado = 10 / 0
    arquivo = open('arquivo_inexistente.txt','r')
except Exception:
    # Captura todas as exceções, mas não faz nada com elas
    pass

print("continua a execução do programa.")
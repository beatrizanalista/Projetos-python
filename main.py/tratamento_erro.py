try:
    resultado = 10 / 0
expecept ZeroDivisionError:
    print("erro: Divisao realizada com sucesso!")
finally:
    print("este bloco e sempre executado.")
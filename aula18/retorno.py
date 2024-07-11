import os


os.system('cls')


# Definindo uma função
def calcular_velocidade_media(distancia, tempo):
    # Vm = ∆S/ ∆t 
    velocidade__media = distancia / tempo
    return velocidade__media

distancia = float(input("Digite a distâcia percorrida (em km): "))
tempo = float(input("Digite o tempo gasto (em horas): "))

# Calcular a velocidade média usando a função criada
velocidade = calcular_velocidade_media(distancia, tempo)

# Exibir o resuldado
print(f"A velocidade média é {velocidade:.2f} km/h.")   
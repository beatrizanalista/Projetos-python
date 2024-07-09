# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 31/06/2024
# atividade 004
#Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. Caso a letra seja o “f" finalize a aplicação. Do contrário,
#imprima novamente a mesma frase até que o caractere “f" seja digitado.

while True:

        entrada = input("Digite uma letra (ou 'sair' para finalizar): ").strip().lower()
        
        if entrada == "sair":
            print("Finalizando a aplicação.")
            break
        elif len(entrada) != 1 or not entrada.isalpha():
            print("Entrada errada. Por favor, digite apenas uma letra.")
            continue
        
        if entrada == 'f':
            print("essa e a letra certa!.")
            break
        else:
            continue # Caso contrário, continua o loop











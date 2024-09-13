# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os 

os.system('cls')


class Algoritmo:
    def impresso_looping(self):
        pass


class Imprima(Algoritmo):
    def impresso_looping(self):
        frase = ''
        while(frase != 'f' and frase != 'F'):
            print('estou em looping!')
            frase = input('Digite uma letra:')
        print()

inexistente = Imprima()
inexistente.impresso_looping()

print('-'*70)
print('fim do programa!')
print()
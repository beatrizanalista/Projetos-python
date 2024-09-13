# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
<<<<<<< HEAD
# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.
=======
# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. 
# Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" 
# seja digitado.
>>>>>>> b14275db405aab2d44d747e0344dcd5d696a129a

import os 

os.system('cls')


class Algoritmo:
<<<<<<< HEAD
=======
    def __init__(self, inicio, fim ):
        self.inicio = inicio
        self.fim = fim

>>>>>>> b14275db405aab2d44d747e0344dcd5d696a129a
    def impresso_looping(self):
        pass


class Imprima(Algoritmo):
<<<<<<< HEAD
=======
    def __init__(self, inicio, fim):
         self.inicio = inicio
         self.fim = fim

>>>>>>> b14275db405aab2d44d747e0344dcd5d696a129a
    def impresso_looping(self):
        frase = ''
        while(frase != 'f' and frase != 'F'):
            print('estou em looping!')
<<<<<<< HEAD
            frase = input('Digite uma letra:')
        print()

inexistente = Imprima()
inexistente.impresso_looping()
=======
        print()

Imprima.impresso_looping()

>>>>>>> b14275db405aab2d44d747e0344dcd5d696a129a

print('-'*70)
print('fim do programa!')
print()
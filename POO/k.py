# curso de desenvolvimento de sistemas
# turma 0152
# autor:Beatriz Victoria
# data: 06/09/2024
# Crie um programa que pede que o usuário digite um nome ou uma frase,
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

import os


os.system('cls')


class Nome:
    def __init__(self, frase):
        self.frase = frase

    def palindromo_verifica(self):
        pass


class Conteudo(Nome):
    def __init__(self, frase):
        self.frase = frase

    def palindromo_verifica(self):
        # frase = ''
            frase_normal = frase.replace(' ', '')
            invertido = frase_normal[:: -1]
            
            if (frase_normal == invertido):
                print(f' {frase} é um palíndromo')
            else:
                print(f'{frase} não é um palíndromo')
frase = input('digite uma palavra:')
aleatorio = Conteudo(frase)
aleatorio.palindromo_verifica()

print('-'*70)
print('fim do programa!')
print()

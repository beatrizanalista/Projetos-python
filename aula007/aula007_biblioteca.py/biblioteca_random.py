import random
import os


os.system('cls')

print('-'*70)
print('biblioteca random')
print('='*70)

print('numero aleatorio')
nemero_aleatorio = random.random()
print(f'o numero gerado foi: {nemero_aleatorio}')
print('.'*70)

print('numero aleatorio interio')
aleatorio_inteiro = random.randint(1, 20)
print(f'o numero inteiro gerado foi: {aleatorio_inteiro}')
print('-'*70)

print('numero aleatorio decimal no intervalo')
aleatorio_decimal = random.uniform(1, 10)
print(f'o numero decimal gerado foi: {aleatorio_decimal}')
print('.'*70)

print('sorteio em lista')
lista = ['Ágata','Coly', 'Isis', 'Bia']
nome_sorteio = random.choice(lista)
print(f'lista: {lista}')
print(f'o nome escolhido foi: {nome_sorteio}')
print('.'*70)

print('embaralhar sequencia')
lista2 = ['Ágata','Coly','Isis','Bia'] 
print(f'lista antiga:{lista2}')
# embaralhado = list(random.shuffle(lista)) da erro
#embaralhado = random.shuffle(lista) saida vazia
random.shuffle(lista2)
print(f'lista nova: {lista2}')
print('.'*70)

print('retorno de elementos unicos de uma populacao')
numeros = [1,2,3,4,5,6,7]
amostra_aleatoria = random.sample(numeros, 5)
print(f'retorna da amostragem: {amostra_aleatoria}')
print('.'*70)
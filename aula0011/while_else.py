import os


os.system('cls')

print('-'*70)
print('estrutura de controle while else')
print('='*70)
print()

print()

contador = 1

while contador < 7:
    print("contador e:", contador)
    contador += 1
    
    # se eu tirar essa condicional o else sera executado
    if contador == 4:
        print(f'conatdor chegou em {contador}. break no while!')
        break
else:
        print("while finalizado!")
        
print()
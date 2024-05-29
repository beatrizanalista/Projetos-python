import os


os.system('cls')

print('-'*50)
print('estrutura de controle validacao e casting')
print('='*50)

soma = 0

for c in range(0, 5):
    
    numero = input('digite um numero [0-5]: ')
    
    #  validacao
    if (not (numero.isnumeric())):
        print(f'"{numero}"entrada invalida!')
        print()
    else:
        #  casting da variavel, ou seja, vai virar um inteiro
        numero = int(numero)
        
        # validando o intervalo pedido
        if (numero >= 0 and numero <= 5):
            print(f'o numero {numero} esta dentro do intervalo [0-5]!')
            print()
        else:
            print(f'"{numero}" entrada invalida!')
            print()
            
print('-'*70)
print()
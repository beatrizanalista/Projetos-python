import os


os.system('cls')

print('-'*70)
print('operadores uteis para')
print('strings e estruturas de dados')
print('='*70)

texto = "ola, mundo!"

print(f'texto: {texto}')
if "mundo" in texto: # verifica a palavra dentro da string
    print('a palavra "mundo" esta presente na string.')
else:
    print('a palavra "mundo" nao esta presente na string.')

    print('.'*70)

    texto2 = "ola, python!"

    print(f'texto: {texto2}')
    if "mundo" not in texto2: # verifica a palavra dentro da string
        print('a palavra "mundo" nao esta presente na  string.')
    else:
        print('a palavra "mundo" esta presente na string.')

        print('.'*70)
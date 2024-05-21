import os


os.system('cls')

print('-'*70)
print('fatiamento de strings')
print('='*70)

frase = 'string em python!'

# exibindo a string original
print(f"string original: {frase}")

# fatiamento: acessando partes especificas da string
# primeiro cinco caracteres
primeiro_cinco = frases[:5]
print(f"primeiros cinco caracteres: {primeiro_cinco}")

# ultimos dez caracteres
ultimos_dez = frase[-10:]
print(f"ultimos dez caracteres: {ultimos_dez}")

# do quarto ao decimo caractere
quarto_ao_decimo = frase[3;10]
print(f"do quarto ao decimo caractere: {quarto_ao_decimo}")

# a cada dois caracteres
a_cada_dois = frase[::2]
print(f'a cada dois caracteres: {a_cada_dois}')

# invertendo a strig
invertida = frase[::-1]
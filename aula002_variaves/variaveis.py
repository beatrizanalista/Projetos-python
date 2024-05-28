# importando a biblioteca de sistema
import os


# limpando o terminal
os.system('cls')

print('-'*70) # firula
print('estudo de variaveis')
print('='*70) # firula

#As variaveis sao declaradas por inferencia
nome ='john doe'
nascimento = 1970
altura = 1.80
peso = 75.5
doador = True
complexo = 3j # python trabalha diretamente com numeros complexos
pi = 3.4 # isso e uma CONSTANTE, seu valor nao deve ser alterado

# saida utilizando o metodo type() para verificar o 
#tipo de variavel
print('\033[31mtipos declarados:\033[0m')
print('\033[0m a var \033[32m nome \033[0m e do tipo: ', type(nome))
print('\033[0m A var \033[32m nascimento \033[0m e do tipo:', type(nascimento))
print('\033[0m A var \033[32m altura \0330m e do tipo: ', type(altura))
print('\033[0m A var \033[32m peso \033[0m e do tipo: ', type(peso))
print('\033[0m A var \033[32m doador \033[0m e do tipo: ', type(doador))
print('\033[0m A var \033[32m complexo \033[0m e do tipo: ',type(complexo))
print('\033[0m A var \033{32m pl \033[0me do tipo: ', type(pi))
print('-'*70)
print('')
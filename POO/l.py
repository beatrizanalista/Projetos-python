# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 06/09/2024
# Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake)
# . O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço

import os


os.system('cls')

usuario_fk = 'usuário'
senha_fk = '123456b'
 
usuario = str(input('digite o nome do usuario: '))
senha = str(input('digite a senha: '))

while True:
    if usuario != usuario_fk or senha != senha_fk:
        usuario = str(input('entre com o usuario:')).loweer()
        senha = str(input('entre com a senha:'))
    else:
        break
    print('verificando ...')

    print('-'*70)
    print('fim do programa!')
    print()
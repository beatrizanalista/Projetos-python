<<<<<<< HEAD
# curso de desenvolvimento de sistemas
# turma 0152 
# autor:Beatriz Victoria
# data: 14/06/2024
# Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor
=======
# curso de desenvolvimento de sistema
# autor:beatriz victoria
# data:16/06/2024
# atividade007

notas  = []
rng  =  0

while  rng  >=  0:
    rng =  float ( input ( "Informe a nota do estudante:" ))

    if  rng <  0 :
        break
    else:
        notas.append( rng )

print()

print ( f"Quantidade de notas lidas: { len ( notas ) } " )   
print ( notas )   
notas . reverse ()   
print ( notas )  
print ( f"A soma de todas as notas e: { sum ( notas ) } " )   
media  =  sum ( notas ) /  len ( notas )   
print ( f"A media das notas e: { media } " )   
print ()
for  range in  notas :   
    if range  >  media :
     print ( "Nota maior que a media:" ,range )
>>>>>>> 3f7ab61e6fcadc15efdfffa8a5ead092080d9d2e

# Trabalho sobre a estrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno:Beatriz Victoria
# Turma: 0152
# Ano: 2024

# (Issubset)-Verifica se o set é um subconjunto de outro set.

# iniciando 
import os


os.system('cls')

print('-'*70)
print('utilizando o issubset ')
print('='*70)

# iniciando um set com elementos  # fruts

set1 = {"banana", "manga", "abacaxi", "laranja", "morango", "goiaba"}
set2 = {"manga", "goiaba",  "uva"}

print(set1.issubset(set2))
print(set1 < set2)
print(set1 <= set2) 
print(set2.issubset(set1))




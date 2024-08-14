# zeroDivisionError
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("erro: Divisão por zero!")
    
# ValueError
try:
    numero = int("não é um número")
except ValueError:
    print("Erro: valor invalido!")
    
# TypeError
try:
    soma = '5' + 5
except TypeError:
    print("Erro: tipo de dado incompativel!")
    
# IndexError
lista = [1 , 2, 3]
try:
    item = lista[5]
except IndexError:
    print("erro: indice fora do intervalo dalista!")
    
# keyError
dicionario = {'chave': 'valor'}
try:
    valor = dicionario['chave_inexistente']
except KeyError:
    print("erro: chave não encontrada no diciónario!")
    
# FileNotfoundError
try:
    with open('arquivo_inexistente.txt', 'r')as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("erro: arquivo não encontrado!")
    
# Ioerror
try:
    with open('arquivo.txt','w')as arquivo:
        conteudo = arquivo.read()
except IoError:
    print("Erro: operacao de E/s falhou!")
    
# AttributeError
class exemplo:
    def_init_(self):
        self.atributo = "valor"
        
objetivo = exemplo()
try:
    # print
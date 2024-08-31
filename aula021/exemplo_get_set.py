import os
import math


class equacao:
    def _init_(self, a=1, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c
        
    # Getters
    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b
    
    def get_c(self):
        return self._c
    
    # Setters
    def set_a(selt, value):
        self_a = value 
        
    def set_b(selt, value):
        self_b = value
        
    def set_c(selt, value):
        self_c = value
        
    def calcular_raizes(self):
        
        # calculando o delta
        delta = self._b ** 2 - 4 * self._c
        
        if delta < 0:
            return 'A equação não possui raizes reais. '
        elif delta == 0:
            raiz = -self._b / (2 * self._a)
            return f'A equacao possui uma raiz real: {raiz}'
        else:
            x1 = (-self._b + math.sqrt(delta)) / (2 * self._a)
            x2 = (-self._b - math.sqrt(delta)) / (2 * self._a)
            return f'A equação possui duas raizes reais: {x1} e {x2}'
        
os.system('cls')

print('-'*70)
print('calculo de equação do 2 grau')
print('='*70)
equacao1 = equacao(1, -3, 2)
print(equacao1.calcular_raizes())

print('-*70')
print('calculo de equacao do 2 grau')
equacao1.set_a(1)
equacao1.set_b(2)
equacao1.set_c(1)
print(equacao1.calcular_raizes())
print('-'*70)
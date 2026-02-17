# Usando teorema de pitagoras
from math import hypot
co = float(input('Informe o comprimento do cateto oposto:'))
ca = float(input('Informe o comprimento do cateto adjacente:'))
hip = hypot(co, ca)
print(f'A hipotenusa vai medir {hip:.2f}')

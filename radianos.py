#  calculo Angulo de cosseno,tangente e seno (180°⊓ radianos)

import math

# lê o calculo em graus
angulo = float(input('Digite um angulo em graus:'))

#converte graus para radianos
rad = math.radians(angulo)

# calcula seno, cosseno e tangente
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

# mostra os resultados
print(f'\33[32m Seno de {angulo}° = {seno:.4f}\33[0m')
print(f'\33[32mCosseno de {angulo}° = {cosseno:.4f}[0m')
print(f'\33[32mTangente de {angulo}° = {tangente:.4f}[0m')
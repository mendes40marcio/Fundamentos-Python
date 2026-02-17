import random

numero_secreto = random.randint(1,10)
tentativas = 0
acertou = False
print('Vou pensar em um numero entre 1,10.')

while not acertou:
    palpite = int(input('Tente adivinhar:'))
    tentativas+= 1
    if palpite == numero_secreto:
        acertou = True
        print(f'Parabens voce acertou em {tentativas} tentativas.')
    elif palpite < numero_secreto:
        print('Mais....tente um numero maior')
    else:
        print('Menos...tente um numero menor')
    # FIM DO PROGRAMA PYTHON


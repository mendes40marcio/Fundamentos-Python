import random

numero_secreto = random.randint(1, 10)
tentativas = 0
limite = 3
acertou = False

print('Vou pensar em um número entre 1 e 10.')
print(f'Você tem {limite} tentativas.')

while tentativas < limite and not acertou:
    palpite = int(input('Tente adivinhar: '))
    tentativas += 1

    if palpite == numero_secreto:
        acertou = True
        print(f'Parabéns! Você acertou em {tentativas} tentativas.')
    elif palpite < numero_secreto:
        print('Mais... tente um número maior.')
    else:
        print('Menos... tente um número menor.')

if not acertou:
    print(f'Que pena! O número era {numero_secreto}.')

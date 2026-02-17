import random

numero_secreto = random.randint(0,5)

palpite_usuario = int(input('Digite um numero entre 0,5:'))

if palpite_usuario == numero_secreto:
    print('\033[1;92m Parabéns!🎉 voce acertou\33[0m')
else:
    print(' \033[1;91m Infelizmente voce errou!😞 boa sorte na proxima vez\33[0m')


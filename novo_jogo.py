import random

numero_secreto = random.randint(0, 5)
tentativas = 3

while tentativas > 0:
    usuario = int(input('Informe um número de 0 a 5: '))

    if usuario == numero_secreto:
        print('Parabéns! 🎉 Você acertou!')
        break
    else:
        tentativas -= 1
        print(f'Você errou 😞 | Tentativas restantes: {tentativas}')

if tentativas == 0:
    print(f'Fim de jogo! O número era {numero_secreto} 😎')

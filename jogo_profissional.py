import random

print('=== JOGO DA ADIVINHAÇÃO ===')

jogar_novamente = 'S'

while jogar_novamente == 'S':
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    limite = 3
    acertou = False

    print('\nPensei em um número entre 1 e 10.')
    print(f'Você tem {limite} tentativas.')

    while tentativas < limite and not acertou:
        try:
            palpite = int(input('Digite seu palpite: '))
            tentativas += 1

            if palpite == numero_secreto:
                acertou = True
                print(f'🎉 Parabéns! Você acertou em {tentativas} tentativas.')
            elif palpite < numero_secreto:
                print('Mais... tente um número maior.')
            else:
                print('Menos... tente um número menor.')

            print(f'Tentativas restantes: {limite - tentativas}')

        except ValueError:
            print('Digite apenas números inteiros!')

    if not acertou:
        print(f'😢 Você perdeu! O número era {numero_secreto}.')

    jogar_novamente = input('\nQuer jogar novamente? [S/N] ').strip().upper()

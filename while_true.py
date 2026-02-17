print('\033[36mTabuada completa:\033[m')
print('=' * 20)

while True:
    try:
        numero = int(input('\033[35mTabuada do número:\033[m '))
        break
    except ValueError:
        print('\033[31mDigite um número válido!\033[mg')

for contador in range(1, 11):
    print(f'\033[32m{numero} x {contador} = {numero * contador}\033[m')

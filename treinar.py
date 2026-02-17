print('\33[31mTabuada completa:\33[m')
print('='*20)
numero = int(input('\33[35mTabuada do numero:\33[m'))

for contador in range (1,11):
    resultado = numero*contador
    print(f'\033[33m{numero} x {contador} = {resultado}\033[m')
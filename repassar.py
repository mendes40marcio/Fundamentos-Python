# Tabuada com o comando while

numero = int(input('Informe um numero:'))
print(f'\n Tabuada {numero}')
print('='*20)

contador= 1
while contador <= 10:
    print(f'{numero} x {contador} = {numero*contador} ')
    contador+=1
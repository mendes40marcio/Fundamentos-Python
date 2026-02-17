while True:
    try:
        numero = int(input('Tabuada do numero:'))
        break
    
    except ValueError:
        print('Digite um numero valído!')


for contador in range (1,11):
    print(f'{numero} x {contador} = {numero*contador}')




# TABUADA DO 1 AO 10

numero = int(input('Informe um numero entre 1 ao 10: '))
contador = 1
print(f'\ntabuada do numero:{numero}')
print('='*20)

while contador <=10:
    resultado = numero*contador
    print(f'{numero} x {contador} = {resultado}')
    contador+= 1  

    
print('FIM DO PROGRAMA 😎')

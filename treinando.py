numero = int(input('\033[35mInforme um numero entre 1,10:\033[m '))
print(f'\033[31m\nTabuada {numero}:\033[m')
contador = 1
while contador <=10:
    resultado = numero * contador
    print(f'\033[32m{numero} x {contador} = {resultado}\033[m')
    contador+=1
    
 
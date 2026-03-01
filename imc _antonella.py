# Antonella e seu Indice corporal de massa


while True:
    try:
        altura = float(input('Informe a sua altura:'))
        peso = float(input('Agora digite o seu peso:'))
        imc  = peso/(altura**2)
        print(f'Antonella seu IMC é {imc:.2f}')

        break
    
        
    except ValueError:
        input('Por favor informe um numero valído!')
        
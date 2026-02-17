numero = -1

while numero < 0 or numero > 10:
    numero = int(input("Digite um número entre 0 e 10: "))
    
    if numero < 0 or numero > 10:
        print("Número inválido! Tente novamente.")

print(f"Número válido informado: {numero}")




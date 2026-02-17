# Exemplo prático com for i in range()

# Solicitar um número do usuário
numero = int(input("Digite um número: "))

print(f"\nTabuada {numero}:")
print("="*30)

# Loop para mostrar a tabuada
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("="*30)

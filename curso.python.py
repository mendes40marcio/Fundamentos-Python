frase = input('Digite uma frase: ').strip().upper()

print('Quantidade de A:', frase.count('A'))
print('Primeira posição do A:', frase.find('A') + 1)
print('Última posição do A:', frase.rfind('A') + 1)

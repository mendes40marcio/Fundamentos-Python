import random
nomes = ['Marcio','Priscila','Nicole','Isaque']

random.shuffle(nomes)
print('Ordem de apresentação')
for posicao, nome in enumerate(nomes,start=1):
    print(f'{posicao}° - {nome}')
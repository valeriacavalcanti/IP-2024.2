import random

nomes = []

while True:
    nome = input('Nome: ')

    if len(nome) == i2:
        break

    nomes.append(nome)

TAM = len(nomes)

print(nomes)

i1 = random.randint(0, TAM - 1)
i2 = random.randint(0, TAM - 1)

aux = nomes[i1]
nomes[i1] = nomes[i2]
nomes[i2] = aux
# nomes[i1], nomes[i2] = nomes[i2], nomes[i1]

print(nomes)
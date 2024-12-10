import random

nomes = []

while True:
    nome = input('Nome: ')

    if len(nome) == 0:
        break

    nomes.append(nome)

TAM = len(nomes)

print(nomes)

for i in range(6):
    i1 = random.randint(0, TAM - 1)
    i2 = random.randint(0, TAM - 1)

    aux = nomes[i1]
    nomes[i1] = nomes[i2]
    nomes[i2] = aux
    # nomes[i1], nomes[i2] = nomes[i2], nomes[i1]

print(nomes)

i = random.randint(0, TAM - 1)

print('Sorteado: ', nomes[i])
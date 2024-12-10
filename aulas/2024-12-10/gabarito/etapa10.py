import random

nomes = []
emails = []

while True:
    nome = input('Nome: ')

    if len(nome) == 0:
        break

    email = input('email: ')

    nomes.append(nome)
    emails.append(email)

TAM = len(nomes)

print(nomes)

for i in range(6):
    i1 = random.randint(0, TAM - 1)
    i2 = random.randint(0, TAM - 1)

    aux = nomes[i1]
    nomes[i1] = nomes[i2]
    nomes[i2] = aux
    # nomes[i1], nomes[i2] = nomes[i2], nomes[i1]

    aux = emails[i1]
    emails[i1] = emails[i2]
    emails[i2] = aux
    # emails[i1], emails[i2] = emails[i2], emails[i1]

print(nomes)

for i in range(TAM):
    prox = i + 1
    if (prox == TAM):
        prox = 0
    print(f'{nomes[i]}({emails[i]}) -> {nomes[prox]}({emails[prox]})')
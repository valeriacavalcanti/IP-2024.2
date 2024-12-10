nomes = []

while True:
    nome = input('Nome: ')

    if len(nome) == 0:
        break

    nomes.append(nome)


print(nomes)
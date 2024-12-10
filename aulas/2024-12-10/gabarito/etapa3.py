nomes = []

while True:
    nome = input('Nome: ')

    if len(nome) == 0:
        break

    nomes.append(nome)

TAM = len(nomes)

print(nomes)

primeiro_indice = 0
ultimo_indice = TAM - 1
nomes[primeiro_indice], nomes[ultimo_indice] = nomes[ultimo_indice], nomes[primeiro_indice]
#nomes[0], nomes[-1] = nomes[-1], nomes[0]

print(nomes)
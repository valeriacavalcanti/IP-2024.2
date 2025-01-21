nomes = []

# ler os nomes
while True:
    nome = input('Nome: ')
    
    if (nome == ''):
        break

    nomes.append(nome)

# exibir os nomes
print(nomes)

# permutar o primeiro com o último
ultimo_indice = len(nomes) - 1
aux = nomes[0]
nomes[0] = nomes[ultimo_indice]
nomes[ultimo_indice] = aux

# exibir todos os nomes
print(nomes)

# ler e armazenar os nomes de 6 pessoas

nomes = [''] * 6
idades = [0] * 6

# ler os nomes
for i in range(6):
    nomes[i] = input('Nome: ')
    idades[i] = int(input('Idade: '))

# exibir os nomes
for i in range(6):
    print(f'{i} - {nomes[i]} - {idades[i]} anos')
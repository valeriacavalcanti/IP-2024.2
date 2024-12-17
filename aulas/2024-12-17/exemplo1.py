idades = [0] * 6
soma = 0

# ler as idades
for i in range(6):
    idades[i] = int(input(f'{i+1}º idade: '))
    #print(idades)

# exibir as idades armazenas (uma por linha)
for i in range(6):
    print(i, idades[i])

# somar os valores do vetor
for i in range(6):
    soma = soma + idades[i]

print('Soma =', soma)

# calcular a média
media = soma / 6
print(f'Média = {media:.1f}')

# exibir as idades acima da média
for i in range(6):
    if (idades[i] > media):
        print(idades[i])

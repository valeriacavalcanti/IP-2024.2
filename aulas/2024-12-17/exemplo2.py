idades = []
soma = 0

# ler as idades
idade = int(input(f'Idade: '))
while (idade >= 0):
    idades.append(idade)
    idade = int(input(f'Idade: '))
    
# exibir as idades armazenas (uma por linha)
for i in range(len(idades)):
    print(i, idades[i])

# somar os valores do vetor
for i in range(len(idades)):
    soma = soma + idades[i]

print('Soma =', soma)

# calcular a média
media = soma / len(idades)
print(f'Média = {media:.1f}')

# exibir as idades acima da média
for i in range(len(idades)):
    if (idades[i] > media):
        print(idades[i])

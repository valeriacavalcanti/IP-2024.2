idades = []
soma = 0

# ler as idades
while (True):
    idade = int(input(f'Idade: '))

    if idade < 0:
        break
    
    idades.append(idade)

    
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

# verificar se tem 18 nas idades lidas
existe = False
for i in range(len(idades)):
    if idades[i] == 18:
        existe = True
        break

if (existe == True):
    print('achei, tem 18')
else:
    print('não achei, não tem 18')

# exibir o maior/menor valor (maior/menor idade)
if (len(idades) > 0):
    maior = menor = idades[0]
    for i in range(1, len(idades)):
        if (idades[i] > maior):
            maior = idades[i]
        if (idades[i] < menor):
            menor = idades[i]

    print(menor, maior)
else:
    print('nenhuma idade digitada')

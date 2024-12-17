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
soma = sum(idades)
print('Soma =', soma)

# calcular a média
media = soma / len(idades)
print(f'Média = {media:.1f}')

# exibir as idades acima da média
for i in range(len(idades)):
    if (idades[i] > media):
        print(idades[i])

# verificar se tem 18 nas idades lidas
if (18 in idades):
    print('achei, tem 18')
else:
    print('não achei, não tem 18')

# exibir o maior/menor valor (maior/menor idade)
menor = min(idades)
maior = max(idades)
print(menor, maior)


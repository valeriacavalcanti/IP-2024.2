import random

soma = 0
qtd_acima_70 = 0
notas = [0] * 10

for i in range(10):
    notas[i] = random.randint(0,100)
    soma = soma + notas[i]
    if (notas[i] >= 70):
        qtd_acima_70 = qtd_acima_70 + 1

media_grupo = soma // 10
#print(notas)

print(f'Média do grupo = {media_grupo}')
print(f'Quantidade acima de 70: {qtd_acima_70}')

# exibir as notas com valor acima da média do grupo
for i in range(10):
    if notas[i] >= media_grupo:
        print(f'{i} - {notas[i]}')
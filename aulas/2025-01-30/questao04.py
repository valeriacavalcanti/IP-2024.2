import random

# declarar matriz 40x6
matriz = []
for i in range(40):
    matriz.append([0] * 6)

# preencher com valores aleatórios entre 1 e 20
for i in range(40):
    for j in range(6):
        matriz[i][j] = random.randint(1, 20)

# Ler um número do usuário
numero = int(input('Número: '))

# Quantas vezes esse valor aparece na matriz
qtd = 0
for i in range(40):
    for j in range(6):
        if matriz[i][j] == numero:
            qtd += 1
print(f'{numero} apareceu {qtd} vezes')

# Qual é o maior valor e o menor valor da matriz
maior = menor = matriz[0][0]
for i in range(40):
    for j in range(6):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]
print(f'Menor = {menor} - Maior = {maior}')

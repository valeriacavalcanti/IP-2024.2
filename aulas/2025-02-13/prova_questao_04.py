import random

soma_diagonal_principal = 0

# obter a ordem da matriz
ordem = int(input('Ordem da matriz: '))

# declarar a matriz de ordem "ordem"
matriz = []
for i in range(ordem):
    matriz.append([0] * ordem)

# preencher a matriz com valores aleatórios [-40,40]
for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = random.randint(-40,40)

# soma dos elementos que estão na diagonal principal
for i in range(ordem):
    soma_diagonal_principal += matriz[i][i]

# soma dos elementos da matriz por linha
for i in range(ordem):
    soma = 0
    for j in range(ordem):
        soma += matriz[i][j]
    print(f'linha = {i} soma = {soma}')


# soma dos elementos da matriz por coluna
for j in range(ordem):
    soma = 0
    for i in range(ordem):
        soma += matriz[i][j]
    print(f'coluna = {j} soma = {soma}')
    

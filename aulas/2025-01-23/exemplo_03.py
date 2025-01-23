# declarar a matriz 10 x 3
notas = []

for i in range(10):
    notas.append([None]*3)

# exibir a matriz
for i in range(10):
    print(notas[i])

# definir nota 100 para todos
for i in range(10):
    print('estudante', i+1)
    soma = 0
    for j in range(3):
        notas[i][j] = int(input('Nota: '))
        soma += notas[i][j]
    media = soma/3
    print(f'Média: {media:.2f}')

# exibir a matriz
for i in range(10):
    print(notas[i])

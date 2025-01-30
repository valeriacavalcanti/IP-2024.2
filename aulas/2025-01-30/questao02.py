# declarar as matrizes: A B C
#ma = [[0,0,0,0], [0,0,0,0]]
#mb = [[0,0,0,0], [0,0,0,0]]
#mc = [[0,0,0,0], [0,0,0,0]]

ma, mb, mc = [], [], []

for i in range(2):
    ma.append([0]*4)
    mb.append([0]*4)
    mc.append([0]*4)

# ler matriz A
print('Elementos da matriz A')
for i in range(2):
    for j in range(4):
        ma[i][j] = int(input('Número: '))

# ler matriz B
print('Elementos da matriz B')
for i in range(2):
    for j in range(4):
        mb[i][j] = int(input('Número: '))

# calcular matriz C
for i in range(2):
    for j in range(4):
        mc[i][j] = ma[i][j] + mb[i][j]

# exibir as matrizes A B C
print(ma)
print(mb)
print(mc)

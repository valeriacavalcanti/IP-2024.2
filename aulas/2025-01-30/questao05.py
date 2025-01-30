import random

# declarar matriz C
mc = []
for i in range(3):
    mc.append([0]*5)

# declarar matriz CT
mct = []
for i in range(5):
    mct.append([0]*3)

# Ler matriz C
for i in range(3):
    for j in range(5):
        mc[i][j] = random.randint(1,10)

# Montar matriz CT
for i in range(3):
    for j in range(5):
        mct[j][i] = mc[i][j]
        
# Exibir C
for i in range(3):
    print(mc[i])

# Exibir CT
for i in range(5):
    print(mct[i])

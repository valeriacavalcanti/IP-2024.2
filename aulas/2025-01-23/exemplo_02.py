m1 = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]

m2 = [[0]*3, [0]*3, [0]*3, [0]*3]

m3 = []
for i in range(4):
    m3.append([0] * 3)

print(m1)
print(m2)
print(m3)

m1[0][0] = 1
m2[0][0] = 2
m3[0][0] = 3

print(m1)
print(m2)
print(m3)

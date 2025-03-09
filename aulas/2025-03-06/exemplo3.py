import random

arquivo = open('numeros.txt', 'w')
for i in range(10000):
    numeros = []
    while len(numeros) < 10:
        num = random.randint(1,100)
        if num not in numeros:
            numeros.append(num)
    arquivo.write(f'{numeros}\n')

arquivo.close()
print('fim')

import random

soma = 0
notas = [] # lista vazia

while True:
    nota = random.randint(-10, 110)

    if (nota < 0) or (nota > 100):
        break
    
    notas.append(nota)
    soma = soma + nota

# exibir todas as notas armazenadas
for i in range(len(notas)):
    print(f'{i} - {notas[i]}')

if len(notas) > 0:
    media = soma/len(notas)
    print(f'Média = {media}')
else:
    print('erro')
import random

menor = 101
maior = -1
soma = qtd = 0

nota = random.randint(-10,110)
while (nota >= 0) and (nota <= 100):
    if (nota < menor):
        menor = nota
    if (nota > maior):
        maior = nota
    qtd += 1
    soma += nota
    
    nota = random.randint(-10,110)

if qtd > 0:
    media = soma/qtd
    print(f'Quantidade: {qtd}')
    print(f'Soma: {soma}')
    print(f'Maior nota: {maior}')
    print(f'Menor nota: {menor}')
    print(f'Média: {media:.1f}')
else:
    print('Sem notas válidas!')

menor = 101
maior = -1
soma = qtd = 0

nota = int(input('Nota: '))
while (nota >= 0) and (nota <= 100):
    if (nota < menor):
        menor = nota
    if (nota > maior):
        maior = nota
    qtd += 1
    soma += nota
    
    nota = int(input('Nota: '))

if qtd > 0:
    media = soma/qtd
    print(f'Quantidade: {qtd}')
    print(f'Soma: {soma}')
    print(f'Maior nota: {maior}')
    print(f'Menor nota: {menor}')
    print(f'Média: {media:.1f}')
else:
    print('Sem notas válidas!')

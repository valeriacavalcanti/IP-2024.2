menor = 101
maior = -1
soma = qtd = 0

while True:
    nota = int(input('Nota: '))
    if (nota < 0) or (nota > 100):
        break
    if (nota < menor):
        menor = nota
    if (nota > maior):
        maior = nota
    qtd += 1
    soma += nota

if qtd > 0:
    media = soma/qtd
    print(f'Quantidade: {qtd}')
    print(f'Soma: {soma}')
    print(f'Maior nota: {maior}')
    print(f'Menor nota: {menor}')
    print(f'Média: {media:.1f}')
else:
    print('Sem notas válidas!')

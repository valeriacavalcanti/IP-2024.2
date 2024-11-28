qtde = 0
soma = 0

for i in range(6):
    num = float(input())
    if (num > 0):
        qtde += 1
        soma += num

media = soma / qtde

print(qtde, 'valores positivos')
print("{:.1f}".format(media))
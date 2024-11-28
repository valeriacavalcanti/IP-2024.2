while True:
    n = int(input('Número: '))
    qtd_div = 0

    for i in range(1, n + 1):
        if (n % i == 0):
            qtd_div += 1

    if (qtd_div == 2):
        break

print(f'{n} é primo')

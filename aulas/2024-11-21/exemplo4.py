for i in range(1, 11):
    multiplicacao = 1

    for j in range(1, i + 1):
        multiplicacao = multiplicacao * j

    print(f'{i}! = {multiplicacao}')

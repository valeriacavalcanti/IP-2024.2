multiplicacao = 1
n = int(input('Número: '))
for i in range(1, n+1):
    multiplicacao = multiplicacao * i

print(f'{n}! = {multiplicacao}')

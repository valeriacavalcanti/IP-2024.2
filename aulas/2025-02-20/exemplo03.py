import random

# Parâmetros: int int int(opcional)
# Retorno: int
def somar(n1, n2, n3=20):
    soma = n1 + n2 + n3
    return soma

# Parâmetros: int
# Retorno: -
def super_print(qtd):
    for i in range(qtd):
        print('IFPB')

# Parâmetro: -
# Retorno: int
def aleatorio():
    valor = random.randint(100, 200)
    return valor

# Parâmetro: -
# Retorno: -
def melhor_time():
    print('Melhor time: FLAMENGO')

# Parâmetro: str (opcional)
# Retorno: -
def parece_melhor_time(time='FLAMENGO'):
    print(f'Parece ser o melhor time: {time}')



# usar a função criada no PROGRAMA PRINCIPAL
soma1 = somar(10,20)        # 50
soma2 = somar(10,20,30)     # 60

valor_aleatorio = aleatorio()

print(f'Soma = {soma1}')
print(f'Soma = {soma2}')

super_print(4)

print(f'Valor aleatório: {valor_aleatorio}')

melhor_time()

parece_melhor_time('Botafogo')
parece_melhor_time()


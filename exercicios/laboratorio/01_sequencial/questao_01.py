import math

qtd_convidados = int(input('Convidados: '))
qtd_resmas = math.ceil(qtd_convidados/500)

print(f'Resmas = {qtd_resmas}')

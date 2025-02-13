trafego = [0] * 12
soma = 0
ultrapassou_media = 0

# ler o trafego da rede
for i in range(12):
    trafego[i] = float(input('Trafego: '))
    soma += trafego[i]

# calcular a média do trafego
media = soma / 12

# contar quantas medicoes do trafego ultrapassou a média
for i in range(12):
    if trafego[i] > media:
        ultrapassou_media += 1

print(f'Média = {media}')
print(f'Quantidade que ultrapassou = {ultrapassou_media}')


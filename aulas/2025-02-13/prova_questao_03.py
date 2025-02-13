vlans = [0] * 30
maior = -1
qtd_vlan_maior_ultima = 0

# ler a quantidade de dispositivos de cada VLAN
# encontrar maior valor
for i in range(30):
    vlans[i] = int(input('Quantidade de dispositivos: '))
    if vlans[i] > maior:
        maior = vlans[i]

# verificar quantidade de vlans com quantidade de dispositivos
# maior do que a última (29)
for i in range(29):
    if vlans[i] > vlans[29]:
        qtd_vlan_maior_ultima += 1

print(f'Número de VLANS: {qtd_vlan_maior_ultima}')
print(f'Maior quantidade de dispositivos: {maior}')

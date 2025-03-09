arquivo = open('dados.txt', 'r')

ips = []
datas = []
anos = []
meses = []

for r in arquivo.read().splitlines():
    # 192.183.120.45 - 17/08/2023
    dados = r.split(' - ')
    ips.append(dados[0])
    datas.append(dados[1].split('/'))
    
arquivo.close()

for i in range(len(datas)):
    if datas[i][2] not in anos:
        anos.append(datas[i][2])
        #print(datas[i][2])
    if datas[i][1] not in meses:
        meses.append(datas[i][1])

print(anos)
print(meses)

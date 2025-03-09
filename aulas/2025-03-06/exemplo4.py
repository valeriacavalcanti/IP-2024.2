arquivo = open('nomes.txt','r')

#conteudo_arquivo = arquivo.read()

#misterio = arquivo.read().splitlines()

for linha in arquivo.read().splitlines():
    print(linha)

#print(misterio)

arquivo.close()

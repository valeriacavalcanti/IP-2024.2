arquivo = open('numeros.txt','r')

for linha in arquivo.read().splitlines():
    print(linha)
    linha = linha.replace('[', '')
    linha = linha.replace(']', '')
    numeros = linha.split(', ')
    print(linha)
    print(numeros)
    break


arquivo.close()

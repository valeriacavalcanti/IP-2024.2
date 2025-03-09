arquivo = open('nomes.txt', 'a')

for i in range(4):
    nome = input('Nome: ')
    arquivo.write(f'{nome}\n')

arquivo.close()


arquivo = open('nomes.txt', 'r')
print(arquivo.read())
arquivo.close()

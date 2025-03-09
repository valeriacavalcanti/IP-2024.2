arquivo = open('nomes.txt', 'w')

for i in range(4):
    nome = input('Nome: ')
    arquivo.write(f'{nome}\n')

arquivo.close()
print('fim')

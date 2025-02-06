nome = input('Nome: ')
qtd = len(nome)

#print(nome)
#print(f'{nome} tem {qtd} caracteres')

for i in range(qtd):
    print(i, nome[i], type(nome[i]), ord(nome[i]))

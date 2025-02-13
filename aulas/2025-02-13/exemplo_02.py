frase = input('Frase: ')
qtd_espacos = 0

# limpar dentro da string
while (frase.find('  ') >= 0 ):
    frase = frase.replace('  ', ' ')

# se o primeiro símbolo for espaco, retirar
if frase[0] == ' ':
    frase = frase[1:]

# se o último símbolo for espaco, retirar
if frase[len(frase) - 1] == ' ':
    frase = frase[:-1]


for i in range(len(frase)):
    if frase[i] == ' ':
        qtd_espacos += 1

qtd_palavras = qtd_espacos + 1

print(f'Quantidade de palavras: {qtd_palavras}')

# verificar se um símbolo é vogal
def eVogal(simbolo: str) -> bool:
    vogais = 'aeiouAEIOU'
    if simbolo in vogais:
        return True
    else:
        return False

# verificar se um texto é composto apenas por vogais
def apenas_vogais(texto: str) -> bool:
    for i in range(len(texto)):
        if eVogal(texto[i]) == False:
            return False
            print('acabou')
    return True

## main
print(eVogal('A'))
print(eVogal('C'))
print(apenas_vogais('aaaaaaeeeeeeiiiiii'))
print(apenas_vogais('aaaaaaxeeeeeeiiiiii'))

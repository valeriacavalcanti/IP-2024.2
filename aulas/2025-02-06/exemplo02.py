simbolo = input('Digite um símbolo: ')
codigo_decimal = ord(simbolo)

print(f'Você digitou {simbolo}')
print(f'Código decimal na tabela ASCII: {codigo_decimal}')


if (simbolo >= '0') and (simbolo <= '9'):
    print('Você digitou um símbolo numérico')
else:
    if (simbolo >= 'A') and (simbolo <= 'Z'):
        print('Você digitou uma letra maiúscula')
    else:
        if (simbolo >= 'a') and(simbolo <= 'z'):
            print('Você digitou uma letra minúscula')
        else:
            print('Você digitou um caractere especial')

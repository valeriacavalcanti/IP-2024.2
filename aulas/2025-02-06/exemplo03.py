codigo_decimal = int(input('Digite um código decimal: '))
simbolo = chr(codigo_decimal)

print(f'Você digitou {simbolo}')
print(f'Código decimal na tabela ASCII: {codigo_decimal}')

if (codigo_decimal >= 48) and (codigo_decimal <= 57):
    print('Você digitou um símbolo numérico')
else:
    if (codigo_decimal >= 65) and (codigo_decimal <= 90):
        print('Você digitou uma letra maiúscula')
    else:
        if (codigo_decimal >= 97) and(codigo_decimal <= 122):
            print('Você digitou uma letra minúscula')
        else:
            print('Você digitou um caractere especial')

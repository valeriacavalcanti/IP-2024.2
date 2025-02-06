simbolo_maiusculo = input('Digite uma letra maiúscula: ')
codigo_decimal_maiusculo = ord(simbolo_maiusculo)

codigo_decimal_minusculo = codigo_decimal_maiusculo + 32
simbolo_minusculo = chr(codigo_decimal_minusculo)

print(simbolo_maiusculo, simbolo_minusculo)
print(codigo_decimal_maiusculo, codigo_decimal_minusculo)

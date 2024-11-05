cotacao = float(input('Cotação: '))
valor_compra = float(input('Valor Compra: '))
valor_compra = valor_compra * cotacao

taxa = valor_compra * 0.2
icms = valor_compra * 0.17

valor_final = valor_compra + taxa + icms

print(f'Taxa importacao: R$ {taxa}')
print(f'ICMS: R$ {icms}')
print(f'Valor Compra: R$ {valor_final}')

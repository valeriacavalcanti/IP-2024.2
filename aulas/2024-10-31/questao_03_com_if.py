cotacao = float(input('Cotação: '))
valor_compra = float(input('Valor Compra: '))

if (valor_compra <= 50):
    taxa_importacao = 0.2
    print('taxa foi de 20%')
else:
    taxa_importacao = 0.6
    print('taxa foi de 60%')
    print('sinto muito')

valor_compra = valor_compra * cotacao  
valor_taxa = valor_compra * taxa_importacao
valor_icms = valor_compra * 0.17

valor_final = valor_compra + valor_taxa + valor_icms

if (valor_final > 1000):
    desconto = valor_final * 0.1
    valor_final = valor_final - desconto

print(f'Taxa importacao: R$ {valor_taxa}')
print(f'ICMS: R$ {valor_icms}')
print(f'Valor Compra: R$ {valor_final}')

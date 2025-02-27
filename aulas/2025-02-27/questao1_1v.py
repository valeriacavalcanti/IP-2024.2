import funcoes

## Programa Principal

#tam = int(input('Tamanho: '))

#isso_ai = 'Marcelo'
numeros = funcoes.gerar_lista(4)
print(numeros)
#exibir_lista(numeros)
#exibir_crishane(numeros)

acima = funcoes.elementos_acima_media(numeros)
qtd_acima = funcoes.qtd_acima_media(numeros)
print(acima, qtd_acima)

abaixo = funcoes.elementos_abaixo_media(numeros)
qtd_abaixo = funcoes.qtd_abaixo_media(numeros)
print(abaixo, qtd_abaixo)

igual = funcoes.elementos_igual_media(numeros)
qtd_igual = funcoes.qtd_igual_media(numeros)
print(igual, qtd_igual)


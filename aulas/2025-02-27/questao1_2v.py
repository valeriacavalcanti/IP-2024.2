#import funcoes
#from funcoes import gerar_lista, elementos_acima_media
from funcoes import *

## Programa Principal

#tam = int(input('Tamanho: '))

#isso_ai = 'Marcelo'
numeros = gerar_lista(4)
print(numeros)
#exibir_lista(numeros)
#exibir_crishane(numeros)

acima = elementos_acima_media(numeros)
qtd_acima = qtd_acima_media(numeros)
print(acima, qtd_acima)

abaixo = elementos_abaixo_media(numeros)
qtd_abaixo = qtd_abaixo_media(numeros)
print(abaixo, qtd_abaixo)

igual = elementos_igual_media(numeros)
qtd_igual = qtd_igual_media(numeros)
print(igual, qtd_igual)


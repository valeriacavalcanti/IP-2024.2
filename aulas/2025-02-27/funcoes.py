import random

def qtd_acima_media(lista: list) -> int:
    elementos = elementos_acima_media(lista)
    return len(elementos)

def elementos_acima_media(lista: list) -> list:
    acima_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if (lista[i] > media):
            acima_media.append(lista[i])
    return acima_media


def qtd_abaixo_media(lista: list) -> int:
    return len(elementos_abaixo_media(lista))


def qtd_igual_media(lista: list) -> int:
    return len(elementos_igual_media(lista))


def elementos_abaixo_media(lista: list) -> list:
    abaixo_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if (lista[i] < media):
            abaixo_media.append(lista[i])
    return abaixo_media


def elementos_igual_media(lista: list) -> list:
    igual_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if (lista[i] == media):
            igual_media.append(lista[i])
    return igual_media


def gerar_lista(tamanho: int) ->list:
    lista = [0] * tamanho
    for i in range(tamanho):
        lista[i] = random.randint(0,100)
    return lista


def exibir_lista(lista: list):
    for i in range(len(lista)):
        print(lista[i])

def exibir_crishane(lista: list):
    print('lista (parâmetro):', lista)
    print('numeros (variável global): ', numeros)
    print('isso_ai (variável global): ', isso_ai)


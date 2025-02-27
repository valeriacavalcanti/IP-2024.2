def misterio(lista):
    valor1 = lista[0]
    valor2 = lista[1]

    for i in range(len(lista)):
        if (lista[i] > valor1):
            valor2 = valor1
            valor1 = lista[i]
        else:
            if (valor1 > lista[i] and lista[i] > valor2):
                valor2 = lista[i]
    return valor2

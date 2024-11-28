qt_par = 0
qt_impar = 0
qt_positivo = 0
qt_negativo = 0

for i in range(5):
    # num = int(input('Número: '))
    num = int(input())

    if num % 2 == 0:
        qt_par = qt_par + 1 # qt_par += 1
    else:
        qt_impar = qt_impar + 1

    if num > 0:
        qt_positivo = qt_positivo + 1
    else:
        if num < 0:
            qt_negativo = qt_negativo + 1


print(f'{qt_par} valor(es) par(es)')
print(f'{qt_impar} valor(es) impar(es)')
print(f'{qt_positivo} valor(es) positivo(s)')
print(f'{qt_negativo} valor(es) negativo(s)')
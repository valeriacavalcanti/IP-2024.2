# loop infinito
while True:
    maior_nota = -1
    soma = 0

    qtd_notas = int(input('Quantidade de notas: '))

    # verificação para encerrar o loop que está lendo a quantidade de notas
    if qtd_notas < 4 or qtd_notas > 10:
        break
    
    for i in range(qtd_notas):

        # loop infinito
        while True:
            nota = int(input(f'Nota {i + 1}: '))
            # verificação para encerrar o loop que está lendo cada nota
            if (nota >= 0) and (nota <= 100):
                break
        
        soma = soma + nota
        if nota > maior_nota:
            maior_nota = nota

    media = soma / qtd_notas

    print(f'Média = {media:.2f}')
    print(f'Maior nota = {maior_nota}')


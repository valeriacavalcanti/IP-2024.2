qtd_aulas = int(input('Quantidade de aulas: '))
qtd_faltas = int(input('Quantidade de faltas: '))

frequencia = (qtd_aulas - qtd_faltas) / qtd_aulas * 100

print(f'Frequencia: {frequencia} %')
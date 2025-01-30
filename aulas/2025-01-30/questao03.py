N_LINHAS = 40
N_COLUNAS = 3

# declarar matriz 40 x 3
notas = []
for i in range(N_LINHAS):
    notas.append([0] * N_COLUNAS)
    
# ler as notas dessa turma
for i in range(N_LINHAS):
    for j in range(N_COLUNAS):
        notas[i][j] = int(input(f'Nota {i} {j}: '))


# Exibir a média de CADA aluno
# Calcular e exibir a média da turma
soma_medias = 0
for i in range(N_LINHAS):
    soma = 0
    for j in range(N_COLUNAS):
        soma += notas[i][j]
    media_aluno = soma/N_COLUNAS
    soma_medias += media_aluno
    print(f'Média do aluno {i}: {media_aluno:.1f}')

media_turma = soma_medias / N_LINHAS
print(f'Media da Turma: {media_turma:.1f}')

# Quantos alunos possuem nota maior do que a
# média da turma
qt_alunos_acima_media = 0
for i in range(N_LINHAS):
    #existe = False
    for j in range(N_COLUNAS):
        if (notas[i][j] > media_turma):
            #existe = True
            qt_alunos_acima_media += 1
            break
                       
    #if existe == True:
     #   qt_alunos_acima_media += 1

print(f'Quantidade acima: {qt_alunos_acima_media}')





qtd_aprovados = int(input('Quantidade de alunos aprovados: '))
qtd_reprovados = int(input('Quantidade de alunos reprovados: '))

porcentagem_aprovados = qtd_aprovados / (qtd_aprovados + qtd_reprovados) * 100

print(f'Foram aprovados {porcentagem_aprovados} %')
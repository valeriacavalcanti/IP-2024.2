soma = 0
qtd_notas_invalidas = 0

for i in range(1,5):
    print(f'Vamos tentar a nota {i}')
    nota = int(input('Nota: '))
    while (nota < 0 or nota > 100):
        print('Nota inválida')
        qtd_notas_invalidas += 1
        nota = int(input('Nota: '))
    soma = soma + nota
    print(f'Nota {i} válida: {nota}')

print(f'Soma das notas válidas = {soma}')
print(f'Notas inválidas: {qtd_notas_invalidas}')

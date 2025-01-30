#1)Declarar a matriz;
m = [[10,20,30,40], [50,60,70,80], [90,100,110,120]]

#2)Exibir o elemento que está na linha 1 coluna 3;
print(m[1][3])

#3)Adicionar o valor 10 ao elemento que está
#  na linha 2 coluna 2;
m[2][2] += 10

#4)Alterar todos os elementos que estão na
#  linha 2 para 200;
for i in range(4):
    m[2][i] = 200

#5)Exibir a soma dos elementos que estão na linha 1;
soma = 0
for i in range(4):
    soma += m[1][i]
print(soma)
    
#6)Exibir a soma dos elementos que estão na coluna 3.
soma = 0
for i in range(3):
    soma += m[i][3]
print(soma)

    

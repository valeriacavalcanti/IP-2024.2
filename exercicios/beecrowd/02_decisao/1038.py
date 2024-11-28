cod, qtde = input().split()

cod, qtde = int(cod), int(qtde)

if (cod == 1):
  valor = qtde * 4.0
elif (cod == 2):
  valor = qtde * 4.5
elif (cod == 3):
  valor = qtde * 5.0
elif (cod == 4):
  valor = qtde * 2.0
else:
  valor = qtde * 1.5

print("Total: R$ {:.2f}".format(valor))
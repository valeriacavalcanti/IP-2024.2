compra = float(input('Valor da Compra: '))
if compra <= 100:
  cash = compra * 0.04
elif compra <= 200:
  cash = compra * 0.06
elif compra <= 400:
  cash = compra * 0.08
else:
  cash = compra * 0.10
print ('cashback =', cash)
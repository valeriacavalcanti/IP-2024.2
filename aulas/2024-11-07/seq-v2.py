compra = float(input('Valor da Compra: '))
if compra <= 100:
  cash = compra * 0.04
elif compra >= 100.01 and compra <= 200:
  cash = compra * 0.06
elif compra >= 200.01 and compra <= 400:
  cash = compra * 0.08
elif compra > 400:
  cash = compra * 0.10
print ('cashback =', cash)
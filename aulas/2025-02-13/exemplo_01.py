st = 'teste TESTE teste 123'
st_maiusculo = ''

for i in range(len(st)):
    if st[i] >= 'a' and st[i] <= 'z':
        codigo_letra_minuscula = ord(st[i])
        codigo_letra_maiuscula = codigo_letra_minuscula - 32
        st_maiusculo += chr(codigo_letra_maiuscula)
    else:
        st_maiusculo += st[i]

    print('- ', id(st_maiusculo), st_maiusculo)

print(st)
print(st_maiusculo)
